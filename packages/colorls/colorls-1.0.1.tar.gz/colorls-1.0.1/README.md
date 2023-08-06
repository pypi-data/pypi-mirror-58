`c*ls`
======

Uses colour and pipes output to less, with a sensible prompt.

Each command is equivalent to:-

    cls      ls -FC
    clls     ls -lF --time-style=long-iso
    cllls    ls -lF --time-style=full-iso
    cals     ls -FCA
    calls    ls -lFA --time-style=long-iso
    callls   ls -lFA --time-style=full-iso
    csls     sudo ls -FC
    cslls    sudo ls -lF --time-style=long-iso
    csllls   sudo ls -lF --time-style=full-iso
    csals    sudo ls -FCA
    csalls   sudo ls -lFA --time-style=long-iso
    csallls  sudo ls -lFA --time-style=full-iso

Development
-----------

Package dependencies are handled by [pipenv](https://pipenv.kennethreitz.org/).
It is assumed that *pipenv* will manage the installation of all concrete
dependency versions.  setup.py reads the dependency info from Pipfile
via the `pipenv` pacakge.

Before you can build the package, you will have to have `make`
installed.  You can then run **`make setup`** to create a [Virtualenv][]
(the `.venv` subdirectory where packages and metadata will be installed)
and then **`. .venv/bin/activate`** to activate it.

Then you can run **`pip install pipenv wheel`** and then use a build
process such as:-

    make build
    make dist
    # ... test .whl file now ...
    make release

Credits
-------

This package was created with [Cookiecutter][] and the [`audreyr/cookiecutter-pypackage`][pp]
project template.

  [Cookiecutter]: https://github.com/audreyr/cookiecutter
  [pp]: https://github.com/audreyr/cookiecutter-pypackage
  [Virtualenv]: http://packaging.python.org/guides/installing-using-pip-and-virtual-environments
