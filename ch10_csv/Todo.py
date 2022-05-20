
from dataclasses import dataclass


@dataclass
class Todo:
    userId:int
    title:str
    completed:bool
    id:int=0
