#!/usr/bin/env python3
#
# This file is part of Vocabulary Football (VocBall).
#
# Copyright (C) 2017-2019 - Thomas Dähnrich <develop@tdaehnrich.de>
#
# VocBall is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# VocBall is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with VocBall. If not, see <http://www.gnu.org/licenses/>.

import configparser
import gettext
import gi
import locale
import os
import subprocess
import sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


# set application name and version

APP = 'vocball'
VERSION = '1.1.0'


# set application paths

HOME_DIR = os.path.expanduser('~')
if os.name == 'posix':
    CONFIG_DIR = os.path.join(HOME_DIR, '.config', APP)
else:
    CONFIG_DIR = os.path.join(os.getenv('APPDATA'), APP)
CONFIG_FILE = os.path.join(CONFIG_DIR, 'config.ini')
TEAMS_FILE = os.path.join(CONFIG_DIR, 'teams.txt')

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
    installed = False
else:
    LOCALE_DIR = os.path.join(ROOT_DIR, 'share', 'locale')
    installed = True
    if not os.path.exists(os.path.join(LOCALE_DIR, 'va')):
        LOCALE_DIR = os.path.join(ROOT_DIR, 'locale')
        installed = False

# application installed by Meson
if os.path.exists('@PKGDATADIR@') and os.path.exists('@LOCALEDIR@'):
   DATA_DIR = '@PKGDATADIR@'
   LOCALE_DIR = '@LOCALEDIR@'
   installed = True

# application installed by pip
else:
    for directory in pip_data_dirs:
       if os.path.exists(directory):
           DATA_DIR = directory
           LOCALE_DIR = os.path.join(directory, '..', 'locale')
           installed = True
           break

PIXMAPS_DIR = os.path.join(DATA_DIR, 'pixmaps')
SOUNDS_DIR = os.path.join(DATA_DIR, 'sounds')
UI_DIR = os.path.join(DATA_DIR, 'ui')


# define global variables

fullscreen_available = True


# main functions of settings

def get_settings():

    global new_settings

    new_settings = False

    config = configparser.ConfigParser()
    if not config.read(CONFIG_FILE):
        os.makedirs(CONFIG_DIR, exist_ok=True)
        default_settings()
        save_config_file()
    else:
        read_config_file(config)

    return fullscreen


def default_settings():

    global fullscreen, dark_theme, language, sound, timer_length, keyboard
    global selection, default_folder, default_file

    fullscreen = False
    dark_theme = False
    language = 'system'
    sound = True
    timer_length = 5
    keyboard = True
    selection = 'source'
    default_folder = HOME_DIR
    default_file = ''


