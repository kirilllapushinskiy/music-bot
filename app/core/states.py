from aiogram.dispatcher.filters.state import StatesGroup, State


class States(StatesGroup):
    searching = State()
    setting_link = State()
    checking_audios = State()
