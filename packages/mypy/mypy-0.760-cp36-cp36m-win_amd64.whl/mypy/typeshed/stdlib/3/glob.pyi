# Stubs for glob
# Based on http://docs.python.org/3/library/glob.html

from typing import List, Iterator, AnyStr, Union
import sys

if sys.version_info >= (3, 6):
    def glob0(dirname: AnyStr, pattern: AnyStr) -> List[AnyStr]: ...
else:
    def glob0(dirname: AnyStr, basename: AnyStr) -> List[AnyStr]: ...

def glob1(dirname: AnyStr, pattern: AnyStr) -> List[AnyStr]: ...

def glob(pathname: AnyStr, *, recursive: bool = ...) -> List[AnyStr]: ...
def iglob(pathname: AnyStr, *, recursive: bool = ...) -> Iterator[AnyStr]: ...

def escape(pathname: AnyStr) -> AnyStr: ...

def has_magic(s: Union[str, bytes]) -> bool: ...  # undocumented
