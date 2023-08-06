Alignak WebUI Graphite Module
=============================

*Shinken / Alignak WebUI module for the Graphite graphs*

.. image:: https://api.travis-ci.org/mohierf/mod-ui-graphite.svg?branch=develop
    :target: https://travis-ci.org/mohierf/mod-ui-graphite
    :alt: Develop branch build status

.. image:: https://api.codacy.com/project/badge/Grade/4ffb2900db7949e98e528a4a9f342d71
    :target: https://www.codacy.com/manual/Shinken_modules/mod-ui-graphite?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mohierf/mod-ui-graphite&amp;utm_campaign=Badge_Grade
    :alt: Development code static analysis

.. image:: https://codecov.io/gh/mohierf/mod-ui-graphite/branch/develop/graph/badge.svg
    :target: https://codecov.io/gh/mohierf/mod-ui-graphite
    :alt: Development code tests coverage

.. image:: https://badge.fury.io/py/alignak_webui_graphite.svg
    :target: https://badge.fury.io/py/alignak-webui-graphite
    :alt: Most recent PyPi version

.. image:: https://img.shields.io/badge/License-AGPL%20v3-blue.svg
    :target: http://www.gnu.org/licenses/agpl-3.0
    :alt: License AGPL v3


Shinken / Alignak module for viewing Graphite graphs in the Web UI.

This module is a refactoring of the ``ui-graphite`` module to allow using it with Shinken or Alignak.

This module allows:
   - to define the Graphite hierarchy configuration
   - to use templates (url or json based) for the graphs
   - to configure:

      - the host check metric name
      - graph and font size for dashboard and host/service page graphs
      - define if warning, critical, min and max thresholds are present on graphs
      - define warning, critical, min and max lines colors
      - define graphs timezone (default is Europe/Paris)
      - define graphs line mode (connected, staircase, slope)

This module is fully compatible with the WebUI2 at its most recent version (Alignak compatible). It is also compatible with the Alignak inner metrics module for the Graphite hierarchy.


Installation
------------

The installation of this module will copy some configuration files in the Alignak default configuration directory (eg. */usr/local/share/alignak*). The copied files are located in the default sub-directory used for the modules (eg. *arbiter/modules*).

**Note** that the module provided templates will be copied to the */usr/local/share/alignak/etc/modules/ui-graphite-templates*. You may add your own templates in this directory -)

From PyPI
~~~~~~~~~
To install the module from PyPI::

    sudo pip install alignak_webui_graphite


From source files
~~~~~~~~~~~~~~~~~
To install the module from the source files (for developing purpose)::

    git clone https://github.com/mohierf/mod-ui-graphite
    cd mod-ui-graphite
    sudo pip install . -e



Bugs, issues and contributing
-----------------------------

Contributions to this project are welcome and encouraged ... `issues in the project repository <https://github.com/mohierf/mod-ui-graphite/issues>`_ are the common way to raise an information.
