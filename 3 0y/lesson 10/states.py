from aiogram.dispatcher.filters.state import StatesGroup, State


class RegistState(StatesGroup):
    full_name = State()
    phone_number = State()
    age = State()
    what_you_want = State()
    free_days = State()
    study = State()
