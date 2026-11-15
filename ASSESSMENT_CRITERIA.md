---
title: "Assessment criteria: six dimensions and five levels"
version: "2.0.0"
status: draft_for_practitioner_pilot
license: MIT
language: en-GB
---

# Assessment criteria: six dimensions and five levels

These are original **Double FW pilot criteria**, not external-model scores, statutory requirements or validated certification rules. Preserve the six dimensions and five levels in [AI AMM.md](AI%20AMM.md). Apply the [scope/authority](MODEL_SCOPE_AND_AUTHORITY.md), [runbook](ASSESSMENT_RUNBOOK.md) and [measurement method](MEASUREMENT_AND_COMPARABLE_EXPERIENCE.md) together.

## How to make a decision

Local IDs `AMM-Dn-xx` identify assessment strands; `AMM-Dn-Lx` identify level cells. These are new repository IDs, not WCAG, W3C, CP, CTL, ACT, SX or IDSO identifiers. A strand can use evidence also relevant elsewhere; record one evidence ID and distinct assertions rather than count the same result repeatedly.

For each scoped dimension, inspect **every applicable strand** against the relevant level cell. Record evidence IDs, dates, actual practice, contradictory findings, gaps and reviewer judgement in the templates. Justify exclusions with evidence, an owner and reconsideration trigger; unknown applicability remains open.

Use these assertion states: **supported**, **partly supported**, **observed weakness**, **insufficient evidence**, **not assessed**, or **not applicable with rationale**. A supported capability is not a technical test pass or legal conformity result. Record any observed barrier separately even when capability is supported.

Award a provisional dimension level only when all applicable strands support that cell’s capability in the declared scope and the relevant positive controls from earlier levels remain evidenced. **Level 1 is an observed reactive pattern, not a positive control that higher levels must retain.** From level 2 onwards, capability builds cumulatively. Higher levels replace the weaknesses of level 1. Missing evidence alone is never a level-1 finding.

If no complete level is supportable, use **Not determined** and report the strand findings. When practice is mixed, show scoped subprofiles and the limiting evidence; do not average levels or issue half-points. A lower evidenced level can be reported with higher-level strengths and a clear scope. Do not infer an organisation-wide level from six numbers.

Unmanaged material contradictions prevent a supported claim that depends on the contradicted capability. A serious blocked task is always reported and routed for action; a strong dimension elsewhere cannot cancel it. Managed incidents do not automatically mean an entire organisation has no capability: show the affected scope, response, residual harm and what the evidence does and does not support.

Scope and evidence rules apply to **every cell** below. Agree evidence sampling by consequence, coverage and period before assessment; include routine work and consequential failures, not only successful demonstrations. There is no universal sample count, elapsed-time threshold or acceptable satisfaction score. Record why the sample supports the claimed repetition and breadth, and what remains unexamined.

## Required UX, branding and QA assets

Under AMM-D3-02, each in-scope foundation/practice needs a versioned intended outcome, owning guidance, applicability, meaningful manual/AT/user evaluation and automatable checks where suitable. Include typography, colour, labelling/naming, alternatives and reading order, plus relevant interaction, motion, structure and language. State automation limits and the reason for manual-primary methods.

Each in-scope pattern/component needs design requirements; implementation techniques; delivery/evaluation methods; versioned reference implementations or owned gaps; manual and meaningful automated tests; user-oriented ACT-style task scripts; actual adoption/change evidence. Local ACT-style scripts are not automatically approved W3C ACT rules. Evaluate configured content, states, variants, themes, supported devices/AT and complete tasks. Follow reverse dependencies after change.

Brand-system work preserves recognisability, purpose, values and distinctiveness while evaluating identification, trust, expectations, value and resonance. These are research questions, not universal feelings inferred from a technical pass. See the owning [delivery crosswalk](DOUBLE_FW_DELIVERY_CROSSWALK.md).

## Dimension 1: Leadership and Governance

