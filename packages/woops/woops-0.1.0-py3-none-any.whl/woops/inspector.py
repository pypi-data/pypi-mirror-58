from typing import List
from typing import Optional

from .frame import Frame


class Inspector:
    def __init__(self, exception: Exception):
        self._exception = exception
        self._frames = None
        self._previous_exception = exception.__context__

    @property
    def exception(self) -> Exception:
        return self._exception

    @property
    def exception_name(self) -> str:
        return self._exception.__class__.__name__

    @property
    def exception_message(self) -> str:
        return str(self._exception)

    @property
    def frames(self) -> List[Frame]:
        if self._frames is not None:
            return self._frames

        frames = []
        tb = self._exception.__traceback__
        while tb:
            frames.append(Frame(tb))

            tb = tb.tb_next

        self._frames = frames

        return self._frames

    @property
    def previous_exception(self) -> Optional[Exception]:
        return self._previous_exception

    def has_previous_exception(self) -> bool:
        return self._previous_exception is not None
