# Weekly GitHub → Hugging Face publication

Source: https://github.com/Double-FW/AI-Accessibility-Maturity-Model

Destination: https://huggingface.co/datasets/GarethFW/AI_Accessibility_Maturity_Model

The destination already exists. This setup exports the approved current assessment guidance into exact documents and sections with source metadata. It does not mirror every repository file, create a dataset, train an LLM, change visibility or publish actual assessment/participant data.

## 1. Configure the publishing credential once

1. Open https://huggingface.co/settings/tokens while signed into GarethFW.
2. Create a fine-grained token. If the page shows presets, choose Custom.
3. Name it `AI-AMM-GitHub-sync` so you can recognise its purpose.
4. Under repository permissions, select only the dataset `GarethFW/AI_Accessibility_Maturity_Model` and enable writing to that selected repository. Keep necessary read permissions. Do not enable broad user-level writing, billing, jobs or inference permissions for this sync. Some related gated-request permissions may be selected automatically by the interface; do not broaden the repository scope to change that behaviour.
5. Create the token and copy it securely. Never paste it into a chat, code file, issue, pull request, dataset card or screenshot.
6. Open https://github.com/Double-FW/AI-Accessibility-Maturity-Model/settings/secrets/actions
7. Choose **New repository secret**. Use the exact name `HF_TOKEN` (underscore, not a hyphen). Paste the token into the Secret field and save it.
8. If HF_TOKEN already exists and its credential has write access to this exact dataset, it can be reused. If it needs replacement, update that secret; do not add a duplicate name. Token scope changes are made in Hugging Face, not by renaming the GitHub secret.

The destination is fixed in `huggingface/export-config.json`. No HF_DATASET_ID variable or full destination URL is needed. Do not change the source/destination constants to publish another repository accidentally.

## 2. Run and verify

1. Open https://github.com/Double-FW/AI-Accessibility-Maturity-Model/actions/workflows/huggingface-sync.yml
2. Choose **Run workflow**, leave the branch on **main**, then choose the green **Run workflow** button.
3. Open the new run. Wait for tests, build and publish to complete successfully. A successful build alone is not publication.
4. Open the Hugging Face destination, select **Files and versions**, and inspect the latest commit, dataset card and `provenance.json`. The source commit must match the GitHub run’s main revision; the dataset/method version is 2.0.0.
5. Confirm `documents.jsonl`, `knowledge_chunks.jsonl`, `LICENSE`, `record_schema.json`, `validation_report.json`, `provenance.json` and the generated `README.md` are present.
6. If a step fails, use the actual failed step/log to diagnose it. Do not paste a token into chat. A permission error may mean the credential lacks write access to this exact existing dataset. A whitespace error requires replacing the secret with a clean token copy.

The workflow also runs on **Mondays at 07:37 UTC**. GitHub schedules can be delayed or disabled after public-repository inactivity. This is one-way publication: author changes in GitHub. Unmanaged raw files in Hugging Face are retained and do not automatically stay current.

## 3. Export scope and interpretation

- The explicit allow-list contains the 24 current assessment Markdown documents; all are required with LICENSE.
- Old `RAG_Reference.md`, `Source_Coverage.md` and `Sources/` copies are excluded from both views. Do not add them to the list to silence a warning.
- Templates, source register, change log and retrieval index are complete-document only. Substantive guidance also produces exact H1/H2 sections, preserving table context and fenced examples.
- Rows carry exact scope and decision-rule context, source path/commit/lines/hashes, draft status and fictional/template labels. Repeated context and overlapping dataset views are not independent evidence.
- No external linked material, repository code, workflow, setup instructions, credentials, raw operational evidence or generated Q&A is exported.
- Draft/pilot status and pending independent calibration, participant review and real pilot remain visible. A faithful export does not validate the method or its future evidence.

The generated dataset card is different from the GitHub README. Let the workflow generate it; do not upload the authoring README over it manually. Existing .gitattributes is expected and preserved.

## 4. Maintainer checks

From the repository root, after committing source/configuration changes:

```bash
python -m pip install -r huggingface/requirements.txt
python -m unittest discover -s tests -p 'test_amm_huggingface.py' -v
python scripts/export_huggingface.py --output ../ai-amm-export-check
```

The exporter reads committed HEAD, including configuration. Uncommitted edits are not its publication preview. Output must be outside the checkout. Tests use fictional fixtures and mocked publication; no live dataset writes occur during tests. No credentials are required for these local checks.

Missing required sources, unsafe/unapproved paths, changed licence or broken 36-strand/30-cell identities block export. New/renamed documents require explicit allow-list review. The seven managed destination files are committed together with a parent-revision guard. Foreign-source provenance, tampered exports or private GitHub source status block publication. No dataset is created and visibility is not changed.
