import asyncio
import inspect

specials = ["setUp", "tearDown"]


def run_corm(self, corm, loop):
    _corm = corm(self)
    is_coroutine = inspect.iscoroutinefunction(corm)
    return loop.run_until_complete(_corm) if is_coroutine else _corm


def wrap_corms(corm, loop):
    def inner(self):

        # currently, we're breaking causality:
        # we need the setUp to run before
        # and guarentee that tearDown is run at the end
        # however, we can't actually run the loop
        # until this method is called, so
        # we'll have to do some additional schenanigans

        return run_corm(self, corm, loop)

    return inner


def wrap_specials(name, corm, loop, previous_loop):
    def inner(self):
        if name == "setUp":
            # setup the loop
            asyncio.set_event_loop(loop)
            return run_corm(self, corm, loop)

        if name == "tearDown":
            # switch out the new loop for the previous one
            result = run_corm(self, corm, loop)
            asyncio.set_event_loop(previous_loop)
            return result

    return inner


def is_a_coro_test(name, coro):
    is_test = name.startswith("test")
    is_coro = inspect.iscoroutinefunction(coro)
    return is_coro and is_test


def asyncnostic(klass):
    # the difference between v1 and v2 of asyncnostic
    # is that v2 will automatically create the loop context
    # and maintain it for every test that is a coroutine
    # and disable it for every normal test.
    # that way, we do not have to explicitly pass the loop
    # variable into the method signature

    previous_loop = asyncio.get_event_loop()

    loop = asyncio.new_event_loop()
    klass_methods_and_coroutines = klass.__dict__

    # copy over all test async methods
    # leave the ones that do not start with test
    # because they are supporting methods

    coroutines = {
        name: coro
        for name, coro in klass_methods_and_coroutines.items()
        if is_a_coro_test(name, coro)
    }

    for name, coro in coroutines.items():

        # transform the coroutine into a method
        # provide the loop if necessary
        # the name cannot change because we want to override the earlier method
        method = wrap_corms(coro, loop)
        setattr(klass, name, method)

    # copy over the setup and teardown
    special_methods = {
        name: method
        for name, method in klass_methods_and_coroutines.items()
        if name in specials
    }

    for name, method in special_methods.items():

        # does not transform, since these are already methods
        # provides loop if necessary
        method = wrap_specials(name, method, loop, previous_loop)
        setattr(klass, name, method)

    return klass


def v2(klass):
    return asyncnostic(klass)
