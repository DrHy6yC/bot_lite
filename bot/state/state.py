from aiogram.fsm.state import StatesGroup, State


class LidFSM(StatesGroup):
    age = State()
    aim = State()
    tutor = State()
    end = State()
