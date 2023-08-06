OCDS Commands
=============

Optional arguments for all commands are:

* ``--encoding ENCODING`` the file encoding
* ``--ascii`` print escape sequences instead of UTF-8 characters
* ``--pretty`` pretty print output
* ``--root-path ROOT_PATH`` the path to the items to process within each input

The inputs can be `concatenated JSON <https://en.wikipedia.org/wiki/JSON_streaming#Concatenated_JSON>`__ or JSON arrays.

Handling edge cases
-------------------

Large packages
~~~~~~~~~~~~~~

If you are working with individual packages that are too large to hold in memory, use the :ref:`echo` command to reduce their size.

Embedded data
~~~~~~~~~~~~~

If you are working with files that embed OCDS data, use the ``--root-path ROOT_PATH`` option to indicate the path to the items to process within each input. For example, if release packages are in an array under a ``results`` key, like so:

.. code:: json

   {
     "results": [
       {
         "uri": "placeholder:",
         "publisher": {"name": ""},
         "publishedDate": "9999-01-01T00:00:00Z",
         "version": "1.1",
         "releases": []
       }
     ]
   }

You can run ``ocdskit <command> --root-path results.items`` to process the release packages. To build the root path, in this case, you join the ``results`` key to the ``item`` literal by a period (the ``item`` literal indicates that the items to process are in an array).

For this next example, you can run ``ocdskit <command> --root-path results.item.ocdsReleasePackage``:

.. code:: json

   {
     "results": [
       {
         "ocdsReleasePackage": {
           {
             "uri": "placeholder:",
             "publisher": {"name": ""},
             "publishedDate": "9999-01-01T00:00:00Z",
             "version": "1.1",
             "releases": []
           }
         }
       }
     ]
   }

detect-format
-------------

Reads OCDS files, and reports whether each is:

* a release package
* a record package
* a release
* a record
* a compiled release
* a versioned release
* a JSON array of one of the above
* `concatenated JSON <https://en.wikipedia.org/wiki/JSON_streaming#Concatenated_JSON>`__ of one of the above

::

    ocdskit detect-format tests/fixtures/realdata/release-package-1.json tests/fixtures/realdata/record-package-1.json

compile
-------

Reads release packages and individual releases from standard input, merges the releases by OCID, and prints the compiled releases.

Optional arguments:

* ``--schema SCHEMA`` the URL or path of the release schema to use
* ``--package`` wrap the compiled releases in a record package
* ``--linked-releases`` if ``--package`` is set, use linked releases instead of full releases, if the input is a release package
* ``--versioned`` if ``--package`` is set, include versioned releases in the record package; otherwise, print versioned releases instead of compiled releases
* ``--uri URI`` if ``--package`` is set, set the record package's ``uri`` to this value
* ``--published-date PUBLISHED_DATE`` if ``--package`` is set, set the record package's ``publishedDate`` to this value
* ``--publisher-name PUBLISHER_NAME`` if ``--package`` is set, set the record package's ``publisher``'s ``name`` to this value
* ``--publisher-uri PUBLISHER_URI`` if ``--package`` is set, set the record package's ``publisher``'s ``uri`` to this value
* ``--publisher-scheme PUBLISHER_SCHEME`` if ``--package`` is set, set the record package's ``publisher``'s ``scheme`` to this value
* ``--publisher-uid PUBLISHER_UID`` if ``--package`` is set, set the record package's ``publisher``'s ``uid`` to this value
* ``--fake`` if ``--package`` is set, set the record package's required metadata to dummy values

If ``--package`` is set, and if the ``--publisher-*`` options aren't used, the output package will have the same publisher as the last input package.

::

    cat tests/fixtures/realdata/release-package-1.json | ocdskit compile > out.json

For the Python API, see :meth:`ocdskit.combine.merge`.

upgrade
-------

Upgrades packages and releases from an old version of OCDS to a new version. Any data not in the old version is passed through. **Note:** Versioned releases within a record package are not upgraded.

OCDS 1.0 `describes <https://standard.open-contracting.org/1.0/en/schema/reference/#identifier>`__ an organization's ``name``, ``identifier``, ``address`` and ``contactPoint`` as relevant to identifying it. OCDS 1.1 `moves <https://standard.open-contracting.org/1.1/en/schema/reference/#parties>`__ organization data into a ``parties`` array. To upgrade from OCDS 1.0 to 1.1, we create an ``id`` for each organization, based on those identifying fields. This can result in duplicates in the ``parties`` array, if the same organization has different or missing values for identifying fields in different contexts. This can also lead to data loss if the same organization has different values for non-identifying fields in different contexts; the command prints warnings in such cases.

