from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RuntimeIdentity:
    app: str
    environment: str
    machine: str
    substrate: str
    role: str
