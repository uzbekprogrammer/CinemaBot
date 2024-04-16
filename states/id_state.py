from aiogram.dispatcher.filters.state import StatesGroup, State


class MediaId(StatesGroup):
    video = State()
    order = State()
