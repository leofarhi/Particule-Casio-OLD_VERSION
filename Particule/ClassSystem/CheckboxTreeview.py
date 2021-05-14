from tkinter import Tk
from tkinter import ttk
from ttkwidgets import CheckboxTreeview as Tree


class CheckboxTreeview(Tree):

    def item_check(self, item):
        """Check item and propagate the state change to ancestors and descendants."""
        self._check_ancestor(item)
        self._check_descendant(item)

    def item_uncheck(self, item):
        """Uncheck item and propagate the state change to ancestors and descendants."""
        self._uncheck_descendant(item)
        self._uncheck_ancestor(item)