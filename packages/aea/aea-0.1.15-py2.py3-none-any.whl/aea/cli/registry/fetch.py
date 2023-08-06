# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------
"""Methods for CLI fetch functionality."""

import click
import os

from aea.cli.registry.utils import (
    request_api, download_file, extract, split_public_id
)


def fetch_agent(public_id: str) -> None:
    """
    Fetch Agent from Registry.

    :param public_id: str public ID of desirable Agent.

    :return: None
    """
    owner, name, version = split_public_id(public_id)
    api_path = '/agents/{}/{}/{}'.format(owner, name, version)
    resp = request_api('GET', api_path)
    file_url = resp['file']

    cwd = os.getcwd()
    filepath = download_file(file_url, cwd)
    target_folder = os.path.join(cwd, name)
    extract(filepath, target_folder)
    click.echo(
        'Agent {} successfully fetched to {}.'
        .format(name, target_folder)
    )
