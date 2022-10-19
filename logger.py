
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'detailed': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(processName)s - %(message)s',  # noqa
            'datefmt': '%y-%m-%d %H:%M:%S',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'detailed',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'bot.log',
            'mode': 'w',
            'formatter': 'detailed',
        },
        'errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'bot_error.log',
            'mode': 'w',
            'formatter': 'detailed',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file', 'errors'],
            'level': 'DEBUG'
        }
    },
    'root': {
        'level': 'DEBUG',
        'formatter': 'detailed',
        'handlers': ['console', 'file', 'errors']
    },
}
