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

from .arguments import (  # noqa: F401
    add_arguments_for_convert,
    add_arguments_for_download,
)
from .data_model import (  # noqa: F401
    CATEGORY_TREE_JSON,
    DATASET_JSON,
    NA,
    PROVIDER_JSON,
    SERIES_JSONL,
    Category,
    CategoryTree,
    DatasetReference,
    NoTimeDimensionError,
    ObservationError,
    SeriesError,
    iter_dataset_references,
    write_category_tree_json,
    write_series_jsonl,
)
from .file_system_utils import iter_child_directories  # noqa: F401
from .formats import (  # noqa: F401
    fetch_or_read_html,
    fetch_or_read_xml,
    fetch_xml,
    read_html,
    read_xml,
    write_html,
    write_json,
    write_jsonl,
    write_xml,
)
from .logging_utils import setup_logging  # noqa: F401
from .resources import (  # noqa: F401
    DbnomicsDatasetResource,
    Resource,
    ResourceId,
    process_resources,
)
from .status import ResourceEvent, ResourceStatus  # noqa: F401
from .utils import find, is_empty, without_empty_values  # noqa: F401
