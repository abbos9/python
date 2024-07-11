from aiogram.dispatcher.filters.state import StatesGroup, State


class SendMessage(StatesGroup):
    letter = State()
    letter2 = State()
    counter = State()




