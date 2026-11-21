# TARA Project Brief: Inoculation Prompting and Prior Association Strength

## Context

Ravi is in TARA, a Manila-based AI safety training program (curriculum is roughly ARENA plus extra components). TARA is in its project phase and this is his main project. He has program-provided compute/API credits and Colab Pro (A100).

Projects are scored on four equally weighted criteria: scale of risk, theory of change, execution, and counterfactual impact.

## Core idea

Test inoculation prompting (IP) using prompts with different hypothesised strengths of prior association with misaligned behaviour, in a reward hacking setting.

Hypothesis: when an inoculation prompt already has a strong association with misaligned behaviour, it is easier to break the conditional gate and produce misaligned behaviour. A weakly associated IP should hold up better.

The main measurement is reward hacking prevalence under weak-association vs. strong-association inoculation prompts.

## How the idea got here

The earlier version (Idea 1) asked whether inoculation prompting works through a "semantic break" (hacking gets re-linked to acceptable behaviour) or through gating on the prompt. The planned setup was small-model SFT, for example on School of Reward Hacks, with week one spent confirming the behavioural effect reproduces.

Mentor feedback, first round: liked the idea, but pointed out existing LessWrong work on inoculation prompting and asked for more precisely defined experiments.

Mentor feedback, second round (Nov 11, 2026):
- Reward hacking is still a worthwhile context, since it is one of the main reasons for concern about AI risk.
- A 1:1 replication would be acceptable but less interesting.
- Testing IP across different hypothesised association strengths extends prior work naturally.
- Suggested combining the ideas: measure reward hacking prevalence when the IP has weak vs. strong prior associations. A second mentor agreed this is a natural next step.

## Open problem to solve first

"Strength of prior association" needs a measure that is independent of the outcome. If prompts are ranked by how much misalignment they end up producing, the hypothesis is circular. Candidate measures, taken before any fine-tuning:
- The base model's log-probability of misaligned completions given each IP.
- A probe on base-model activations for each IP.

## Separate backup idea (Idea 2, not the current focus)

Explained principles vs. bare rules in constitution training for an oversight-related value. Arms: rule, explained, hardened explanation, length-matched control. Tests OOD generalization and robustness to "the reason doesn't apply here" arguments. Mentors said it links clearly to catastrophic risk but wanted more detail on dataset construction and fine-tuning.
