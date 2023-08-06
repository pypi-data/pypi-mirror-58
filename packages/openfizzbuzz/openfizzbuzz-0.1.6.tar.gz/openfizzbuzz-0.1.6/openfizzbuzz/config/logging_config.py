LOGCONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'default': {
            'format': '%(asctime)s :: %(levelname)s :: %(name)s :: %(message)s'
        }
    },

    'handlers': {
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },

    'loggers': {
        'main': {
            'handlers': ['stream_handler'],
            'level': 'WARN'
        },
        'settings': {
            'handlers': ['stream_handler'],
            'level': 'WARN'
        },
        'fizzbuzz': {
            'handlers': ['stream_handler'],
            'level': 'WARN'
        },
        'letter': {
            'handlers': ['stream_handler'],
            'level': 'WARN'
        },
        'word': {
            'handlers': ['stream_handler'],
            'level': 'WARN'
        }

    }
}
