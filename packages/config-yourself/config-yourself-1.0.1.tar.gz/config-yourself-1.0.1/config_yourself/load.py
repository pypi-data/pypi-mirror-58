# Copyright 2018 Blink Health LLC

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     https://www.apache.org/licenses/LICENSE-2.0

__all__ = ["file", "env"]

import json
import os
from yaml import safe_load
from os import path
from config_yourself.exceptions import InvalidConfig


def env(prefix="CONFIG"):
    """Loads all environment variables prefixed with `prefix.`

    For example, setting the environment variable `CONFIG.override.key="true"` would
    set `key` of `override` to `True`.

    :param str prefix: The prefix to use when filtering environment variables. (default: `CONFIG`)

    :return: A dictionary of loaded values from the environment
    :rtype: dict[str,Any]
    """

    prefix = prefix + "."
    keys = [k.replace(prefix, "", 1) for k in os.environ if k.startswith(prefix)]

    data = dict()
    for key in keys:
        path = key.split(".")
        node = data

        for idx, leaf in enumerate(path):
            if idx + 1 == len(path):
                value = os.environ[prefix + key]
                try:
                    value = json.loads(value)
                except ValueError:
                    pass

                node[leaf] = value
            else:
                node[leaf] = dict()
                node = node[leaf]

    return data


def file(path):
    """returns the dict representation of yaml file at `path`

    :param str path: The path of the file to parse as YAML.

    :return: A dictionary of loaded values from the file
    :rtype: dict[str,Any]
    """
    if not path.exists(path):
        raise InvalidConfig("File not found at '{}'".format(path))

    if not path.isfile(path):
        raise InvalidConfig("Path at '{}' is not a file".format(path))

    with open(path, "r") as config_file:
        return safe_load(config_file.read())
