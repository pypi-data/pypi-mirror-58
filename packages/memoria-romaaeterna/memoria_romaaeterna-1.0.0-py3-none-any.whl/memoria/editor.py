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

from copy import deepcopy
from collections import defaultdict
from settings import _


# define global variables

unit_names = []
voc_file_path = ''
voc_units = defaultdict(list)
voc_units_orig = defaultdict(list)


# main functions of editor

def open_existing_vocabulary_list(self):

    from list import load_vocabulary_list, get_vocabulary, get_vocabulary_error
    global unit_names, voc_file_path, voc_units, voc_units_orig

    file_accessible = False
    dialog = load_vocabulary_list(self.winEditor)

    response = dialog.run()
    if response == Gtk.ResponseType.ACCEPT:
        voc_file_path = dialog.get_filename()
        secondary_text, voc_units = get_vocabulary(self.listEditorUnits, voc_file_path)
        if secondary_text:
            get_vocabulary_error(voc_file_path, self.winEditor, secondary_text)
            reset_editor(self)
        else:
            file_accessible = True
    dialog.destroy()

    if file_accessible:
        path, file = os.path.split(voc_file_path)
        self.lblEditorFileName.set_text(file)
        self.treeEditorUnits.set_cursor(Gtk.TreePath(0), self.treecolEditorUnits, False)
        treeiter, unit_selected = get_selected_editor_unit(self)
        update_editor_values(self, unit_selected)
        voc_units_orig = deepcopy(voc_units)
        unit_names = []
        for i in range(len(self.listEditorUnits)):
            unit_names.append(self.listEditorUnits[i][2])
        if len(unit_names) > 1:
            self.btnEditorUnitRemove.set_sensitive(True)
        else:
            self.btnEditorUnitRemove.set_sensitive(False)


def check_vocabulary_list_changed(self):

    voc_changed = False
    if voc_units != voc_units_orig:
        voc_changed = True
    return voc_changed


def save_new_vocabulary_list(self):

    from settings import default_folder
    global voc_file_path

    if voc_file_path:
        voc_file_path_backup = voc_file_path
    else:
        voc_file_path_backup = ''

    dialog = Gtk.FileChooserDialog(_("Save Vocabulary List"),
        self.winEditor, Gtk.FileChooserAction.SAVE,
        (_("Cancel"), Gtk.ResponseType.CANCEL, _("Save"), Gtk.ResponseType.ACCEPT))
    dialog.set_current_folder(default_folder)
    dialog.set_do_overwrite_confirmation(True)
    filter_csv = Gtk.FileFilter()
    filter_csv.set_name('CSV')
    filter_csv.add_mime_type('text/csv')
    filter_csv.add_pattern('*.[Cc][Ss][Vv]')
    dialog.add_filter(filter_csv)

    response = dialog.run()
    if response == Gtk.ResponseType.ACCEPT:
        voc_file_path = dialog.get_filename()
        if not voc_file_path[-4:].lower() == '.csv':
            voc_file_path = voc_file_path + '.csv'
        message_text = write_vocabulary(self, voc_file_path)
        if message_text:
            if voc_file_path_backup:
                voc_file_path = voc_file_path_backup
            else:
                voc_file_path = ''
            error_dialog = Gtk.MessageDialog(self.winEditor, 0,
                Gtk.MessageType.ERROR, Gtk.ButtonsType.CLOSE, message_text)
            error_dialog.run()
            error_dialog.destroy()
        else:
            path, file = os.path.split(voc_file_path)
            self.lblEditorFileName.set_text(file)
    dialog.destroy()


def write_vocabulary(self, voc_file_path):

    import re
    global voc_units_orig

    message_text = ""

    try:
        voc_file = open(voc_file_path + '~', 'w', encoding='utf-8')
    except (OSError, PermissionError):
        message_text = _("Could not save vocabulary list: No write permissions.")
        return message_text

    # sort unit names in natural order
    # code adapted from: https://blog.codinghorror.com/sorting-for-humans-natural-sort-order/
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    unit_names.sort(key=alphanum)

    line = ""
    for unit_name in unit_names:
        for i in range(len(voc_units[unit_name])):
            vocable1 = voc_units[unit_name][i][0]
            vocable2 = voc_units[unit_name][i][1]
            if vocable1 and vocable2:
                line = str(unit_name) + "," + vocable1 + "," + vocable2 + "\n"
                voc_file.write(line)
    voc_file.close()

    if not line:
        message_text = _("Could not save vocabulary list: List is empty.")
        os.remove(voc_file_path + '~')
    else:
        voc_units_orig = deepcopy(voc_units)
        os.replace(voc_file_path + '~', voc_file_path)

    return message_text


