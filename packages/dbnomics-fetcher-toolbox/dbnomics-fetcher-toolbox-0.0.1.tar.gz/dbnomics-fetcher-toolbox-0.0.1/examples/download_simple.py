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
from pathlib import Path
from typing import Iterator

from dbnomics_fetcher_toolbox import (
    Resource,
    add_arguments_for_download,
    process_resources,
    setup_logging,
    status,
)


async def main():
    parser = argparse.ArgumentParser()
    add_arguments_for_download(parser)
    args = parser.parse_args()
    setup_logging(args)

    resources = list(prepare_resources(args.target_dir))
    events = status.load_events(args.target_dir)

    with status.open_writer(args) as append_event:
        await process_resources(
            resources=resources,
            args=args,
            process_resource=process_resource,
            on_event=append_event,
            events=events,
        )


class MyResource(Resource):
    file: Path
    url: str

    def delete(self):
        self.file.unlink()


def prepare_resources(target_dir: Path) -> Iterator[MyResource]:
    for i in range(3):
        resource_id = f"DATASET{i}"
        yield MyResource(
            id=resource_id,
            url=f"https://stats.provider.com/datasets/{i}.xls",
            file=(target_dir / resource_id).with_suffix(".txt"),
        )


def process_resource(resource: MyResource):
    # if resource.id == 'DATASET2':
    #     raise ValueError("oh no!")
    resource.file.write_text(resource.url)


if __name__ == "__main__":
    asyncio.run(main())
