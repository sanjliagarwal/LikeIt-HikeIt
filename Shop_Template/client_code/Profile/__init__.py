from ._anvil_designer import ProfileTemplate
from anvil import *
import anvil.users
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import stripe.checkout

class Profile(ProfileTemplate):
  def __init__(self, user, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user = user
    self.name = None
    self.difficulty_level = None
    if not self.difficulty_level:
      self.all_done.enabled = False

  def all_done_click(self, **event_args):
    """This method is called when the button is clicked"""
    row = app_tables.userprofile.add_row(email=self.user['email'],
                                         difficulty_level=self.difficulty_level,
                                         name=self.name)
    open_form('Form1')
    

  def breezy_check_box_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if self.breezy_check_box.checked:
      self.easy_check_box.checked = False
      self.humane_check_box.checked = False
      self.insane_check_box.checked = False
      self.difficulty_level = 1
      self.all_done.enabled = True
    else:
      if not self.difficulty_level:
        self.all_done.enabled = False

  def easy_check_box_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if self.easy_check_box.checked:
      self.humane_check_box.checked = False
      self.insane_check_box.checked = False
      self.breezy_check_box.checked = False
      self.difficulty_level = 3
      self.all_done.enabled = True
    else:
      if not self.difficulty_level:
        self.all_done.enabled = False

  def humane_check_box_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if self.humane_check_box.checked:
      self.insane_check_box.checked = False
      self.breezy_check_box.checked = False
      self.easy_check_box.checked = False
      self.difficulty_level = 5
      self.all_done.enabled = True
    else:
      if not self.difficulty_level:
        self.all_done.enabled = False

  def insane_check_box_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if self.insane_check_box.checked:
      self.breezy_check_box.checked = False
      self.easy_check_box.checked = False
      self.humane_check_box.checked = False
      self.difficulty_level = 7
      self.all_done.enabled = True
    else:
      if not self.difficulty_level:
        self.all_done.enabled = False

  def name_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.name = self.name_text_box.text

