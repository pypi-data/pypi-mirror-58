# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['fn_graph_studio']

package_data = \
{'': ['*']}

install_requires = \
['dash>=1.7,<2.0',
 'dash_core_components>=1.6,<2.0',
 'dash_interactive_graphviz>=0.0.2,<0.0.3',
 'dash_split_pane>=1.0,<2.0',
 'dash_treeview_antd>=0.0.1,<0.0.2',
 'fn_graph>=0.1.0,<0.2.0',
 'pandas>=0.25.3,<0.26.0',
 'plotly>=4.4,<5.0']

setup_kwargs = {
    'name': 'fn-graph-studio',
    'version': '0.1.1',
    'description': 'A web based explorer for fn_graph function composers',
    'long_description': None,
    'author': 'James Saunders',
    'author_email': 'james@businessoptics.biz',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
