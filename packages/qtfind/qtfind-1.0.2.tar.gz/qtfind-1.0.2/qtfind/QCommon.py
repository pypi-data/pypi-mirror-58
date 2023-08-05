import re
import sys
from pathlib import Path

from PyQt5.QtCore import QRect, QSize
from PyQt5.QtGui import QFont, QColor, QClipboard
from PyQt5.QtWidgets import QMessageBox, QApplication

# key: (highlight, link, index, menu label)
dict_tones = {'orange': (QColor(218, 130, 42, 128), QColor(218, 130, 42), 3, 'Dark / &Orange'),
              'green': (QColor(42, 218, 130, 128), QColor(42, 218, 130), 2, 'Dark / &Green'),
              'pink': (QColor(218, 42, 130, 128), QColor(218, 42, 130), 4, 'Dark / &Pink'),
              'blue': (QColor(42, 130, 218, 128), QColor(42, 130, 218), 1, 'Dark / &Blue'),
              'default': (None, None, 0, '&Default')}

dict_slots = {dict_tones['orange'][3]: ('dark', 'orange'),
              dict_tones['green'][3]: ('dark', 'green'),
              dict_tones['pink'][3]: ('dark', 'pink'),
              dict_tones['blue'][3]: ('dark', 'blue'),
              dict_tones['default'][3]: ('default', 'default')}


def init_geometry(widget, left, top, width, height, is_max=True):
    widget.setGeometry(QRect(left, top, width, height))
    if is_max:
        widget.setMaximumSize(QSize(width, height))
    else:
        widget.setMinimumSize(QSize(width, height))


def set_bold(is_bold):
    bold = QFont()
    bold.setBold(is_bold)
    return bold


def get_max_width(widgets):
    widths = []
    for widget in widgets:
        widths += [item.width() for item in widget]

    return max(widths), min(widths)


def feedback_message(title, text, msg_icon=QMessageBox.Information, parent=None):
    # icon values:
    # QMessageBox.Information = 1
    # QMessageBox.Warning = 2
    box = QMessageBox()
    box.setText(text)
    box.setWindowTitle(title)
    box.setParent(parent)
    box.setIcon(msg_icon)
    box.setStandardButtons(QMessageBox.Ok)
    box.exec_()


def get_error_details():
    exc_type: object
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    line_no = tb.tb_lineno
    filename = f.f_code.co_filename
    return f'In: {str(Path(filename).stem)} ({str(line_no)})\n{exc_type}:\n{exc_obj}'


# main window specific functions
def set_tab_order(main_win):
    main_win.setTabOrder(main_win.header_layout.txt_search, main_win.header_layout.txt_path)
    main_win.setTabOrder(main_win.header_layout.btn_path, main_win.header_layout.btn_search)
    main_win.setTabOrder(main_win.header_layout.btn_search, main_win.opt_general.rdb_widgets[0])
    main_win.setTabOrder(main_win.opt_general.rdb_widgets[0], main_win.opt_general.chk_widgets[0])
    main_win.setTabOrder(main_win.opt_general.chk_widgets[0], main_win.opt_general.chk_widgets[1])
    main_win.setTabOrder(main_win.opt_general.chk_widgets[1], main_win.opt_general.chk_widgets[2])
    main_win.setTabOrder(main_win.opt_general.chk_widgets[2], main_win.opt_general.chk_widgets[3])
    main_win.setTabOrder(main_win.opt_general.chk_widgets[3], main_win.opt_general.cmb_type)
    main_win.setTabOrder(main_win.opt_general.cmb_type, main_win.opt_general.chk_widgets[4])
    main_win.setTabOrder(main_win.opt_general.chk_widgets[4], main_win.opt_general.txt_size)
    main_win.setTabOrder(main_win.opt_general.txt_size, main_win.opt_general.cmb_size)
    main_win.setTabOrder(main_win.opt_general.cmb_size, main_win.opt_filesystem.chk_widgets[0])
    main_win.setTabOrder(main_win.opt_filesystem.chk_widgets[0], main_win.opt_filesystem.spn_depth)
    main_win.setTabOrder(main_win.opt_filesystem.spn_depth, main_win.opt_filesystem.rdb_widgets[0])
    main_win.setTabOrder(main_win.opt_filesystem.rdb_widgets[0], main_win.opt_filesystem.cmb_fstype)
    main_win.setTabOrder(main_win.opt_filesystem.cmb_fstype, main_win.opt_permissions.cmb_perms)
    main_win.setTabOrder(main_win.opt_permissions.cmb_perms, main_win.opt_permissions.txt_perms)
    main_win.setTabOrder(main_win.opt_permissions.txt_perms, main_win.opt_permissions.chk_widgets[0])
    main_win.setTabOrder(main_win.opt_permissions.chk_widgets[0], main_win.opt_permissions.chk_widgets[1])
    main_win.setTabOrder(main_win.opt_permissions.chk_widgets[1], main_win.opt_permissions.cmb_modes)
    main_win.setTabOrder(main_win.opt_permissions.cmb_modes, main_win.opt_time.cmb_time)
    main_win.setTabOrder(main_win.opt_time.cmb_time, main_win.opt_time.rdb_widgets[0])
    main_win.setTabOrder(main_win.opt_time.rdb_widgets[0], main_win.opt_time.rdb_widgets[1])
    main_win.setTabOrder(main_win.opt_time.rdb_widgets[1], main_win.opt_time.rdb_widgets[2])
    main_win.setTabOrder(main_win.opt_time.rdb_widgets[2], main_win.opt_time.spn_time)


def is_globbing(text):
    regex = r"[?*\[\]^!${}|]+"
    return True if re.search(regex, text) else False


def command2clipboard(text):
    clip = QApplication.clipboard()
    if text:
        clip.setText(text, QClipboard.Clipboard)


def full_strip(text):
    regex = r"\s{2,}"

    return re.sub(regex, ' ', text.strip())
