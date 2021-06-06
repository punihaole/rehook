from .settings import *


DEBUG = False
ALLOWED_HOSTS = [
    'localhost',
    'dev-webhooks.rocketreach.co',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'www', 'static')
