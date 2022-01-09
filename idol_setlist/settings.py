import os

env = os.getenv("ENV")

if env == "production":
    from .settings_production import *
else:
    from .settings_local import *