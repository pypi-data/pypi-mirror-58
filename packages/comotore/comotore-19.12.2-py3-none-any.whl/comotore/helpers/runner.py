"""
    Runner helper
"""

import asyncio
import signal
import functools
import platform


def run(coro):
    loop = asyncio.get_event_loop()

    main_future = asyncio.ensure_future(coro, loop=loop)

    def signal_interrupt():
        main_future.cancel()

    def signal_interrupt_for_win(_):
        main_future.cancel()

    async def shutdown(loop_):
        pending_tasks = [
            t for t in asyncio.Task.all_tasks(loop=loop_) if not t.done() and t is not asyncio.current_task(loop_)
        ]
        list(map(lambda t: t.cancel(), pending_tasks))
        await asyncio.gather(*pending_tasks, loop=loop_, return_exceptions=True)
        loop_.stop()

    try:
        for sig in [signal.SIGINT, signal.SIGTERM]:
            loop.add_signal_handler(sig, functools.partial(signal_interrupt))
    except NotImplementedError:
        # if platform.system() == "Windows":
        #     import win32api
        #     win32api.SetConsoleCtrlHandler(signal_interrupt_for_win, True)

        async def periodic_sleep():
            try:
                while True:
                    await asyncio.sleep(1)
            except KeyboardInterrupt:
                main_future.cancel()
            except asyncio.CancelledError:
                pass
        asyncio.ensure_future(periodic_sleep(), loop=loop)

    try:
        loop.run_until_complete(main_future)
    except KeyboardInterrupt:
        print("Interrupted")
        main_future.cancel()
    finally:
        loop.run_until_complete(shutdown(loop))
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
