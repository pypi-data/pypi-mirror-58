import shlex

from PyQt5.QtCore import QProcess, pyqtSlot
from PyQt5.QtGui import QIcon

from qtfind.QAbout import QAbout
from qtfind.QFileSystem import *
from qtfind.QGenreal import *
from qtfind.QHeader import *
from qtfind.QPermissions import *
from qtfind.QSpacers import *
from qtfind.QTime import *
from qtfind.settings import Settings
from qtfind.QLabelClick import *


# create main window
class QtFind(QMainWindow):
    """Create main window with all necessary widgets"""

    def __init__(self, app_icon, title):
        # initialize parent class 1st
        super().__init__()
        # set window title
        self.status_bar = QStatusBar()
        self.title = title
        self.app_icon = app_icon
        self.theme = Settings()
        self.__new_width = 0
        # set min dimensions
        self.__width = 620
        self.__height = 400
        self.__widget_height = 32
        self.__status = ('Ready.', 'Running...')
        ##################################################################
        self.process = QProcess()
        self.process.readyReadStandardOutput.connect(self.read_output)
        self.process.readyReadStandardError.connect(self.read_errors)
        self.process.finished.connect(self.process_finished)
        ###################################################################
        # initialize user interface
        self.__init_ui(self.app_icon)

    def __init_ui(self, app_icon):
        self.setup_menu()
        # label for statusbar
        self.lbl_command = QLabelClick('',trigger=Trigger.DOUBLE, button=Qt.LeftButton)
        self.lbl_command.mouse_double_pressed.connect(self.copy_command)
        self.lbl_status = QLabel(self.__status[0])
        self.setup_statusbar()
        # bind the class keyPressEvent method to a customized one
        self.keyPressEvent = self.key_PressEvent
        # set app icon (png file)
        self.setWindowIcon(QIcon(app_icon))
        # assign title
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.__width, self.__height)
        # set layout for options
        self.opt_scroll = QScrollArea()
        # QWidget used because QScrollArea doesn't take QLayout (QVBoxLayout...)
        self.main_box = QWidget()
        self.options_layout = QVBoxLayout()
        self.footer_layout = QHBoxLayout()
        self.results = QListWidget(self)
        self.results.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.layout = QVBoxLayout()
        # master layout (the only layout with parent set to self)
        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget(self)
        # initialize layouts and widgets
        self.opt_general = QGeneral(self.__widget_height)
        self.opt_filesystem = QFileSystem(self.__widget_height)
        self.opt_permissions = QPermissions(self.__widget_height)
        self.opt_time = QTime(self.__widget_height)
        self.header_layout = QHeader()

        # return the width of the largest item
        self.__largest_width()

        # setting a common width to all widgets
        self.__update_layouts()

        # assigning widgets to their layout
        self.options_layout.addWidget(self.opt_general)
        self.options_layout.addWidget(self.opt_filesystem)
        self.options_layout.addWidget(self.opt_permissions)
        self.options_layout.addWidget(self.opt_time)
        self.options_layout.addSpacerItem(QVSpacerItem())

        # assigning the layout to a widget
        self.main_box.setLayout(self.options_layout)

        # assigning the widget to a opt_scroll area
        self.opt_scroll.setWidget(self.main_box)
        self.opt_scroll.setWidgetResizable(True)
        self.opt_scroll.horizontalScrollBar().setVisible(False)

        # fixed width for opt_scroll area widget independently from the window's size
        self.opt_scroll.setFixedWidth(self.__new_width + 34)

        # contains the options and results layouts
        self.footer_layout.addWidget(self.opt_scroll)
        self.footer_layout.addWidget(self.results)

        # add global children layouts
        self.main_layout.addLayout(self.header_layout)
        self.main_layout.addLayout(self.footer_layout)
        # set main layout to the display widget
        self.main_widget.setLayout(self.main_layout)
        # the following is to resize the widget with the window
        self.setCentralWidget(self.main_widget)

        self.header_layout.txt_search.setFocus()

    def __largest_width(self):
        """Retrieve the largest width from given layouts"""
        self.__new_width = max([self.opt_general.widget_width,
                                self.opt_filesystem.widget_width,
                                self.opt_permissions.widget_width,
                                self.opt_time.widget_width])

    def __update_layouts(self):
        """Set a unified width for layouts"""
        self.opt_general.widget_width = self.__new_width
        self.opt_general.update_geometry()

        self.opt_filesystem.widget_width = self.__new_width
        self.opt_filesystem.update_geometry()

        self.opt_permissions.widget_width = self.__new_width
        self.opt_permissions.update_geometry()

        self.opt_time.widget_width = self.__new_width
        self.opt_time.update_geometry()

    def set_center(self):
        """Center the window on the screen"""
        self.main_rect = self.frameGeometry()
        self.center_point = QDesktopWidget().availableGeometry().center()
        self.main_rect.moveCenter(self.center_point)
        self.move(self.main_rect.topLeft())

    def setup_menu(self):
        """Set a menu and submenus"""
        self.menu_bar = self.menuBar()
        self.settings_menu = self.menu_bar.addMenu('&Actions')

        self.clear_action = QAction('C&lear')
        self.clear_action.setShortcut('Ctrl+L')

        self.copy_action = QAction('&Copy command')
        self.copy_action.setShortcut('Ctrl+C')

        self.exit_action = QAction('&Exit')
        self.exit_action.setShortcut('Ctrl+Q')

        self.cancel_action = QAction('Ca&ncel')
        self.cancel_action.setShortcut('Ctrl+Z')
        self.cancel_action.setEnabled(False)

        self.about_action = QAction('&About')
        self.about_action.setShortcut('F1')

        self.about_qt_action=QAction('About Qt')

        self.theme_action = QMenu('&Theme', self.settings_menu)
        # the QActionGroup is used for exclusivity
        self.themes_group = QActionGroup(self.theme_action)
        self.themes_group.setExclusive(True)
        self.default_action = QAction('&Default', self.theme_action, checkable=True)
        self.default_action.setChecked(True)
        self.dark_blue_action = QAction('Dark / &Blue', self.theme_action, checkable=True)
        self.dark_green_action = QAction('Dark / &Green', self.theme_action, checkable=True)
        self.dark_orange_action = QAction('Dark / &Orange', self.theme_action, checkable=True)
        self.dark_pink_action = QAction('Dark / &Pink', self.theme_action, checkable=True)

        self.themes_group.addAction(self.default_action)
        self.themes_group.addAction(self.dark_blue_action)
        self.themes_group.addAction(self.dark_green_action)
        self.themes_group.addAction(self.dark_orange_action)
        self.themes_group.addAction(self.dark_pink_action)

        self.theme_action.addActions([self.default_action,
                                      self.dark_blue_action,
                                      self.dark_green_action,
                                      self.dark_orange_action,
                                      self.dark_pink_action])

        self.settings_menu.addMenu(self.theme_action)
        self.settings_menu.addAction(self.clear_action)
        self.settings_menu.addAction(self.copy_action)
        self.settings_menu.addAction(self.cancel_action)
        self.settings_menu.addAction(self.about_action)
        self.settings_menu.addAction(self.about_qt_action)
        self.settings_menu.addSeparator()
        self.settings_menu.addAction(self.exit_action)
        self.settings_menu.triggered[QAction].connect(self.process_trigger)

    def setup_statusbar(self):
        self.setStatusBar(self.status_bar)
        self.lbl_status.setAlignment(Qt.AlignRight)
        self.lbl_command.setAlignment(Qt.AlignLeft)
        self.status_bar.addPermanentWidget(self.lbl_command, 1)
        self.status_bar.addPermanentWidget(self.lbl_status, 0)

    def show_about(self):
        """Show about dialog"""
        self.about_diag = QAbout(self, self.app_icon)
        self.about_diag.exec_()

    def on_btn_search_clicked(self):
        """
        Collect selected options,
        Construct command,
        Execute it,
        Show results in the list
        """
        self.results.clear()

        header = self.header_layout.collect_args()

        if not header:
            return

        self.cancel_action.setEnabled(True)
        command = full_strip(self.all_args(header))
        self.lbl_command.setText(command)
        self.lbl_status.setText(self.__status[1])
        self.run_command(command)

    def on_btn_path_clicked(self):
        """Execute commands on event of the search button clicked"""
        directory = QFileDialog.getExistingDirectory(self.header_layout.btn_search, "Choose directory",
                                                     str(self.header_layout.current_path))
        if not self.header_layout.validate_path(directory):
            feedback_message('Error', 'Invalid directory', QMessageBox.Warning)

    def process_trigger(self, widget):
        """Execute action connected to the menu item

        keyword arguments:
        widget -- QAction passed automatically by the caller
        """
        if widget.text() == '&Exit':
            qApp.quit()

        if widget.text() == '&About':
            self.show_about()
            return

        if widget.text() == 'About Qt':
            QApplication.instance().aboutQt()
            return

        if widget.text() == 'C&lear':
            self.clear_options()
            return

        if widget.text() == 'Ca&ncel':
            self.process.terminate()
            self.cancel_action.setEnabled(False)
            return

        if widget.text() == '&Copy command':
            command2clipboard(self.lbl_command.text())

    def clear_options(self):
        """Reset all options to their defaults"""
        self.lbl_command.setText('')
        self.lbl_status.setText(self.__status[0])
        self.results.clear()
        # widgets in QHeader
        self.header_layout.txt_path.setText('')
        self.header_layout.txt_search.setText('')
        self.opt_general.rdb_widgets[0].setChecked(True)
        self.opt_general.rdb_size[0].setChecked(True)

        # widgets in QGeneral
        for option_index in range(1, len(self.opt_general.rdb_widgets)):
            self.opt_general.rdb_widgets[option_index].setChecked(False)

        for option in self.opt_general.chk_widgets:
            option.setChecked(False)

        self.opt_general.setChecked(True)

        # widgets in QFileSystem
        for option in self.opt_filesystem.rdb_widgets:
            option.setChecked(False)

        for option in self.opt_filesystem.chk_widgets:
            option.setChecked(False)

        self.opt_filesystem.setChecked(False)

        # widgets in QPermissions
        self.opt_permissions.txt_perms.setText('')
        for option in self.opt_permissions.chk_widgets:
            option.setChecked(False)

        self.opt_permissions.setChecked(False)

        # widgets in QTime
        for option in self.opt_time.rdb_widgets:
            option.setChecked(False)

        self.opt_time.setChecked(False)

        # set focus to the search box
        self.header_layout.txt_search.setFocus()

    def key_PressEvent(self, event):
        """Capture pressed key and execute Search button function
        if the pressed key is return or enter (numpad)"""
        if event.key() in [Qt.Key_Return, Qt.Key_Enter]:
            self.on_btn_search_clicked()

    def all_args(self, header):
        """Retrieve the command's arguments

        keyword arguments:
        header -- widget containing mandatory fields
        """
        command = ''
        dict_arguments = {}

        self.opt_general.collect_args(dict_arguments)
        if self.opt_filesystem.isChecked():
            self.opt_filesystem.collect_args(dict_arguments)
        if self.opt_permissions.isChecked():
            self.opt_permissions.collect_args(dict_arguments)
        if self.opt_time.isChecked():
            self.opt_time.collect_args(dict_arguments)

        if 'name' in dict_arguments:
            command = f'find {header[1]} {dict_arguments["name"]} {header[0]} '

        if 'path' in dict_arguments:
            command = f'find {header[1]} {dict_arguments["path"]} {header[0]} '

        if 'regex' in dict_arguments:
            command = f'find {header[1]} {dict_arguments["regex"]} {header[0]} '

        for key, value in dict_arguments.items():
            if key not in ['name', 'path', 'regex']:
                command += value + ' '

        return command

    def QByteArray2str(self, s):
        return str(s, encoding="utf8", errors="replace")

    # the following functions are used to run the shell command
    # and updating the results in realtime
    def run_command(self, command):
        lst_command = shlex.split(command.replace('  ', ' ').strip())
        self.process.start(lst_command[0], lst_command[1:])

    def copy_command(self):
        command2clipboard(self.lbl_command.text())

    @pyqtSlot()
    def read_output(self):
        line = self.QByteArray2str(self.process.readAllStandardOutput()).split(sep='\n')
        self.results.addItems(line)

    @pyqtSlot()
    def read_errors(self):
        line = self.QByteArray2str(self.process.readAllStandardError()).split(sep='\n')
        with open('log', 'a') as f:
            f.write('\n'.join(line))

    def process_finished(self, exitCode, exitStatus):
        self.lbl_status.setText(self.__status[0])
        self.results.takeItem(self.results.count() - 1)
        self.cancel_action.setEnabled(False)

    @property
    def theme_name(self):
        return self.theme.get_theme('theme', 'tone')

    @theme_name.setter
    def theme_name(self, theme):
        self.theme.save_theme(theme[0], theme[1])
