import pytest
import mock
import warnings
from config_yourself.util import default_config_chain


class TestAppConfig(object):
    @mock.patch("os.path.isfile")
    @pytest.mark.parametrize(
        "input_args,expected_chain",
        [
            (
                # test no arguments
                {},
                ["./config/defaults.yml", "./config/local.yml"],
            ),
            (
                # test setting config file
                {"config_file": "./config/environment.yml"},
                ["./config/defaults.yml", "./config/environment.yml"],
            ),
            (
                # test before
                {"before": ["other-defaults"]},
                ["./config/other-defaults.yml", "./config/local.yml"],
            ),
            (
                # test before with custom extension
                {"before": ["other-defaults.yaml"]},
                ["./config/other-defaults.yaml", "./config/local.yml"],
            ),
            (
                # test after
                {"after": ["override"]},
                [
                    "./config/defaults.yml",
                    "./config/local.yml",
                    "./config/override.yml",
                ],
            ),
            (
                # test override config_folder
                {"config_folder": "./overriden-folder"},
                ["./overriden-folder/defaults.yml", "./overriden-folder/local.yml",],
            ),
            (
                # test existing personal file
                {},
                [
                    "./config/defaults.yml",
                    "./config/local.yml",
                    "./config/personal.yml",
                ],
            ),
        ],
    )
    def test_default_chain(self, mock_isfile, input_args, expected_chain):
        mock_isfile.side_effect = lambda filename: filename in expected_chain

        assert default_config_chain(**input_args) == expected_chain
