from PyQt5.QtWidgets import *

from qtfind.QCommon import *


class QHeader(QGridLayout):
    def __init__(self):
        super().__init__()
        self.current_path = str(Path.home())
        self.lbl_search = QLabel('Looking for:')
        self.lbl_search.setFont(set_bold(True))
        init_geometry(self.lbl_search, self.lbl_search.x(), self.lbl_search.y(), 94, 25)
        self.txt_search = QLineEdit()
        self.btn_path = QToolButton()
        self.btn_path.setText('...')
        self.txt_path = QLineEdit()
        self.btn_search = QPushButton('Search')
        self.btn_search.setDefault(True)
        self.cmb_criteria = QComboBox()
        self.cmb_criteria.addItems(('Contains', 'Starts with', 'Ends with', 'Exactly'))

        # added horizontal layout for esthetics
        self.select_layout = QHBoxLayout()
        self.select_layout.addWidget(self.txt_path)
        self.select_layout.addWidget(self.btn_path)

        init_geometry(self.btn_search, 0, 0, 94, 25)
        self.addWidget(self.lbl_search, 0, 0, 1, 1)
        self.addWidget(self.txt_search, 0, 1, 1, 5)
        self.addWidget(self.cmb_criteria, 0, 6, 1, 1)
        self.addWidget(self.btn_search, 0, 7, 1, 1)
        self.addLayout(self.select_layout, 1, 0, 1, 8)

        # slots
        self.on_pattern_changed()
        self.txt_path.textChanged.connect(self.on_pattern_changed)
        self.txt_search.textChanged.connect(self.on_pattern_changed)

    def validate_path(self, directory):
        """Return true if the path exists and it is a directory

        keyword arguments:
        directory -- path to validate"""
        if not directory:
            return False

        if Path(directory).is_dir():
            self.current_path = directory
            self.txt_path.setText(directory)
            return True

        return False

    ###########################################
    # slots
    ###########################################
    def on_pattern_changed(self):
        self.btn_search.setEnabled(bool(self.txt_path.text()) and bool(self.txt_search.text()))

    ############################################

    def collect_args(self):
        directory = self.txt_path.text()
        if not self.validate_path(directory):
            feedback_message('Error', 'Invalid directory', QMessageBox.Warning)
            return

        pattern = self.txt_search.text()
        if not pattern:
            feedback_message('Error', 'Invalid search criteria', QMessageBox.Warning)
            return

        if ' ' in directory:
            directory = f"'{directory}'"

        if is_globbing(pattern) or (self.cmb_criteria.currentIndex() == 3):
            return f"'{pattern}'", directory

        if self.cmb_criteria.currentIndex() == 0:
            pattern = f"'*{pattern}*'"
        elif self.cmb_criteria.currentIndex() == 1:
            pattern = f"'{pattern}*'"
        elif self.cmb_criteria.currentIndex() == 2:
            pattern = f"'*{pattern}'"

        return pattern, directory
