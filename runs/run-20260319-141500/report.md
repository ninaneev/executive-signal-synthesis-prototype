# From Signals to Decisions: A Framework for Executive Signal Synthesis in AI Systems

**Author:** Nina Cressoni
**Affiliation:** Flowity AI
**Status:** Research preprint
**Version:** run-20260319-141500
**Date:** March 2026

---

## Abstract

Organizations continuously generate heterogeneous information across operational systems — from customer interactions and support activity to internal discussions, market observations, and incident reports. Despite this volume, organizational information rarely reaches decision-makers in a structured, prioritized, or actionable form. This gap creates conditions of executive decision latency: leadership acts on incomplete pattern recognition, delayed synthesis, and fragmented context.

This paper proposes **Executive Signal Synthesis (ESS)** — a methodological research framework for transforming fragmented organizational signals into structured, explainable, executive-level decision intelligence. ESS defines signals as discrete, decision-relevant informational units and synthesis as a process distinct from aggregation or summarization, requiring cross-source pattern recognition and explicit interpretive reasoning.

The framework comprises four analytical stages: Ingestion, Classification, Clustering, and Synthesis. A prototype implementation in Python — using TF-IDF vectorization and K-means clustering over a synthetic signal dataset — was developed to evaluate the feasibility of the pipeline. Prototype evaluation results demonstrate that heterogeneous signals from multiple organizational source types can be grouped into cross-source patterns (cross-source ratio: 0.67; signal compression ratio: 1.67x) and transformed into structured executive decision briefs.

ESS is presented as a methodological research contribution rather than a production system. Prototype limitations are explicit: synthetic data, keyword-based classification, absence of semantic embeddings, and exploratory evaluation metrics. Future research directions include semantic signal representation, graph-based pattern detection, formal decision quality evaluation, and human-in-the-loop validation.

---

## 1. Problem

Modern organizations continuously generate large volumes of heterogeneous information. Customer support interactions, sales conversations, internal meeting notes, product usage observations, community discussions, and operational incident reports constitute a continuous stream of organizational data. Each source is independently managed, formatted differently, and consumed — if consumed at all — in isolation.

Despite this volume, this information rarely reaches decision-makers in a form that is structured, prioritized, or actionable. The result is a persistent and systematic gap: the signals an organization produces do not translate into the decisions its leadership can make.

This gap is not primarily a data collection problem. Most organizations have abundant raw information. The problem is structural: information remains distributed across source systems, lacks a shared schema, and requires significant manual effort to interpret in combination. Executives operate under conditions of signal fragmentation — processing isolated reports rather than synthesized intelligence — which increases decision latency and reduces strategic coherence.

Daft and Lengel (1986) formally characterized this as an *equivocality* problem: organizational actors face not a shortage of data but a surplus of uninterpreted, ambiguous information requiring clarity and frame construction. Weick (1995) described the same challenge through the lens of organizational sensemaking — the ongoing process by which actors construct plausible interpretations of environmental cues. Critically, sensemaking is a cognitive process that current information systems do not systematically support at the executive level.

This research proposes that the gap between organizational signal production and executive decision-making can be partially addressed through a systematic, computational methodology — one that does not replace executive judgment but structures the information environment for it.

---

## 2. Why Current Systems Fail

Existing decision support and analytics tools do not close this gap. Their failure is structural, not incidental.

**Business intelligence (BI) platforms** are designed for data retrieval and metric presentation. Dashboards surface numbers; reports aggregate rows. They answer queries but do not generate interpretations. The assumption is that the analyst or executive will perform the synthesis step — which is precisely the step that scales poorly under information volume and source heterogeneity.

**Search systems** retrieve documents matching a query. They do not detect patterns across documents, assess cross-source significance, or produce decision-relevant abstractions.

**Summarization tools** condense individual documents. They operate on single inputs and produce compressed versions of those inputs. They do not cross-reference multiple heterogeneous sources to detect emergent patterns.

Gorry and Scott Morton (1971) established the foundational taxonomy of management information needs, distinguishing structured decisions (amenable to algorithmic support) from semi-structured and unstructured decisions (requiring human judgment augmented by system intelligence). Executive decision-making is predominantly semi-structured to unstructured — the category where existing BI and search tools provide the least support.

