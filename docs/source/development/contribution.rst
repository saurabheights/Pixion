Contribution Guidelines
=======================

Thank you for contributing to Pixion. To help maintain a consistent, high-quality
codebase, please install the developer tools below and run the appropriate
tasks before opening a merge request.


Developer dependencies
----------------------

Taskfile
~~~~~~~~

We use `Taskfile <https://taskfile.dev/>`_ to automate common development
workflows and task aliases. Follow the official Taskfile documentation for
platform-specific installation instructions. On systems that support snap, you
can install it with:

.. code-block:: shell

   sudo snap install task --classic

Enable shell completions (optional):

.. code-block:: shell

   echo 'eval "$(task --completion bash)"' >> ~/.bashrc

(See the Taskfile installation guide for Windows and other platforms.)

Ruff
~~~~

Ruff is used for linting and automatic formatting. Run the project's lint and
format tasks with:

.. code-block:: shell

   task run-lint


Pre-commit Hook
~~~~~~~~~~~~~~~~

We recommend using `pre-commit <https://pre-commit.com/>`_ to run Ruff on each
commit automatically. Install and enable the hook with:

.. code-block:: shell

   pip install pre-commit
   pre-commit install


If you have questions or need assistance, please open an issue or start a
discussion in the repository. Thanks for helping keep Pixion clean and reliable.
