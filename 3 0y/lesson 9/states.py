from aiogram.dispatcher.filters.state import StatesGroup, State


class CalculatorState(StatesGroup):
    num1 = State()
    num2 = State()
    sign = State()