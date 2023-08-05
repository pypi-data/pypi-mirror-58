# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Custom Widgets Collection"""

from sys import platform
import tkinter as tk
import tkinter.ttk as ttk
from ._dialog import Dialog

_BIND = '<Button-2><ButtonRelease-2>' if platform == 'darwin' else '<Button-3><ButtonRelease-3>'
_LINESEP = '\n'


class EntryCustom(ttk.Entry):
    """ entry Custom """
    def __init__(self, *args, **kwargs) -> None:
        super(EntryCustom, self).__init__(*args, **kwargs)
        self.menu = None
        self.bind('<Button-1><ButtonRelease-1>', self._cb_dismiss_menu)
        self.bind_class('Entry', '<Control-a>', self._cb_select_all)
        self.bind(_BIND, self._cb_show_menu)
        self.bind('<<Paste>>', self._cb_paste)

    def _cb_select_all(self, *args):
        if platform == 'darwin':
            self.focus_force()
        self.selection_range(0, tk.END)
        return 'break'

    def _cb_show_menu(self, event):
        _create_menu(self)
        if self.menu:
            self.menu.post(event.x_root, event.y_root)
        if platform == 'darwin':
            self.selection_clear()

    def _cb_dismiss_menu(self, event):
        if self.menu:
            self.menu.unpost()

    def _cb_paste(self, event):
        try:
            self.delete(tk.SEL_FIRST, tk.SEL_LAST)
        except Exception:  # pylint: disable=broad-except
            pass

        try:
            self.insert(tk.INSERT, self.clipboard_get())
        except Exception:  # pylint: disable=broad-except
            pass

        return 'break'


class TextCustom(tk.Text):
    """ Text Custom """
    def __init__(self, *args, **kwargs) -> None:
        super(TextCustom, self).__init__(*args, **kwargs)
        self.menu = None
        self.bind('<Button-1><ButtonRelease-1>', self._cb_dismiss_menu)
        self.bind_class('Text', '<Control-a>', self._cb_select_all)
        self.bind(_BIND, self._cb_show_menu)
        self.bind('<1>', lambda event: self.focus_set())
        self.bind('<<Paste>>', self._cb_paste)

    def _cb_select_all(self, *args):
        # do not select the new line that the text widget automatically adds at the end
        self.tag_add(tk.SEL, 1.0, tk.END + '-1c')
        return 'break'

    def _cb_show_menu(self, event):
        _create_menu(self)
        if self.menu:
            self.menu.post(event.x_root, event.y_root)

    def _cb_dismiss_menu(self, event):
        if self.menu:
            self.menu.unpost()

    def _cb_paste(self, event):
        try:
            self.delete(tk.SEL_FIRST, tk.SEL_LAST)
        except Exception:  # pylint: disable=broad-except
            pass

        try:
            self.insert(tk.INSERT, self.clipboard_get())
        except Exception:  # pylint: disable=broad-except
            pass

        return 'break'


class EntryPopup(EntryCustom):
    """ Entry Popup """
    def __init__(self, controller,
                 section_name, property_name,
                 parent, text, **options) -> None:
        # If relwidth is set, then width is ignored
        super(EntryPopup, self).__init__(parent, **options)
        self._controller = controller
        self._section_name = section_name
        self._property_name = property_name
        self._text = text
        self.insert(0, self._text)
        self.focus_force()
        self.bind("<Unmap>", self._cb_update_value)
        self.bind("<FocusOut>", self._cb_update_value)

    def select_all(self):
        """ select all text """
        self.focus_force()
        self.selection_range(0, tk.END)

    def _cb_update_value(self, *ignore):
        new_text = self.get()
        valid = True
        if self._text != new_text:
            self._text = new_text
            valid = self._controller.cb_property_set(self._section_name,
                                                     self._property_name,
                                                     new_text)
        if valid:
            self.destroy()
        else:
            self.select_all()


