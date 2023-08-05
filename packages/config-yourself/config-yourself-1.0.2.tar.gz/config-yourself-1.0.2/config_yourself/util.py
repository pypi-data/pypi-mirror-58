# Copyright 2018 Blink Health LLC

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     https://www.apache.org/licenses/LICENSE-2.0

try:  # pragma: no cover
    # YAY PYTHON!
    # noinspection PyPackageRequirements
    from collections.abc import Mapping, Hashable
except ImportError:  # pragma: no cover
    try:
        # noinspection PyPackageRequirements
        from collections import Mapping, Hashable
    except ImportError:
        # noinspection PyPackageRequirements
        from future.moves.collections import Mapping, Hashable
import warnings
from os import environ, path
from config_yourself.exceptions import InvalidConfig


def merge_dicts(src, dest, parent=[]):
    for key in dest:
        full_path = parent + [key]
        if key in src:
            if isinstance(src[key], Mapping) and isinstance(dest[key], Mapping):
                if src[key].get("encrypted", False):
                    msg = (
                        "Overriding an encrypted value at <{}>. This can lead to trouble, since these "
                        "values were likely encrypted with different keys!"
                    )
                    warnings.warn(msg.format(".".join(full_path)), DeprecationWarning)
                src[key] = merge_dicts(src[key], dest[key], parent=full_path)
            elif src[key] == dest[key]:
                pass  # same leaf value
            else:
                src[key] = dest[key]
        else:
            # don't let overrides create keys
            msg = (
                "Trying to override a value on a non-existing default! "
                "The value at path <{}> will be ignored".format(".".join(full_path))
            )
            warnings.warn(msg, DeprecationWarning)
            pass
    return src


def default_config_chain(
    config_file=None, before=None, after=None, config_folder="./config"
):
    """Generate a chain of config file path names

    With no arguments, this means:

    * the ``"{config_folder}/defaults.yml"`` file,
    * a file located at ``os.environ.get("CONFIG_FILE", path.join(config_folder, "local.yml"))``
    * a ``"{config_folder}/personal.yml"`` file, if it exists

    :param Optional[str] config_file: the path to the main config file to load, usually in the form of ``./config/your-environment-name.yml``. (default: ``os.environ.get("CONFIG_FILE", "./config/local.yml")``)
    :param Optional[list[str]] before: File names to load before ``config_file`` without (default: `['default']`)
    :param Optional[list[str]] after: File names to apply after ``config_file`` if they exist (default: `['personal']`)
    :param Optional[str] config_folder: Base folder path to look for files in, (default: `./config`)

    :returns: A list of path names
    :rtype: list[str]
    """

    if config_file is None:
        config_file = environ.get("CONFIG_FILE", path.join(config_folder, "local.yml"))
        if not path.isfile(config_file):
            # Help users debug missing/mistyped CONFIG_FILEs
            raise InvalidConfig(
                message="CONFIG_FILE='{}' is not a file".format(config_file)
            )

    if before is None:
        before = ["defaults"]

    if not isinstance(before, list):
        raise TypeError("before is not a list")

    if after is None:
        after = ["personal"]

    if not isinstance(after, list):
        raise TypeError("after is not a list")

    # extract some details about the main file
    full_path_config_file = path.abspath(config_file)
    if config_folder is None:
        config_folder = path.dirname(full_path_config_file)
    _main_ext = path.splitext(config_file)[1]

    def name_to_path(name):
        if not name.endswith(".yml") and not name.endswith(".yaml"):
            name = "{}{}".format(name, _main_ext)
        return path.join(config_folder, name)

    # the chain of files to merge before decrypting
    # Add the resolved before files
    chain = [name_to_path(file_name) for file_name in before]

    # Add the main config file
    chain.append(config_file)

    # Add after files if they exist
    for f in [name_to_path(file_name) for file_name in after]:
        if path.isfile(f):
            chain.append(f)

    return chain
