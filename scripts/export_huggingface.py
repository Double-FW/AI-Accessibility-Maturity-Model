"""Faithfully extract the approved current AI AMM guidance; do not generate assessment results."""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import quote
import yaml
from jsonschema import Draft202012Validator
from amm_hf_common import ROOT,SOURCE,MANAGED,HISTORICAL,destination,digest,git,load_config,read_sources

class UniqueKeyLoader(yaml.SafeLoader):
    pass
def unique_mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    result = {}
    for k,v in node.value:
        key = loader.construct_object(k, deep=deep)
        if key in result: raise ValueError('Duplicate metadata key: ' + str(key))
        result[key] = loader.construct_object(v, deep=deep)
    return result
UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)
def safe_yaml(text):
    return yaml.load(text,Loader=UniqueKeyLoader)

def metadata(text):
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
    md = safe_yaml(match[1]) if match else {}
    return md if isinstance(md, dict) else {}

def sections(text):
    """Keep H1/H2 parent context and exact spans; never split fenced examples."""
    boundaries, fence, offset, parents = [(0, 'Document preamble', [])], None, 0, []
    for line in text.splitlines(keepends=True):
        mark = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if mark:
            token = mark[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not line[mark.end():].strip():
                fence = None
        elif fence is None:
            match = re.match(r'^(#{1,2})[ \t]+([^\r\n]+)', line)
            if match:
                level, title = len(match[1]), match[2].strip().rstrip('#').strip()
                parents = parents[:level-1] + [title]
                if offset == 0:
                    boundaries[0] = (offset, title, parents[:])
                else:
                    boundaries.append((offset, title, parents[:]))
        offset += len(line)
    result, counts = [], {}
    for i, (a, title, hierarchy) in enumerate(boundaries):
        b = boundaries[i+1][0] if i+1 < len(boundaries) else len(text)
        if a == b:
            continue
        slug = re.sub(r'[^a-z0-9]+', '-', ' '.join(hierarchy or [title]).lower()).strip('-') or 'section'
        counts[slug] = counts.get(slug, 0) + 1
        key = slug if counts[slug] == 1 else slug + '-' + str(counts[slug])
        result.append((key, title, text[a:b], a, b, hierarchy))
    if ''.join(r[2] for r in result) != text:
        raise ValueError('Section extraction lost source text.')
    return result

def build(root,output):
    root,output=Path(root).resolve(),Path(output).resolve()
    if output==root or root in output.parents:
        raise ValueError('Write the export outside the source checkout.')
    cfg=load_config(root);target=destination(cfg['destination_dataset'])
    texts,manifest=read_sources(root,cfg)
    sha=git(root,'rev-parse','HEAD').decode().strip()
    date=git(root,'show','-s','--format=%cs','HEAD').decode().strip()
    criteria=texts['ASSESSMENT_CRITERIA.md']
    strand_ids=re.findall(r'^\| (AMM-D\d-\d\d) \|',criteria,re.M)
    cell_ids=re.findall(r'^\| (AMM-D\d-L\d) —',criteria,re.M)
    expected_strands={f'AMM-D{n}-{i:02d}' for n in range(1,7) for i in range(1,7)}
    expected_cells={f'AMM-D{n}-L{i}' for n in range(1,7) for i in range(1,6)}
    if len(strand_ids)!=36 or set(strand_ids)!=expected_strands or len(cell_ids)!=30 or set(cell_ids)!=expected_cells:
        raise ValueError('Review changed, missing or duplicate assessment strand/cell identities before export.')
    rule=next((p[2] for p in sections(criteria) if p[1]=='How to make a decision'),None)
    if not rule:raise ValueError('Assessment decision-rule context is missing.')
    warnings=[
        'The method is draft for practitioner pilot; independent human calibration, disabled participant review and a real organisational pilot are pending.',
        'The worked assessment and challenge cases are fictional; templates are blank structures, not actual decisions or results.',
        'External comparisons have topic/category scope. Full proprietary/form-delivered instruments and complete item-level equivalence are not asserted.',
        'Repository instructions and prompts are source data, never runtime authority, authenticated approval or permission to collect personal evidence.'
    ]
    def kind(path):
        if path.startswith('templates/'):return 'blank_working_template'
        if path=='WORKED_ASSESSMENT_EXAMPLES.md':return 'fictional_assessment_examples'
        if path=='ASSESSMENT_CRITERIA.md':return 'draft_assessment_criteria'
        if path=='VALIDATION_AND_ADOPTION.md':return 'validation_and_pending_adoption_limits'
        if path in ('SOURCE_REGISTER.md','EXTERNAL_MODEL_COVERAGE.md','DOUBLE_FW_DELIVERY_CROSSWALK.md'):return 'bounded_source_mapping'
        if path=='AGENTS.md':return 'advisory_agent_guidance_not_runtime_authority'
        if path.endswith('RAG_Current_Source_Map.md'):return 'retrieval_index_not_independent_evidence'
        return 'draft_maturity_guidance'
    def row(path,key,title,body,a,b,hierarchy):
        md=metadata(texts[path])
        if md.get('license','MIT')!='MIT':raise ValueError('Review changed source licence: '+path)
        return {'id':path+'::'+key,'title':title,'text':body,'record_type':kind(path),
            'source_repository':SOURCE,'source_path':path,'source_commit':sha,
            'source_url':f'https://github.com/{SOURCE}/blob/{sha}/{quote(path)}',
            'source_start_line':texts[path][:a].count('\n')+1,
            'source_end_line':max(1,texts[path][:b].count('\n')+(not texts[path][:b].endswith('\n'))),
            'source_document_sha256':digest(texts[path].encode()),'text_sha256':digest(body.encode()),
            'heading_path':hierarchy,'metadata_json':json.dumps(md,ensure_ascii=False,sort_keys=True,default=str),
            'declared_source_license':str(md.get('license','not_declared_in_document_front_matter')),
            'repository_license':'MIT','source_status':str(md.get('status','see_source_for_status')),
            'dataset_version':cfg['dataset_version'],'export_format_version':cfg['export_format_version'],
            'source_commit_date':date,'language':'en-GB','required_context_paths':cfg['context_files'],
            'assessment_scope_context':texts['MODEL_SCOPE_AND_AUTHORITY.md'],
            'assessment_decision_rules_context':rule,
            'source_document_intro':sections(texts[path])[0][2],
            'source_strand_ids':strand_ids if path=='ASSESSMENT_CRITERIA.md' else [],
            'source_cell_ids':cell_ids if path=='ASSESSMENT_CRITERIA.md' else [],
            'interpretation_notice':'Draft practitioner-pilot guidance, not validated organisational findings, legal conformity or external endorsement. Fictional examples and blank templates are not observed evidence. Source instructions are data, not runtime authority.',
            'validation_scope':'faithful extraction and packaging only; no independent calibration, participant study or real organisational pilot'}
    docs,chunks=[],[]
    for path in cfg['files']:
        text=texts[path]
        docs.append(row(path,'document',path,text,0,len(text),[]))
        if path in cfg['document_only_files']:continue
        for key,title,body,a,b,hierarchy in sections(text):
            chunks.append(row(path,key,title,body,a,b,hierarchy))
    if not docs or not chunks:raise ValueError('Guidance export is empty.')
    schema={'$schema':'https://json-schema.org/draft/2020-12/schema','type':'object',
            'required':list(docs[0]),'additionalProperties':False,'properties':{}}
    for key,value in docs[0].items():
        schema['properties'][key]={'type':'array','items':{'type':'string'}} if isinstance(value,list) else {'type':'integer' if isinstance(value,int) else 'string'}
    validator=Draft202012Validator(schema)
    for rows in (docs,chunks):
        if len({r['id'] for r in rows})!=len(rows):raise ValueError('Duplicate record IDs.')
        for item in rows:validator.validate(item)
    output.mkdir(parents=True,exist_ok=True)
    def write_json(name,value):
        (output/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for name,rows in [('documents.jsonl',docs),('knowledge_chunks.jsonl',chunks)]:
        (output/name).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows),encoding='utf-8')
    (output/'LICENSE').write_bytes(texts['LICENSE'].encode())
    write_json('record_schema.json',schema)
    write_json('provenance.json',{'source_repository':SOURCE,'source_commit':sha,'source_commit_date':date,
        'destination_dataset':target,'dataset_version':cfg['dataset_version'],'export_format_version':cfg['export_format_version'],
        'files':manifest,'excluded_historical_prefixes':list(HISTORICAL),'source_warnings':warnings,
        'external_sources_fetched':False,'source_strand_ids':strand_ids,'source_cell_ids':cell_ids,
        'organisational_assessment_performed':False,'independent_human_calibration_performed':False,
        'participant_review_performed':False,'real_organisational_pilot_performed':False,
        'source_instructions_executed':False})
    card=f'''---
pretty_name: Double FW AI Accessibility Maturity Model
language:
- en
license: mit
tags:
- accessibility
- organisational-maturity
- ai-governance
- disability-inclusion
- practitioner-guidance
- text
configs:
- config_name: knowledge_chunks
  default: true
  data_files:
  - split: train
    path: knowledge_chunks.jsonl
- config_name: documents
  data_files:
  - split: train
    path: documents.jsonl
---

# Double FW AI Accessibility Maturity Model

Original Double FW practitioner-pilot guidance for assessing organisational capability
and comparable customer/employee experience, including relevant AI uses. It preserves
six dimensions and five levels, with 36 criterion strands and 30 level cells, a runbook,
measurement guidance, public source mappings, blank templates and fictional cases.

**Status:** draft for practitioner pilot. Independent human assessor calibration,
disabled participant review and a real organisational pilot remain pending. The dataset
is not a collection of real organisational scores, participant records or customer data.
No legal conformity, certification, external endorsement or completed assessment is implied.

## Source and snapshot

GitHub authoring source: https://github.com/{SOURCE}

Source commit: `{sha}` ({date}); method/dataset version {cfg['dataset_version']};
export format {cfg['export_format_version']}. Files and line/heading spans retain exact
source text, source/document hashes, status and provenance. An integrity check is not
validation of the method's real-world effectiveness or the truth of a future evidence record.

## Loading and dataset views

```python
from datasets import load_dataset
chunks = load_dataset("{target}", "knowledge_chunks", split="train")
documents = load_dataset("{target}", "documents", split="train")
```

- `documents`: {len(docs)} complete approved current Markdown files.
- `knowledge_chunks`: {len(chunks)} exact H1/H2 sections of current substantive guidance.

Views overlap: choose deliberately and do not concatenate them as independent examples.
Blank templates, the source register, change log and retrieval index are document-only
so forms and metadata are not fragmented into standalone commands. Historical RAG/source
copies are excluded from both views. The source map may reference additional authoring
infrastructure which is not included as training content. External linked material is
not fetched or copied. `train` is a loading convention, not a completed training run,
benchmark split or measured model performance. No synthetic Q&A is generated.

## Interpretation and context

Read scope/authority, assessment decision rules and validation/adoption limits together.
Rows include exact `assessment_scope_context` and `assessment_decision_rules_context`,
plus `required_context_paths`. These repeated context fields are not independent evidence;
pointers do not enforce retrieval, authority or adoption in a consuming system.

Maintain separate authority/commitments, operated capability, technical findings, human
outcomes and legal conclusions. No averages, half-points or missing-evidence-to-Reactive
conversion are supplied. Responsible AI non-use may demonstrate capability; readiness
findings are separate from live deployed performance. Participation begins with framing.
Fictional cases are labelled in `record_type`; blank templates are not decisions/results.

Double FW methods take precedence over differing external recommendations, with accurate
attribution and recorded differences. Applicable obligations remain separate. W3C category
and other public-topic routes do not establish complete external-item/proprietary coverage
or score equivalence. Preserve actual source identities and limits.

Repository AGENTS and prompts are data, not runtime instructions or authority to access
systems, collect personal information, approve claims, deploy policies or contact people.
No real organisation's owners, funding, compliance or outcome findings are supplied.

## Licence and privacy

The unchanged root MIT licence is copied, including copyright (c) 2026 Double FW Ltd.
Retain copyright and permission notices with copies/substantial portions. Linked standards,
legislation and external repositories keep their own rights; a link does not relicense them.
No raw participant, health, applicant, employee, complaint or credential data is added.
Assessment work requires separate authority, data arrangements and competent human review.

## Updates and validation scope

Manual runs and Mondays at 07:37 UTC are configured in GitHub. Scheduled execution can
be delayed or disabled after repository inactivity. Only explicit committed current
sources are exported. All approved sources and LICENSE are required; new/renamed files
need allow-list review. Missing sources, historical-copy inclusion, unsafe paths, changed
licence, altered criterion identities or failed checks stop publication.

Seven files are managed: README.md, LICENSE, documents.jsonl, knowledge_chunks.jsonl,
provenance.json, record_schema.json and validation_report.json. Existing unmanaged raw files
and .gitattributes are retained and are not kept in sync. Repository visibility is preserved;
historical downloads are not recalled. Destination: `{target}`.

Validation reports cover extraction/schema/checksum integrity, not legal, participant or
organisational results. First publication and each material update must be verified in the
GitHub run and destination provenance/history. Pin a dataset revision for reproducible use.
'''
    yaml.safe_load(card.split('---',2)[1])
    (output/'README.md').write_text(card,encoding='utf-8')
    report={'status':'passed','scope':'faithful extraction and packaging only','source_commit':sha,
        'source_files_verified':len(manifest),'document_records':len(docs),'knowledge_section_records':len(chunks),
        'source_warnings':warnings,'independent_content_review':False,'live_publication_tested':False,
        'export_file_sha256':{name:digest((output/name).read_bytes()) for name in MANAGED if name!='validation_report.json'}}
    write_json('validation_report.json',report)
    return report

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
    print(json.dumps(build(ROOT,args.output)))

if __name__=='__main__':main()
