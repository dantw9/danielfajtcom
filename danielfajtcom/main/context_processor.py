import env


def current_env(request):
    return {
        'current_env': env.ENV
    }


def tailwind_file(request):
    return {
        'tailwind_file': env.TAILWIND_FILE
    }