| Strand ID | Assessable requirement |
| --- | --- |
| AMM-D1-01 | **Commitments and authority.** Trace adopted commitments and applicable obligations to scope, decision rights and intended human outcomes. Keep aspirations and unconfirmed duties separate. |
| AMM-D1-02 | **Participation and challenge.** Give affected people usable ways to influence scope, interpretation and decisions; retain dissent, missing perspectives and the response. |
| AMM-D1-03 | **Resources and capacity.** Confirm actual funding or other capacity, protected time, specialist access and responsibility for delivery; a proposal is not an allocation. |
| AMM-D1-04 | **Programme and supplier accountability.** Connect programme priorities, procurement decisions and service dependencies to real receiving owners and escalation routes. |
| AMM-D1-05 | **Reporting and decisions.** Report capability, technical findings, human outcomes and legal conclusions separately, with uncertainties and decisions needed. |
| AMM-D1-06 | **Review and continuity.** Operate review, succession, reassessment and source-change processes; maintain decisions when staff, suppliers, systems or scope change. |

### Level evidence cells

| Cell / level | Observable capability in this dimension | Minimum evidence type | Insufficient or contradictory evidence | Reassessment trigger |
| --- | --- | --- | --- | --- |
| AMM-D1-L1 — Reactive | Observed decisions are driven by incidents or individuals; responsibility and resources are inconsistent. | Actual incident decisions, unowned work and accounts checked across the scoped unit. | No files supplied is insufficient evidence, not proof of Reactive practice. | A confirmed owner, adoption decision or changed organisational scope. |
| AMM-D1-L2 — Foundational | Scope, commitments, owners, participation and resource needs are documented for adoption or have begun locally. | Dated scope/authority records, affected people’s input, approved plans distinguished from proposed allocations. | A policy template or named sponsor with no confirmed remit cannot support Foundational. | Adoption, budget/capacity change or a missing receiving owner. |
| AMM-D1-L3 — Operational | Owners exercise delegated decisions and fund/sequence recurring work, with participation and evidence-backed reporting. | Sampled real decisions, resource allocation, handoffs and follow-up across the assessment period. | Unfunded actions, unconfirmed delegation or reports with no decisions block this cell. | A missed material commitment, ownership change or new supplier dependency. |
| AMM-D1-L4 — Integrated | Cross-functional strategy, funding, risks and service evidence influence each other through functioning review. | Records of cross-unit trade-offs, escalation resolved by authorised owners, continuity and reassessment. | A single well-run team cannot support an integrated organisation-wide claim. | Restructure, significant service change or unresolved cross-unit contradiction. |
| AMM-D1-L5 — Transformative | The organisation changes strategy using sustained participation and challenged outcome evidence, and maintains capability through change. | Repeated strategy decisions, disconfirming evidence acted on, successor/continuity exercise and implemented learning. | A vision statement, awards or assumed universal outcomes cannot demonstrate transformation. | Strategic promise change, persistent exclusion or failed continuity test. |

The common scope, sampling, assertion-state and progression rules above apply to every cell. Record case-specific evidence and all applicable strand findings; these examples of evidence are not a substitute for the judgement.

## Dimension 2: Culture and Capability

| Strand ID | Assessable requirement |
| --- | --- |
| AMM-D2-01 | **Role competence.** Define and evaluate practical accessibility skills for leadership, procurement, design, content, engineering, QA, HR, research and support as applicable. |
| AMM-D2-02 | **Learning in practice.** Link role-based learning, coaching and specialist support to changed work, not attendance alone. |
| AMM-D2-03 | **Champions and peer support.** Confirm sponsorship, coordination, protected capacity, continuing learning and operational handoffs; champions do not inherit every owner’s duties. |
| AMM-D2-04 | **Employment lifecycle.** Assess recruitment, application tools, onboarding, communication, work systems, development, progression, performance and exit where in scope. |
| AMM-D2-05 | **Adjustments and assistive technology.** Provide confidential, usable routes to request, fund, deliver, maintain and review adjustments and AT support without avoidable repeated disclosure. |
| AMM-D2-06 | **Culture and participation.** Observe how people raise barriers, challenge assumptions and influence priorities; do not make disabled colleagues represent everyone or perform unpaid diagnostic work. |

