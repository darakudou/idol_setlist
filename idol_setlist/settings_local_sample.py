from .settings_base import *

DEBUG = True

SECRET_KEY = ""

"""
セキュリティキーの生成方法
from django.core.management.utils import get_random_secret_key

secret_key = get_random_secret_key()
これで作ったキーを各自のlocalにセットする
"""