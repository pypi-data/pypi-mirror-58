#!/usr/bin/env python

import asyncio
import code

from qtoggleserver import commands


def execute():
    import qtoggleserver  # required for locals()

    loop = asyncio.get_event_loop()

    loop.run_until_complete(commands.init())

    commands.logger.info('starting interactive shell')
    code.interact(local=locals())

    loop.run_until_complete(commands.done())
    loop.run_until_complete(loop.shutdown_asyncgens())

    commands.logger.info('bye!')


if __name__ == '__main__':
    execute()
