.. image:: https://travis-ci.org/jeremiedecock/jhunt.svg?branch=master
    :target: https://travis-ci.org/jeremiedecock/jhunt

==================
JHunt - Job Hunter
==================

Copyright (c) 2015-2018 Jeremie DECOCK (http://www.jdhp.org)

* Web site: http://www.jdhp.org/projects_en.html
* Source code: https://github.com/jeremiedecock/jhunt
* Issue tracker: https://github.com/jeremiedecock/jhunt/issues
* JHunt on PyPI: https://pypi.python.org/pypi/jhunt
* JHunt on Anaconda Cloud: https://anaconda.org/jdhp/jhunt


Description
===========

JHunt is an open source tool to manage job adverts for job
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

You can install, upgrade, uninstall JHunt with these commands (in a
terminal)::

    pip install --pre jhunt
    pip install --upgrade jhunt
    pip uninstall jhunt

Or, if you have downloaded the JHunt source code::

    python3 setup.py install

.. There's also a package for Debian/Ubuntu::
.. 
..     sudo apt-get install jhunt

Windows
-------

.. Note:
.. 
..     The following installation procedure has been tested to work with Python
..     3.4 under Windows 7.
..     It should also work with recent Windows systems.

You can install, upgrade, uninstall JHunt with these commands (in a
`command prompt`_)::

    py -m pip install --pre jhunt
    py -m pip install --upgrade jhunt
    py -m pip uninstall jhunt

Or, if you have downloaded the JHunt source code::

    py setup.py install

MacOSX
-------

Note:

    The following installation procedure has been tested to work with Python
    3.5 under MacOSX 10.9 (*Mavericks*).
    It should also work with more recent MacOSX systems.

You can install, upgrade, uninstall JHunt with these commands (in a
terminal)::

    pip install --pre jhunt
    pip install --upgrade jhunt
    pip uninstall jhunt

Or, if you have downloaded the JHunt source code::

    python3 setup.py install

JHunt requires Qt5 and its Python 3 bindings plus few additional
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

To search for bugs or report them, please use the JHunt Bug Tracker at:

    https://github.com/jeremiedecock/jhunt/issues


License
=======

This project is provided under the terms and conditions of the
`MIT License`_.

.. _MIT License: http://opensource.org/licenses/MIT
.. _JHunt: https://github.com/jeremiedecock/jhunt
.. _command prompt: https://en.wikipedia.org/wiki/Cmd.exe
