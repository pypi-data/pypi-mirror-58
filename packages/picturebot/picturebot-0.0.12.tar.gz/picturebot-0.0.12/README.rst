==========
picturebot
==========


.. image:: https://img.shields.io/pypi/v/picturebot.svg
        :target: https://pypi.python.org/pypi/picturebot

.. image:: https://img.shields.io/travis/Tomekske/picturebot.svg
        :target: https://travis-ci.org/Tomekske/picturebot

.. image:: https://readthedocs.org/projects/picturebot/badge/?version=latest
        :target: https://picturebot.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Program to ease picture development flow 


* Free software: MIT license
* Documentation: https://picturebot.readthedocs.io.


Features
--------

* Create a workspace directory
* Create flows within the workspace directory
* Renaming filenames according to the project within a certain flow
* Create a backup of the baseflow directory
* Automatically open the config file
* Check whether all the pictures within a shoot are edited


TODO
----

* Update documentation
* Multiple workspaces support
* Upload pictures to google pictures

Usage
-----
Create a workspace::
 pb workspace -c
Initialize workspace::
 pb workspace -i
Make a copy of a picture in the backup flow::
 pb -b <filename>
Make a copy of all pictures within the base flow and copy them to the backup flow::
 pb -bs
Rename a picture within the baseflow accordingly to it's shootname::
 pb -r <filename> <index>
Rename all pictures within the baseflow accordingly to it's shootname::
 pb -mr
Convert a raw picture within the baseflow to a jpg format and store it within the preview flow::
 pb -c <filename>
Open config file in an editor::
 pb config -s
Print config file location::
 pb config -l
Print picturebot script version::
 pb config -v
Create a new shoot::
 pb config -v <name> <dd-MM-YYYY>

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
