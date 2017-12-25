import time

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

from presentation.base.scroller import Scroller
from presentation.max7219.max7219_formatter_factory import Max7219FormatterFactory
from presentation.scroller_presenter import ScrollerPresenter


class Max7219Scroller(Scroller):
    _CONTRAST = 10
    _CLOCK_DURATION_SECONDS = 5

    _device = None

    def __init__(self):
        serial = spi(port=0, device=0, gpio=noop())
        self._device = max7219(serial, cascaded=4, block_orientation=-90, rotate=2)
        self._device.contrast(self._CONTRAST)
        presenter = ScrollerPresenter(self, Max7219FormatterFactory())
        presenter.initialize()

    def show_clock(self):
        for i in range(0, self._CLOCK_DURATION_SECONDS):
            self._show_time()
            time.sleep(1)

    def _show_time(self):
        time_format = "%H:%M" if int(time.time()) % 2 == 0 else "%H %M"
        formatted_time = time.strftime(time_format)
        virtual = viewport(self._device, width=32, height=8)
        with canvas(virtual) as draw:
            draw.text((1, -2), formatted_time, fill="white")

    def show_text(self, text):
        show_message(self._device, text, fill="white", font=proportional(CP437_FONT))
