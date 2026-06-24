# This file will tell other files what my models are supposed to look like.

from pydantic import BaseModel

class ShiftInput(BaseModel): 
    shift_start: str
    shift_end: str
    context: str
    tasks: list[str]