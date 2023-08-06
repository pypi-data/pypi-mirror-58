DBnomics fetcher toolbox
========================

`DBnomics`_ is a database of macro-economic data aggregated from a great number of
world-wide providers (see the `complete list <https://db.nomics.world/providers>`_).

Its usage is free of charge, its source code is licensed under the
GNU Affero GPL v3+, and data is redistributed freely under the same conditions as
the original provider.

In DBnomics, data acquisition is done by *fetchers*, small programs that download data
from the provider infrastructure, and convert it to a common data model and format.
Each fetcher covers a particular data provider.
Fetchers are scheduled on a regular basis in order to keep DBnomics data up to date.

`dbnomics-fetcher-toolbox`_ is a Python package containing several tools and patterns
to ease the development of a fetcher. It helps to capitalize between fetchers and
reduce the burden in solving bugs.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   design_goals
   writing_a_fetcher
   dbnomics_fetcher_toolbox


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _DBnomics: https://db.nomics.world/
.. _dbnomics-fetcher-toolbox: https://pypi.org/project/dbnomics-fetcher-toolbox
