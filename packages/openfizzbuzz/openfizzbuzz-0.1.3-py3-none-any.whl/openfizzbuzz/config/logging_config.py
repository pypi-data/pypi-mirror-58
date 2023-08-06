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
            'handlers': ['file_handler', 'stream_handler'],
            'level': 'WARN'
        },
        'settings': {
            'handlers': ['file_handler', 'stream_handler'],
            'level': 'WARN'
        },
        'fizzbuzz': {
            'handlers': ['file_handler', 'stream_handler'],
            'level': 'WARN'
        },
        'letter': {
            'handlers': ['file_handler', 'stream_handler'],
            'level': 'WARN'
        },
        'word': {
            'handlers': ['file_handler', 'stream_handler'],
            'level': 'WARN'
        }

    }
}
