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

import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from collections import defaultdict
from settings import _


# main functions for loading vocabulary list
# shared by options popover and editor window

def load_vocabulary_list(parent_window):

    from settings import default_folder

    dialog = Gtk.FileChooserDialog(_("Load Vocabulary List"),
        parent_window, Gtk.FileChooserAction.OPEN,
        (_("Cancel"), Gtk.ResponseType.CANCEL, _("Open"), Gtk.ResponseType.ACCEPT))
    dialog.set_current_folder(default_folder)
    filter_csv = Gtk.FileFilter()
    filter_csv.set_name('CSV')
    filter_csv.add_mime_type('text/csv')
    filter_csv.add_pattern('*.[Cc][Ss][Vv]')
    filter_txt = Gtk.FileFilter()
    filter_txt.set_name('Text')
    filter_txt.add_mime_type('text/plain')
    filter_txt.add_pattern('*.[Tt][Xx][Tt]')
    dialog.add_filter(filter_csv)
    dialog.add_filter(filter_txt)

    return dialog


def get_vocabulary(list_store, voc_file_path):

    voc_all = []
    voc_units = defaultdict(list)
    list_store.clear()

    try:
        voc_file = open(voc_file_path, 'r', encoding='utf-8')
    except IOError:
        secondary_text = _("The file could not be opened.")
        return secondary_text, voc_units

    voc_rows = voc_file.read().split("\n")
    voc_file.close()

    for i in range(len(voc_rows)-1):
        voc_columns = voc_rows[i].replace(";",",").replace("\t",",").split(",")
        try:
            if voc_columns[0] and voc_columns[1] and voc_columns[2]:
                voc_all.append(voc_columns)
        except IndexError:
            pass
    if not voc_all:
        secondary_text = _("The data has to be separated by comma, semicolon or tab.")
        return secondary_text, voc_units

    unit_names = []
    for i in range(len(voc_all)):
        if not voc_all[i][0] in unit_names:
            unit_names.append(voc_all[i][0])
            unit_names.sort()
            unit_label = _("Unit {}").format(voc_all[i][0])
            unit_data = (False, unit_label, voc_all[i][0])
            list_store.append(unit_data)

    for unit_name in unit_names:
        for i in range(len(voc_all)):
            if unit_name == voc_all[i][0]:
                voc_units[unit_name].append(tuple(voc_all[i][1:3]))

    if not len(list_store):
        secondary_text = _("The data structure has to be: [unit],[vocable],[translation].")
        return secondary_text, voc_units

    secondary_text = ""
    return secondary_text, voc_units


def get_vocabulary_error(voc_file_path, parent_window, secondary_text):

    path, file = os.path.split(voc_file_path)
    message_text = _("Vocabulary list '{}' could not be loaded!").format(file)
    error_dialog = Gtk.MessageDialog(parent_window, 0,
        Gtk.MessageType.ERROR, Gtk.ButtonsType.CLOSE, message_text)
    error_dialog.format_secondary_text(secondary_text)
    error_dialog.run()
    error_dialog.destroy()
