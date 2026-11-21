"""Association measure 1: base-model log-probability of misaligned completions given an IP."""


def misaligned_logprob_score(model, tokenizer, ip_text: str, pairs: list[dict]) -> float:
    """Mean log p(misaligned) - log p(aligned) over completion pairs, conditioned on ip_text.

    pairs: [{"prompt": ..., "misaligned": ..., "aligned": ...}, ...]
    """
    raise NotImplementedError
