import functools

_SCENARIO = []


def get_scenarios():
    return _SCENARIO


def scenario(weight):
    def _scenario(func, *args, **kw):
        _SCENARIO.append((weight, func, args, kw))

        @functools.wraps(func)
        def __scenario():
            return func(*args, **kw)
        return __scenario

    return _scenario


_SETUP = []


def get_setup():
    if len(_SETUP) == 0:
        return None
    return _SETUP[0]


def setup():
    def _setup(func, *args, **kw):
        if len(_SETUP) > 0:
            raise ValueError("You can't have two setup functions")

        _SETUP.append(func)

        @functools.wraps(func)
        def __setup():
            return func(*args, **kw)
        return __setup

    return _setup
