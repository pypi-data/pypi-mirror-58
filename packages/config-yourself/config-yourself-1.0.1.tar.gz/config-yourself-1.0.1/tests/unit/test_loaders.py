# coding=utf-8
from __future__ import print_function
import pytest
from moto import mock_kms
from config_yourself import load


# noinspection PyClassHasNoInit
@mock_kms
class TestLoaders(object):
    @pytest.mark.parametrize(
        ["env", "result"],
        [
            [{"CONFIG.string": "value"}, {"string": "value"}],
            [{"CONFIG.boolean": "true"}, {"boolean": True}],
            [{"CONFIG.nested.boolean": "true"}, {"nested": {"boolean": True}}],
        ],
    )
    def test_env_loader(self, monkeypatch, env, result):
        for k, v in env.items():
            monkeypatch.setenv(k, v)
        assert load.env() == result
