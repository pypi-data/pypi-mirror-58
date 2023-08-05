from PyQt5.QtWidgets import *

from qtfind.QCommon import *


class QFileSystem(QGroupBox):
    def __init__(self, widget_height=32, *__args):
        super().__init__(*__args)
        self.setTitle('Filesystem:')
        # set font weight
        self.setFont(set_bold(True))
        self.setCheckable(True)
        self.setChecked(False)
        self.__class_dimensions = [0, 0]
        self.__widget_height = widget_height
        self.__fs_types = ['btrfs', 'exfat', 'ext3', 'ext4', 'f2fs', 'hfs', 'hfs+', 'jfs', 'nilfs2', 'ntfs', 'reiserfs',
                           'udf', 'vfat', 'xfs']
        self.__rdb_labels = ['Only this partition', 'CD-ROM/MS-DOS filesystems', 'Other filesystem']
        self.__chk_labels = ['Depth']
        self.rdb_widgets = []
        self.chk_widgets = []
        self.__form_layout = QFormLayout()
        self.cmb_fstype = QComboBox()
        self.spn_depth = QSpinBox()

        for i in range(len(self.__rdb_labels)):
            self.rdb_widgets.append(QRadioButton(self.__rdb_labels[i]))
            self.rdb_widgets[-1].setFont(set_bold(False))
            self.rdb_widgets[-1].adjustSize()
            init_geometry(self.rdb_widgets[-1], 0, 0,
                          self.rdb_widgets[-1].width(),
                          self.rdb_widgets[-1].height())

        for i in range(len(self.__chk_labels)):
            self.chk_widgets.append(QCheckBox(self.__chk_labels[i]))
            self.chk_widgets[-1].setFont(set_bold(False))
            self.chk_widgets[-1].adjustSize()
            init_geometry(self.chk_widgets[-1], 0, 0,
                          self.chk_widgets[-1].width(),
                          self.chk_widgets[-1].height())

        # add predefined items, set font and geometry
        self.spn_depth.setFont(set_bold(False))
        self.spn_depth.setMinimum(-999999)
        self.spn_depth.setMaximum(999999)
        self.spn_depth.setValue(0)
        self.spn_depth.adjustSize()

        self.cmb_fstype.addItems(self.__fs_types)
        self.cmb_fstype.setFont(set_bold(False))
        self.cmb_fstype.adjustSize()

        self.__form_layout.addRow(self.chk_widgets[0], self.spn_depth)
        self.__form_layout.addRow(self.rdb_widgets[0])  # , '')
        self.__form_layout.addRow(self.rdb_widgets[1])  # , '')
        self.__form_layout.addRow(self.rdb_widgets[2], self.cmb_fstype)

        self.widget_height = self.__widget_height * 5
        self.widget_width = get_max_width([self.rdb_widgets, self.chk_widgets])[0] + 20

        self.update_geometry()

        # assign the layout to the groupbox general
        self.setLayout(self.__form_layout)
        self.adjustSize()

        # slots
        self.chk_widgets[0].stateChanged.connect(self.on_depth_checked)
        self.rdb_widgets[2].toggled.connect(self.on_fstype_changed)
        self.toggled.connect(self.on_group_toggled)

    def collect_args(self, dict_args):
        depth_value = int(self.spn_depth.text())
        if self.chk_widgets[0].isChecked() and depth_value:
            if depth_value < 0:
                dict_args['depth'] = '-mindepth ' + str(abs(depth_value)) + ' '
            else:
                dict_args['depth'] = '-maxdepth ' + str(abs(depth_value)) + ' '

        if self.rdb_widgets[0].isChecked():
            dict_args['xdev'] = '-xdev '
            return

        if self.rdb_widgets[1].isChecked():
            dict_args['cdrom'] = '-noleaf '
            return

        if self.rdb_widgets[2].isChecked():
            dict_args['other'] = '-fstype ' + self.cmb_fstype.currentText() + ' '

    ###########################################
    # slots
    ###########################################
    def on_depth_checked(self):
        state = self.chk_widgets[0].isChecked() and self.chk_widgets[0].isEnabled()
        self.spn_depth.setEnabled(state)

    def on_fstype_changed(self):
        state = self.rdb_widgets[2].isChecked() and self.rdb_widgets[2].isEnabled()
        self.cmb_fstype.setEnabled(state)

    def on_group_toggled(self):
        self.on_depth_checked()
        self.on_fstype_changed()

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
