#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Shrimadhav U K
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from telegram import (
    Update
)
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
from bot import Config, INPUT_PHONE_NUMBER


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ ConversationHandler entry_point /start """
    await update.message.reply_text(
        Config.START_TEXT,
        parse_mode="html"
    )
    return INPUT_PHONE_NUMBER
