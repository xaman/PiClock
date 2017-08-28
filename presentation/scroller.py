import scrollphathd
import time
from scrollphathd.fonts import font5x7

from presentation.scroller_presenter import ScrollerPresenter


class Scroller(object):
    _SCROLL_WAIT = 0.02
    _PAUSE_AFTER_SCROLL = 1.0
    _SCROLL_OFFSET = 17
    _SCREEN_ROTATION = 180

    def __init__(self):
        self._initialize_scroller()
        scrollphathd.rotate(degrees=self._SCREEN_ROTATION)

    def _initialize_scroller(self):
        presenter = ScrollerPresenter(self)
        presenter.initialize()

    def show_text(self, text):
        length = scrollphathd.write_string(" %s " % text, font=font5x7, brightness=0.2)
        for i in range(0, length - self._SCROLL_OFFSET):
            self._scroll()
        self._clear_screen()
        time.sleep(self._PAUSE_AFTER_SCROLL)

    def _scroll(self):
        scrollphathd.show()
        scrollphathd.scroll()
        time.sleep(self._SCROLL_WAIT)

    def _clear_screen(self):
        scrollphathd.clear()
        scrollphathd.show()
