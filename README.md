# External AI Brain Research Prototype

This repository contains a limited research prototype accompanying the preprint:

**Cressoni, N. (2026). _External AI Brain Systems for Executive Decision Support: A Conceptual Research Agenda for Founder-Led Organizations_. Preprint.**

## Research framing

This repository supports the research direction of **External AI Brain Systems**: AI-based executive intelligence layers that ingest heterogeneous business signals, interpret them in context, synthesize them into decision-relevant patterns, and produce prioritized guidance for human leadership.

The goal of this prototype is to test whether fragmented business signals can be transformed into structured executive decision support.

## Relationship to Flowity AI

The academic contribution concerns the broader category of **External AI Brain Systems**.

A prototype system aligned with this research direction is under development by the author through the startup **Flowity AI**.

This repository is **not** the Flowity AI production system. It is a limited research validation artifact designed to demonstrate methodology, feasibility, and evaluation paths.

## What this repository includes

- synthetic multi-source business signal data
- a signal taxonomy for research prototyping
- Python scripts for ingestion, tagging, clustering, and synthesis
- a notebook showing the full validation flow
- sample executive decision brief outputs

## What this repository does not include

- proprietary production architecture
- confidential customer data
- private implementation logic
- source code for any commercial system
- patent-sensitive technical details

## Research question

How can fragmented, heterogeneous business signals be transformed into explainable executive decision support for founder-led organizations?

## Prototype workflow

1. Load synthetic business signals from multiple sources
2. Normalize and score records
3. Classify signal type and business impact
4. Group related patterns across sources
5. Generate an executive decision brief

## Example use cases

- identifying repeated onboarding friction
- surfacing cross-source churn signals
- summarizing founder-relevant risks from unstructured information
- producing early decision briefs for audits or pilot reviews

## Quick start

### Local Python setup

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\\Scripts\\activate   # Windows
pip install -r requirements.txt
python -m src.generate_brief