**Note:** OCDS 1.0 uses the `whole-list merge <https://standard.open-contracting.org/1.0/en/schema/merging/#merging-rules>`__ strategy on the ``suppliers`` array to prepare the compiled release and versioned release, whereas OCDS 1.1 uses the `identifier merge <https://standard.open-contracting.org/1.1/en/schema/merging/#identifier-merge>`__ strategy. This means that you should merge first and then upgrade.

::

    cat tests/fixtures/realdata/release-package-1.json | ocdskit upgrade 1.0:1.1 > out.json

For the Python API, see :doc:`../api/upgrade`.

If a *release* package is too large, you can upgrade its individual releases using ``--root-path releases.item``.

.. _package-records:

package-records
---------------

Reads records from standard input, and prints one record package.

Optional positional arguments:

* ``extension`` add this extension to the package
* ``--uri URL`` set the record package's ``uri`` to this value
* ``--published-date PUBLISHED_DATE`` set the record package's ``publishedDate`` to this value
* ``--publisher-name PUBLISHER_NAME`` set the record package's ``publisher``'s ``name`` to this value
* ``--publisher-uri PUBLISHER_URI`` set the record package's ``publisher``'s ``uri`` to this value
* ``--publisher-scheme PUBLISHER_SCHEME`` set the record package's ``publisher``'s ``scheme`` to this value
* ``--publisher-uid PUBLISHER_UID`` set the record package's ``publisher``'s ``uid`` to this value
* ``--fake`` set the record package's required metadata to dummy values

::

    cat tests/fixtures/record_*.json | ocdskit package-records > out.json

To convert record packages to a record package, you can use the ``--root-path`` option::

    cat tests/fixtures/realdata/record-package* | ocdskit package-records --root-path records.item.records

If ``--uri`` and ``--published-date`` are not set, the output package will be invalid. Use ``--fake`` to set placeholder values.

For the Python API, see :meth:`ocdskit.combine.package_records`.

.. _package-releases:

package-releases
----------------

Reads releases from standard input, and prints one release package.

Optional positional arguments:

* ``extension`` add this extension to the package
* ``--uri URL`` set the release package's ``uri`` to this value
* ``--published-date PUBLISHED_DATE`` set the release package's ``publishedDate`` to this value
* ``--publisher-name PUBLISHER_NAME`` set the release package's ``publisher``'s ``name`` to this value
* ``--publisher-uri PUBLISHER_URI`` set the release package's ``publisher``'s ``uri`` to this value
* ``--publisher-scheme PUBLISHER_SCHEME`` set the release package's ``publisher``'s ``scheme`` to this value
* ``--publisher-uid PUBLISHER_UID`` set the release package's ``publisher``'s ``uid`` to this value
* ``--fake`` set the release package's required metadata to dummy values

::

    cat tests/fixtures/release_*.json | ocdskit package-releases > out.json

To convert record packages to a release package, you can use the ``--root-path`` option::

    cat tests/fixtures/realdata/record-package* | ocdskit package-releases --root-path records.item.releases

If ``--uri`` and ``--published-date`` are not set, the output package will be invalid. Use ``--fake`` to set placeholder values.

For the Python API, see :meth:`ocdskit.combine.package_releases`.

combine-record-packages
-----------------------

Reads record packages from standard input, collects packages and records, and prints one record package.

If the ``--publisher-*`` options aren't used, the output package will have the same publisher as the last input package.

Optional arguments:

* ``--uri URL`` set the record package's ``uri`` to this value
* ``--published-date PUBLISHED_DATE`` set the record package's ``publishedDate`` to this value
* ``--publisher-name PUBLISHER_NAME`` set the record package's ``publisher``'s ``name`` to this value
* ``--publisher-uri PUBLISHER_URI`` set the record package's ``publisher``'s ``uri`` to this value
* ``--publisher-scheme PUBLISHER_SCHEME`` set the record package's ``publisher``'s ``scheme`` to this value
* ``--publisher-uid PUBLISHER_UID`` set the record package's ``publisher``'s ``uid`` to this value
* ``--fake`` set the record package's required metadata to dummy values

::

    cat tests/fixtures/record-package_*.json | ocdskit combine-record-packages > out.json

If you need to create a single package that is too large to hold in your system's memory, please `comment on this issue <https://github.com/open-contracting/ocdskit/issues/119>`__.

