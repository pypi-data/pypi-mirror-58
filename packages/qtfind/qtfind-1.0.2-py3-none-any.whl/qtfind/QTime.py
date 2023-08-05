from PyQt5.QtWidgets import *

from qtfind.QCommon import *


class QTime(QGroupBox):
    def __init__(self, widget_height=32, *__args):
        super().__init__(*__args)
        self.setTitle('Time:')
        self.setFont(set_bold(True))
        self.setCheckable(True)
        self.setChecked(False)
        self.__class_dimensions = [0, 0]
        self.__widget_height = widget_height
        self.__items = ['Last accessed', 'Last changed', 'Last modified']
        self.__rdb_labels = ['minutes', 'hours', 'days']
        self.rdb_widgets = []
        self.__grid_layout = QGridLayout()
        self.cmb_time = QComboBox()
        self.spn_time = QSpinBox()

        for i in range(len(self.__rdb_labels)):
            self.rdb_widgets.append(QRadioButton(self.__rdb_labels[i]))
            self.rdb_widgets[-1].setFont(set_bold(False))
            self.rdb_widgets[-1].adjustSize()
            init_geometry(self.rdb_widgets[-1], 0, 0,
                          self.rdb_widgets[-1].width(),
                          self.rdb_widgets[-1].height())

        # add predefined items, set font and geometry
        self.spn_time.setFont(set_bold(False))
        self.spn_time.setMaximum(999999)
        self.spn_time.setMinimum(-999999)
        self.spn_time.setValue(0)
        self.spn_time.adjustSize()

        self.cmb_time.addItems(self.__items)
        self.cmb_time.setFont(set_bold(False))
        self.cmb_time.adjustSize()

        self.__grid_layout.addWidget(self.rdb_widgets[0], 0, 0, 1, 1)
        self.__grid_layout.addWidget(self.rdb_widgets[1], 0, 1, 1, 1)
        self.__grid_layout.addWidget(self.rdb_widgets[2], 0, 2, 1, 1)
        self.__grid_layout.addWidget(self.spn_time, 1, 0, 1, 3)
        self.__grid_layout.addWidget(self.cmb_time, 2, 0, 1, 3)

        self.widget_height = self.__widget_height * 4
        self.widget_width = get_max_width([self.rdb_widgets])[0] + 20

        self.update_geometry()

        # assign the layout to the groupbox general
        self.setLayout(self.__grid_layout)
        self.adjustSize()

        # slots
        self.rdb_widgets[2].toggled.connect(self.on_days_toggled)
        self.toggled.connect(self.on_group_toggled)

    def collect_args(self, dict_args):
        if self.rdb_widgets[2].isChecked():
            dict_args['time'] = '-used ' + self.spn_time.text()
            return

        access = ['-a', '-c', '-m']
        if self.rdb_widgets[0].isChecked():
            dict_args['time'] = access[self.cmb_time.currentIndex()] + 'min ' + self.spn_time.text() + ' '
        else:
            dict_args['time'] = access[self.cmb_time.currentIndex()] + 'time ' + self.spn_time.text() + ' '

    ###########################################
    # slots
    ###########################################
    def on_days_toggled(self):
        self.cmb_time.setEnabled(not self.rdb_widgets[2].isChecked() and self.rdb_widgets[2].isEnabled())

    def on_group_toggled(self):
        self.on_days_toggled()

    ############################################

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

    def update_geometry(self):
        init_geometry(self, 0, 0, self.widget_width, self.widget_height)
