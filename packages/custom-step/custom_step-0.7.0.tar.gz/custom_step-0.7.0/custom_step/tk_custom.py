# -*- coding: utf-8 -*-

"""The graphical part of a Custom step"""

import seamm
import custom_step
import pprint  # noqa: F401
import tkinter as tk


class TkCustom(seamm.TkNode):
    """The node_class is the class of the 'real' node that this
    class is the Tk graphics partner for
    """

    node_class = custom_step.Custom

    def __init__(
        self,
        tk_flowchart=None,
        node=None,
        canvas=None,
        x=120,
        y=20,
        w=200,
        h=50
    ):
        '''Initialize a node

        Keyword arguments:
        '''
        self.dialog = None

        super().__init__(
            tk_flowchart=tk_flowchart,
            node=node,
            canvas=canvas,
            x=x,
            y=y,
            w=w,
            h=h
        )

    def create_dialog(self):
        """Create the dialog!"""
        frame = super().create_dialog('Edit Custom Python')

        # Put in the editor window
        textarea = custom_step.TextArea(frame)
        textarea.insert(1.0, self.node.script)
        textarea.pack(expand=tk.YES, fill=tk.BOTH)
        self['textarea'] = textarea

    def right_click(self, event):
        """Probably need to add our dialog...
        """

        super().right_click(event)
        self.popup_menu.add_command(label="Edit..", command=self.edit)

        self.popup_menu.tk_popup(event.x_root, event.y_root, 0)

    def handle_dialog(self, result):
        """Do the right thing when the dialog is closed.
        """
        if result is None or result == 'Cancel':
            self.dialog.deactivate(result)
            self['textarea'].delete(1.0, 'end')
            self['textarea'].insert(1.0, self.node.script)
        elif result == 'Help':
            self.help()
        elif result == 'OK':
            self.dialog.deactivate(result)
            # Capture the parameters from the widgets
            self.node.script = self['textarea'].get(1.0, tk.END)
        else:
            self.dialog.deactivate(result)
            raise RuntimeError(
                "Don't recognize dialog result '{}'".format(result)
            )