### Level evidence cells

| Cell / level | Observable capability in this dimension | Minimum evidence type | Insufficient or contradictory evidence | Reassessment trigger |
| --- | --- | --- | --- | --- |
| AMM-D2-L1 — Reactive | Skill gaps and support depend on individual advocacy; employee access problems are handled inconsistently. | Observed role practices, support routes and employment/adjustment cases in protected summary form. | An empty training register alone does not show absent skills or low culture. | New role, reported exclusion or discovery of an unusable adjustment route. |
| AMM-D2-L2 — Foundational | Role capability needs, accessible learning, participation and employment/AT support responsibilities are identified. | Skills/capacity plan, support ownership, accessible participation arrangements and scoped employment review. | Attendance targets or mandatory disclosure without usable support do not establish capability. | Onboarding change, new skill demand or inaccessible learning material. |
| AMM-D2-L3 — Operational | Relevant staff demonstrate skills in routine work; champions have capacity and employment/adjustment routes operate. | Observed work, learning applied to decisions, supported champion handoffs and minimised adjustment outcome evidence. | Completed courses without practice evidence or forced reliance on a volunteer block the claim. | Skill regression, delayed material adjustment or loss of specialist capacity. |
| AMM-D2-L4 — Integrated | Capability is coordinated across functions and employment stages; feedback changes learning and system decisions. | Cross-role work, adjustment continuity through handovers and evaluated changes to learning/workflows. | Uneven HR or supplier practice hidden by one strong team prevents a whole-scope claim. | Role redesign, shared-system change or recurring handover failure. |
| AMM-D2-L5 — Transformative | Disabled people sustain influence over capability and culture; succession and peer learning maintain changed practice. | Funded influence, challenged policy/practice changes, maintained skills through turnover and relevant outcome follow-up. | Network membership growth or a positive survey alone does not establish cultural transformation. | Turnover, cultural harm report or evidence that influence no longer changes decisions. |

The common scope, sampling, assertion-state and progression rules above apply to every cell. Record case-specific evidence and all applicable strand findings; these examples of evidence are not a substitute for the judgement.

## Dimension 3: Design, Delivery, and Operations

| Strand ID | Assessable requirement |
| --- | --- |
| AMM-D3-01 | **Requirements and lifecycle.** Connect applicable requirements, intended outcomes and adopted policy to discovery, planning, procurement, delivery, release, operation and retirement. |
| AMM-D3-02 | **UX and brand systems.** For in-scope foundations/practices and patterns/components, maintain the assets specified below and show actual adoption in configured services. |
| AMM-D3-03 | **Content and communications.** Manage accessible internal/external communications, documents and media through authoring, review, publishing, alternative formats and maintenance. |
| AMM-D3-04 | **Layered QA and release.** Use canonical requirements/test identities and appropriate automated, expert manual, AT and participant methods; retain gaps, actual results and authorised release decisions. |
| AMM-D3-05 | **Procurement and supplier lifecycle.** Assess selection, specifications, evaluation of supplier evidence, contracts/remedies, acceptance, renewal, material change, correction and exit; an ACR/VPAT is not independent proof. |
| AMM-D3-06 | **Support, complaints and correction.** Test discoverability and usability of employee/customer support, handovers, complaint/challenge routes, interim access, repair, retest and feedback learning. |

### Level evidence cells

