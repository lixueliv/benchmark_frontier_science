# AT2018cow Frontier-Science LLM Benchmark (AT2018cow-FSCI)

## Overview

This package provides a seven-dimension benchmark for evaluating frontier-science reasoning in large language models (LLMs), using the astrophysical transient AT2018cow as a motivating case. The benchmark evaluates:

- D1 Literature Discovery
- D2 Literature Synthesis
- D3 Claim Verification
- D4 Hypothesis Discrimination
- D5 Formal Scientific Reasoning
- D6 Hypothesis Generation
- D7 Frontier Open Question Reasoning

The package is intended for NeurIPS 2026 Evaluations & Datasets submission review and reproducibility.

## Contents

```text
croissant_metadata.json        Croissant metadata file with core and minimal RAI fields
data/tasks.json                Full benchmark task definitions for D1-D7
data/scoring_config.json       Scoring rubrics and hallucination cap rules
data/score_table.json          Reported model scores from the paper
examples/submission_template.json  Template for recording evaluated model outputs
examples/gold_expected_outputs.json Short gold-answer expectations for each dimension
scripts/evaluate.py            Minimal scoring script
LICENSE.txt                    CC-BY-4.0 license notice
```

## How to Use

1. Fill `examples/submission_template.json` with model responses, raw scores, and flags.
2. Run:

```bash
python scripts/evaluate.py --metadata croissant_metadata.json --tasks data/tasks.json --submission examples/submission_template.json
```

3. The script outputs percentage scores per dimension and the average score.

## Scoring

Each dimension uses an independent raw score and converts it to percentage:

```text
Percentage Score = Raw Score / Max Raw Score * 100
```

Hallucination caps and plausibility caps are applied after raw-score conversion. For example, invented evidence may cap a dimension score at 50%, while physically impossible reasoning may reduce a score to 0%.

## Important Notes

- This package does **not** redistribute copyrighted paper excerpts.
- Literature citations and roles are included for reproducibility, but users should obtain source texts from lawful sources.
- Expert review is recommended for final scoring, especially for D4-D7.
- Replace placeholder dataset URLs in `croissant_metadata.json` with the final hosted dataset URL before OpenReview submission.
- Validate the Croissant metadata file using the official Croissant validator before submission.

## Citation

Please cite the associated paper and the source AT2018cow literature cited in the metadata.