def save_config_file():

    config = configparser.ConfigParser()
    config['General'] = {
        'fullscreen': fullscreen,
        'dark_theme': dark_theme,
        'language': language,
        'sound': sound,
        'timer_length': timer_length,
        'keyboard': keyboard}
    config['Vocabulary'] = {
        'selection': selection,
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

    global fullscreen, dark_theme, language, sound, timer_length, keyboard
    global selection, default_folder, default_file

    modify_config = False

    try:
        fullscreen = config['General'].getboolean('fullscreen', fallback=False)
    except (KeyError, ValueError):
        fullscreen = False
        modify_config = True

    try:
        dark_theme = config['General'].getboolean('dark_theme', fallback=False)
    except (KeyError, ValueError):
        dark_theme = False
        modify_config = True

    try:
        language = config['General'].get('language', fallback='system')
    except (KeyError, ValueError):
        language = 'system'
        modify_config = True

    try:
        sound = config['General'].getboolean('sound', fallback=True)
    except (KeyError, ValueError):
        sound = True
        modify_config = True

    try:
        timer_length = config['General'].getint('timer_length', fallback=5)
    except (KeyError, ValueError):
        timer_length = 5
        modify_config = True

    try:
        keyboard = config['General'].getboolean('keyboard', fallback=True)
    except (KeyError, ValueError):
        keyboard = True
        modify_config = True

    try:
        selection = config['Vocabulary'].get('selection', fallback='source')
    except (KeyError, ValueError):
        selection = 'source'
        modify_config = True

    try:
        default_folder = config['Vocabulary'].get('default_folder', fallback=HOME_DIR)
    except (KeyError, ValueError):
        default_folder = HOME_DIR
        modify_config = True
    finally:
        if not os.path.exists(default_folder):
            default_folder = HOME_DIR
            modify_config = True

    try:
        default_file = config['Vocabulary'].get('default_file', fallback='')
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

    global latin_workaround, _

    # workaround for Latin language
    if os.name == 'posix':
        locales = subprocess.getoutput('locale -a')
        if 'C.UTF-8' in locales:
            latin_workaround = True
        else:
            latin_workaround = False
    else:
        latin_workaround = True

    # setup for Linux
    if os.name == 'posix':
        locale.bindtextdomain(APP, LOCALE_DIR)
        locale.textdomain(APP)
        if language == 'Latin' and latin_workaround:
            os.environ['LANG'] = 'C.UTF-8'
            _ = gettext.translation(APP, LOCALE_DIR, ['va']).gettext
        else:
            _ = gettext.gettext

    # setup for MS Windows
    else:
        import ctypes
        libintl = ctypes.cdll.LoadLibrary('libintl-8')
        # call encode() to prevent encoding errors with non-ASCII characters
        libintl.bindtextdomain(APP.encode('utf-8'), LOCALE_DIR.encode('utf-8'))
        libintl.bind_textdomain_codeset(APP.encode('utf-8'), 'UTF-8'.encode('utf-8'))
        if language == 'Latin' and latin_workaround:
            os.environ['LANG'] = 'va'
            _ = gettext.translation(APP, LOCALE_DIR, ['va']).gettext
        else:
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


def deactivate_fullscreen():

    global fullscreen_available

    fullscreen_available = False


def apply_new_settings(do_or_done):

    global new_settings

    if do_or_done:
        new_settings = not new_settings

    return new_settings


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

        # General
        self.swtFullscreen.set_active(fullscreen)
        if not fullscreen_available:
            self.swtFullscreen.set_sensitive(False)
            self.swtFullscreen.set_tooltip_text(_("Not available for current screen size"))
        self.swtDarkTheme.set_active(dark_theme)
        if installed:
            if language == 'system':
                self.cmbLanguage.set_active(0)
                if not latin_workaround:
                    self.cmbLanguage.set_sensitive(False)
                    self.cmbLanguage.set_tooltip_text(_("Not available for OS / uninstalled application"))
            else:
                self.cmbLanguage.set_active(1)
        else:
            self.cmbLanguage.set_active(0)
            self.cmbLanguage.set_sensitive(False)
            self.cmbLanguage.set_tooltip_text(_("Not available for OS / uninstalled application"))
        self.swtSound.set_active(sound)
        self.spnbtnTimerLength.set_value(timer_length)
        self.swtKeyboard.set_active(keyboard)

        # Vocabulary
        if selection == "source":
            self.togbtnSource.set_active(True)
        if selection == "target":
            self.togbtnTarget.set_active(True)
        if selection == "both":
            self.togbtnBoth.set_active(True)
        self.filbtnVocabularyFolder.set_filename(default_folder)
        if default_file:
            self.filbtnVocabularyFile.set_filename(default_file)


    def on_btnVocabularyFolderClear_clicked(self, widget):

        self.filbtnVocabularyFolder.set_filename(HOME_DIR)


    def on_btnVocabularyFileClear_clicked(self, widget):

        self.filbtnVocabularyFile.unselect_all()


    def on_togbtnVocabularySelection_clicked(self, widget):

        name = widget.get_property("name")
        if not widget.get_active():
            return
        else:
            widget.set_active(True)
            for button in (self.togbtnSource, self.togbtnTarget, self.togbtnBoth):
                if button.get_property("name") != name:
                    button.set_active(False)


    def on_btnSettingsApply_clicked(self, widget):

        global fullscreen, dark_theme, language, sound, timer_length, keyboard
        global selection, default_folder, default_file

        # General
        fullscreen_prior = fullscreen
        fullscreen = self.swtFullscreen.get_active()
        dark_theme = self.swtDarkTheme.get_active()
        language_prior = language
        if self.cmbLanguage.get_active() == 0:
            language = 'system'
        else:
            language = 'Latin'
        sound = self.swtSound.get_active()
        timer_length = self.spnbtnTimerLength.get_value_as_int()
        keyboard = self.swtKeyboard.get_active()

        # Vocabulary
        if self.togbtnSource.get_active():
            selection = "source"
        if self.togbtnTarget.get_active():
            selection = "target"
        if self.togbtnBoth.get_active():
            selection = "both"
        default_folder = self.filbtnVocabularyFolder.get_filename()
        default_file = self.filbtnVocabularyFile.get_filename()
        if not default_file:
            default_file = ''

        if fullscreen_prior != fullscreen or language_prior != language:
            message_text = _("You have to restart the application to pick up the change.")
            dialog = Gtk.MessageDialog(self.winSettings, 0,
                Gtk.MessageType.INFO, Gtk.ButtonsType.OK, message_text)
            dialog.run()
            dialog.destroy()

        apply_new_settings(True)
        save_config_file()
        self.winSettings.hide()


    def on_winSettings_delete_event(self, widget, event):

        self.winSettings.hide()
        return True
