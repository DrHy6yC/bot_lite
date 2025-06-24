from aiogram.fsm.state import StatesGroup, State


class LidFSM(StatesGroup):
    start = State()
    age = State()
    aim = State()
    tutor = State()
    end = State()