Shim et al. (2002) traced the evolution of decision support technology over three decades, observing that each generation of DSS extended the information sources it could integrate but consistently stopped short of providing synthesis-level intelligence. The trend toward richer, more automated decision support has been identified, but not systematically realized.

The fundamental failure of current systems is not their inability to access data. It is the absence of a systematic methodology for transforming fragmented signals into structured intelligence — what this paper calls *synthesis*. This missing layer sits between raw data processing and executive cognition, and its absence forces executives to perform cross-source interpretation manually, under time pressure, with incomplete and inconsistently formatted inputs.

---

## 3. Definition: Signals

The term *signal* is used in this framework with a specific technical meaning, distinct from its common use in noise-signal metaphors.

**Definition.** A *business signal* is any discrete, machine-readable unit of organizational information that carries implicit decision-relevant content.

Signals may originate from multiple source types, including but not limited to:

- customer support interactions (tickets, chat transcripts)
- sales conversations (call summaries, prospect notes)
- product usage observations (behavioral data, drop-off events)
- community activity (forum posts, social observations)
- internal meeting notes (recorded discussions, decisions)
- operational incident reports (system failures, process exceptions)
- market observations (competitive intelligence, price signals)

Signals share several structural properties:

1. **Heterogeneity** — signals originate from different systems, in different formats, at different frequencies.
2. **Partial observability** — no single signal provides a complete picture of any organizational state.
3. **Schema absence** — signals across sources do not share a common data model.
4. **Latent value** — the decision-relevant content of any signal is not fully apparent from the signal alone; it emerges through cross-signal interpretation.

This last property is critical. A support ticket describing "onboarding confusion" has limited decision value in isolation. A sales note describing "prospect drop-off due to complexity" has limited value in isolation. When grouped with an internal meeting note about "activation delays," the combined signal cluster becomes a meaningful organizational pattern warranting executive attention.

Weick's (1995) sensemaking framework characterizes organizational actors as processing *cues* — discrete informational stimuli extracted from the environment — rather than complete data objects. Klein et al.'s (2006) data-frame theory further models the bidirectional relationship between incoming cues and the cognitive frames that interpret them. ESS operationalizes this theoretical understanding: signals are the cues; synthesis is the frame-construction process.

---

## 4. Definition: Synthesis

Synthesis — as used in this framework — requires precise differentiation from two adjacent and often conflated operations: *aggregation* and *summarization*.

**Aggregation** is counting or grouping: counting signals by source, by type, by time period. Aggregation preserves the original units and adds a quantitative dimension. It does not interpret.

**Summarization** is compression: condensing a document or corpus into a shorter version. Summarization preserves the semantic content of individual inputs but does not generate new interpretive frames from their combination.

**Synthesis** is distinct from both. Signal synthesis involves:

1. **Cross-source pattern recognition** — detecting that signals from multiple, independent sources exhibit structural similarity or convergence.
2. **Organizational significance assessment** — determining whether a detected pattern has decision-relevant implications for the organization.
3. **Interpretive reasoning** — producing a structured interpretation that explicitly traces from source signals to organizational insight, with reasoning available for inspection.

The output of synthesis is not a compressed version of inputs. It is a new artifact — a *decision frame* — constructed from the combined evidence of multiple signals and designed to be actionable by an executive decision-maker.

This distinction has direct methodological consequences. A summarization tool applied to five signals about onboarding would produce five shorter descriptions. An ESS synthesis would detect that three of those signals, from three independent organizational sources, converge on a shared pattern — onboarding friction with revenue implications — and produce a single, prioritized, decision-directed interpretation.

The synthesis concept aligns with Zhao et al.'s (2020) treatment of multi-source knowledge fusion and with Dong and Srivastava's (2015) technical framework for heterogeneous data integration, both of which position synthesis as a fundamentally different operation from mere data collection or compression.

---

## 5. The ESS Framework

Executive Signal Synthesis (ESS) is a methodological research framework for transforming fragmented organizational signals into structured, explainable, executive-level decision intelligence.

ESS is proposed as a *framework* in the methodological sense: a structured set of analytical stages, each with defined input, operation, and output, which together constitute a complete signal-to-decision processing pipeline. It is not a product specification or a system architecture; it is a research-level description of what such a pipeline must accomplish.

### Framework Overview

