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
    'version': '0.1.0a2',
    'description': 'Sudoku solver with step-by-step guidance',
    'long_description': '========\nOverview\n========\n\nSudoku solver with step-by-step guidance\n\nInstallation\n============\n\n.. code-block:: bash\n\n    pip install dokusan\n\nQuickstart\n==========\n\nSudoku Solver\n-------------\n\nThe following code displays all steps leading to solution:\n\n.. code-block:: python\n\n    from dokusan import entities, techniques\n\n\n    class Unsolvable(Exception):\n        pass\n\n\n    def list_steps(sudoku: entities.Sudoku):\n        all_techniques = (\n            techniques.PencilMarking,\n            techniques.LoneSingle,\n            techniques.HiddenSingle,\n            techniques.NakedPair,\n            techniques.NakedTriplet,\n            techniques.LockedCandidate,\n            techniques.XYWing,\n            techniques.UniqueRectangle,\n        )\n        while not sudoku.is_solved():\n            for technique in all_techniques:\n                try:\n                    result = technique(sudoku).first()\n                except techniques.NotFound as exc:\n                    continue\n                else:\n                    sudoku.update(result.changes)\n                    yield result\n                    break\n            else:\n                raise Unsolvable\n\n    _ = 0\n\n    sudoku = entities.Sudoku.from_list([\n        [_, _, _, _, 9, _, 1, _, _],\n        [_, _, _, _, _, 2, 3, _, _],\n        [_, _, 7, _, _, 1, 8, 2, 5],\n        [6, _, 4, _, 3, 8, 9, _, _],\n        [8, 1, _, _, _, _, _, _, _],\n        [_, _, 9, _, _, _, _, _, 8],\n        [1, 7, _, _, _, _, 6, _, _],\n        [9, _, _, _, 1, _, 7, 4, 3],\n        [4, _, 3, _, 6, _, _, _, 1],\n    ])\n\n    for step in list_steps(sudoku):\n        print(step.combination)\n\nSudoku Generator\n----------------\n\nGenerator algorithm is mainly based on\n`article <https://dlbeer.co.nz/articles/sudoku.html>`_ by Daniel Beer.\nThe average time to generate Sudoku with rank of 150 is 700ms.\n\nTo generate a new sudoku:\n\n.. code-block:: python\n\n    from dokusan.generator import generate\n\n\n    generate(min_rank=150)\n\nRanking and Sudoku difficulty\n*****************************\n\n``min_rank`` option is used to roughly estimate the difficulty of the sudoku.\nSudoku with rank lower than 100 contains only naked/hidden singles.\nSudoku with rank greater than 150 might contains\nNaked Subsets/Locked Candidate/XY Wing/etc...,\nhowever this is not always guaranteed.\n\nFor higher ranks it is also not guaranteed that generated Sudoku rank\nwill be higher than provided ``min_rank``,\nso to ensure sudoku has desired rank one can do the following:\n\n.. code-block:: python\n\n    from dokusan import stats\n    from dokusan.generator import generate\n\n    min_rank = 450\n    while stats.rank(sudoku := generate(min_rank=min_rank)) < min_rank:\n        continue\n',
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
