# -*- coding: utf-8 -*-
from decouple import config
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


AWS_ACCESS_KEY_ID = config('AWS_KEY', '')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET', '')
AWS_STORAGE_BUCKET_NAME = config('BUCKET_NAME', '')
AWS_SEARCH_DIR = config('AWS_DIR', '')
FILE_PATH = os.path.join(BASE_DIR, config('PROCESSOS_FILE', 'processos.txt'))
DOWNLOAD_PATH = config('DOWNLOAD_PATH', '')