ESS operates across four analytical stages:

| Stage | Input | Operation | Output |
|---|---|---|---|
| **1. Ingestion** | Heterogeneous signal sources | Normalize into structured intermediate representation | Structured signal records |
| **2. Classification** | Structured signal records | Assign type, domain, urgency, and risk metadata | Tagged signal records |
| **3. Clustering** | Tagged signal records | Detect cross-source patterns via similarity grouping | Signal clusters |
| **4. Synthesis** | Signal clusters | Generate decision-relevant interpretation and executive brief | Executive decision artifact |

### Stage Descriptions

**Ingestion** is the boundary operation of the framework. It receives signals from heterogeneous sources — each with its own format, schema, and vocabulary — and normalizes them into a structured intermediate representation suitable for downstream analytical processing. Normalization includes at minimum: common field mapping, text standardization, and source attribution.

**Classification** assigns analytical metadata to each signal. Classification serves two purposes: (a) it enables downstream filtering and prioritization by signal type and urgency; (b) it adds the organizational context — domain, risk profile, impact category — that is necessary for synthesis to produce meaningful interpretations rather than generic pattern descriptions.

**Clustering** is the cross-source pattern detection stage. It groups signals by semantic or structural similarity, with the goal of identifying *convergent signals* — cases where independent organizational sources are producing information that, in combination, indicates a shared organizational state or emerging issue. Cross-source clustering is the technical mechanism that makes synthesis different from single-document analysis.

**Synthesis** transforms cluster-level evidence into an executive decision artifact — a structured brief that explicitly traces from signal sources to pattern to organizational interpretation to recommended action. The brief must be legible to an executive decision-maker and must expose enough of its reasoning chain to be trusted and, where necessary, questioned.

### Relationship to Explainability

Miller (2019) and Arrieta et al. (2020) establish that AI-generated outputs used in organizational decision contexts must be explainable in ways that are contrastive (why this interpretation rather than another?), selective (highlighting the most decision-relevant factors), and socially appropriate for the intended audience. ESS is designed with this requirement in mind: the traceable path from source signals through classification, clustering, and synthesis to executive recommendation constitutes the explanation chain.

At prototype stage, this chain is implemented through interpretable methods (keyword classification, TF-IDF, K-means) with explicit source attribution at every stage. More sophisticated explanation mechanisms are identified as a future research priority.

---

## 6. Implementation Mapping

The ESS framework is directly instantiated in an open-source Python prototype. Each framework stage maps to a dedicated implementation module.

### Stage-to-Module Mapping

| ESS Stage | Module | Operation |
|---|---|---|
| Ingestion | `src/ingest.py` | `load_signals()` reads JSON signal dataset; `normalize_signals()` lowercases text |
| Classification | `src/classify.py` | `classify_signal()` applies keyword rules for urgency, churn risk, revenue risk; `apply_classification()` joins tags to DataFrame |
| Clustering | `src/cluster.py` | `cluster_signals()` applies TF-IDF vectorization and K-means (k=3, random_state=42) |
| Synthesis | `src/synthesize.py` | `synthesize_clusters()` aggregates per-cluster evidence: count, sources, sample signal, evidence IDs |
| Brief Generation | `src/generate_brief.py` | End-to-end pipeline orchestration; writes structured markdown executive brief |
| Evaluation | `src/evaluate.py` | Computes cross-source ratio, compression ratio, urgency distribution |

The complete pipeline is executable via a single command: `python run_pipeline.py`, confirming prototype reproducibility.

### Implementation Characteristics

**Ingestion** (`src/ingest.py`): Signals are loaded from a JSON file (`data/synthetic_business_signals.json`) into a pandas DataFrame. Text normalization (lowercase) prepares inputs for NLP processing. This lightweight implementation confirms the structural feasibility of the ingestion stage while explicitly omitting production concerns (streaming, authentication, schema validation).

**Classification** (`src/classify.py`): Signal classification uses keyword-based rules. Urgency is assigned as "high" when signal text contains terms associated with operational friction ("delay," "confusion," "struggling"). Churn and revenue risk flags are applied based on business-domain keywords. This rule-based approach is interpretable and auditable but does not generalize beyond the training vocabulary. It represents the lower bound of classification sophistication — sufficient for prototype validation, insufficient for production deployment.

