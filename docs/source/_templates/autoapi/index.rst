API Reference
=============

The API Reference provides an organized, auto-generated view of Pixion's
public modules, classes, and functions. Content on this page is produced from
project source code and docstrings using Sphinx AutoAPI. Use the navigation
below to open the top-level API pages.

.. toctree::
   :titlesonly:

   {% for page in pages|selectattr("is_top_level_object") %}
   {{ page.include_path }}
   {% endfor %}

