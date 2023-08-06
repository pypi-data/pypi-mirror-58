Tracklr
=======

.. contents::
      :local:


Introduction
------------

``Tracklr`` is a command-line toolset for processing `iCalendar` feeds.


Installation
------------

Install ``tracklr`` via ``pip``::

    pip install git+https://gitlab.com/markuz/tracklr

Or::

    pip install https://gitlab.com/markuz/tracklr/-/archive/master/tracklr-master.tar.bz2


Configuration
-------------

Out of the box ``tracklr`` uses its own configuration stored in ``Tracklr.__config__``.

For PDF reports ``tracklr`` uses by default its own HTML template in ``tracklr.pdf.Pdf.__template__``.

``tracklr`` provides ``init`` command to create ``tracklr.yml`` and ``pdf.html`` files either in
user config directory eg. ``~/.config/tracklr/`` or current working directory (default).

See ``tracklr init --help`` for more details.


Usage
-----

::

    # setup local config
    tracklr init config

    # setup global pdf.html uses for all tracklr instances
    tracklr init template --user-config-dir

    # show configuration
    tracklr show

    # show only 2019-02 events
    tracklr ls -d 2019-02

    # show only 2019 @tracklr events
    tracklr ls -d 2019 -i @tracklr

    # generate 2019 @tracklr PDF report 
    tracklr pdf -d 2019 -i @tracklr

    # show all hours matching tag #tags
    tracklr tag -i "#tags"


Development
-----------

`Tracklr` git repository is available at https://gitlab.com/markuz/tracklr

Pull requests are welcome. For more information, see https://tracklr.com/development.html


Documentation
-------------

Project documentation for the current version is available at https://tracklr.com/

Source of the documentaton is available at `Tracklr`'s repository
https://gitlab.com/markuz/tracklr/tree/master/docs/source


License
-------

`BSD 3-clause Clear License <https://gitlab.com/markuz/tracklr/blob/master/LICENSE>`_