**Clustering** (`src/cluster.py`): TF-IDF vectorization converts signal texts into term-weighted feature vectors. K-means clustering (k=3) groups signals by vector similarity. The choice of TF-IDF + K-means reflects an intentional design decision: these methods are interpretable, computationally lightweight, and well-understood — properties that prioritize validation clarity over representational richness. Limitations of this approach are discussed in Section 9.

**Synthesis** (`src/synthesize.py`): Cluster summaries are constructed by aggregating evidence from all signals within each cluster: signal count, list of unique source types, a sample signal text, and traceable signal IDs. This produces per-cluster records that are the direct inputs to executive brief generation.

**Brief Generation** (`src/generate_brief.py`): The executive brief is written as structured markdown, organizing patterns by cluster with source attribution, evidence counts, and suggested executive actions. The output format is designed to be scannable by a decision-maker in under two minutes.

### Prototype Evaluation Results

The prototype was evaluated on a synthetic dataset of 5 business signals drawn from 6 organizational source types.

| Metric | Value |
|---|---|
| Total signals processed | 5 |
| Total clusters produced | 3 |
| Cross-source clusters | 2 |
| Cross-source ratio | 0.67 |
| Signal compression ratio | 1.67× |
| High-urgency signals detected | 3 |

*Source: `outputs/evaluation_report.md`*

**Cross-source ratio (0.67)** indicates that 2 of 3 clusters successfully grouped signals from multiple independent organizational sources — the primary validation target for ESS's cross-source pattern detection claim.

**Signal compression ratio (1.67×)** indicates that the system reduced 5 raw signals to 3 decision-relevant clusters — a modest but demonstrable compression into structured patterns.

These results are exploratory. The dataset is synthetic and small. They demonstrate the structural feasibility of the ESS pipeline but do not support generalization claims about performance at scale or on real organizational data.

---

## 7. Example Flow

The following example traces a complete ESS pipeline execution using actual prototype output.

### Input Signals

Three signals are received from independent organizational sources:

| Signal ID | Source | Text |
|---|---|---|
| sig_002 | sales_call_summary | "prospect concerned about implementation effort and time to see value" |
| sig_003 | meeting_note | "team discussed repeated onboarding delays affecting enterprise clients" |
| sig_001 | support_ticket | "customer reports confusion during onboarding and unclear first report interpretation" |

### Stage 1: Ingestion

All three signals are normalized into structured records. Text is lowercased and loaded into a uniform DataFrame with fields: `id`, `source`, `text`.

### Stage 2: Classification

Keyword classification assigns metadata:
- sig_002: `urgency=medium`, `possible_revenue_risk=True` (contains "implementation")
- sig_003: `urgency=high`, `possible_revenue_risk=True` (contains "delay", "enterprise")
- sig_001: `urgency=high` (contains "confusion")

### Stage 3: Clustering

TF-IDF vectorization encodes the signal texts as term-frequency feature vectors. K-means groups sig_001 and sig_003 into **Pattern 1** (both share vocabulary around "onboarding" delays and client impact); sig_002 is assigned to **Pattern 0** as a distinct signal on implementation effort.

**Pattern 1** is a cross-source cluster: it spans `meeting_note` and `support_ticket` — two independent organizational sources converging on the same problem domain.

### Stage 4: Synthesis

The synthesis stage produces the following cluster-level output for Pattern 1:

```
Pattern 1:
  Signal Count: 2
  Sources: meeting_note, support_ticket
  Example: "team discussed repeated onboarding delays affecting enterprise clients"
  Evidence IDs: sig_003, sig_005
```

*Source: outputs/sample_decision_brief.md*

### Executive Decision Brief

The generated executive brief surfaces Pattern 1 as a priority item:

> **Pattern 1 — Cross-source signal: Onboarding delays**
> Two independent organizational sources (internal meeting, support ticket) report repeated onboarding delays affecting enterprise clients.
> **Suggested action:** Prioritize investigation of enterprise onboarding process — signals appear in multiple business contexts indicating systemic rather than isolated occurrence.

This output traces directly from source signals to organizational interpretation. The reasoning chain is exposed: which signals contributed, from which sources, and why this pattern warrants executive attention.

---

## 8. Implications

