Design goals
============

This section is a guide explaining how to write a fetcher for DBnomics, or maintaining
an existing one.
Let's dive into the different tasks that a fetcher has to do,
the constraints it has to follow, and how it fits into DBnomics architecture.

Be self-contained
-----------------

A fetcher must be able to run independently from any infrastructure.
In order to achieve this, fetchers just write data to the file-system.

This allows anyone to run it without having to run the complete DBnomics infrastructure.

Keep provider data
------------------

Fetchers download data from the provider infrastructure and write it to the
file-system as-is.

Providers usually distribute data as:

* static files (sometimes called bulk download):
  XML, JSON, CSV, XLSX, sometime archived in ZIP files
* web API, with responses being XML, JSON, etc.

File formats can be:

* machine-readable: XML, JSON, CSV
* human-readable: XLSX files using formatting, colors, etc.

Convert data to DBnomics data model
-----------------------------------

Fetchers convert downloaded data to a common data model.
This allows the DBnomics platform to index data coming from all providers in a
full-text search engine, and become an aggregator.

The constraints defined by DBnomics data model are documented here TODO.

Keep past revisions
-------------------

Most of the time, providers do not give access to the past revisions of data.
However it is often important to access them for `reproducibility`_,
for example to run computations that were written in the past, with the data that was
available at that time.

Fetchers rely on `Git`_ to handle revisions.

Avoid false revisions
---------------------

Downloaded data sometimes differs sightly from one download to another, even if both
downloads correspond to the same revision.

For example, there can be a ``prepared_at`` date in an XML file,
or a random URL to a CSS stylesheet in an HTML file used to bypass the browser cache.

Keeping them would create false revisions, so fetchers are allowed to remove
those specificities in downloaded data in order to avoid them.

Ensure revision consistency
---------------------------

During the download or the conversion of data, some errors can occur.
An error can lead to the situation where a dataset is partially written.

In that case, fetchers have to cancel writing the dataset, otherwise this would
create a partial revision in which some data is updated while
the rest comes from the previous revision.

Error handling
--------------


Scheduling
----------

Fetchers are scheduled on a regular basis in order to keep DBnomics data up to date.

.. _reproducibility: https://en.wikipedia.org/wiki/reproducibility
.. _Git: https://git-scm.com/
