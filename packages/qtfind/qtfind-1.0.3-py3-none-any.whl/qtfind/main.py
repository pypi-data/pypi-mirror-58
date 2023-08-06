from PyQt5.QtGui import QPalette

from qtfind.QFind import *


app_icon=str(Path(Path(__file__).parent).joinpath('Icon.png'))

app = QApplication(sys.argv)
main_window = QtFind(app_icon, 'QtFind')

PRIMARY_DARK = QColor(53, 53, 53)
TEXT_DARK = QColor(255, 255, 255)
DISABLED_DARK = QColor(128, 128, 128)
BASE_DARK = QColor(25, 25, 25)


def theme_wrapper(action):
    set_theme(*dict_slots[action.text()])


def set_theme(theme, tone=''):
    if theme == 'default':
        # use app.setPalette(app.style().standardPalette()) to
        # reset the default palette
        app.setPalette(app.style().standardPalette())

    elif theme == 'dark':
        """Set the palette to a dark theme"""
        # app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        # use a palette to switch to dark colors/theme:
        palette = QPalette()

        palette.setColor(QPalette.Window, PRIMARY_DARK)
        palette.setColor(QPalette.WindowText, TEXT_DARK)
        palette.setColor(QPalette.Base, BASE_DARK)
        palette.setColor(QPalette.AlternateBase, PRIMARY_DARK)
        palette.setColor(QPalette.ToolTipBase, TEXT_DARK)
        palette.setColor(QPalette.ToolTipText, TEXT_DARK)
        palette.setColor(QPalette.Text, TEXT_DARK)
        palette.setColor(QPalette.Button, PRIMARY_DARK)
        palette.setColor(QPalette.ButtonText, TEXT_DARK)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, dict_tones[tone][1])
        palette.setColor(QPalette.Highlight, dict_tones[tone][0])
        palette.setColor(QPalette.HighlightedText, TEXT_DARK)
        palette.setColor(QPalette.Disabled, QPalette.Text, DISABLED_DARK)
        palette.setColor(QPalette.Disabled, QPalette.WindowText, DISABLED_DARK)
        palette.setColor(QPalette.Disabled, QPalette.ButtonText, DISABLED_DARK)

        app.setPalette(palette)

    main_window.theme_name = (theme, tone)


def assign_slots():
    """Assign signals to slots"""
    main_window.header_layout.btn_search.clicked.connect(main_window.on_btn_search_clicked)
    main_window.header_layout.btn_path.clicked.connect(main_window.on_btn_path_clicked)
    main_window.theme_action.triggered[QAction].connect(theme_wrapper)


def init_theme():
    theme, tone = main_window.theme_name
    set_theme(theme, tone)

    index = dict_tones[tone][2]
    main_window.theme_action.actions()[index].setChecked(True)


def main():
    # Force the style to be the same on all OSs:
    app.setStyle('Fusion')

    init_theme()
    set_tab_order(main_window)
    assign_slots()

    main_window.set_center()
    main_window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()