def get_selected_editor_unit(self):

    global unit_selected

    model, treeiter = self.treeEditorUnits.get_selection().get_selected()
    unit_selected = model[treeiter][2]
    return treeiter, unit_selected


def update_editor_values(self, unit_name):

    self.listEditorVocabulary.clear()
    for voc_pair in voc_units[unit_name]:
        self.listEditorVocabulary.append(voc_pair)
    self.listEditorVocabulary.append(("", ""))
    self.entUnitName.set_text(unit_name)
    check_vocabulary_data(self, "")


def check_vocabulary_data(self, text):

    # check for incomplete vocable pairs
    voc_pair_incomplete = False
    for i in range(len(self.listEditorVocabulary)):
        vocable1 = self.listEditorVocabulary[i][0]
        vocable2 = self.listEditorVocabulary[i][1]
        if (vocable1 and not vocable2) or (vocable2 and not vocable1):
            voc_pair_incomplete = True
    if voc_pair_incomplete:
        tooltip = _("There are incomplete vocable pairs in this unit. They will not be saved!")
        self.imgVocabularyWarning.set_tooltip_text(tooltip)
        self.imgVocabularyWarning.show()
    else:
        self.imgVocabularyWarning.hide()

    # add new empty row, if data is written in last row
    model, treeiter = self.treeEditorVocabulary.get_selection().get_selected()
    if text and not model.iter_next(treeiter):
        self.listEditorVocabulary.append(("", ""))


def reset_editor(self):

    global unit_names, voc_file_path, voc_units, voc_units_orig

    self.listEditorUnits.clear()
    unit_label = _("Unit {}").format("")
    self.listEditorUnits.append((False, unit_label, ""))
    unit_names = [""]
    voc_units = defaultdict(list)
    voc_units_orig = deepcopy(voc_units)

    self.treeEditorUnits.set_cursor(Gtk.TreePath(0), self.treecolEditorUnits, False)
    get_selected_editor_unit(self)
    self.listEditorVocabulary.clear()
    self.listEditorVocabulary.append(("", ""))
    self.entUnitName.set_text("")
    self.entUnitName.set_property("has-focus", True)
    icon_position = Gtk.EntryIconPosition.SECONDARY
    self.entUnitName.set_icon_from_icon_name(icon_position, "dialog-warning-symbolic")
    self.entUnitName.set_icon_activatable(icon_position, False)
    self.entUnitName.set_icon_tooltip_text(icon_position, _("Unit name must not be empty"))
    self.lblEditorFileName.set_text(_("Untitled List"))
    self.btnEditorUnitRemove.set_sensitive(False)
    self.btnEditorUnitAdd.set_sensitive(False)
    self.treeEditorUnits.set_sensitive(False)
    self.treeEditorVocabulary.set_sensitive(False)
    voc_file_path = ''


# initialize editor window and manage widgets

