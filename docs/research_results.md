# Research Results

Repository: executive-signal-synthesis-prototype  
Author: Nina Cressoni  
Affiliation: Flowity AI

This document records experimental observations for the research direction:

**External AI Brain Systems for Executive Decision Support**

---

## Experiment 1 — Cross-Source Signal Detection

Goal: determine whether heterogeneous signals from different organizational sources can be automatically grouped into coherent patterns.

Dataset size: 5 signals

Clusters detected: 3

Cross-source clusters: 2

Cross-source ratio: 66.7%

Interpretation:

Two of the three detected patterns contain signals originating from multiple business sources. This indicates that the prototype can identify recurring issues across organizational boundaries rather than treating each signal independently.

This supports the hypothesis that lightweight NLP pipelines can detect cross-source patterns relevant to executive decision-making.

---

## Experiment 2 — Signal Compression

Goal: measure whether the system reduces fragmented signals into a smaller number of decision-relevant patterns.

Signals processed: 5

Clusters produced: 3

Signal compression ratio: 1.67x

Interpretation:

The prototype compressed five raw signals into three aggregated patterns. This suggests that heterogeneous inputs can be transformed into structured decision units suitable for executive review, even in a minimal test setting.

---

## Experiment 3 — Decision Abstraction

Goal: evaluate whether clustered signals can be transformed into actionable executive guidance.

Input signals: 5

Detected patterns: 3

Generated executive actions: 3

Interpretation:

The prototype reduced raw signals into a small set of decision-relevant themes and generated suggested executive actions. This demonstrates a transformation from fragmented observations into structured decision guidance.

---

## Sensitivity Check

Alternative clustering run:

Clusters detected: 4

Cross-source clusters: 1

Cross-source ratio: 25%

Signal compression ratio: 1.25x

Interpretation:

When the number of clusters increased, cross-source grouping became weaker. This suggests that the current prototype is sensitive to clustering configuration and should be interpreted as an early-stage research validation artifact rather than a final model.
