#BROKER_URL = 'amqp://guest:guest@localhost:5672//'

#CELERY_ALWAYS_EAGER = True

CELERY_RESULT_BACKEND = 'amqp'
CELERY_RESULT_PERSISTENT = False
CELERY_TASK_RESULT_EXPIRES = 10
CELERY_DISABLE_RATE_LIMITS = True
CELERY_SEND_TASK_ERROR_EMAILS = True

CELERY_ACKS_LATE = True
CELERYD_PREFETCH_MULTIPLIER = 1  # limit number of tasks a worker can reserve
CELERY_IGNORE_RESULT = True  # results wastes time and resources
CELERY_DEFAULT_QUEUE = 'default'
CELERY_QUEUES = {
    'default': {
        'binding_key': 'task.#',
    },
    'upload_responses': {
        'binding_key': 'upload_responses.#',
    },
    'classify_excel': {
        'binding_key': 'classify_excel.#',
    },
    'message_export': {
        'binding_key': 'message_export.#',
    },
    'start_poll': {
        'binding_key': 'start_poll.#',
    },
    'process_message': {
        'binding_key': 'process_message.#',
    },
    'handle_incoming': {
        'binding_key': 'handle_incoming.#',
    },
    'reprocess_responses': {
        'binding_key': 'reprocess_responses.#',
    },
    'push_to_mtrac': {
        'binding_key': 'push_to_mtrac.#'
    },
    'process_uploaded_contacts': {
        'binding_key': 'process_uploaded_contacts.#'
    },
    'process_assign_group': {
        'binding_key': 'process_assign_group.#'
    },
    'export_poll': {
        'binding_key': 'export_poll.#'
    },
    'extract_gen_reports': {
        'binding_key': 'extract_gen_reports.#'
    }
}
CELERY_DEFAULT_EXCHANGE = 'tasks'
CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'
CELERY_DEFAULT_ROUTING_KEY = 'task.default'
#CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"

BROKER_HOST = "127.0.0.1"
BROKER_PORT = 5672
BROKER_USER = "ureport"
BROKER_PASSWORD = "ureport"
BROKER_VHOST = "ureport"

CELERY_ROUTES = {
    'message_classifier.tasks.upload_responses': {
        'queue': 'upload_responses',
        'routing_key': 'upload_responses.result'
    },
    'message_classifier.tasks.classify_excel': {
        'queue': 'classify_excel',
        'routing_key': 'classify_excel.result'
    },
    'message_classifier.tasks.message_export': {
        'queue': 'message_export',
        'routing_key': 'message_export.result'
    },
    'ureport.tasks.start_poll': {
        'queue': 'start_poll',
        'routing_key': 'start_poll.result'
    },
    'ureport.tasks.process_message': {
        'queue': 'process_message',
        'routing_key': 'process_message.result'
    },
    'rapidsms_httprouter.tasks.handle_incoming': {
        'queue': 'handle_incoming',
        'routing_key': 'handle_incoming.result'
    },
    'ureport.tasks.reprocess_responses': {
        'queue': 'reprocess_responses',
        'routing_key': 'reprocess_responses.result'
    },
    'ureport.tasks.push_to_mtrac': {
        'queue': 'push_to_mtrac',
        'routing_key': 'push_to_mtrac.result'
    },
    'ureport.tasks.process_uploaded_contacts': {
        'queue': 'process_uploaded_contacts',
        'routing_key': 'process_uploaded_contacts.result'
    },
    'ureport.tasks.process_assign_group': {
        'queue': 'process_assign_group',
        'routing_key': 'process_assign_group.result'
    },
    'ureport.tasks.export_poll': {
        'queue': 'export_poll',
        'routing_key': 'export_poll.result'
    },
    'ureport.tasks.extract_gen_reports': {
        'queue': 'extract_gen_reports',
        'routing_key': 'extract_gen_reports.result'
    }

}

SERVER_EMAIL = 'Ureport Background Tasks<background@ureport.ug>'

ADMINS = (
    ('Kenneth Matovu', 'kbonky@gmail.com'),
    ('Arga', 'arghacha@thoughtworks.com'),
)

CELERY_IMPORTS = (
    'ureport.tasks',
    'message_classifier.tasks',
    'rapidsms_httprouter.tasks'
)
