import os
import sys

from __version__ import __title__


main_dir = os.environ.get('USERPROFILE')
fallback_dir = os.path.join(os.path.dirname(sys.argv[0]), 'bot')

if not main_dir:
    os.mkdir(fallback_dir)

ROOT_DIR = os.path.join(
    main_dir or fallback_dir,
    f'.{__title__}',
)

# create root directory if it doesn't already exists
if not os.path.exists(ROOT_DIR):
    os.mkdir(ROOT_DIR)

DB_DIR = os.path.join(ROOT_DIR, 'database')

# create database directory if it doesn't already exists
if not os.path.exists(DB_DIR):
    os.mkdir(DB_DIR)

DB_PATH = os.path.join(DB_DIR, f'{__title__}.db')
