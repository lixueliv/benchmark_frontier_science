# Dataset Card: AT2018cow-FSCI

## Dataset Summary
AT2018cow-FSCI is a benchmark for evaluating LLMs on frontier-science reasoning using AT2018cow. It contains task definitions, prompts, scoring rubrics, hallucination cap rules, gold-answer expectations, model score tables, and a minimal evaluator.

## Intended Uses
- Evaluate LLMs on scientific reasoning.
- Diagnose strengths and weaknesses across seven independent dimensions.
- Support development of multi-agent AI systems for scientific discovery.

## Not Intended Uses
- The benchmark should not be used as a substitute for expert scientific judgment.
- It should not be used to claim a definitive scientific solution to AT2018cow.
- It should not be used for training models on copyrighted source papers unless licenses permit.

## Data Composition
- `data/tasks.json`: D1-D7 benchmark definitions.
- `data/scoring_config.json`: Scoring rubrics and cap rules.
- `data/score_table.json`: Scores reported in the associated paper.
- `examples/`: Submission template and gold-output summaries.
- `scripts/evaluate.py`: Minimal score calculation script.

## Ethical Considerations
No human-subject data or personally identifiable information is included. The main risk is overreliance on LLM-generated scientific interpretations. The benchmark mitigates this by requiring evidence grounding, uncertainty handling, hallucination caps, and domain-expert review.

## Maintenance
Version 1.0.0. Future versions should add additional scientific domains and record all changes.
