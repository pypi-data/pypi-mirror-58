from typing import Any, Optional

class HashAlgo:
    digest_size: Any
    block_size: Any
    def __init__(self, hashFactory, data: Optional[Any] = ...) -> None: ...
    def update(self, data): ...
    def digest(self): ...
    def hexdigest(self): ...
    def copy(self): ...
    def new(self, data: Optional[Any] = ...): ...
