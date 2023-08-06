.. image:: https://travis-ci.org/jeremiedecock/taskmg.svg?branch=master
    :target: https://travis-ci.org/jeremiedecock/taskmg

=======
Task-Mg
=======

Copyright (c) 2015-2020 Jeremie DECOCK (http://www.jdhp.org)

* Web site: http://www.jdhp.org/projects_en.html
* Source code: https://github.com/jeremiedecock/taskmg
* Issue tracker: https://github.com/jeremiedecock/taskmg/issues
* Task-Mg on PyPI: https://pypi.python.org/pypi/taskmg
* Task-Mg on Anaconda Cloud: https://anaconda.org/jdhp/taskmg


Description
===========

This software is an open source task manager.

.. warning::

    This project is in beta stage.


Dependencies
============

- Python >= 3.0
- Qt5 for Python
- Pandas


.. _install:

Installation
============

Gnu/Linux
---------

You can install, upgrade, uninstall Task-Mg with these commands (in a
terminal)::

    pip install --pre taskmg
    pip install --upgrade taskmg
    pip uninstall taskmg

Or, if you have downloaded the Task-Mg source code::

    python3 setup.py install

.. There's also a package for Debian/Ubuntu::
.. 
..     sudo apt-get install taskmg

Windows
-------

.. Note:
.. 
..     The following installation procedure has been tested to work with Python
..     3.4 under Windows 7.
..     It should also work with recent Windows systems.

You can install, upgrade, uninstall Task-Mg with these commands (in a
`command prompt`_)::

    py -m pip install --pre taskmg
    py -m pip install --upgrade taskmg
    py -m pip uninstall taskmg

Or, if you have downloaded the Task-Mg source code::

    py setup.py install

MacOSX
-------

Note:

    The following installation procedure has been tested to work with Python
    3.5 under MacOSX 10.9 (*Mavericks*).
    It should also work with more recent MacOSX systems.

You can install, upgrade, uninstall Task-Mg with these commands (in a
terminal)::

    pip install --pre taskmg
    pip install --upgrade taskmg
    pip uninstall taskmg

Or, if you have downloaded the Task-Mg source code::

    python3 setup.py install

Task-Mg requires Qt5 and its Python 3 bindings plus few additional
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

To search for bugs or report them, please use the Task-Mg Bug Tracker at:

    https://github.com/jeremiedecock/taskmg/issues


License
=======

This project is provided under the terms and conditions of the
`MIT License`_.

.. _MIT License: http://opensource.org/licenses/MIT
.. _Task-Mg: https://github.com/jeremiedecock/taskmg
.. _command prompt: https://en.wikipedia.org/wiki/Cmd.exe