class ComboboxPopup(ttk.Combobox):
    """ Combobox Popup """
    def __init__(self, controller, section_name,
                 property_name, parent, **options) -> None:
        self._orig_values = []
        if 'values' in options:
            self._orig_values = options['values']
            options['values'] = ['' if v is None else str(v) for v in self._orig_values]

        super(ComboboxPopup, self).__init__(parent, **options)
        self._controller = controller
        self._section_name = section_name
        self._property_name = property_name
        self.focus_force()
        self.bind("<Unmap>", self._cb_update_value)
        self.bind("<FocusOut>", self._cb_update_value)
        self.bind("<<ComboboxSelected>>", self._cb_select)
        self._text = None

    def _cb_select(self, *ignore):
        new_text = self.get()
        if self._text != new_text:
            self._text = new_text
            selected_index = self.current()
            if selected_index >= 0:
                new_text = self._orig_values[selected_index]
            self._controller.cb_property_set(self._section_name,
                                             self._property_name,
                                             new_text)

    def _cb_update_value(self, *ignore):
        new_text = self.get()
        selected_index = self.current()
        state = self.state()
        combo_state = state[0] if isinstance(state, tuple) and state else None
        if combo_state is None or combo_state != 'pressed':
            self.destroy()

        if self._text != new_text:
            self._text = new_text
            if selected_index >= 0:
                new_text = self._orig_values[selected_index]
            self._controller.cb_property_set(self._section_name,
                                             self._property_name,
                                             new_text)


class TextPopup(ttk.Frame):
    """ Text Popup """
    def __init__(self, controller, section_name,
                 property_name, parent, text, **options) -> None:
        super(TextPopup, self).__init__(parent, **options)
        self._child = TextCustom(self, wrap=tk.NONE, state=tk.NORMAL)
        self._hscrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        self._vscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self._child.config(yscrollcommand=self._vscrollbar.set)
        self._child.config(xscrollcommand=self._hscrollbar.set)
        self._vscrollbar.config(command=self._child.yview)
        self._hscrollbar.config(command=self._child.xview)

        self._hscrollbar.pack(side=tk.BOTTOM, fill=tk.X, expand=tk.FALSE)
        self._vscrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=tk.FALSE)
        self._child.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        self.pack()

        self._controller = controller
        self._section_name = section_name
        self._property_name = property_name
        self._text = text
        if self._text is not None:
            self._child.insert(tk.END, self._text)

        self._child.focus_force()
        self.bind("<Unmap>", self._cb_update_value)
        self.bind("<FocusOut>", self._cb_update_value)

    def select_all(self):
        """ select all text """
        self._child.focus_force()
        # do not select the new line that the text widget automatically adds at the end
        self._child.tag_add(tk.SEL, 1.0, tk.END + '-1c')

    def _cb_update_value(self, *ignore):
        sep_pos = -len(_LINESEP)
        new_text = self._child.get(1.0, tk.END)
        if len(new_text) >= len(_LINESEP) and new_text[sep_pos:] == _LINESEP:
            new_text = new_text[:sep_pos]

        valid = True
        if self._text != new_text:
            self._text = new_text
            valid = self._controller.cb_property_set(self._section_name,
                                                     self._property_name,
                                                     new_text)
        if valid:
            self.destroy()
        else:
            self.select_all()


class PropertyEntryDialog(Dialog):
    """ Property Entry Dialog """
    def __init__(self, controller, section_name, parent) -> None:
        super(PropertyEntryDialog, self).__init__(controller, parent, "New Property")
        self._section_name = section_name
        self.label_text = None
        self.label = None

    def body(self, parent, options):
        ttk.Label(parent,
                  text="Name:",
                  borderwidth=0).grid(padx=7, pady=6, row=0)

        self.entry = EntryCustom(parent, state=tk.NORMAL)
        self.entry.grid(padx=(0, 7), pady=6, row=0, column=1)
        self.label_text = tk.StringVar()
        self.label = ttk.Label(parent, foreground='red',
                               textvariable=self.label_text,
                               borderwidth=0)
        self.label.grid(padx=(7, 7),
                        pady=6,
                        row=1,
                        column=0,
                        columnspan=2)
        self.label.grid_remove()
        return self.entry  # initial focus

    def validate(self):
        self.label.grid_remove()
        self.label_text = self.controller.validate_property_add(self._section_name,
                                                                self.entry.get().strip())
        if self.label_text is None:
            return True

        self.label.grid()
        return False

    def apply(self):
        self.result = self.entry.get()