| Cell / level | Observable capability in this dimension | Minimum evidence type | Insufficient or contradictory evidence | Reassessment trigger |
| --- | --- | --- | --- | --- |
| AMM-D3-L1 — Reactive | Delivery and support are mainly reactive, with inconsistent requirements, supplier checks or corrective follow-up. | Sampled releases, supplier choices, inaccessible communications and incident/support traces. | No automated scan or missing document alone cannot determine delivery maturity. | An essential barrier, new release or supplier procurement. |
| AMM-D3-L2 — Foundational | Scope, delivery owners, requirements and plans for systems, suppliers, communications and support are established. | Gap inventory, linked UX/brand assurance plan, proposed tests, procurement requirements and support/correction plan. | Planned controls do not count as executed tests or accepted supplier performance. | First implementation, changed requirements or a missing assurance asset. |
| AMM-D3-L3 — Operational | Requirements and layered evidence are used in repeated delivery; supplier/support issues are owned, corrected and retested. | Actual configured assets, release decisions, manual/AT and relevant user evidence, supplier assessment and restored-task retests. | A clean scan, unverified ACR or closed issue without restored-task evidence blocks an unqualified claim. | Component/content/model change, failed critical task or missed correction. |
| AMM-D3-L4 — Integrated | Shared systems, supplier lifecycle and complete journeys are governed together, with reverse-dependency change control. | Cross-consumer adoption, variant/state coverage, renewal/change decisions and regression through affected journeys. | A reference component pass does not prove configured content, integration or whole-service access. | Foundation/token change, contract renewal, integration drift or shared defect. |
| AMM-D3-L5 — Transformative | The organisation prevents recurring classes of exclusion by changing systems, procurement and operations using challenged evidence. | Implemented shared-cause prevention, maintained reference assets, retirement/transition evidence and outcome follow-up across relevant consumers. | More automation, zero reported defects or a design-system catalogue alone cannot establish transformation. | Recurrent exclusion, new product modality or evidence that prevention no longer works. |

The common scope, sampling, assertion-state and progression rules above apply to every cell. Record case-specific evidence and all applicable strand findings; these examples of evidence are not a substitute for the judgement.

## Dimension 4: Data, Measurement, and Comparable Experience

| Strand ID | Assessable requirement |
| --- | --- |
| AMM-D4-01 | **Outcome and task definitions.** Define meaningful tasks and correct end states, including navigation, comprehension, effort/time, choice, continuity, recovery, dignity and satisfaction. |
| AMM-D4-02 | **Inclusive research.** Plan accessible participation and include non-entry, abandonment, relevant access methods/intersections and missing voices; preserve influence and disagreement. |
| AMM-D4-03 | **Ethical measurement.** Minimise data, separate participation consent from processing decisions, protect small groups and review retention, access, providers and any proposed reuse. |
| AMM-D4-04 | **Comparability and uncertainty.** Specify context, denominators, scale, method/version, chosen or forced assistance, missingness and uncertainty before comparison; do not use universal speed or satisfaction thresholds. |
| AMM-D4-05 | **Finding integrity.** Keep observation, participant account, interpretation and hypothesis distinct; no complaints is not satisfaction and a technical pass is not a complete experience. |
| AMM-D4-06 | **Learning and decision value.** Use bounded findings to change priorities and practices; retain negative cases, unresolved issues, retest and alternative explanations for apparent improvement. |

### Level evidence cells

| Cell / level | Observable capability in this dimension | Minimum evidence type | Insufficient or contradictory evidence | Reassessment trigger |
| --- | --- | --- | --- | --- |
| AMM-D4-L1 — Reactive | Measurement relies on isolated proxies or anecdote, without consistent task definitions or evidence limits. | Actual dashboard use and decision records showing proxy dependence or missing context. | No survey supplied is not proof that no research or outcome evidence exists. | A misleading claim, new task or missing/contradictory evidence. |
| AMM-D4-L2 — Foundational | Tasks, outcomes, ethical data decisions and accessible research methods are defined for the scoped decision. | Protocol, measure dictionary, recruitment/access plan and explicit missing-data/assistance definitions. | An unpiloted question is not a validated instrument; a sample plan is not a result. | Protocol/instrument change, new audience or changed data purpose. |
| AMM-D4-L3 — Operational | Collected technical, operational and participant evidence supports bounded findings and actual decisions. | Defined denominators/context, correct-end-state observations, chosen/forced support and participant accounts linked to decisions. | Satisfaction without completion evidence, excluded non-completers or unsupported causal claims block the cell. | New exclusion pattern, incompatible export or material non-response. |
| AMM-D4-L4 — Integrated | Findings are compared across relevant journeys/time with stable definitions, protected data and transparent uncertainty. | Comparable measurement versions, distribution/negative-case review and decisions explaining changed scope and alternative causes. | Changing denominators or averaging away severe barriers prevents a whole-scope claim. | Definition, population, provider or collection-method change. |
| AMM-D4-L5 — Transformative | The organisation challenges and improves its measurement and strategy with affected people, preserving limits and dissent. | Revised methods based on identified bias, implemented decisions, retest and sustained ethical review of evidence use. | A statistical-significance label, LLM rating or sentiment score is not sufficient evidence. | Privacy concern, missing population or failure of findings to inform action. |

