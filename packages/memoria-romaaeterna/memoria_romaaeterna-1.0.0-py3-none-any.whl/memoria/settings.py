#!/usr/bin/env python3
#
# This file is part of Memoria.
#
# Copyright (C) 2019 - Thomas Dähnrich <develop@tdaehnrich.de>
#
# Memoria is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# Memoria is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Memoria. If not, see <http://www.gnu.org/licenses/>.

import configparser
import gettext
import gi
import locale
import os
import sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


# set application name and version

APP = 'memoria'
VERSION = '1.0.0'


# set application paths

HOME_DIR = os.path.expanduser('~')
if os.name == 'posix':
    CONFIG_DIR = os.path.join(HOME_DIR, '.config', APP)
else:
    CONFIG_DIR = os.path.join(os.getenv('APPDATA'), APP)
CONFIG_FILE = os.path.join(CONFIG_DIR, 'config.ini')
HIGHSCORE_FILE = os.path.join(CONFIG_DIR, 'highscore.csv')
PLAYERS_FILE = os.path.join(CONFIG_DIR, 'players.txt')

pip_data_dirs = (
    os.path.join(sys.prefix, 'share', APP),             # standard
    os.path.join(HOME_DIR, '.local', 'share', APP),     # user
    os.path.join(HOME_DIR, 'share', APP)                # home
    )

# application uninstalled or MS Windows environment
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
DATA_DIR = os.path.join(ROOT_DIR, 'data')
if os.name == 'posix':
    LOCALE_DIR = os.path.join(ROOT_DIR, 'locale')
else:
    LOCALE_DIR = os.path.join(ROOT_DIR, 'share', 'locale')
    if not os.path.exists(LOCALE_DIR):
        LOCALE_DIR = os.path.join(ROOT_DIR, 'locale')

# application installed by Meson
if os.path.exists('@PKGDATADIR@') and os.path.exists('@LOCALEDIR@'):
   DATA_DIR = '@PKGDATADIR@'
   LOCALE_DIR = '@LOCALEDIR@'

# application installed by pip
else:
    for directory in pip_data_dirs:
       if os.path.exists(directory):
           DATA_DIR = directory
           LOCALE_DIR = os.path.join(directory, '..', 'locale')
           break

PIXMAPS_DIR = os.path.join(DATA_DIR, 'pixmaps')
SOUNDS_DIR = os.path.join(DATA_DIR, 'sounds')
UI_DIR = os.path.join(DATA_DIR, 'ui')


# main functions of settings

def get_settings():

    config = configparser.ConfigParser()
    if not config.read(CONFIG_FILE):
        os.makedirs(CONFIG_DIR, exist_ok=True)
        default_settings()
        save_config_file()
    else:
        read_config_file(config)


def default_settings():

    global dark_theme, sound, timer_length, default_player_number, default_folder, default_file

    dark_theme = False
    sound = True
    timer_length = 3
    default_player_number = 2
    default_folder = HOME_DIR
    default_file = ''


def save_config_file():

    config = configparser.ConfigParser()
    config['General'] = {
        'dark_theme': dark_theme,
        'sound': sound,
        'timer_length': timer_length,
        'default_player_number': default_player_number}
    config['VocabularyLists'] = {
        'default_folder': default_folder,
        'default_file': default_file}
    try:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            config.write(f)
    except PermissionError:
        message_text = _("Could not save configuration file: No write permissions.")
        error_dialog = Gtk.MessageDialog(self.winSettings, 0,
            Gtk.MessageType.ERROR, Gtk.ButtonsType.CLOSE, message_text)
        error_dialog.run()
        error_dialog.destroy()


def read_config_file(config):

    global dark_theme, sound, timer_length, default_player_number, default_folder, default_file

    modify_config = False

    try:
        dark_theme = config['General'].getboolean('dark_theme', fallback=False)
    except (KeyError, ValueError):
        dark_theme = False
        modify_config = True

    try:
        sound = config['General'].getboolean('sound', fallback=True)
    except (KeyError, ValueError):
        sound = True
        modify_config = True

    try:
        timer_length = config['General'].getint('timer_length', fallback=3)
    except (KeyError, ValueError):
        timer_length = 3
        modify_config = True

    try:
        default_player_number = config['General'].getint('default_player_number', fallback=2)
    except (KeyError, ValueError):
        default_player_number = 2
        modify_config = True

    try:
        default_folder = config['VocabularyLists'].get('default_folder', fallback=HOME_DIR)
    except (KeyError, ValueError):
        default_folder = HOME_DIR
        modify_config = True
    finally:
        if not os.path.exists(default_folder):
            default_folder = HOME_DIR
            modify_config = True

    try:
        default_file = config['VocabularyLists'].get('default_file', fallback='')
    except (KeyError, ValueError):
        default_file = ''
        modify_config = True
    finally:
        if not os.path.exists(default_file):
            default_file = ''
            modify_config = True

    if modify_config:
        save_config_file()


