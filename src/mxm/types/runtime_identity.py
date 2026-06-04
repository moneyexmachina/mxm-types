from dataclasses import dataclass
from typing import NewType

AppId = NewType("AppId", str)
Environment = NewType("Environment", str)
MachineId = NewType("MachineId", str)
RuntimeSubstrate = NewType("RuntimeSubstrate", str)
RuntimeRole = NewType("RuntimeRole", str)


@dataclass(frozen=True, slots=True)
class RuntimeIdentity:
    app: AppId
    environment: Environment
    machine: MachineId
    substrate: RuntimeSubstrate
    role: RuntimeRole
