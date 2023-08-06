LOGCONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'default': {
            'format': '%(asctime)s :: %(levelname)s :: %(name)s :: %(message)s'
        }
    },

    'handlers': {
        'file_handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'filename': 'openfizzbuzz/logs/openfizzbuzz.log',
            'maxBytes': 1000000
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },

    'loggers': {
        'main': {
            'handlers': ['file_handler', 'stream_handler'],
            'level': 'DEBUG'
        },
        'settings': {
            'handlers': ['file_handler', 'stream_handler'],
            'level': 'DEBUG'
        },
        'fizzbuzz': {
            'handlers': ['file_handler', 'stream_handler'],
            'level': 'DEBUG'
        },
        'letter': {
            'handlers': ['file_handler', 'stream_handler'],
            'level': 'DEBUG'
        },
        'word': {
            'handlers': ['file_handler', 'stream_handler'],
            'level': 'DEBUG'
        }

    }
}
