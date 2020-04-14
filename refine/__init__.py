import inspect


def lazy_run(fn, conds, *args, **kwargs):
    """Run a function only if any
    of the specified conditions return True"""
    name = f'{fn.__module__}#{fn.__name__}'
    if all(c() for c in conds):
        print('Running', name)
        fn(*args, **kwargs)
    else:
        print('Skipping', name)


def pipeline(segments):
    for fn, conds in segments:
        if inspect.ismodule(fn):
            # Look for function named "process"
            fn = getattr(fn, 'process')
        lazy_run(fn, conds)