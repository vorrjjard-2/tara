# Inoculation Prompting and Prior Association Strength

Ravi and Fahad's TARA project.

**Question:** Does an inoculation prompt (IP) protect a model less well when the prompt already carries a strong prior association with misaligned behaviour?

**Hypothesis:** An IP with a strong prior association makes it easier to break the conditional gate, so reward hacking spreads to contexts where the IP is absent. A weakly associated IP holds up better.

**Main measurement:** reward hacking prevalence after SFT on reward hacking data, compared across IPs whose association strength was measured *before* fine-tuning.

Full background and mentor feedback: [docs/brief.md](docs/brief.md).

## Avoiding circularity

Association strength has to be measured independently of the outcome. If IPs were ranked by how much misalignment they produce, the hypothesis would be true by definition. So every IP is scored on the **base model, before any training**, using:

1. **Log-prob score:** the base model's log p(misaligned completion) − log p(aligned completion), given the IP.
2. **Probe score:** the IP's projection onto a linear probe direction that separates misaligned from aligned contexts in base-model activations.

Both scores are computed and recorded before any training run starts. The two scores should also agree with each other, which serves as a sanity check.

## Pipeline

| Step | Script | What it does |
|---|---|---|
| 0 | `scripts/00_reproduce_baseline.py` | Confirm the standard IP effect reproduces on our model and dataset (week 1). |
| 1 | `scripts/01_measure_association.py` | Score every candidate IP with the log-prob and probe measures on the base model. |
| 2 | `scripts/02_build_datasets.py` | Build one SFT dataset per IP arm (same data, different IP prepended), plus a no-IP control. |
| 3 | `scripts/03_train.py` | LoRA SFT, one run per arm per seed. |
| 4 | `scripts/04_evaluate.py` | Measure the reward hacking rate with and without the IP at test time. |
| 5 | `scripts/05_analyze.py` | Relate pre-training association scores to post-training reward hacking. |

## Layout

```
configs/            experiment settings (base.yaml) and candidate IPs (prompts/)
data/raw/           downloaded datasets (gitignored)
data/processed/     built SFT arms (gitignored)
docs/               project brief, notes, decisions
notebooks/          exploration and Colab notebooks
results/            association scores, checkpoints, evals, figures (gitignored)
scripts/            numbered pipeline entry points
src/tara_ip/
  association/      logprob.py, probe.py (pre-training measures)
  data/             dataset building and IP insertion
  training/         LoRA SFT
  eval/             reward hacking measurement
  utils.py          config loading, seeding
tests/
```

## Setup

The project uses [uv](https://docs.astral.sh/uv/) for package management.

```bash
uv sync                  # create .venv and install deps (including the dev group)
cp .env.example .env     # add HF, OpenRouter, and W&B keys
uv run pytest
uv run python scripts/01_measure_association.py
uv add <package>         # add a dependency
```

To work on Colab (A100), clone the repo, then run `pip install uv && uv pip install --system -e .`.

## Status

Scaffold only. Every module is a stub. Open decisions:
- Which base model to use (a small open model that fits on one A100).
- Which dataset to use (School of Reward Hacks is the leading candidate).
- The set of candidate IPs, spanning a range of hypothesised association strengths.
- How to detect reward hacking in evals.
