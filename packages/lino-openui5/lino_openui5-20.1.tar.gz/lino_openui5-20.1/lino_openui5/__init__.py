"""
.. autosummary::
   :toctree:

    openui5
    projects

"""


import os

from os.path import join, dirname
fn = join(dirname(__file__), 'setup_info.py')
exec(compile(open(fn, "rb").read(), fn, 'exec'))
__version__ = SETUP_INFO['version']

# intersphinx_urls = dict(docs="http://openui5.lino-framework.org")
srcref_url = 'https://github.com/lino-framework/openui5/blob/master/%s'
# doc_trees = ['docs']
