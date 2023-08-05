ABlog for Sphinx
================

ABlog is a Sphinx extension that converts any documentation or personal
website project into a full-fledged blog with:

  * `Atom feeds`_
  * `Archive pages`_
  * `Blog sidebars`_
  * `Disqus integration`_
  * `Font-Awesome integration`_
  * `Easy GitHub Pages deploys`_

.. _Atom feeds: https://ablog.readthedocs.org/blog/atom.xml
.. _Archive pages: https://ablog.readthedocs.org/blog/
.. _Blog sidebars: https://ablog.readthedocs.org/manual/ablog-configuration-options/#sidebars
.. _Disqus integration: https://ablog.readthedocs.org/manual/ablog-configuration-options/#disqus-integration
.. _Font-Awesome integration: https://ablog.readthedocs.org/manual/ablog-configuration-options/#fa
.. _Easy GitHub Pages deploys: https://ablog.readthedocs.org/manual/deploy-to-github-pages/

.. _installation:

Installation
------------

You can install ABlog using pip_::

    pip install -U ablog

This will also install `Sphinx <http://sphinx-doc.org/>`_, Alabaster_,
Werkzeug_, Invoke_, dateutil_ respectively required for building your website,
making it look good, generating feeds, running deploy commands, and parsing
dates.

.. _pip: https://pip.pypa.io
.. _Werkzeug: https://werkzeug.pocoo.org/
.. _Alabaster: https://github.com/bitprophet/alabaster
.. _Invoke: https://www.pyinvoke.org/
.. _dateutil: https://pypi.python.org/pypi/python-dateutil

Getting Started
---------------

If you are starting a new project, see `ABlog Quick Start`_ guide.

If you already have a project, enable blogging by making following changes in ``conf.py``:

.. code-block:: python

  # 1. Add 'ablog' to list of extensions
  extensions = [
      '...',
      'ablog'
  ]

  # 2. Add ablog templates path
  import ablog

  # 2a. if `templates_path` is not defined
  templates_path = [ablog.get_html_templates_path()]

  # 2b. if `templates_path` is defined
  templates_path.append(ablog.get_html_templates_path())

.. _ABlog Quick Start: https://ablog.readthedocs.org/manual/ablog-quick-start


How it works
------------

If you are new to Sphinx_ and reStructuredText markup language,
you might find `reStructuredText Primer`_ useful. Once you have
content (in ``.rst`` files), you can post *any page* using the
:rst:dir:`post` directive as follows:

.. _reStructuredText Primer: http://sphinx-doc.org/rest.html

.. code-block:: rst

  .. post:: Apr 15, 2014
     :tags: earth, love, peace
     :category: python
     :author: me
     :location: SF
     :language: en

ABlog will index all files posted as above and list them in archives and feeds
specified in ``:tag:``, ``:category:``, etc. options.

You can also include a list of posts using :rst:dir:`postlist` directive:

.. code-block:: rst

  .. postlist::
     :list-style: circle
     :category: Manual
     :format: {title}
     :sort:

For ABlog documentation, this converts to the following where you
can find more about configuring and using ABlog:

.. postlist::
   :category: Manual
   :list-style: circle
   :format: {title}
   :sort:

.. only:: html

   .. image:: https://secure.travis-ci.org/sunpy/ablog.png?branch=devel
      :target: https://travis-ci.org/#!/sunpy/ablog

   .. image:: https://readthedocs.org/projects/ablog/badge/?version=latest
      :target: https://ablog.readthedocs.org/


.. toctree::
   :hidden:
   :glob:

   */*
