from aiogram.dispatcher.filters.state import StatesGroup, State


class RegistState(StatesGroup):
    full_name = State()
    phone_number = State()
    age = State()
    jins = State()
    birth_day = State()
    address = State()
    who_is_people = State()
    metrics = State()
    long = State()
    weight = State()


class CourseState(StatesGroup):
    full_name = State()
    phone_number = State()
    age = State()
    free_time = State()
    reason_study = State()
    branch = State()
