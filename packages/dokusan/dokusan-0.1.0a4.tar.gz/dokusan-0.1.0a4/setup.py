# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['dokusan']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dokusan',
    'version': '0.1.0a4',
    'description': 'Sudoku generator and solver with a step-by-step guidance',
    'long_description': '========\nOverview\n========\n\n.. start-badges\n\n.. image:: https://github.com/unmade/dokusan/workflows/Lint%20and%20tests/badge.svg\n    :alt: Build Status\n    :target: https://github.com/unmade/dokusan/blob/master/.github/workflows/lint-and-tests.yml\n\n.. image:: https://codecov.io/gh/unmade/dokusan/branch/master/graph/badge.svg\n    :alt: Coverage Status\n    :target: https://codecov.io/gh/unmade/dokusan\n\n.. image:: https://img.shields.io/pypi/v/dokusan.svg\n    :alt: PyPI Package latest release\n    :target: https://pypi.org/project/dokusan\n\n.. image:: https://img.shields.io/pypi/wheel/dokusan.svg\n    :alt: PyPI Wheel\n    :target: https://pypi.org/project/dokusan\n\n.. image:: https://img.shields.io/pypi/pyversions/dokusan.svg\n    :alt: Supported versions\n    :target: https://pypi.org/project/dokusan\n\n.. image:: https://img.shields.io/badge/License-GPLv3-purple.svg\n    :alt: GPLv3 License\n    :target: https://github.com/unmade/dokusan/blob/master/LICENSE\n\n.. end-badges\n\nSudoku generator and solver with a step-by-step guidance\n\nInstallation\n============\n\n.. code-block:: bash\n\n    pip install dokusan\n\nQuickstart\n==========\n\nSudoku Solvers\n--------------\n\nStep-by-step solver\n*******************\n\nThis solver tries to solve sudoku using human-like strategies.\nCurrently following techniques are supported:\n\n- Naked/Hidden singles\n- Naked Pairs/Triplets\n- Locked Candidate\n- XY-Wing\n- Unique Rectangle\n\nFor example to see all techniques that sudoku has:\n\n.. code-block:: python\n\n    from dokusan import solvers\n    from dokusan.entities import BoxSize, Sudoku\n\n\n    sudoku = Sudoku.from_list(\n        [\n            [0, 0, 0, 0, 9, 0, 1, 0, 0],\n            [0, 0, 0, 0, 0, 2, 3, 0, 0],\n            [0, 0, 7, 0, 0, 1, 8, 2, 5],\n            [6, 0, 4, 0, 3, 8, 9, 0, 0],\n            [8, 1, 0, 0, 0, 0, 0, 0, 0],\n            [0, 0, 9, 0, 0, 0, 0, 0, 8],\n            [1, 7, 0, 0, 0, 0, 6, 0, 0],\n            [9, 0, 0, 0, 1, 0, 7, 4, 3],\n            [4, 0, 3, 0, 6, 0, 0, 0, 1],\n        ],\n        box_size=BoxSize(3, 3),\n    )\n\n    {step.combination.name for step in solvers.steps(sudoku)}\n\nBacktracking-based solver\n*************************\n\nThis solver is based on backtracking algorithm,\nhowever slightly modified to work fast\n\n.. code-block:: python\n\n    from dokusan import solvers\n    from dokusan.entities import BoxSize, Sudoku\n\n\n    sudoku = Sudoku.from_list(\n        [\n            [0, 0, 0, 0, 0, 0, 0, 0, 0],\n            [0, 0, 0, 0, 0, 3, 0, 8, 5],\n            [0, 0, 1, 0, 2, 0, 0, 0, 0],\n            [0, 0, 0, 5, 0, 7, 0, 0, 0],\n            [0, 0, 4, 0, 0, 0, 1, 0, 0],\n            [0, 9, 0, 0, 0, 0, 0, 0, 0],\n            [5, 0, 0, 0, 0, 0, 0, 7, 3],\n            [0, 0, 2, 0, 1, 0, 0, 0, 0],\n            [0, 0, 0, 0, 4, 0, 0, 0, 9],\n        ],\n        box_size=BoxSize(3, 3),\n    )\n\n    solvers.backtrack(sudoku)\n\nSudoku Generator\n----------------\n\nGenerator algorithm is mainly based on\n`article <https://dlbeer.co.nz/articles/sudoku.html>`_ by Daniel Beer.\nThe average time to generate Sudoku with rank of 150 is 700ms.\n\nTo generate a new sudoku:\n\n.. code-block:: python\n\n    from dokusan import generators\n\n\n    generators.random_sudoku(avg_rank=150)\n\nRanking and Sudoku difficulty\n*****************************\n\n``avg_rank`` option roughly defines the difficulty of the sudoku.\nSudoku with rank lower than 100 contains only naked/hidden singles.\nSudoku with rank greater than 150 contains\nNaked Subsets/Locked Candidate/XY Wing/etc...,\nhowever this is not always guaranteed.\n\nFor higher ranks it is also not guaranteed that generated Sudoku rank\nwill be higher than provided ``avg_rank``,\nso to ensure sudoku has desired rank one can do the following:\n\n.. code-block:: python\n\n    from dokusan import generators, stats\n\n\n    avg_rank = 450\n    while stats.rank(sudoku := generators.random_sudoku(avg_rank)) < avg_rank:\n        continue\n',
    'author': 'Aleksei Maslakov',
    'author_email': 'lesha.maslakov@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
