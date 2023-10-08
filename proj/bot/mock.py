from __future__ import annotations

import collections
import itertools
import logging
import unittest.mock
from asyncio import AbstractEventLoop
from typing import Iterable, Optional

import discord
from aiohttp import ClientSession
from discord.ext.commands import Context
from pydis_core.async_stats import AsyncStatsClient
from pydis_core.site_api import APIClient
from botrun import bot

class MockBot(CustomMockMixin, unittest.mock.MagicMock):
    """
    A MagicMock subclass to mock Bot objects.
    Instances of this class will follow the specifications of `discord.ext.commands.Bot` instances.
    For more information, see the `MockGuild` docstring.
    """
    spec_set = bot(
        command_prefix=unittest.mock.MagicMock(),
        redis_session=unittest.mock.MagicMock(),
        http_session=unittest.mock.MagicMock(),
        allowed_roles=[1],
        guild_id=1,
        intents=discord.Intents.all(),
    )
    additional_spec_asyncs = ("wait_for",)

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.http_session = unittest.mock.create_autospec(spec=ClientSession, spec_set=True)
        self.stats = unittest.mock.create_autospec(spec=AsyncStatsClient, spec_set=True)
        self.add_cog = unittest.mock.AsyncMock()
#макет сообщения и контекста
message_data = {
    'id': 1,
    'webhook_id': 431341013479718912,
    'attachments': [],
    'embeds': [],
    'application': {"id": 4, "description": "A Python Bot", "name": "Python Discord", "icon": None},
    'activity': 'mocking',
    'channel': unittest.mock.MagicMock(),
    'edited_timestamp': '2019-10-14T15:33:48+00:00',
    'type': 'message',
    'pinned': False,
    'mention_everyone': False,
    'tts': None,
    'content': 'content',
    'nonce': None,
}
state = unittest.mock.MagicMock()
channel = unittest.mock.MagicMock()
channel.type = discord.ChannelType.text
message_instance = discord.Message(state=state, channel=channel, data=message_data)

# Create a Context instance to get a realistic MagicMock of `discord.ext.commands.Context`
context_instance = Context(
    message=unittest.mock.MagicMock(),
    prefix="!",
    bot=MockBot(),
    view=None
)
context_instance.invoked_from_error_handler = None
