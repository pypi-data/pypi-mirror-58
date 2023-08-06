import sys

# Select GUI toolkit
for libname in ("PySide2", "PyQt5"):
    if libname in sys.modules:
        QWidget = sys.modules[libname].QtWidgets.QWidget
        break
else:
    raise ImportError("Need to import PySide2.QtWidgets or PyQt5.QtWidgets first.")


class BaseCanvas:
    """ Represents the root rectangular region to draw to.
    """

    _swapchain = None

    # todo: use camelCase instead

    def wgpu_get_size(self):
        raise NotImplementedError()

    def wgpu_get_pixel_ratio(self):
        raise NotImplementedError()

    def wgpu_get_window_id(self):
        raise NotImplementedError()

    def configureSwapChain(self, device, format, usage):
        self._swapchain = device._gui_configureSwapChain(self, format, usage)  # noqa
        return self._swapchain

    def drawFrame(self):
        return


class QGpuWidget(BaseCanvas, QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._err_hashes = {}

        WA_PaintOnScreen = 8  # QtCore.Qt.WA_PaintOnScreen
        self.setAttribute(WA_PaintOnScreen, True)
        self.setAutoFillBackground(False)

    def paintEngine(self):
        # https://doc.qt.io/qt-5/qt.html#WidgetAttribute-enum  WA_PaintOnScreen
        return None

    def paintEvent(self, event):
        try:
            self.drawFrame()
            if self._swapchain is not None:
                self._swapchain._gui_present()  # noqa - a.k.a swap buffers
        except Exception:
            # Enable PM debuging
            sys.last_type, sys.last_value, sys.last_traceback = sys.exc_info()
            msg = str(sys.last_value)
            msgh = hash(msg)
            if msgh in self._err_hashes:
                count = self._err_hashes[msgh] + 1
                self._err_hashes[msgh] = count
                shortmsg = msg.split("\n", 1)[0].strip()[:50]
                sys.stderr.write(f"Error in draw again ({count}): {shortmsg}\n")
            else:
                self._err_hashes[msgh] = 1
                sys.stderr.write(f"Error in draw: " + msg.strip() + "\n")
                traceback.print_last(6)

    def wgpu_get_size(self):
        return self.width(), self.height()

    def wgpu_get_pixel_ratio(self):
        raise NotImplementedError()

    def wgpu_get_window_id(self):
        return self.winId()