The common scope, sampling, assertion-state and progression rules above apply to every cell. Record case-specific evidence and all applicable strand findings; these examples of evidence are not a substitute for the judgement.

## Dimension 5: AI, Automation, and Intelligent Systems

| Strand ID | Assessable requirement |
| --- | --- |
| AMM-D5-01 | **Inventory and purpose.** Know actual AI uses, suppliers, versions, roles, affected people and purpose; record justified non-use and avoid unsupported blanket legal classifications. |
| AMM-D5-02 | **Selection, data and procurement.** Evaluate accessibility, relevant model/data risks, contractual change notices, data flows and supplier claims for the actual use; verify sources through specialist routes. |
| AMM-D5-03 | **Access and outcome evaluation.** Evaluate complete interfaces and AI-specific behaviours, generated outputs, uncertainty, meaningful alternatives and consequential outcomes with appropriate specialist/participant evidence. |
| AMM-D5-04 | **Human oversight and permissions.** Confirm competent human authority, accessible intervention, challenge, stop/override, minimum permissions and separation of untrusted retrieved text from authorised actions. |
| AMM-D5-05 | **Release, monitoring and change.** Link release decisions to evidence and monitor model, prompt, retrieval, renderer, tools, permissions and supplier changes; re-evaluate affected tasks and record limits. |
| AMM-D5-06 | **Incident, recovery and retirement.** Detect and investigate harms, communicate accessibly, restore access, suspend/rollback safely where appropriate, support remedy and govern replacement or retirement. |

### Level evidence cells

| Cell / level | Observable capability in this dimension | Minimum evidence type | Insufficient or contradictory evidence | Reassessment trigger |
| --- | --- | --- | --- | --- |
| AMM-D5-L1 — Reactive | AI use or purchasing is reactive or poorly understood, with inconsistent inclusion oversight. | Actual use discovery, decisions and incident accounts showing ungoverned operation or adoption. | No deployed AI is not low maturity; unknown inventory is not a verified absence. | New AI discovery, supplier change or reported harm. |
| AMM-D5-L2 — Foundational | AI inventory, purpose, actual owners and review/oversight/evaluation plans exist, including a reasoned non-use route. | Inventory and scope record, supplier/data questions, participation and oversight plan; readiness-only scope if no deployment. | An AI ethics statement without real uses/roles or a planned test counted as run cannot support the cell. | Proposed adoption, new data/tool permission or unclear legal role. |
| AMM-D5-L3 — Operational | Relevant lifecycle controls operate for the scoped uses, or actual non-use governance and safe readiness exercises are evidenced. | Real selection/release/monitoring decisions, accessible intervention and task evaluation; actual non-use decisions and labelled drills where appropriate. | An LLM self-rating, assumed fairness from an accessible UI or simulation presented as live operation blocks the claim. | Model/prompt/retrieval/tool change, adverse decision or failed oversight. |
| AMM-D5-L4 — Integrated | Shared AI dependencies, service outcomes, oversight and supplier changes are managed together across affected uses. | Versioned affected-use maps, exercised change/incident handoffs and cross-surface regression; readiness claims remain bounded. | One model test cannot cover every integration or future output; ungoverned uses cannot be silently excluded. | Material supplier update, new action permission or ineffective fallback. |
| AMM-D5-L5 — Transformative | The organisation learns across uses and may redesign, decline, suspend or retire AI to sustain participation and trust. | Implemented decisions based on affected people’s evidence, effective recovery/retirement and recurring oversight learning. | AI deployment volume or predicted benefits alone cannot establish transformation or live performance. | Persistent exclusion, strategic use change or inability to restore safe access. |

