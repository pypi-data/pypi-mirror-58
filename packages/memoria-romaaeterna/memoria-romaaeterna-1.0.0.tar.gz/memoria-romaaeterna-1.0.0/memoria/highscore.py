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

import gettext
import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from settings import HIGHSCORE_FILE, UI_DIR, _


# main functions of high score

def open_highscore_file():

    global highscore_unsorted

    file_data = []
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, 'r', encoding='utf-8') as f:
            file_data = f.read().split("\n")

    highscore_unsorted = {}
    for i in range(len(file_data)):
        try:
            player, score = file_data[i].split(",")
            highscore_unsorted[player] = score
        except ValueError:
            pass

    return list(filter(None, file_data))


def update_highscore_values(winner):

    global highscore_unsorted

    if winner.name in highscore_unsorted.keys():
        score_old = int(highscore_unsorted[winner.name])
        score_new = score_old + 1
        highscore_unsorted[winner.name] = str(score_new)
    else:
        highscore_unsorted[winner.name] = str(1)
    save_highscore_file()


def show_highscore(self):

    self.listHighScore.clear()

    highscore_sorted = sorted(highscore_unsorted.items(), reverse=True, key=lambda x: x[1])
    highscore_range = len(highscore_sorted)
    if highscore_range > 5:
        highscore_range = 5
    for n in range(highscore_range):
        self.listHighScore.append((str(n+1), highscore_sorted[n][0], highscore_sorted[n][1]))

    # modify place of players with equal number of victories
    for n in range(len(self.listHighScore)-1):
        if n != len(self.listHighScore)-1:
            if self.listHighScore[n+1][2] == self.listHighScore[n][2]:
                self.listHighScore[n+1][0] = ""

    self.treeHighScore.set_cursor(Gtk.TreePath(0), self.treecolHighScorePlace, False)


def show_delete_message(self, message_text, delete_all):

    dialog = Gtk.MessageDialog(self.winHighScore, 0,
        Gtk.MessageType.QUESTION, Gtk.ButtonsType.YES_NO, message_text)

    response = dialog.run()
    if response == Gtk.ResponseType.YES:
        delete_highscore_values(self, delete_all)
    dialog.destroy()


def delete_highscore_values(self, delete_all):

    global highscore_unsorted

    if delete_all:
        with open(HIGHSCORE_FILE, 'w', encoding='utf-8') as f:
            f.write("")
        self.listHighScore.clear()
        highscore_unsorted = {}
    else:
        model, treeiter = self.treeHighScore.get_selection().get_selected()
        player_selected = model[treeiter][1]
        self.listHighScore.remove(treeiter)
        highscore_unsorted.pop(player_selected)
        show_highscore(self)
        save_highscore_file()

    if not highscore_unsorted:
        self.lblHighScore.set_text(_("The high score\nis empty."))
        self.lblCongratulations.hide()
        self.treeHighScore.hide()
        self.btnDeleteHighScore.hide()


def save_highscore_file():

    with open(HIGHSCORE_FILE, 'w', encoding='utf-8') as f:
        for player in highscore_unsorted:
            line = player.replace(",","") + "," + highscore_unsorted[player] + "\n"
            f.write(line)


# initialize high score window and manage widgets

class HighScore(Gtk.Window):

    def __init__(self, winGame):

        self.builder = Gtk.Builder()
        self.builder.add_from_file(os.path.join(UI_DIR, 'highscore.ui'))
        self.builder.connect_signals(self)

        for obj in self.builder.get_objects():
            if issubclass(type(obj), Gtk.Buildable):
                name = Gtk.Buildable.get_name(obj)
                setattr(self, name, obj)

        self.winHighScore.set_transient_for(winGame)
        self.winHighScore.show()


    def on_winHighScore_show(self, widget):

        from game import game_over, players_number, winner

        file_data = open_highscore_file()

        # game is finished
        if game_over:
            if file_data:
                if winner.name and players_number > 1:
                    update_highscore_values(winner)
                    player_name = winner.get_colored_player_name()
                    markup = player_name + "\n" + _("won the game!")
                    self.lblHighScore.set_markup(markup)
                    self.lblCongratulations.show()
                elif players_number > 1:
                    self.lblHighScore.set_text(_("The game\nended in a draw!"))
                    self.lblCongratulations.hide()
                else:
                    self.lblHighScore.set_text(_("The game\nis finished!"))
                    self.lblCongratulations.hide()
                show_highscore(self)
                self.treeHighScore.show()
                self.btnDeleteHighScore.show()
            else:
                if winner.name and players_number > 1:
                    update_highscore_values(winner)
                    show_highscore(self)
                    player_name = winner.get_colored_player_name()
                    markup = player_name + "\n" + _("won the game!")
                    self.lblHighScore.set_markup(markup)
                    self.lblCongratulations.show()
                    self.treeHighScore.show()
                    self.btnDeleteHighScore.show()
                elif players_number > 1:
                    self.lblHighScore.set_text(_("The game\nended in a draw!"))
                    self.lblCongratulations.hide()
                    self.treeHighScore.hide()
                    self.btnDeleteHighScore.hide()
                else:
                    self.lblHighScore.set_text(_("The game\nis finished!"))
                    self.lblCongratulations.hide()
                    self.treeHighScore.hide()
                    self.btnDeleteHighScore.hide()

        # menu item "High score" was clicked
        else:
            if file_data:
                show_highscore(self)
                self.lblHighScore.set_text(_("Hall of Fame"))
                self.treeHighScore.show()
                self.btnDeleteHighScore.show()
            else:
                self.lblHighScore.set_text(_("The high score\nis empty."))
                self.treeHighScore.hide()
                self.btnDeleteHighScore.hide()
            self.lblCongratulations.hide()


    def on_btnDeleteHighScore_clicked(self, widget):

        if not Gtk.check_version(3,22,0):
            self.popmenHighScore.popup()
        else:
            self.popmenHighScore.show_all()


    def on_menuDeleteSelectedPlayer_clicked(self, widget):

        message_text = _("Do you want to delete the selected player?")
        show_delete_message(self, message_text, False)


    def on_menuDeleteAllPlayers_clicked(self, widget):

        message_text = _("Do you want to delete the complete high score?")
        show_delete_message(self, message_text, True)


    def on_winHighScore_delete_event(self, widget, event):

        self.winHighScore.hide()
        return True
