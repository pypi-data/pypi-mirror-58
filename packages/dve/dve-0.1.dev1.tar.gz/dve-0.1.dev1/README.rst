.. image:: https://travis-ci.org/jeremiedecock/dve.svg?branch=master
    :target: https://travis-ci.org/jeremiedecock/dve

============================
Python Data Versatile Editor
============================

Copyright (c) 2015-2018 Jeremie DECOCK (http://www.jdhp.org)

* Web site: http://www.jdhp.org/projects_en.html
* Source code: https://github.com/jeremiedecock/dve
* Issue tracker: https://github.com/jeremiedecock/dve/issues
* DVE on PyPI: https://pypi.python.org/pypi/dve
* DVE on Anaconda Cloud: https://anaconda.org/jdhp/dve


Description
===========

DVE is an open source tool to manage job adverts for job
seekers.

.. warning::

    This project is in beta stage.


Dependencies
============

- Python >= 3.0
- Qt5 for Python
- Matplotlib
- Pandas


.. _install:

Installation
============

Gnu/Linux
---------

You can install, upgrade, uninstall DVE with these commands (in a
terminal)::

    pip install --pre dve
    pip install --upgrade dve
    pip uninstall dve

Or, if you have downloaded the DVE source code::

    python3 setup.py install

.. There's also a package for Debian/Ubuntu::
.. 
..     sudo apt-get install dve

Windows
-------

.. Note:
.. 
..     The following installation procedure has been tested to work with Python
..     3.4 under Windows 7.
..     It should also work with recent Windows systems.

You can install, upgrade, uninstall DVE with these commands (in a
`command prompt`_)::

    py -m pip install --pre dve
    py -m pip install --upgrade dve
    py -m pip uninstall dve

Or, if you have downloaded the DVE source code::

    py setup.py install

MacOSX
-------

Note:

    The following installation procedure has been tested to work with Python
    3.5 under MacOSX 10.9 (*Mavericks*).
    It should also work with more recent MacOSX systems.

You can install, upgrade, uninstall DVE with these commands (in a
terminal)::

    pip install --pre dve
    pip install --upgrade dve
    pip uninstall dve

Or, if you have downloaded the DVE source code::

    python3 setup.py install

DVE requires Qt5 and its Python 3 bindings plus few additional
libraries to run.

.. These dependencies can be installed using MacPorts::
.. 
..     port install gtk3
..     port install py35-gobject3
..     port install py35-matplotlib

.. or with Hombrew::
.. 
..     brew install gtk+3
..     brew install pygobject3


Bug reports
===========

To search for bugs or report them, please use the DVE Bug Tracker at:

    https://github.com/jeremiedecock/dve/issues


License
=======

This project is provided under the terms and conditions of the
`MIT License`_.

.. _MIT License: http://opensource.org/licenses/MIT
.. _DVE: https://github.com/jeremiedecock/dve
.. _command prompt: https://en.wikipedia.org/wiki/Cmd.exe
