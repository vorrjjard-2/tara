from tara_ip.utils import ROOT, load_config


def test_base_config_loads():
    cfg = load_config(ROOT / "configs" / "base.yaml")
    assert "model" in cfg
