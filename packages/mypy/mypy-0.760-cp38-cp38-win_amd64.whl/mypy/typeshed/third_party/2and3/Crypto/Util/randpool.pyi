from typing import Any, Optional

__revision__: str

class RandomPool:
    bytes: Any
    bits: Any
    entropy: Any
    def __init__(self, numbytes: int = ..., cipher: Optional[Any] = ..., hash: Optional[Any] = ..., file: Optional[Any] = ...) -> None: ...
    def get_bytes(self, N): ...
    def randomize(self, N: int = ...): ...
    def stir(self, s: str = ...): ...
    def stir_n(self, N: int = ...): ...
    def add_event(self, s: str = ...): ...
    def getBytes(self, N): ...
    def addEvent(self, event, s: str = ...): ...
