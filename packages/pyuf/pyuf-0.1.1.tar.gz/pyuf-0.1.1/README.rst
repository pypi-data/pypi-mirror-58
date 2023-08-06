PyUF: Python Union-Find
=======================

Implementation of the ``Union-Find`` data structure in Python.

Data is divided into different groups ("partitions"). Each group has a name,
and a set of objects. Over this setup, we want to support two operations:

    * ``find(x)``: Return the name of the group where x belongs to.
    * ``union(g1, g2)``: Given two groups, merge them into one. The new
      meta-group contains all the elements from ``g1`` and ``g2``.

Example usage:

.. code:: python

    >>> space = UnionFindSpace(
        Partition("letters", "abcdef"),
        Partition("numbers", range(5)),
    )

    >>> space.find("a")
    letters

    >>> space.find(1)
    numbers

    >>> partition = space.union("letters", "numbers")
    >>> partition.name
    letters_numbers


    # It's possible to indicate the name of the  group

    >>> partition = space.union("letters", "numbers", "alpha")
    >>> partition.name
    alpha


Development
^^^^^^^^^^^
In order to start working or testing with this repository, you'll need to create and activate a new virtual environment.
Respectively, the commands are the following ones

.. code:: bash

    $ python3 -m venv env
    $ source env/bin/activate

After that you can setup the environment with:

.. code:: bash

    $ make install-dev
    $ make test

Make sure that:

    1. The test pass successfully
    2. The code is properly formatted (this can be checked with ``make lint`` and corrected with ``make format``).
