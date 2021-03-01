import os
import sys
from pathlib import Path

from __version__ import __title__


default_dir = os.environ.get('USERPROFILE')
fallback_dir = os.path.join(os.path.dirname(sys.argv[0]), 'bot')

# define project base directory for logging and database querying
ROOT_DIR = Path(os.path.join(default_dir or fallback_dir, f'.{__title__}'))

DB_DIR = Path(os.path.join(ROOT_DIR, 'database'))
# define and create database directory
DB_DIR.mkdir(exist_ok=True, parents=True)

DB_PATH = os.path.join(DB_DIR, f'{__title__}.db')