class Editor(Gtk.Window):

    def __init__(self, winGame):

        from settings import UI_DIR

        self.builder = Gtk.Builder()
        self.builder.add_from_file(os.path.join(UI_DIR, 'editor.ui'))
        self.builder.connect_signals(self)

        for obj in self.builder.get_objects():
            if issubclass(type(obj), Gtk.Buildable):
                name = Gtk.Buildable.get_name(obj)
                setattr(self, name, obj)

        self.winEditor.set_transient_for(winGame)
        self.winEditor.show()


    def on_winEditor_show(self, widget):

        reset_editor(self)


    def on_btnEditorOpen_clicked(self, widget):

        voc_changed = check_vocabulary_list_changed(self)

        if voc_changed:
            self.dlgEditor.set_markup(_("Do you want to save the current vocabulary list before opening a new one?"))
            self.btnDialogEditorNoSave.set_label(_("Open"))
            if not voc_file_path:
                self.btnDialogEditorSave.set_label(_("Save as …"))
            else:
                self.btnDialogEditorSave.set_label(_("Save"))
            self.dlgEditor.show()
        else:
            open_existing_vocabulary_list(self)


    def on_btnEditorNew_clicked(self, widget):

        voc_changed = check_vocabulary_list_changed(self)

        if voc_changed:
            self.dlgEditor.set_markup(_("Do you want to save the current vocabulary list before creating a new one?"))
            self.btnDialogEditorNoSave.set_label(_("New"))
            if not voc_file_path:
                self.btnDialogEditorSave.set_label(_("Save as …"))
            else:
                self.btnDialogEditorSave.set_label(_("Save"))
            self.dlgEditor.show()
        else:
            reset_editor(self)


    def on_btnEditorSaveAs_clicked(self, widget):

        save_new_vocabulary_list(self)


    def on_btnEditorSave_clicked(self, widget):

        if not voc_file_path:
            save_new_vocabulary_list(self)
        else:
            message_text = write_vocabulary(self, voc_file_path)
            if message_text:
                error_dialog = Gtk.MessageDialog(self.winEditor, 0,
                    Gtk.MessageType.ERROR, Gtk.ButtonsType.CLOSE, message_text)
                error_dialog.run()
                error_dialog.destroy()


    def on_entUnitName_changed(self, widget):

        self.btnEditorUnitAdd.set_sensitive(False)
        self.treeEditorUnits.set_sensitive(False)
        self.treeEditorVocabulary.set_sensitive(False)

        if widget.get_text():
            unit_name = widget.get_text()
            treeiter, unit_selected = get_selected_editor_unit(self)
            if unit_name == unit_selected:
                icon_name = ""
                icon_activate = False
                icon_tooltip = ""
                self.btnEditorUnitAdd.set_sensitive(True)
                self.treeEditorUnits.set_sensitive(True)
                self.treeEditorVocabulary.set_sensitive(True)
            else:
                if unit_name in unit_names:
                    icon_name = "dialog-warning-symbolic"
                    icon_activate = False
                    icon_tooltip = _("Unit already exists")
                else:
                    icon_name = "go-next-symbolic"
                    icon_activate = True
                    icon_tooltip = _("Name unit")
        else:
            icon_name = "dialog-warning-symbolic"
            icon_activate = False
            icon_tooltip = _("Unit name must not be empty")

        icon_position = Gtk.EntryIconPosition.SECONDARY
        widget.set_icon_from_icon_name(icon_position, icon_name)
        widget.set_icon_activatable(icon_position, icon_activate)
        widget.set_icon_tooltip_text(icon_position, icon_tooltip)


    def on_entUnitName_icon_press(self, widget, icon_position, event):

        global unit_names, voc_units

        treeiter, unit_selected = get_selected_editor_unit(self)
        unit_name = widget.get_text()
        unit_label = _("Unit {}").format(unit_name)
        self.listEditorUnits.set(treeiter, 0, False, 1, unit_label, 2, unit_name)
        self.btnEditorUnitAdd.set_sensitive(True)
        self.treeEditorUnits.set_sensitive(True)
        self.treeEditorVocabulary.set_sensitive(True)

        unit_names.append(unit_name)
        unit_names.remove(unit_selected)
        voc_units[unit_name] = voc_units[unit_selected]
        voc_units.pop(unit_selected)

        icon_position = Gtk.EntryIconPosition.SECONDARY
        widget.set_icon_from_icon_name(icon_position, "")
        widget.set_icon_activatable(icon_position, False)
        widget.set_icon_tooltip_text(icon_position, "")

        # set focus on top left cell of vocabulary tree view when new unit is created
        row, column_object = self.treeEditorVocabulary.get_cursor()
        if not row and len(self.listEditorVocabulary) == 1:
            self.treeEditorVocabulary.set_cursor(0, self.treecolEditorVocable, True)


    def on_entUnitName_key_press_event(self, widget, event):

        # intercept input of , and ;
        if event.keyval == 44 or event.keyval == 59 or event.keyval == 65452:
            event.keyval = 0

        # enter key was pressed
        if event.keyval == 65293 or event.keyval == 65421:
            icon_position = Gtk.EntryIconPosition.SECONDARY
            if not self.entUnitName.get_icon_name(icon_position) == "dialog-warning-symbolic":
                self.on_entUnitName_icon_press(self.entUnitName, icon_position, event)


    def on_btnEditorUnitAdd_clicked(self, widget):

        global unit_names

        model, treeiter = self.treeEditorUnits.get_selection().get_selected()

        unit_names.append("")
        unit_label = _("Unit {}").format("")
        position = int(model.get_string_from_iter(treeiter))+1
        self.listEditorUnits.insert_with_valuesv(position, [0, 1, 2], [False, unit_label, ""])
        self.treeEditorUnits.set_cursor(position, self.treecolEditorUnits, False)
        self.btnEditorUnitRemove.set_sensitive(True)
        self.entUnitName.set_property("has-focus", True)

        update_editor_values(self, "")


    def on_btnEditorUnitRemove_clicked(self, widget):

        global unit_names, voc_units

        treeiter, unit_selected = get_selected_editor_unit(self)

        if voc_units[unit_selected]:
            message_text = _("Do you want to delete unit {}?").format(unit_selected)
            dialog = Gtk.MessageDialog(self.winEditor, 0,
                Gtk.MessageType.QUESTION, Gtk.ButtonsType.YES_NO, message_text)
            response = dialog.run()
            if response == Gtk.ResponseType.YES:
                self.listEditorUnits.remove(treeiter)
                unit_names.remove(unit_selected)
                voc_units.pop(unit_selected)
            dialog.destroy()
        else:
            self.listEditorUnits.remove(treeiter)
            unit_names.remove(unit_selected)
            voc_units.pop(unit_selected)

        treeiter, unit_selected = get_selected_editor_unit(self)
        update_editor_values(self, unit_selected)

        self.treeEditorUnits.set_sensitive(True)
        self.btnEditorUnitAdd.set_sensitive(True)
        if len(self.listEditorUnits) == 1:
            widget.set_sensitive(False)


    def on_treeEditorUnits_row_activated(self, widget, path, column):

        treeiter, unit_selected = get_selected_editor_unit(self)
        update_editor_values(self, unit_selected)


    def on_treeEditorVocabulary_key_release_event(self, widget, event):

        # don't navigate through tree view when new unit was created
        if len(self.listEditorVocabulary) == 1:
            return

        # navigate through tree view with enter and tab key
        if event.keyval == 65293 or event.keyval == 65289:
            # get current row and column
            row, column_object = widget.get_cursor()
            columns = widget.get_columns()
            column_active = columns.index(column_object)
            column_left = columns[0]
            column_right = columns[1]

            if row and column_active == 0:
                # move cursor from left to right column
                widget.set_cursor(row, column_right, True)

            if row and column_active == 1:
                # enter key pressed: move cursor from right to left column in next row
                if event.keyval == 65293:
                    row.next()
                    widget.set_cursor(row, column_left, True)
                # tab key pressed: move cursor from right to left column
                if event.keyval == 65289:
                    widget.set_cursor(row, column_left, True)


    def on_treeEditorVocabulary_focus_out_event(self, widget, event):

        global voc_units

        treeiter, unit_selected = get_selected_editor_unit(self)
        if not unit_selected:
            return

        vocabulary = []
        for i in range(len(self.listEditorVocabulary)):
            vocable1 = self.listEditorVocabulary[i][0].replace(",","").replace(";","")
            vocable2 = self.listEditorVocabulary[i][1].replace(",","").replace(";","")
            if vocable1 or vocable2:
                voc_pair = (vocable1, vocable2)
                vocabulary.append(voc_pair)
        voc_units[unit_selected] = vocabulary


    def on_celltxtEditorVocable_edited(self, renderer, path, text):

        self.listEditorVocabulary[path][0] = text
        check_vocabulary_data(self, text)


    def on_celltxtEditorTranslation_edited(self, renderer, path, text):

        self.listEditorVocabulary[path][1] = text
        check_vocabulary_data(self, text)


    def on_btnDialogEditorCancel_clicked(self, widget):

        self.dlgEditor.hide()


    def on_btnDialogEditorNoSave_clicked(self, widget):

        self.dlgEditor.hide()
        if widget.get_label() == _("Close without Saving"):
            self.winEditor.hide()
        if widget.get_label() == _("New"):
            reset_editor(self)
        if widget.get_label() == _("Open"):
            open_existing_vocabulary_list(self)


    def on_btnDialogEditorSave_clicked(self, widget):

        if not voc_file_path:
            save_new_vocabulary_list(self)
            if voc_file_path:
                self.dlgEditor.hide()
        else:
            message_text = write_vocabulary(self, voc_file_path)
            if message_text:
                error_dialog = Gtk.MessageDialog(self.winEditor, 0,
                    Gtk.MessageType.ERROR, Gtk.ButtonsType.CLOSE, message_text)
                error_dialog.run()
                error_dialog.destroy()
            else:
                self.dlgEditor.hide()
                if self.btnDialogEditorNoSave.get_label() == _("Close without Saving"):
                    self.winEditor.hide()


    def on_winEditor_delete_event(self, widget, event):

        self.on_treeEditorVocabulary_focus_out_event(self.treeEditorVocabulary, None)
        voc_changed = check_vocabulary_list_changed(self)

        if voc_changed:
            self.dlgEditor.set_markup(_("Do you want to save the current vocabulary list before closing?"))
            self.btnDialogEditorNoSave.set_label(_("Close without Saving"))
            if not voc_file_path:
                self.btnDialogEditorSave.set_label(_("Save as …"))
            else:
                self.btnDialogEditorSave.set_label(_("Save"))
            self.dlgEditor.show()
        else:
            self.winEditor.hide()

        return True
