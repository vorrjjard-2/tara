"""Measure reward hacking prevalence, with and without the IP at test time."""


def reward_hacking_rate(model, tokenizer, eval_dataset, system_prompt: str | None) -> float:
    raise NotImplementedError
