from PyQt5.QtWidgets import *

from qtfind.QCommon import *
from qtfind.QSpacers import *


class QGeneral(QGroupBox):
    def __init__(self, widget_height=32, *__args):
        super().__init__(*__args)
        self.setTitle('General:')
        self.setFont(set_bold(True))
        self.__widget_height = widget_height
        self.__class_dimensions = [0, 0]
        self.__file_types = ('File', 'Directory', 'Link', 'Block', 'Socket', 'Pipe', 'Character')
        self.__file_size = ('Bytes', 'KiB', 'MiB', 'GiB')
        self.__rdb_labels = ('Name', 'Path', 'RegEx')
        self.__chk_labels = ('Case sensitive', 'Empty', 'Executable', 'Type', 'Size')
        self.__rdb_lbl_size = ('Greater then', 'Less than')
        self.__regex_type = ('emacs', 'sed', 'findutils-default', 'ed', 'gnu-awk', 'grep', 'posix-awk', 'awk',
                             'posix-basic', 'posix-egrep', 'egrep', 'posix-extended', 'posix-minimal-basic')
        self.cmb_regex_type = QComboBox()
        self.rdb_widgets = []
        self.chk_widgets = []
        self.rdb_size = []
        self.__form_layout = QFormLayout()
        self.__layout_size = QHBoxLayout()
        # container of greater/less than
        self.__group_size = QWidget()
        self.__layout_container = QVBoxLayout()
        self.txt_size = QSpinBox()
        self.cmb_size = QComboBox()
        self.cmb_type = QComboBox()

        for i in range(len(self.__rdb_labels)):
            self.rdb_widgets.append(QRadioButton(self.__rdb_labels[i]))
            self.rdb_widgets[-1].setFont(set_bold(False))
            self.rdb_widgets[-1].adjustSize()
            init_geometry(self.rdb_widgets[-1], 0, 0,
                          self.rdb_widgets[-1].width(),
                          self.rdb_widgets[-1].height())

        # select minimum option
        self.rdb_widgets[0].setChecked(True)

        for i in range(len(self.__chk_labels)):
            self.chk_widgets.append(QCheckBox(self.__chk_labels[i]))
            self.chk_widgets[-1].setFont(set_bold(False))
            self.chk_widgets[-1].adjustSize()
            init_geometry(self.chk_widgets[-1], 0, 0,
                          self.chk_widgets[-1].width(),
                          self.chk_widgets[-1].height())

        for label in self.__rdb_lbl_size:
            self.rdb_size.append(QRadioButton(label))
            self.rdb_size[-1].setFont(set_bold(False))
            self.rdb_size[-1].adjustSize()
            init_geometry(self.rdb_size[-1], 0, 0,
                          self.rdb_size[-1].width(),
                          self.rdb_size[-1].height())

        self.__layout_size.setContentsMargins(0, 0, 0, 0)
        self.__layout_size.addWidget(self.rdb_size[0])
        self.__layout_size.addWidget(self.rdb_size[1])
        self.__group_size.setContentsMargins(0, 0, 0, 0)
        self.__group_size.setLayout(self.__layout_size)
        self.__group_size.adjustSize()

        self.rdb_size[0].setChecked(True)

        self.txt_size.setFont(set_bold(False))
        self.txt_size.setMinimum(1)
        self.txt_size.setMaximum(999999)
        self.txt_size.adjustSize()

        # add predefined items, set font and geometry
        self.cmb_size.addItems(self.__file_size)
        self.cmb_size.setFont(set_bold(False))
        self.cmb_size.adjustSize()

        self.cmb_type.addItems(self.__file_types)
        self.cmb_type.setFont(set_bold(False))
        self.cmb_type.adjustSize()

        self.cmb_regex_type.addItems(self.__regex_type)
        self.cmb_regex_type.setFont(set_bold(False))
        self.cmb_regex_type.adjustSize()

        self.__form_layout.addRow(self.rdb_widgets[0], self.chk_widgets[0])
        self.__form_layout.addRow(self.rdb_widgets[1], self.chk_widgets[1])
        self.__form_layout.addRow(self.rdb_widgets[2], self.cmb_regex_type)
        self.__form_layout.addRow(self.chk_widgets[2])

        self.__form_layout.addRow(self.chk_widgets[3], self.cmb_type)

        self.__form_layout.addRow(self.chk_widgets[4], self.txt_size)
        self.__form_layout.addRow('', self.cmb_size)

        self.__layout_container.addLayout(self.__form_layout)
        self.__layout_container.addWidget(self.__group_size)
        self.__layout_container.addSpacerItem(QVSpacerItem())

        self.widget_height = self.__widget_height * 10
        self.widget_width = sum(get_max_width([self.rdb_widgets, self.chk_widgets])) + 40
        self.update_geometry()

        # assign the layout to the groupbox general
        self.setLayout(self.__layout_container)
        self.adjustSize()

        ## slots
        self.on_size_state_changed()
        self.on_type_state_changed()
        self.on_regex_toggled()
        self.chk_widgets[4].stateChanged.connect(self.on_size_state_changed)
        self.chk_widgets[3].stateChanged.connect(self.on_type_state_changed)
        self.rdb_widgets[2].toggled.connect(self.on_regex_toggled)

    def collect_args(self, dict_args):
        case = self.chk_widgets[0].isChecked()
        file_type = {'File': 'f', 'Directory': 'd', 'Link': 'l', 'Block': 'b', 'Socket': 's', 'Pipe': 'p',
                     'Character': 'c'}
        file_size = {'Bytes': 'c', 'KiB': 'k', 'MiB': 'M', 'GiB': 'G'}
        args = ({False: '-iname ', True: '-name '}, {False: '-ipath ', True: '-path '})

        if self.chk_widgets[1].isChecked():
            dict_args['empty'] = '-empty '

        if self.chk_widgets[2].isChecked():
            dict_args['executable'] = '-executable '

        if self.chk_widgets[3].isChecked():
            dict_args['type'] = f'-type {file_type[self.cmb_type.currentText()]} '

        if self.chk_widgets[4].isChecked():
            compare = '+' if self.rdb_size[0].isChecked() else '-'
            dict_args['size'] = f'-size {compare}{self.txt_size.text()}{file_size[self.cmb_size.currentText()]} '

        if self.rdb_widgets[0].isChecked():
            dict_args['name'] = args[0][case]
            return

        if self.rdb_widgets[1].isChecked():
            dict_args['path'] = args[1][case]
            return

        if self.rdb_widgets[2].isChecked():
            dict_args['regex'] = f'-regextype {self.__regex_type[self.cmb_regex_type.currentIndex()]} -regex '
            return

    ###########################################
    # slots
    ###########################################
    def on_size_state_changed(self):
        state = self.chk_widgets[4].isChecked()
        self.__group_size.setEnabled(state)
        self.txt_size.setEnabled(state)
        self.cmb_size.setEnabled(state)

    def on_type_state_changed(self):
        state = self.chk_widgets[3].isChecked()
        self.cmb_type.setEnabled(state)

    def on_regex_toggled(self):
        state = self.rdb_widgets[2].isChecked()
        self.cmb_regex_type.setEnabled(state)

    ############################################

    def update_geometry(self):
        init_geometry(self, 0, 0, self.widget_width, self.widget_height)

    @property
    def widget_height(self):
        return self.__class_dimensions[1]

    @widget_height.setter
    def widget_height(self, value):
        self.__class_dimensions[1] = value

    @property
    def widget_width(self):
        return self.__class_dimensions[0]

    @widget_width.setter
    def widget_width(self, value):
        self.__class_dimensions[0] = value