For the Python API, see :meth:`ocdskit.combine.combine_record_packages`.

combine-release-packages
------------------------

Reads release packages from standard input, collects releases, and prints one release package.

If the ``--publisher-*`` options aren't used, the output package will have the same publisher as the last input package.

Optional arguments:

* ``--uri URL`` set the release package's ``uri`` to this value
* ``--published-date PUBLISHED_DATE`` set the release package's ``publishedDate`` to this value
* ``--publisher-name PUBLISHER_NAME`` set the release package's ``publisher``'s ``name`` to this value
* ``--publisher-uri PUBLISHER_URI`` set the release package's ``publisher``'s ``uri`` to this value
* ``--publisher-scheme PUBLISHER_SCHEME`` set the release package's ``publisher``'s ``scheme`` to this value
* ``--publisher-uid PUBLISHER_UID`` set the release package's ``publisher``'s ``uid`` to this value
* ``--fake`` set the release package's required metadata to dummy values

::

    cat tests/fixtures/release-package_*.json | ocdskit combine-release-packages > out.json

If you need to create a single package that is too large to hold in your system's memory, please `comment on this issue <https://github.com/open-contracting/ocdskit/issues/119>`__.

For the Python API, see :meth:`ocdskit.combine.combine_release_packages`.

.. _split-record-packages:

split-record-packages
---------------------

Reads record packages from standard input, and prints smaller record packages for each.

::

    cat tests/fixtures/realdata/record-package-1-2.json | ocdskit split-record-packages 2 | split -l 1 -a 4

The ``split`` command will write files named ``xaaaa``, ``xaaab``, ``xaaac``, etc. Don't combine the OCDS Kit ``--pretty`` option with the ``split`` command.

.. _split-release-packages:

split-release-packages
----------------------

Reads release packages from standard input, and prints smaller release packages for each.

::

    cat tests/fixtures/realdata/release-package-1-2.json | ocdskit split-release-packages 2 | split -l 1 -a 4

The ``split`` command will write files named ``xaaaa``, ``xaaab``, ``xaaac``, etc. Don't combine the OCDS Kit ``--pretty`` option with the ``split`` command.

tabulate
--------

Load packages into a database.

Optional arguments:

* ``--drop`` drop all tables before loading
* ``--schema SCHEMA`` the release-schema.json to use

::

    cat release_package.json | ocdskit tabulate sqlite:///data.db

For the format of ``database_url``, see the `SQLAlchemy documentation <https://docs.sqlalchemy.org/en/rel_1_1/core/engines.html#database-urls>`__.

validate
--------

Reads JSON data from standard input, validates it against the schema, and prints errors.

Optional arguments:

* ``--schema SCHEMA`` the URL or path of the schema to validate against
* ``--check-urls`` check the HTTP status code if "format": "uri"
* ``--timeout TIMEOUT`` timeout (seconds) to GET a URL
* ``--verbose`` print items without validation errors

::

    cat tests/fixtures/* | ocdskit validate

.. _echo:

echo
----

Repeats the input, applying ``--encoding``, ``--ascii``, ``--pretty`` and ``--root-path``, and using the UTF-8 encoding.

You can use this command to reformat data:

-  Use UTF-8 encoding::

      cat iso-8859-1.json | ocdskit --encoding iso-8859-1 echo > utf-8.json

-  Use ASCII characters only::

      cat unicode.json | ocdskit --ascii echo > ascii.json

-  Use UTF-8 characters where possible::

      cat ascii.json | ocdskitecho > unicode.json

-  Pretty print::

      cat compact.json | ocdskit --pretty echo > pretty.json

-  Make compact::

      cat pretty.json | ocdskit echo > compact.json

You can also use this command to extract releases from release packages, and records from record packages. This is especially useful if a single package is too large to hold in memory.

-  Split a large record package into smaller packages of 100 records each::

      cat large-record-package.json | ocdskit echo --root-path records.item | ocdskit package-records --size 100

-  Split a large release package into smaller packages of 1,000 releases each::

      cat large-release-package.json | ocdskit echo --root-path releases.item | ocdskit package-releases --size 1000

Note that the package metadata from the large package won't be retained in the smaller packages; you can use the optional arguments of the :ref:`package-records` and :ref:`package-releases` commands to set the package metadata.

If the single package is small enough to hold in memory, you can use the :ref:`split-record-packages` and :ref:`split-release-packages` commands instead, which retain the package metadata.
