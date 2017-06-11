=========
Elm Magic
=========


.. image:: https://img.shields.io/pypi/v/elm_magic.svg
        :target: https://pypi.python.org/pypi/elm_magic

.. image:: https://img.shields.io/travis/ali--/elm_magic.svg
        :target: https://travis-ci.org/ali--/elm_magic

.. image:: https://readthedocs.org/projects/elm-magic/badge/?version=latest
        :target: https://elm-magic.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/ali--/elm_magic/shield.svg
     :target: https://pyup.io/repos/github/ali--/elm_magic/
     :alt: Updates

Elm Magic provides IPython magic commands that execute elm-lang code

SYNOPSYS
-----
    %%elm 
          ... <elm-lang code> ...
              
                  
              - or - 
                  

    %%elm -i elm-lang/http elm-lang/mouse -w /tmp/myelmdir
          ... <elm-lang code> ...

    This magic will (1) set working dir to /tmp/myelmdir (or temporary dir)
       (2) install elm-lang/http and elm-lang/mouse with elm-package install
       (3) compile the cell input with elm-make 
       (4) display the cell output as html

USAGE
-----
    first install elm_magic

      git clone git@github.com:ali--/elm_magic.git
      cd elm_magic
      pip install -e .

      if elm and nodejs are not installed, you can try:

          elm_magic install --target <install-dir>

          where <install-dir> is writable by the current user.
            and in the user's PATH

                  e.g /usr/local/ or /opt/conda

    then in IPython or Jupyter:
 
        %load_ext elm_magic

    then start using the %%elm magic:
     
        %%elm 
          ... elm-lang code ...

    see or set configuration parameters:

        %config ElmMagic

Features
--------

* provides %%elm magic that executes elm-lang and displayes the result
* can be used with any kernel
* directory used by elm-make is configurable
* provides cli for installing nodejs and elm

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.
Started with the help of https://github.com/abingham/jupyter-elm-kernel

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

* Free software: GNU General Public License v3
* Documentation: https://elm-magic.readthedocs.io.


