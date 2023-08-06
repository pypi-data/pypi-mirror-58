from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import *

from qtfind.QCommon import set_bold


class QAbout(QDialog):
    def __init__(self, parent, app_icon):
        super().__init__(parent)
        self.app_icon = app_icon

        self.lbl_name = QLabel('QtFind v1.0.3')
        self.lbl_description = QLabel('Graphical interface for the powerful command find')
        self.lbl_link = QLabel('<a href="https://github.com/amad3v/QtFind">GitHub.com</a>')
        self.lbl_copyright = QLabel('\nCopyright \xa9 2019 - amad3v\n')
        self.lbl_warning = QLabel('This program comes with absolutely no warranty.')
        self.license_link = 'https://www.gnu.org/licenses/gpl-3.0.html'
        self.license_text = f'See the <a href="{self.license_link}">GNU General Public License</a>' \
                            ' version 3 or later for details.'

        self.small_print = QFont()
        self.small_print.setPointSize(8)

        self.setWindowTitle('About QtFind')
        self.__init_ui(self.app_icon)

    def __init_ui(self, app_icon):
        # create picture container
        self.lbl_container = QLabel(self)
        self.lbl_container.setPixmap(QPixmap(app_icon))
        self.lbl_container.setAlignment(Qt.AlignCenter)

        # app label
        self.lbl_name.setFont(set_bold(True))
        self.lbl_name.setAlignment(Qt.AlignCenter)

        # app description
        self.lbl_description.setAlignment(Qt.AlignCenter)

        # app link
        self.lbl_link.setOpenExternalLinks(True)
        self.lbl_link.setAlignment(Qt.AlignCenter)

        # copyright
        self.lbl_copyright.setAlignment(Qt.AlignCenter)
        self.lbl_copyright.setFont(self.small_print)

        # warning
        self.lbl_warning.setAlignment(Qt.AlignCenter)
        self.lbl_warning.setFont(self.small_print)

        # license
        self.lbl_license = QLabel(self.license_text)
        self.lbl_license.setOpenExternalLinks(True)
        self.lbl_license.setAlignment(Qt.AlignCenter)
        self.lbl_license.setFont(self.small_print)

        # global layout
        self.global_layout = QVBoxLayout()
        self.global_layout.addWidget(self.lbl_container)
        self.global_layout.addWidget(self.lbl_name)
        self.global_layout.addWidget(self.lbl_description)
        self.global_layout.addWidget(self.lbl_link)
        self.global_layout.addWidget(self.lbl_copyright)
        self.global_layout.addWidget(self.lbl_warning)
        self.global_layout.addWidget(self.lbl_license)

        # dialog settings
        self.setWindowIcon(QIcon(app_icon))
        self.setWindowModality(Qt.ApplicationModal)
        self.setLayout(self.global_layout)
