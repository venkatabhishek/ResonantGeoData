import os

from celery import Celery
import configurations.importer

os.environ['DJANGO_SETTINGS_MODULE'] = 'rgd.settings'
if not os.environ.get('DJANGO_CONFIGURATION'):
    raise ValueError('The environment variable "DJANGO_CONFIGURATION" must be set.')
configurations.importer.install()

# Using a string config_source means the worker doesn't have to serialize
# the configuration object to child processes.
app = Celery('rgd', config_source='django.conf:settings', namespace='CELERY')
app.conf.task_default_queue = 'default'

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
