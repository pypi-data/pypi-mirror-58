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

"""Sections view"""

import tkinter as tk
import tkinter.ttk as ttk
from ._scrollbarview import ScrollbarView


class SectionsView(ScrollbarView):
    """ Aqua Browser Sections View """
    _TAG_PLUGGABLE_TYPE = 'PLUGGABLE_TYPE'
    _TAG_PLUGGABLE = 'PLUGGABLE'
    _TAG_PROBLEMS = 'PROBLEMS'
    _TAG_DEPENDS = 'DEPENDS'
    _TAG_DEPENDENCY = 'DEPENDENCY'

    def __init__(self, controller, parent, **options) -> None:
        super(SectionsView, self).__init__(parent, **options)
        self._controller = controller
        ttk.Style().configure("BrowseSectionsView.Treeview.Heading", font=(None, 12, 'bold'))
        self._tree = ttk.Treeview(self, style='BrowseSectionsView.Treeview', selectmode=tk.BROWSE)
        self._tree.heading('#0', text='Sections')
        self._tree.bind('<<TreeviewSelect>>', self._cb_tree_select)
        self.init_widgets(self._tree)

    def clear(self):
        """ clear view """
        for i in self._tree.get_children():
            self._tree.delete([i])

    def populate(self, algos):
        """ populate view with pluggables  """
        self.clear()
        root_identifier = None
        for pluggable_type, section_types in algos.items():
            identifier = self._tree.insert('',
                                           tk.END,
                                           text=pluggable_type,
                                           values=[''],
                                           tags=SectionsView._TAG_PLUGGABLE_TYPE)
            if root_identifier is None:
                root_identifier = identifier

            child_identifier = None
            for pluggable_name, pluggable_name_values in section_types.items():
                child_identifier = self._tree.insert(identifier,
                                                     tk.END,
                                                     text=pluggable_name,
                                                     values=[pluggable_type],
                                                     tags=SectionsView._TAG_PLUGGABLE)

                problems = pluggable_name_values['problems']
                if problems:
                    self._tree.insert(child_identifier,
                                      tk.END,
                                      text='problems',
                                      values=[pluggable_type, pluggable_name],
                                      tags=SectionsView._TAG_PROBLEMS)

                depends = pluggable_name_values['depends']
                if depends:
                    depends_identifier = self._tree.insert(child_identifier,
                                                           tk.END,
                                                           text='depends',
                                                           values=[pluggable_type, pluggable_name],
                                                           tags=SectionsView._TAG_DEPENDS)
                    for dependency in depends:
                        if 'pluggable_type' in dependency:
                            self._tree.insert(depends_identifier,
                                              tk.END,
                                              text=dependency['pluggable_type'],
                                              values=[pluggable_type, pluggable_name],
                                              tags=SectionsView._TAG_DEPENDENCY)

            if child_identifier is not None:
                self._tree.see(child_identifier)

        if root_identifier is not None:
            self._tree.see(root_identifier)

    def has_selection(self):
        """ check if an entry is selected """
        return self._tree.selection()

    def _cb_tree_select(self, event):
        for item in self._tree.selection():
            item_tag = self._tree.item(item, 'tag')[0]
            if item_tag == SectionsView._TAG_PLUGGABLE_TYPE:
                item_text = self._tree.item(item, 'text')
                self._controller.pluggable_type_select(item_text)
            elif item_tag == SectionsView._TAG_PLUGGABLE:
                item_text = self._tree.item(item, 'text')
                values = self._tree.item(item, 'values')
                self._controller.pluggable_schema_select(values[0], item_text)
            elif item_tag == SectionsView._TAG_PROBLEMS:
                values = self._tree.item(item, 'values')
                self._controller.pluggable_problems_select(values[0], values[1])
            elif item_tag == SectionsView._TAG_DEPENDS:
                values = self._tree.item(item, 'values')
                self._controller.pluggable_depends_select(values[0], values[1])
            elif item_tag == SectionsView._TAG_DEPENDENCY:
                item_text = self._tree.item(item, 'text')
                values = self._tree.item(item, 'values')
                self._controller.pluggable_dependency_select(values[0], values[1], item_text)

            return
