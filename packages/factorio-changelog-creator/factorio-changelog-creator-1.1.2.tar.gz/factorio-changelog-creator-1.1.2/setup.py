# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['factorio_changelog_creator']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['factorio-changelog-creator = '
                     'factorio_changelog_creator.cli:main']}

setup_kwargs = {
    'name': 'factorio-changelog-creator',
    'version': '1.1.2',
    'description': 'A script to generate multiple Factorio changelog formats.',
    'long_description': '# Factorio Changelog Creator\n\nThis is a quick and dirty python script for generating changelog for Factorio mods in various formats.\n\n## Quick install\n\nInstall latest version from PYPI\n\n```code:: bash\npip install factorio-changelog-creator\n```\n\nInstall the current dev version from _GitHub_\n\n```code:: bash\npip install git+https://github.com/Roang-zero1/factorio-changelog-creator.git\n```\n\n## Usage\n\nGet the script file and put it somewhere on your computer.\n\nRun the script from the command line using `factorio-changelog-creator`. If no parameters are given, it will look for a file named `changelog.json` in the directory it was called from and it will output into the same directory.\n\nThere is a command line help available, which can be outputted with `factorio-changelog-creator -h`.\n\n```text\nusage: factorio-changelog-creator [-h]\n                                  [-f {md,ingame,forum} [{md,ingame,forum} ...]]\n                                  [-v]\n                                  [output_dir] [input_file]\n\nFactorio changelog generator\n\npositional arguments:\n  output_dir            Directory where the files will be written\n  input_file            JSON file to parse for changes\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -f {md,ingame,forum} [{md,ingame,forum} ...], --formats {md,ingame,forum} [{md,ingame,forum} ...]\n                        Which format[s] should be generated\n  -v, --verbose         Output verbosity\n```\n\nBy default the markdown and in-game changelog will be generated. The forum changelog can be generated with `python3 changelog-script.py -f forum`.\n\n- `changelog_forum.txt`: The syntax forums.factorio.com uses\n- `CHANGELOG.md`: A markdown syntax that should work both on mods.factorio.com and GitHub\n- `changelog.txt`: The syntax the game uses - this is what should be left in the mod\n\n## Format\n\nThe changelog definition file should be a JSON file containing a dictionary of version dictionaries.\n\nThe format of the dictionary is this:\n\n```json\n{\n  "0.1.0": {\n    "date": "2019-06-08", -- Optional, can be anything\n\n    "Changes": ["Change without category"], --Changes will be put in the Other Category\n\n    "Categories": { -- Categories may be any string\n      "Features": ["Change in category"]\n    }\n  }\n}\n```\n\nChanges can be declared as simple strings, or as a table in the following format:\n\n```json\n{\n  "change": "Change description", -- Mandatory\n  "more": "https://link.to.nowhere.com", -- Optional\n  "by": "Name", -- Optional\n}\n```\n\n`more` and `by` work in the same way, but have different meanings: `more` is a link with more information and `by` is\nthe author of the change.\nThey can be either a single entry or a list of entries, the list will be outputted comma-separated.\nEach entry may either be a plain string that will be directly used or a dictionary with a single entry in the format:\n\n```json\n{\n  "url_text": "url_target"\n}\n```\n\nDepending on the format either a link will be generated of if this in not possible `more` will use the `url_target` value and `by` will use the `url_text`.\n\n## Acknowledgement\n\nInitial Lua implementation by theRustyKnife/factorio-changelog-script\n',
    'author': 'Roang_zero1',
    'author_email': 'lucas@brandstaetter.tech',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Roang-zero1/factorio-changelog-creator',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
