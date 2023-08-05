"""Manage application settings"""
import shelve
from pathlib import Path


class Settings:
    def __init__(self):
        # settings file (full path) .../settings
        self.__settings_dir = Path(Path.home().joinpath('.config/qtfind'))
        self.__settings_file = Path(self.__settings_dir.joinpath('settings'))
        self.__exist = False
        self.__file_exit()
        # default path, in case settings.dat doesn't exist (e.g. 1st launch)
        # joins the path in __settings_path to Home directory
        self.__fail_safe_theme = 'default'
        self.__fail_safe_tone = 'default'
        self.__theme = {}
        self.__load_settings()

    def __file_exit(self):
        """Check if the file exists"""
        if self.__settings_dir.is_dir():
            self.__exist = Path(str(self.__settings_file) + '.dat').is_file()
        else:
            self.__exist = False
            self.__settings_dir.mkdir(parents=True, exist_ok=True)

    def __load_settings(self):
        if self.__exist:
            with shelve.open(str(self.__settings_file)) as db:
                self.__theme = {'theme': db['theme'], 'tone': db['tone']}
        else:
            self.__theme = {'theme': self.__fail_safe_theme, 'tone': self.__fail_safe_tone}

    def __save_settings(self):
        with shelve.open(str(self.__settings_file)) as db:
            db['theme'] = self.__theme['theme']
            db['tone'] = self.__theme['tone']

    def save_theme(self, theme, tone):
        """Save theme.

        Keyword arguments:
        theme -- theme's name
        tone -- theme's tone
        """
        self.__theme['theme'] = theme
        self.__theme['tone'] = tone
        self.__save_settings()

    def get_theme(self, theme, tone):
        """Load theme.

        Keyword arguments:
        theme -- theme's name
        tone -- theme's tone
        """
        return self.__theme[theme], self.__theme[tone]

