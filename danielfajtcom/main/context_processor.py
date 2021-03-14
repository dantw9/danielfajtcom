import env


def current_env(request):
    return {
        'current_env': env.ENV
    }