The common scope, sampling, assertion-state and progression rules above apply to every cell. Record case-specific evidence and all applicable strand findings; these examples of evidence are not a substitute for the judgement.

## Dimension 6: Ethics, Risk, and Organisational Trust

| Strand ID | Assessable requirement |
| --- | --- |
| AMM-D6-01 | **Rights and applicability.** Establish which legal, contractual and adopted policy requirements apply through competent review; maintain separate conformity and maturity conclusions. |
| AMM-D6-02 | **Risk and fair outcomes.** Assess exclusion, safety, financial and employment consequences, dignity and disadvantage; prioritise actual impact rather than complaint volume or average scores. |
| AMM-D6-03 | **Privacy and responsible information use.** Protect participant and employee records, limit collection and inferences, manage access/retention and forbid unapproved training reuse or public raw evidence. |
| AMM-D6-04 | **Accessible remedy.** Provide usable information, correction, complaints, explanation and challenge routes with actual owners; verify restored access rather than count closed tickets. |
| AMM-D6-05 | **Trust, brand and claims.** Test consistency between organisational promises and experience, including POURS lenses; qualify evidence, avoid assumed feelings, endorsement and unsupported ESG claims. |
| AMM-D6-06 | **Independent challenge and resilience.** Use proportionate separation of evidence preparation, review and approval; test escalation, continuity and learning, preserving conflicts and unverified claims. |

### Level evidence cells

| Cell / level | Observable capability in this dimension | Minimum evidence type | Insufficient or contradictory evidence | Reassessment trigger |
| --- | --- | --- | --- | --- |
| AMM-D6-L1 — Reactive | Risks, claims or remedies are managed ad hoc with unclear evidence or authority. | Actual cases and claims showing unresolved impact, unsupported assertions or inconsistent remedy. | An absent risk log alone does not establish absence of risk work. | Material harm, disputed claim or inaccessible remedy. |
| AMM-D6-L2 — Foundational | Rights/risk/privacy scope, review ownership, claim limits and usable remedy plans are established. | Applicability questions, minimised data decisions, conflict records and named review/remedy responsibilities. | A maturity label cannot substitute for a legal decision or confer data permission. | Scope/legal-source change, new data use or disputed authority. |
| AMM-D6-L3 — Operational | Risk, information use, claims and remedies are reviewed in practice and correction is verified for affected tasks. | Real review decisions, access restrictions, challenged claims and remedy/retest records with unresolved consequences visible. | A favourable rating, consent checkbox or complaint closure without investigation cannot support the cell. | Incident, adverse decision, privacy issue or failed corrective action. |
| AMM-D6-L4 — Integrated | Governance connects risks and evidence across functions, suppliers and journeys, with independent challenge and continuity. | Cross-function risk decisions, conflicts resolved with authority, usable escalation and exercised continuity. | Committee consensus without evidence or inability to challenge a preparer’s decision prevents an integrated claim. | New shared risk, ownership change or ineffective escalation. |
| AMM-D6-L5 — Transformative | The organisation changes incentives, promises and practices using sustained challenge and verified learning, preserving rights and trust. | Implemented strategic corrections, consequential claim restraint, participant influence and maintained remedy through change. | Claims of universal trust, compliance or ESG benefit without bounded evidence do not establish transformation. | Broken promise, recurrent rights impact or suppressed negative evidence. |

The common scope, sampling, assertion-state and progression rules above apply to every cell. Record case-specific evidence and all applicable strand findings; these examples of evidence are not a substitute for the judgement.

## Review and follow-up

Record the proposed level or Not determined, evidence period, scope/coverage limits, unresolved material barriers, higher-level strengths and the next decision. The review/approval owner must be a real person with confirmed authority. Where one person fills several roles, record the limitation and obtain proportionate outside challenge for consequential claims.

Use [worked cases](WORKED_ASSESSMENT_EXAMPLES.md) for desk exercises and [validation/adoption](VALIDATION_AND_ADOPTION.md) for what has actually been checked. Do not treat this documentation or its examples as independent validation of the rubric.
