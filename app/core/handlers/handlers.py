import abc
from typing import Optional

from aiogram import types as tg_types
from aiogram.dispatcher import FSMContext

from app.core.extensions import InlineStack
from app.utils import Singleton


class Handler(Singleton):
    def __init__(self):
        from_user: Optional[tg_types.User]


class MessageHandler(Handler, abc.ABC):
    async def __call__(self, message: tg_types.Message, state: FSMContext, *args, **kwargs):
        await InlineStack.delete_all(message.from_user.id)
        self.from_user = message.from_user
        self.state = await state.get_state()
        await self.handle(message, *args, **kwargs)

    @abc.abstractmethod
    async def handle(self, message: tg_types.Message, *args, **kwargs):
        pass


class CallbackQueryHandler(Handler, abc.ABC):
    async def __call__(self, callback_query: tg_types.CallbackQuery, *args, **kwargs):
        self.from_user = callback_query.from_user
        self.callback_data = kwargs['callback_data']
        await self.handle(callback_query, *args, **kwargs)

    @abc.abstractmethod
    async def handle(self, callback_query: tg_types.CallbackQuery, *args, **kwargs):
        pass