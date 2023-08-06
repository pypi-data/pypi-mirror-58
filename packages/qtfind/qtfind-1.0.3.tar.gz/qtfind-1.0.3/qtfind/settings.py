"""Manage application settings"""
import shelve
from pathlib import Path


class Settings:
    def __init__(self):
        self.__settings_dir = Path(Path.home().joinpath('.config/qtfind'))
        self.__settings_file = Path(self.__settings_dir.joinpath('settings'))
        self.__is_settings_dir()
        self.__fail_safe_theme = 'default'
        self.__fail_safe_tone = 'default'
        self.__theme = {}
        self.__load_settings()

    def __is_settings_dir(self):
        """Check if the settings directory exists"""
        if not self.__settings_dir.is_dir():
            self.__settings_dir.mkdir(parents=True, exist_ok=True)

    def __load_settings(self):
        try:
            with shelve.open(str(self.__settings_file)) as db:
                self.__theme = {'theme': db['theme'], 'tone': db['tone']}
        except KeyError as e:
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
