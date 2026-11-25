from typing import Dict, Optional
from maxapi.filters import F
from maxapi.utils.inline_keyboard import InlineKeyboardBuilder
from maxapi.types.attachments.buttons import CallbackButton
from utils import GROUP_CHAT_TEST_ID, GROUP_CHAT_WORK_ID, bot, logger, file_path_report, file_path_month
from maxapi import Dispatcher, types
from maxapi.types import Command, BotStarted, MessageCreated, MessageCallback
import io
import logging
from maxapi.context import MemoryContext, StatesGroup, State
import aiohttp

dp = Dispatcher()