cython-package-build-example
============================

This package is an example of a Python module using Cython with a GitHub Action
that builds it for different platforms and and uploads the package to PyPI
(test PyPi: https://test.pypi.org/project/cython-package-build-example).

This package does not do anything useful, it is just an example. It implements
a "hello world" function in Cython.

Project structure
-----------------

- **.github/workflows/build-sdist.yml** - GitHub Action that builds the source distribution (sdist) of the package and uploads it to PyPI
- **.github/workflows/build-wheels.yml** - GitHub Action that builds the wheels of the package and uploads them to PyPI.
- **pyproject.toml** - configuration file for the build process. See:
    - https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/ - PIP documentation about pyproject.toml
    - https://peps.python.org/pep-0621/ - PEP 621 - describes the metadata that you can put into the pyproject.toml file
- **setup.py** - additional configuration for Cython that couldn't be put into the pyproject.toml file. See: https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html#basic-setup-py
- **src/__init__.py** - package definition file (it also defines the version of the package)
- **src/main.pyx** - Cython source file with the :code:`hello()` function.
- **bump_version.py** - Python script used for updating the version number in the :code:`src/__init__.py` file and for tagging the git commit with that version.
- **clear_build_files.py** - Python script that removes the files created during the build process (these files are .gitignored).

How to build and upload the package using this setup?
-----------------------------------------------------

Assuming that the repository is connected to GitHub most of the work is automated
all you need to do is running the `bump_version.py` script and pushing the changes
and the tags to GitHub.

.. code-block:: bash

    python bump_version.py
    git push
    git push --tags

Before pushing you need to setup the PYPI_TOKEN secret in the GitHub repository settings.

See:
- https://docs.github.com/en/actions/reference/encrypted-secrets#creating-encrypted-secrets-for-a-repository - setting up a secret
- https://packaging.python.org/en/latest/tutorials/packaging-projects/ - packaging Python projects tutorial

Note that the token has to have the :code:`pypi-` prefix. An example token would look like this:

.. code-block:: bash

    pypi-adsjfhalsjdHALKJadslkjfhasdJHASd879273gfoasugoAYfasjkdgfasd70fhausdflaksdjfhaosd7

**Note:** This is not a real token, it's just me hitting the keyboard randomly.

Pushing tags that match the :code:`*.*.*` pattern triggers two GitHub Actions. One of them builds
wheels (binary packages) and the other one builds the source distribution (sdist). Generated files
are uploaded to PyPI and to the GitHub release.

.. WARNING::

    Building wheels for linux is very slow. It takes about 40 minutes.

Configuration of the GitHub Actions
-----------------------------------

The github actions are setup to upload to test PyPI. If you want to upload to the real PyPI you
need to modify them. Simply change the "Publish to PyPI" workflow step to use a command that
points at PyPI (using the :code:`--repository pypi` instead of :code:`--repository testpypi`).

Currently the GitHub actions are configured to build the wheels for Python 3.11. If you want to
change it, add different versions to the :code:`matrix` in the :code:`build-wheels.yml` file.


Important links
---------------

This section contains some links that I found useful while setting up this project. Some of them
are already mentioned in the text above.

- :code:`twine`: https://twine.readthedocs.io/en/latest/index.html
- :code:`cibuildwheel`: https://cibuildwheel.readthedocs.io
- The problems with linux wheels (PEP 513): https://peps.python.org/pep-0513/
- Why am I not using :code:`build`?: https://github.com/pypa/build/issues/480
- How to package Python projects: https://packaging.python.org/en/latest/tutorials/packaging-projects/
- The structure of :code:`pyproject.toml`: https://peps.python.org/pep-0621/
- Creating API tokens on PyPI: https://pypi.org/help/#apitoken