from typing import Optional

from pydantic import BaseModel


class Student(BaseModel):
    age: Optional[str] = None
    aim: Optional[str] = None
    tutor: Optional[str] = None
