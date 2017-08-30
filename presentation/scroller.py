import scrollphathd
import time
from scrollphathd.fonts import font5x7

from presentation import clock_font
from presentation.scroller_presenter import ScrollerPresenter


class Scroller(object):
    _BRIGHTNESS = 0.12
    _SCROLL_WAIT = 0.02
    _PAUSE_AFTER_SCROLL = 1.0
    _SCROLL_OFFSET = 17
    _SCREEN_ROTATION = 180
    _CLOCK_DURATION_SECONDS = 10

    def __init__(self):
        scrollphathd.rotate(degrees=self._SCREEN_ROTATION)
        presenter = ScrollerPresenter(self)
        presenter.initialize()

    def show_clock(self):
        self._clear_screen()
        for i in range(0, self._CLOCK_DURATION_SECONDS):
            scrollphathd.clear()
            self._show_time()
            self._blink_clock_points()
            scrollphathd.show()
            time.sleep(1)

    def _show_time(self):
        formatted_time = time.strftime("%H:%M")
        scrollphathd.write_string(formatted_time, font=clock_font, brightness=self._BRIGHTNESS)

    def _blink_clock_points(self):
        if int(time.time()) % 2 == 0:
            scrollphathd.clear_rect(8, 0, 1, 7)

    def show_text(self, text):
        self._clear_screen()
        length = scrollphathd.write_string(" %s " % text, font=font5x7, brightness=self._BRIGHTNESS)
        for i in range(0, length - self._SCROLL_OFFSET):
            self._scroll()
        self._clear_screen()

    def _scroll(self):
        scrollphathd.show()
        scrollphathd.scroll()
        time.sleep(self._SCROLL_WAIT)

    def _clear_screen(self):
        scrollphathd.clear()
        scrollphathd.show()
