from PyQt5.QtWidgets import *
from qtfind.QCommon import *


class QPermissions(QGroupBox):
    def __init__(self, widget_height=32, *__args):
        super().__init__(*__args)
        self.setTitle('Permissions:')
        self.setFont(set_bold(True))
        self.setCheckable(True)
        self.setChecked(False)
        self.__class_dimensions = [0, 0]
        self.__widget_height = widget_height
        self.__perm_labels = ['Owner', 'Group', 'Owner ID', 'Group ID', 'No owner', 'No group', 'Attributes']
        self.__chk_perms = ['Readable', 'Writable']
        self.__cmb_modes = ['Contains', 'At least', 'Exactly']
        self.chk_widgets = []
        self.__form_layout = QFormLayout()
        self.cmb_perms = QComboBox()
        self.txt_perms = QLineEdit()
        self.cmb_modes = QComboBox()

        for i in range(len(self.__chk_perms)):
            self.chk_widgets.append(QCheckBox(self.__chk_perms[i]))
            self.chk_widgets[-1].setFont(set_bold(False))
            self.chk_widgets[-1].adjustSize()
            init_geometry(self.chk_widgets[-1], 0, 0,
                          self.chk_widgets[-1].width(),
                          self.chk_widgets[-1].height())

        # add predefined items, set font and geometry
        self.cmb_perms.addItems(self.__perm_labels)
        self.cmb_perms.setFont(set_bold(False))
        self.cmb_perms.adjustSize()

        self.cmb_modes.addItems(self.__cmb_modes)
        self.cmb_modes.setFont(set_bold(False))
        self.cmb_modes.adjustSize()

        self.txt_perms.setFont(set_bold(False))

        self.__form_layout.addRow(self.cmb_perms, self.txt_perms)
        self.__form_layout.addRow(self.chk_widgets[0], self.chk_widgets[1])
        self.__form_layout.addRow(self.cmb_modes)

        self.widget_height = self.__widget_height * 5
        self.widget_width = get_max_width([self.chk_widgets])[0] + 20

        self.update_geometry()

        # assign the layout to the groupbox general
        self.setLayout(self.__form_layout)
        self.adjustSize()

        # slots
        self.cmb_perms.currentIndexChanged.connect(self.on_perms_index_changed)
        self.toggled.connect(self.on_perms_index_changed)

    def collect_args(self, dict_args):
        param = self.txt_perms.text()

        if not param:
            return

        modes = ('/', '-', '')
        mode = modes[self.cmb_modes.currentIndex()]
        permissions = (f'-user {param} ', f'-group {param} ', f'-uid {param} ',
                       f'-gid {param} ', '-nouser ', '-nogroup ', f'-perm {mode}{param} ')

        read_write = {True: ('-readable ', '-writable '), False: ('', '')}

        print(self.cmb_modes.currentIndex())

        dict_args['permissions'] = permissions[self.cmb_perms.currentIndex()]

        for i, chk_widget in enumerate(self.chk_widgets):
            dict_args['permissions'] += read_write[chk_widget.isChecked()][i]

    ###########################################
    # slots
    ###########################################
    def on_perms_index_changed(self):
        self.cmb_modes.setEnabled((self.cmb_perms.currentIndex() == 6) and self.cmb_perms.isEnabled())

    def on_group_toggled(self):
        self.on_perms_index_changed()

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
