.. Pixion documentation master file, created by
   sphinx-quickstart on Thu Dec 18 15:11:33 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Pixel Perception Lib
================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   pixion
   tools

Introduction
------------

Tools and Library built at Pixel Perception


Installing the library
------------

.. code-block:: bash

   pip install pixion


Library Features
------------

TODO.


Extra Tools
------------

Library provides following tools:

.. code-block:: text

   # Allows color thresholding of webcam/image/videos in HSV format .
   hue-picker


For more details, see ``tools/README.md`` inside the repository.


Contribution Guidelines
------------

Install the following tools and run appropriate tasks for linting and formatting
before pushing a merge request.


Developer Dependencies
----------------------

Taskfile

We use `Taskfile <https://taskfile.dev/>`_ to allow developers to run common tasks.
Do enable
`autocompletion <https://taskfile.dev/installation/#setup-completions>`_.

.. code-block:: shell

   sudo snap install task --classic
   echo 'eval "$(task --completion bash)"' >> ~/.bashrc


Ruff


To apply ruff checks and formatting, run:

.. code-block:: shell

   task run-lint


Pre-Commit Hook


You can use pre-commit to trigger ``ruff check`` and ``ruff format`` on each
git commit.

.. code-block:: shell

   pip install pre-commit
   pre-commit install


License
------------

Distributed under the terms of the **GNU General Public License v3**.