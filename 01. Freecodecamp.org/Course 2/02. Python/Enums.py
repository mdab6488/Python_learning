from enum import Enum


class State(Enum):
    """
    Enum class to represent the state of a process.
    """

    INACTIVE = 0
    ACTIVE = 1


print(State.INACTIVE)  # State.INACTIVE
print(State.ACTIVE)  # State.ACTIVE

print(State.INACTIVE.name)  # INACTIVE
print(State.ACTIVE.name)  # ACTIVE

print(State.INACTIVE.value)  # 0
print(State.ACTIVE.value)  # 1

print(State(1))  # State.ACTIVE
print(State["ACTIVE"])  # State.ACTIVE
print(State["ACTIVE"].value)  # 1

print(list(State))  # [<State.INACTIVE: 0>, <State.ACTIVE: 1>]
