"""Association measure 2: linear probe on base-model activations.

Train a probe to separate misaligned vs. aligned contexts, then score each IP by
its projection onto the probe direction.
"""


def train_probe(activations, labels, layer: int):
    raise NotImplementedError


def score_prompt(probe, model, tokenizer, ip_text: str, layer: int) -> float:
    raise NotImplementedError
