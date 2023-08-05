"""Error etc. info dialog."""

import wx

def show_message_dialog(message, msg_type="Info"):
    """General purpose info dialog in GUI mode."""
    # Type can be 'Info', 'Error', 'Question', 'Exclamation'
    dial = wx.MessageDialog(None, message, msg_type, wx.OK)
    dial.ShowModal()
