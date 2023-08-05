import inspect

from types import TracebackType


class Frame:
    def __init__(self, frame: TracebackType) -> None:
        self._frame = frame
        self._frame_info = inspect.getframeinfo(frame)
        self._lines = None
        self._file_content = None

    @property
    def frame(self) -> TracebackType:
        return self._frame

    @property
    def lineno(self) -> int:
        return self._frame_info.lineno

    @property
    def filename(self) -> str:
        return self._frame_info.filename

    @property
    def function(self) -> str:
        return self._frame_info.function

    @property
    def line(self) -> str:
        return self._frame_info.code_context[0]

    @property
    def file_content(self) -> str:
        if self._file_content is None:
            filename = inspect.getsourcefile(self._frame) or inspect._getfile(
                self._frame
            )

            if not filename:
                self._file_content = ""
            else:
                try:
                    with open(filename) as f:
                        self._file_content = f.read()
                except OSError:
                    self._file_content = ""

        return self._file_content