The research presented here has implications at two levels: methodological and applied. These implications are stated with appropriate epistemic caution — the current prototype is exploratory, and stronger claims require validation at scale on real organizational data.

### Methodological Implications

**For decision support systems research:** ESS proposes a specific architectural response to a gap identified in DSS literature since Gorry and Scott Morton (1971): the need for semi-structured decision support at the executive level. The four-stage signal-to-decision pipeline provides a concrete, implementable architecture that can be studied, extended, and evaluated empirically. It grounds the abstract concept of "executive decision intelligence" in a testable methodological framework.

**For explainable AI research:** ESS suggests that explainability in organizational AI systems is not just a property of individual model outputs but of the entire information pipeline — from signal ingestion through classification, clustering, and synthesis. The traceable evidence chain produced by ESS aligns with Miller's (2019) argument that satisfying explanations must be selective and contrastive, not exhaustive. Studying how different synthesis architectures affect executive trust and decision quality is an open research problem.

**For organizational information processing:** ESS provides a computational instantiation of sensemaking processes described by Weick (1995) and Klein et al. (2006). This opens research questions about whether computational sensemaking can complement rather than compete with human organizational cognition, and under what conditions automated synthesis may introduce interpretation biases.

### Applied Implications

If signal synthesis becomes systematic and reproducible in organizational contexts, it may enable:

- **Reduced executive cognitive load** — pre-synthesized signal intelligence reduces the manual cross-referencing burden on leadership (Leidner & Elam, 1995).
- **Earlier cross-functional risk detection** — cross-source clustering may surface emerging issues before they appear in any single reporting system.
- **Traceable decision evidence** — synthesis outputs with explicit evidence chains create auditable decision records, supporting governance and retrospective analysis.
- **Continuous organizational intelligence** — replacing periodic reporting cycles with continuous signal processing could reduce decision latency.

These implications are conditional. They assume that synthesis quality is sufficient (validated on real data), that executive stakeholders adopt and trust the outputs (requiring human-in-the-loop validation), and that the system is integrated into existing organizational information flows (an engineering and change management challenge beyond the research scope).

---

## 9. Limitations

The limitations of this research are explicit and intentional. ESS is presented as a prototype-stage research framework; the following constraints are acknowledged as design boundaries of the current work, not empirical surprises.

**1. Synthetic dataset.** The prototype was evaluated on 5 synthetic signals designed to simulate organizational signal environments. This dataset size is insufficient for statistical generalization. Performance on real organizational data — with greater volume, vocabulary diversity, and semantic complexity — is unknown and must be evaluated in future work.

**2. Keyword-based classification.** The classification module uses string matching against a predefined keyword vocabulary. This approach is interpretable but brittle: it does not generalize to paraphrases, domain-specific language variation, or signals that carry urgency through implication rather than explicit keywords. It constitutes a lower bound on classification sophistication.

**3. TF-IDF + K-means clustering.** TF-IDF treats text as a bag of words, losing syntactic structure and semantic context. K-means requires a fixed cluster count (k=3 in this prototype), does not model uncertainty in cluster assignment, and is sensitive to vocabulary variation across source types. These are known limitations of the chosen methods; they were selected for interpretability and computational simplicity at prototype stage.

**4. Rule-based synthesis.** The synthesis module produces structured summaries by aggregation — it does not generate natural language interpretations or perform reasoning over cluster evidence. The executive brief format is template-driven. This limits the richness and contextual nuance of the synthesis output.

**5. Exploratory evaluation metrics.** The evaluation metrics used (cross-source ratio, compression ratio, urgency distribution) are exploratory indicators of pipeline behavior, not validated measures of decision support quality. There is no formal benchmark for what constitutes a "good" executive synthesis, and establishing such a benchmark is a significant open research problem.

These limitations delineate the boundary between what this work demonstrates (structural feasibility of the ESS pipeline) and what it does not demonstrate (effectiveness at scale, decision quality, stakeholder adoption, generalizability).

---

## 10. Future Work

The current prototype establishes the conceptual and structural foundation of ESS. Each identified limitation suggests a specific research direction.

**Semantic signal representation.** Replacing TF-IDF with sentence-level embeddings (e.g., sentence transformers, domain-adapted language models) would enable clustering based on semantic similarity rather than surface vocabulary overlap. This is the highest-priority technical extension and is expected to significantly improve cross-source pattern detection on diverse real-world signals.

