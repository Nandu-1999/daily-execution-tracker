from enum import Enum


class ActivityCategory(str, Enum):
    UPSKILLING = "UPSKILLING"
    WORK = "WORK"
    EXERCISE = "EXERCISE"
    RESEARCH = "RESEARCH"
    PERSONAL = "PERSONAL"