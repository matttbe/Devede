#!/usr/bin/python

import os
from glob import glob
from distutils.core import setup

def get_data_files():
    return [
        (os.path.join('share', 'applications'), ['devede.desktop']),
        (os.path.join('share', 'pixmaps'), ['devede.svg']),
        (os.path.join('share', 'devede'), glob("interface/*")),
        (os.path.join('share', 'devede'), glob('pixmaps/*g')),
        (os.path.join('share', 'devede'), ['devede.svg']),
        (os.path.join('share', 'devede'), ['devedesans.ttf']),
        (os.path.join('share', 'devede', 'backgrounds'), glob('pixmaps/backgrounds/*')),
        (os.path.join('share', 'doc', 'devede', 'html'), glob('docs/html/*'))
    ]

def get_py_modules():
    return [i.replace(".py","") for i in glob("devede_*.py")]

setup(
    name = 'devede',
    version = '3.21.0',
    author = "Sergio Costas",
    author_email = "raster@rastersoft.com",
    url = "http://www.rastersoft.com/programas/devede.html",
    license = 'GPL-3',
    py_modules = get_py_modules(),
    scripts=['devede.py'],
    data_files = get_data_files()
)