class PropertyComboDialog(Dialog):
    """ Property Combo Dialog """
    def __init__(self, controller, section_name, parent) -> None:
        super(PropertyComboDialog, self).__init__(controller, parent, 'New Property')
        self._section_name = section_name
        self.label_text = None
        self.label = None

    def body(self, parent, options):
        ttk.Label(parent,
                  text="Name:",
                  borderwidth=0).grid(padx=7, pady=6, row=0)
        self.entry = ttk.Combobox(parent,
                                  exportselection=0,
                                  state='readonly',
                                  values=options['values'])
        self.entry.current(0)
        self.entry.grid(padx=(0, 7), pady=6, row=0, column=1)
        self.label_text = tk.StringVar()
        self.label = ttk.Label(parent, foreground='red',
                               textvariable=self.label_text,
                               borderwidth=0)
        self.label.grid(padx=(7, 7),
                        pady=6,
                        row=1,
                        column=0,
                        columnspan=2)
        self.label.grid_remove()
        return self.entry  # initial focus

    def validate(self):
        self.label.grid_remove()
        self.label_text = self.controller.validate_property_add(self._section_name,
                                                                self.entry.get().strip())
        if self.label_text is None:
            return True

        self.label.grid()
        return False

    def apply(self):
        self.result = self.entry.get()


class SectionComboDialog(Dialog):
    """ Section Combo Dialog """
    def __init__(self, controller, parent) -> None:
        super(SectionComboDialog, self).__init__(controller, parent, "New Section")
        self.label_text = None
        self.label = None

    def body(self, parent, options):
        ttk.Label(parent,
                  text='Name:',
                  borderwidth=0).grid(padx=7,
                                      pady=6,
                                      row=0)
        self.entry = ttk.Combobox(parent,
                                  exportselection=0,
                                  state='readonly',
                                  values=options['sections'])
        self.entry.current(0)
        self.entry.grid(padx=(0, 7), pady=6, row=0, column=1)
        self.label_text = tk.StringVar()
        self.label = ttk.Label(parent, foreground='red',
                               textvariable=self.label_text,
                               borderwidth=0)
        self.label.grid(padx=(7, 7),
                        pady=6,
                        row=1,
                        column=0,
                        columnspan=2)
        self.label.grid_remove()
        return self.entry  # initial focus

    def validate(self):
        self.label.grid_remove()
        self.label_text = self.controller.validate_section_add(self.entry.get().lower().strip())
        if self.label_text is None:
            return True

        self.label.grid()
        return False

    def apply(self):
        self.result = self.entry.get().lower().strip()


def _create_menu(w):
    state = str(w['state'])
    w.menu = tk.Menu(w, tearoff=0)
    if state == tk.NORMAL:
        w.menu.add_command(label='Cut')
    w.menu.add_command(label='Copy')
    if state == tk.NORMAL:
        w.menu.add_command(label='Paste')
    w.menu.add_separator()
    w.menu.add_command(label='Select all')

    if state == tk.NORMAL:
        w.menu.entryconfigure('Cut',
                              command=lambda: w.focus_force() or w.event_generate('<<Cut>>'))
    w.menu.entryconfigure('Copy',
                          command=lambda: w.focus_force() or w.event_generate('<<Copy>>'))
    if state == tk.NORMAL:
        w.menu.entryconfigure('Paste',
                              command=lambda: w.focus_force() or w.event_generate('<<Paste>>'))

    if platform == 'darwin' and isinstance(w, ttk.Entry):
        w.menu.entryconfigure('Select all',
                              command=lambda: w.after(0, w._cb_select_all))
    else:
        w.menu.entryconfigure('Select all',
                              command=lambda: w.focus_force() or w._cb_select_all(None))