**Graph-based pattern detection.** Signals and their relationships may be better represented as a graph than as a flat feature space. Graph-based methods would enable multi-hop relationship modeling — detecting, for example, that a signal about customer churn, a signal about product performance degradation, and a signal about support volume increase jointly indicate a systemic risk that no pairwise clustering would surface.

**Formal evaluation framework.** A validated metric for executive synthesis quality is a foundational research contribution this field lacks. Candidate approaches include: human expert evaluation protocols, decision outcome tracking in longitudinal organizational studies, and information-theoretic measures of synthesis informativeness. Establishing this benchmark is necessary for ESS to mature from prototype to validated methodology.

**Real-world organizational signal streams.** Evaluating ESS on live organizational data — from real support systems, CRM records, meeting transcriptions, and operational logs — is required to assess generalizability and to surface the signal diversity, noise levels, and schema heterogeneity that synthetic datasets cannot replicate.

**Human-in-the-loop validation.** ESS outputs are intended for executive consumers. Systematic study of how executives interact with, trust, question, and act on synthesized signal intelligence is essential for framework refinement. This research direction connects ESS to the broader human-AI collaboration literature and to XAI evaluation methodology (Arrieta et al., 2020).

**Multi-modal signal integration.** Current signals are text-based. Extending ESS to structured numerical data (metrics, KPIs), audio transcripts, and visual information would require multi-modal fusion architectures (Zhao et al., 2020) and would significantly expand the organizational coverage of the framework.

---

## 11. References

Arrieta, A. B., Díaz-Rodríguez, N., Del Ser, J., Bennetot, A., Tabik, S., Barbado, A., García, S., Gil-López, S., Molina, D., Benjamins, R., Chatila, R., & Herrera, F. (2020). Explainable Artificial Intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI. *Information Fusion, 58*, 82–115. https://doi.org/10.1016/j.inffus.2019.12.012

Daft, R. L., & Lengel, R. H. (1986). Organizational information requirements, media richness and structural design. *Management Science, 32*(5), 554–571. https://doi.org/10.1287/mnsc.32.5.554

Dong, X. L., & Srivastava, D. (2015). *Big Data Integration*. Synthesis Lectures on Data Management. Morgan & Claypool Publishers. https://doi.org/10.2200/S00578ED1V01Y201404DTM040

Gorry, G. A., & Scott Morton, M. S. (1971). A framework for management information systems. *Sloan Management Review, 13*, 55–70. https://dspace.mit.edu/handle/1721.1/47936

Klein, G., Moon, B., & Hoffman, R. R. (2006). Making sense of sensemaking 2: A macrocognitive model. *IEEE Intelligent Systems, 21*(5), 88–92. https://doi.org/10.1109/MIS.2006.100

Leidner, D. E., & Elam, J. J. (1995). The impact of executive information systems on organizational design, intelligence, and decision making. *Organization Science, 6*(6), 645–664. https://doi.org/10.1287/orsc.6.6.645

Miller, T. (2019). Explanation in artificial intelligence: Insights from the social sciences. *Artificial Intelligence, 267*, 1–38. https://doi.org/10.1016/j.artint.2018.07.007

Ribeiro, M. T., Singh, S., & Guestrin, C. (2016). "Why should I trust you?": Explaining the predictions of any classifier. *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, 1135–1144. https://doi.org/10.1145/2939672.2939778

Shim, J. P., Warkentin, M., Courtney, J. F., Power, D. J., Sharda, R., & Carlsson, C. (2002). Past, present, and future of decision support technology. *Decision Support Systems, 33*(2), 111–126. https://doi.org/10.1016/S0167-9236(01)00139-7

Weick, K. E. (1995). *Sensemaking in Organizations*. SAGE Publications. ISBN: 9780803971776

Zhao, X., Jia, Y., Li, A., Jiang, R., & Song, Y. (2020). Multi-source knowledge fusion: A survey. *World Wide Web, 23*(4), 2567–2592. https://doi.org/10.1007/s11280-020-00811-0

---

*This paper is a research preprint. The associated prototype is available as an open-source repository. Flowity AI is identified as the institutional affiliation context. The ESS framework is presented as a methodological research contribution. All prototype limitations are explicitly stated.*
