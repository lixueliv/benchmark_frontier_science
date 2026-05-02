#!/usr/bin/env python3
"""Minimal evaluator for the AT2018cow Frontier-Science LLM Benchmark.

This script converts raw scores to percentages and applies simple cap flags.
It is intentionally conservative: final expert adjudication should be used
for scientific correctness, hallucination severity, and physical plausibility.
"""

import argparse
import json
from pathlib import Path


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def percentage(raw_score, max_raw):
    if max_raw <= 0:
        return 0.0
    raw_score = max(0.0, min(float(raw_score), float(max_raw)))
    return raw_score / float(max_raw) * 100.0


def apply_caps(dim_id, percent_score, flags, scoring):
    """Apply common hallucination/plausibility caps based on evaluator flags."""
    caps = scoring.get("hallucination_cap_rules", {}) or scoring.get("hallucination_caps", {})
    score = percent_score

    # Generic flags used in submission_template.json.
    if flags.get("physically_impossible", False):
        score = min(score, 0.0)
    if flags.get("invented_evidence", False) or flags.get("hallucination", False):
        # Default severe hallucination cap if dimension-specific cap is not explicitly numeric.
        score = min(score, 50.0)
    if flags.get("unsupported_overclaim", False):
        score = min(score, 50.0)
    if flags.get("evidence_mismatch", False):
        score = min(score, 50.0)

    # Dimension-specific string caps such as "max 50%" or "0%".
    for flag_name, cap_value in caps.items():
        normalized_flag = flag_name.replace("-", "_").replace(" ", "_")
        if flags.get(normalized_flag, False):
            if isinstance(cap_value, (int, float)):
                score = min(score, float(cap_value))
            elif isinstance(cap_value, str):
                if "0%" in cap_value:
                    score = min(score, 0.0)
                elif "50%" in cap_value:
                    score = min(score, 50.0)
                elif "25%" in cap_value:
                    score = min(score, 25.0)
    return score


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--metadata", default="croissant_metadata.json")
    parser.add_argument("--tasks", default="data/tasks.json")
    parser.add_argument("--submission", default="examples/submission_template.json")
    args = parser.parse_args()

    tasks = load_json(args.tasks)
    submission = load_json(args.submission)

    dim_meta = {d["id"]: d for d in tasks["dimensions"]}
    results = {}

    for dim_id, entry in submission.get("responses", {}).items():
        meta = dim_meta.get(dim_id)
        if not meta:
            continue
        raw_score = entry.get("raw_score", 0)
        max_raw = entry.get("max_raw_score", meta["raw_range"][1])
        pct = percentage(raw_score, max_raw)
        pct = apply_caps(dim_id, pct, entry.get("flags", {}), meta.get("scoring", {}))
        results[dim_id] = round(pct, 2)

    avg = round(sum(results.values()) / len(results), 2) if results else 0.0
    output = {"dimension_scores_percent": results, "average_score_percent": avg}

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