def setup_language():

    global _

    # setup for Linux
    if os.name == 'posix':
        locale.bindtextdomain(APP, LOCALE_DIR)
        locale.textdomain(APP)

    # setup for MS Windows
    else:
        import ctypes
        libintl = ctypes.cdll.LoadLibrary('libintl-8')
        # call encode() to prevent encoding errors with non-ASCII characters
        libintl.bindtextdomain(APP.encode('utf-8'), LOCALE_DIR.encode('utf-8'))
        libintl.bind_textdomain_codeset(APP.encode('utf-8'), 'UTF-8'.encode('utf-8'))
        os.environ['LANG'] = locale.getdefaultlocale()[0]

    _ = gettext.gettext
    gettext.bindtextdomain(APP, LOCALE_DIR)
    gettext.textdomain(APP)
    locale.setlocale(locale.LC_ALL, '')

    return _


def setup_headerbar(headerbar, button):

    decoration = Gtk.Settings.get_default().get_property("gtk-decoration-layout")
    if "close" in decoration.split(":")[0]:
        headerbar.child_set_property(button, "pack-type", Gtk.PackType.END)


def set_filter_for_file_button(filebutton):

    filter_csv = Gtk.FileFilter()
    filter_csv.set_name('CSV')
    filter_csv.add_mime_type('text/csv')
    filter_csv.add_pattern('*.[Cc][Ss][Vv]')
    filebutton.add_filter(filter_csv)

    filter_txt = Gtk.FileFilter()
    filter_txt.set_name('Text')
    filter_txt.add_mime_type('text/plain')
    filter_txt.add_pattern('*.[Tt][Xx][Tt]')
    filebutton.add_filter(filter_txt)


# initialize settings window and manage widgets

class Settings(Gtk.Window):

    def __init__(self, winGame):

        self.builder = Gtk.Builder()
        self.builder.add_from_file(os.path.join(UI_DIR, 'settings.ui'))
        self.builder.connect_signals(self)

        for obj in self.builder.get_objects():
            if issubclass(type(obj), Gtk.Buildable):
                name = Gtk.Buildable.get_name(obj)
                setattr(self, name, obj)

        setup_headerbar(self.headSettings, self.btnSettingsApply)
        set_filter_for_file_button(self.filbtnVocabularyFile)

        self.winSettings.set_transient_for(winGame)
        self.winSettings.show()


    def on_winSettings_show(self, widget):

        self.swtDarkTheme.set_active(dark_theme)
        self.swtSound.set_active(sound)
        self.spnbtnTimerLength.set_value(timer_length)
        self.spnbtnPlayerNumber.set_value(default_player_number)
        self.filbtnVocabularyFolder.set_filename(default_folder)
        if default_file:
            self.filbtnVocabularyFile.set_filename(default_file)


    def on_btnVocabularyFolderClear_clicked(self, widget):

        self.filbtnVocabularyFolder.set_filename(HOME_DIR)


    def on_btnVocabularyFileClear_clicked(self, widget):

        self.filbtnVocabularyFile.unselect_all()


    def on_btnSettingsApply_clicked(self, widget):

        global dark_theme, sound, timer_length, default_player_number, default_folder, default_file

        dark_theme = self.swtDarkTheme.get_active()
        sound = self.swtSound.get_active()
        timer_length = self.spnbtnTimerLength.get_value_as_int()
        default_player_number = self.spnbtnPlayerNumber.get_value_as_int()
        default_folder = self.filbtnVocabularyFolder.get_filename()
        default_file = self.filbtnVocabularyFile.get_filename()
        if not default_file:
            default_file = ''

        save_config_file()
        Gtk.Settings.get_default().set_property("gtk-application-prefer-dark-theme", dark_theme)
        self.winSettings.hide()


    def on_winSettings_delete_event(self, widget, event):

        self.winSettings.hide()
        return True
