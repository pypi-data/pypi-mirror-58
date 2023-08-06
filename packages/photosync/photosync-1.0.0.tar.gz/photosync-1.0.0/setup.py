# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['photosync']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['photosync = photosync.photosync:main']}

setup_kwargs = {
    'name': 'photosync',
    'version': '1.0.0',
    'description': 'Synchronize your phone photos easily',
    'long_description': '=========\nphotosync\n=========\n\nSynchronize your phone photos easily\n\nEach time you take new photos with your phone and you want to transfer them to your computer you have the same problem:\nwhen did you last transfer them? What should you transfer? How to know if you have already back them up? This program is\nhere to help solving that problem. It is not really a synchronisation program. Actually it will keep track of already\ntransferred files, so you copy each file from the source once. When copied, you can sort, move, reorganize them or whatever.\nYou don\'t need to keep them as there were transferred to avoid them being transferred again next time. That\'s why it is not\nreally a synchronization program.\n\nThe "database" is a clear text JSON file optimized for quick finding.\n\nAs of my Android phone, photo and video file names have to contain the following pattern : ``(IMG|VID)_YYYYMMDD``.\n\ninstallation\n------------\n\n::\n\n    pip install .\n\nThis will install a ``photosync`` script.\n\nusage\n-----\n\n::\n\n    usage: photosync [-h] [-d DB] [-v] src dest\n\n    positional arguments:\n      src             where are the photos you want to copy\n      dest            where you want to copy your photos\n\n    optional arguments:\n      -h, --help      show this help message and exit\n      -d DB, --db DB  the location of the file that contains information about\n                      already transferred photos\n      -v, --verbose\n\n\n',
    'author': 'Alexandre G',
    'author_email': 'alex.git@ralouf.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/bravefencermusashi/photosync',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
