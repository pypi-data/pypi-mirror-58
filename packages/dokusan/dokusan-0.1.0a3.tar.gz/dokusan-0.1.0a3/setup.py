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
    'version': '0.1.0a3',
    'description': 'Sudoku solver with step-by-step guidance',
    'long_description': '========\nOverview\n========\n\nSudoku solver with step-by-step guidance\n\nInstallation\n============\n\n.. code-block:: bash\n\n    pip install dokusan\n\nQuickstart\n==========\n\nSudoku Solvers\n--------------\n\nStep-by-step solver\n*******************\n\nThis solver tries to solve sudoku using human-like strategies.\nCurrently following techniques are supported:\n\n- Naked/Hidden singles\n- Naked Pairs/Triplets\n- Locked Candidate\n- XY-Wing\n- Unique Rectangle\n\nFor example to see all techniques that sudoku has:\n\n.. code-block:: python\n\n    from dokusan import solvers\n    from dokusan.entities import BoxSize, Sudoku\n\n\n    sudoku = Sudoku.from_list(\n        [\n            [0, 0, 0, 0, 9, 0, 1, 0, 0],\n            [0, 0, 0, 0, 0, 2, 3, 0, 0],\n            [0, 0, 7, 0, 0, 1, 8, 2, 5],\n            [6, 0, 4, 0, 3, 8, 9, 0, 0],\n            [8, 1, 0, 0, 0, 0, 0, 0, 0],\n            [0, 0, 9, 0, 0, 0, 0, 0, 8],\n            [1, 7, 0, 0, 0, 0, 6, 0, 0],\n            [9, 0, 0, 0, 1, 0, 7, 4, 3],\n            [4, 0, 3, 0, 6, 0, 0, 0, 1],\n        ],\n        box_size=BoxSize(3, 3),\n    )\n\n    {step.combination.name for step in solvers.steps(sudoku)}\n\nBacktracking-based solver\n*************************\n\nThis solver is based on backtracking algorithm,\nhowever slightly modified to work fast\n\n.. code-block:: python\n\n    from dokusan import solvers\n    from dokusan.entities import BoxSize, Sudoku\n\n\n    sudoku = Sudoku.from_list(\n        [\n            [0, 0, 0, 0, 0, 0, 0, 0, 0],\n            [0, 0, 0, 0, 0, 3, 0, 8, 5],\n            [0, 0, 1, 0, 2, 0, 0, 0, 0],\n            [0, 0, 0, 5, 0, 7, 0, 0, 0],\n            [0, 0, 4, 0, 0, 0, 1, 0, 0],\n            [0, 9, 0, 0, 0, 0, 0, 0, 0],\n            [5, 0, 0, 0, 0, 0, 0, 7, 3],\n            [0, 0, 2, 0, 1, 0, 0, 0, 0],\n            [0, 0, 0, 0, 4, 0, 0, 0, 9],\n        ],\n        box_size=BoxSize(3, 3),\n    )\n\n    solvers.backtrack(sudoku)\n\nSudoku Generator\n----------------\n\nGenerator algorithm is mainly based on\n`article <https://dlbeer.co.nz/articles/sudoku.html>`_ by Daniel Beer.\nThe average time to generate Sudoku with rank of 150 is 700ms.\n\nTo generate a new sudoku:\n\n.. code-block:: python\n\n    from dokusan import generators\n\n\n    generators.random_sudoku(min_rank=150)\n\nRanking and Sudoku difficulty\n*****************************\n\n``min_rank`` option is used to roughly estimate the difficulty of the sudoku.\nSudoku with rank lower than 100 contains only naked/hidden singles.\nSudoku with rank greater than 150 might contain\nNaked Subsets/Locked Candidate/XY Wing/etc...,\nhowever this is not always guaranteed.\n\nFor higher ranks it is also not guaranteed that generated Sudoku rank\nwill be higher than provided ``min_rank``,\nso to ensure sudoku has desired rank one can do the following:\n\n.. code-block:: python\n\n    from dokusan import generators, stats\n\n\n    min_rank = 450\n    while stats.rank(sudoku := generators.random_sudoku(min_rank=min_rank)) < min_rank:\n        continue\n',
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
