import unittest
import unittest.mock
import botrun
import discord          
from discord.ext import commands

import collections
import itertools
import logging
import unittest
import unittest.mock
from asyncio import AbstractEventLoop
from typing import Iterable, Optional

import discord
from aiohttp import ClientSession
from discord.ext.commands import Context
from pydis_core.async_stats import AsyncStatsClient
from pydis_core.site_api import APIClient
from botrun import bot

class test_bot_unit(unittest.TestCase):
    
    def test_ping(self):
        msg = context_instance
        self.assertEqual(botrun.ping(msg), 'pong...')

if __name__ == '__main__':
    unittest.__main__


# Create a Context instance to get a realistic MagicMock of `discord.ext.commands.Context`
context_instance = Context(
    message='ping',
    view=None
)
context_instance.invoked_from_error_handler = None
