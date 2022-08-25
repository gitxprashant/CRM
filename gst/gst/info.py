import os

EMAIL_USE_TLS= True
EMAIL_HOST= 'smtp-mail.outlook.com'
EMAIL_HOST_USER= 'fintax.gsc@outlook.com'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASS']
EMAIL_PORT=587