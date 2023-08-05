#!/usr/bin/env python

# dbnomics-fetcher-toolbox
# Toolbox of functions and data structures helping writing DBnomics fetchers.
# By: Christophe Benz <christophe.benz@cepremap.org>
#
# Copyright (C) 2019 Cepremap
# https://git.nomics.world/dbnomics/dbnomics-fetcher-toolbox
#
# dbnomics-fetcher-toolbox is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# dbnomics-fetcher-toolbox is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import argparse
import asyncio
import shutil
from functools import partial
from pathlib import Path
from typing import List

from dbnomics_fetcher_toolbox import (
    Resource,
    add_arguments_for_download,
    process_resources,
    setup_logging,
    status,
)
from dbnomics_fetcher_toolbox.parts import Dimensions, SplitOneDimension, process_parts


async def main():
    parser = argparse.ArgumentParser()
    add_arguments_for_download(parser)
    args = parser.parse_args()
    setup_logging(args)

    resources = prepare_resources(args.target_dir)
    events = status.load_events(args.target_dir)

    with status.open_writer(args) as append_event:
        await process_resources(
            resources=resources,
            args=args,
            process_resource=partial(
                process_resource, args=args, on_event=append_event, events=events
            ),
            on_event=append_event,
            events=events,
        )


class MyResource(Resource):
    dir: Path
    url: str

    def create_context(self):
        self.dir.mkdir(exist_ok=True)

    def delete(self):
        shutil.rmtree(self.dir)


def prepare_resources(target_dir: Path) -> List[MyResource]:
    resource_id = "DATASET1"
    return [
        MyResource(
            id=resource_id,
            dir=target_dir / resource_id,
            url="https://api.provider.com/datasets/1",
        ),
    ]


async def process_resource(resource: MyResource, args, on_event, events):
    await process_parts(
        resource=resource,
        args=args,
        initial_dimensions={"FREQ": ["A", "M", "Q"]},
        process_part=partial(process_part, resource=resource),
        on_event=on_event,
        events=events,
    )


def process_part(
    dimensions: Dimensions,
    dimensions_str: str,
    is_initial_dimensions: bool,
    resource: MyResource,
):
    if is_initial_dimensions:
        raise SplitOneDimension
    if dimensions_str == "623474c3fafbe1f491cf460a083b75d6":  # second splitted part
        raise ValueError("oh no!")
    name = f"{resource.id}-{dimensions_str}.txt"
    (resource.target_dir / name).write_text(f"{resource.url}\n{dimensions_str}\n")


if __name__ == "__main__":
    asyncio.run(main())
