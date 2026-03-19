# Research Architect Plan — ESS Paper Rewrite
**Run:** run-20260319-141500
**Date:** 2026-03-19
**Agent:** research-architect

---

## Canonical Title
**From Signals to Decisions: A Framework for Executive Signal Synthesis in AI Systems**

Author: Nina Cressoni
Affiliation: Flowity AI (downstream application context only)
Target: Zenodo preprint, Lattes-compatible, FAPESP PIPE positioning

---

## Primary Research Question

Can a structured methodological framework — Executive Signal Synthesis (ESS) — systematically transform fragmented, heterogeneous organizational signals into interpretable, executive-level decision intelligence using lightweight AI techniques, and can a prototype implementation validate the core feasibility of this pipeline?

---

## Subquestions

1. **Definition:** What constitutes a "business signal," and how can signals be formally defined as machine-readable, decision-relevant units distinct from raw data or documents?
2. **Synthesis distinction:** How does signal synthesis differ from aggregation (counting/grouping) and summarization (compression), and why does this distinction matter for decision support?
3. **Framework design:** What four-stage pipeline architecture (Ingestion → Classification → Clustering → Synthesis) enables cross-source pattern detection and structured executive output?
4. **Prototype validation:** Can a lightweight Python prototype using TF-IDF and K-means clustering demonstrate feasibility of cross-source pattern detection on synthetic organizational signals?
5. **Limitations:** What are the methodological constraints of keyword-based classification, TF-IDF vectorization, and K-means for signal synthesis, and how do these limit generalizability?
6. **Future directions:** What research directions — semantic embeddings, graph-based detection, formal evaluation metrics, human-in-the-loop validation — would advance ESS beyond prototype stage?

---

## Scope of the Rewrite

### What This Paper IS:
- A **methodological research contribution** proposing ESS as a formal framework
- A **prototype validation artifact** demonstrating feasibility (not production deployment)
- An **academically credible preprint** suitable for Zenodo and FAPESP positioning
- Grounded in decision support systems, explainable AI, and information synthesis literature

### What This Paper IS NOT:
- A product description or commercial pitch
- A paper about multi-agent AI systems or automation workflows
- A paper about any specific AI vendor or tooling
- A paper exclusively for "founder-led" organizations (too narrow)

---

## Required Structural Mapping

| Section | Current State | Rewrite Action |
|---------|--------------|----------------|
| Abstract | Missing | **ADD** — structured abstract with problem, method, results, contribution |
| 1. Problem | Adequate skeleton | **EXPAND** — add literature context, quantify the gap |
| 2. Why Current Systems Fail | Thin | **EXPAND** — ground in BI/DSS literature; name specific failure modes |
| 3. Definition: Signals | Adequate | **REFINE** — add formal definition, cite signal theory |
| 4. Definition: Synthesis | Adequate | **REFINE** — sharpen distinction from aggregation/summarization |
| 5. ESS Framework | Adequate | **EXPAND** — full table + stage descriptions + theoretical grounding |
| 6. Implementation Mapping | Thin | **EXPAND** — code-grounded, include metrics from evaluation_report |
| 7. Example Flow | Thin | **EXPAND** — traced end-to-end scenario with actual prototype outputs |
| 8. Implications | Placeholder | **REWRITE** — research and applied implications with nuance |
| 9. Limitations | Good | **KEEP + EXPAND** — add methodological honesty section |
| 10. Future Work | List only | **EXPAND** — specific research directions with rationale |
| 11. References | Empty | **ADD** — 8–12 traceable academic citations |

---

## Canonical Framing Rules (enforced throughout)

- Rename "External AI Brain Systems" → "Executive Signal Synthesis (ESS)" throughout
- Remove "founder-led organizations" → use "organizations" or "executive decision-makers"
- No mention of Claude, AI agents, multi-agent orchestration, or automation tooling
- Flowity AI: mention once in affiliation context only, not as paper subject
- All claims must be grounded in either: (a) prototype evidence, or (b) cited literature
- Prototype limitations must be stated explicitly — no overclaiming

---

## Evidence Needed (for subsequent phases)

### Document Evidence (Phase 2):
- src/classify.py — keyword classification rules and urgency logic
- src/cluster.py — TF-IDF + KMeans implementation
- src/synthesize.py — cluster-to-summary logic
- src/generate_brief.py — brief generation logic
- src/ingest.py — signal normalization
- src/evaluate.py — evaluation metrics
- outputs/evaluation_report.md — actual metric values
- outputs/sample_decision_brief.md — actual prototype output
- docs/framework_mapping.md — framework-to-code alignment
- run_pipeline.py — end-to-end execution proof

### Web/Literature Evidence (Phase 3 — minimum required):
1. Decision Support Systems (DSS) literature — Simon (1960), Power (2002)
2. Explainable AI (XAI) — Gunning et al. (2019), DARPA XAI program
3. Organizational signal processing / sense-making — Weick (1995)
4. Information synthesis / knowledge synthesis — concept from IS literature
5. Business intelligence limitations — Negash (2004) or similar
6. NLP for enterprise/organizational data — recent survey

---

## Success Criteria for Final Paper

- [ ] Abstract present and structured
- [ ] All 11 sections populated with non-placeholder content
- [ ] At least 8 traceable references in Section 11
- [ ] Prototype metrics cited in Section 6 (from evaluation_report.md)
- [ ] Limitations section is explicit and honest (not marketing-softened)
- [ ] No mention of Claude, agents, orchestration, or private tooling
- [ ] ESS framing consistent throughout (no "External AI Brain" residue)
- [ ] Suitable for Zenodo DOI submission
- [ ] FAPESP-level academic rigor
