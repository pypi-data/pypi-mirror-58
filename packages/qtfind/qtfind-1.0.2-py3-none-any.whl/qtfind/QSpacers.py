from PyQt5.QtWidgets import QSpacerItem, QSizePolicy


class QHSpacerItem(QSpacerItem):
    def __init__(self, width=0, height=0):
        super(QHSpacerItem, self).__init__(width, height, QSizePolicy.Expanding, QSizePolicy.Minimum)


class QVSpacerItem(QSpacerItem):
    def __init__(self, width=0, height=0):
        super(QVSpacerItem, self).__init__(width, height, QSizePolicy.Minimum, QSizePolicy.Expanding)
