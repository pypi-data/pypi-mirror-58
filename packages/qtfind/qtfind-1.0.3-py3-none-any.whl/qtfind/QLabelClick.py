from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QLabel
import enum


class Trigger(enum.Enum):
    PRESS = 0
    RELEASE = 1
    DOUBLE = 2
    MOVE = 3


class QLabelClick(QLabel):
    """QLabel class supporting mouse clicks"""
    mouse_pressed = pyqtSignal()  # clicked
    mouse_double_pressed = pyqtSignal()  # double_clicked
    mouse_released = pyqtSignal()
    mouse_moved = pyqtSignal()

    def __init__(self, text: str, trigger: Trigger = Trigger.PRESS, button=Qt.AllButtons, parent=None):
        QLabel.__init__(self, text, parent)
        self.button = button
        self.trigger = trigger

    def mouseDoubleClickEvent(self, mouse_event):
        if self.trigger != Trigger.DOUBLE:
            return

        if self.button in (mouse_event.button(), Qt.AllButtons):
            self.mouse_double_pressed.emit()

    def mousePressEvent(self, mouse_event):
        print(self.button)
        print(self.trigger)
        if self.trigger != Trigger.PRESS:
            return

        if self.button in (mouse_event.button(), Qt.AllButtons):
            self.mouse_pressed.emit()

    def mouseReleaseEvent(self, mouse_event):
        if self.trigger != Trigger.RELEASE:
            return

        if self.button in (mouse_event.button(), Qt.AllButtons):
            self.mouse_released.emit()

    def mouseMoveEvent(self, mouse_event):
        if self.trigger != Trigger.MOVE:
            return

        if self.button in (mouse_event.button(), Qt.AllButtons):
            self.mouse_moved.emit()
