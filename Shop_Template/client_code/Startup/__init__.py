from ._anvil_designer import StartupTemplate
from anvil import *
import anvil.users
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..Profile import Profile

class Startup(StartupTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.banner.role = ['spaced-title', 'left-right-padding']

  def log_in_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.login_with_form()
    self.user = anvil.users.get_user()
    print(f"This user has logged in: {self.user['email']}")
    if not self.check_if_user_profile_exists(self.user['email']):
      open_form('Profile', user=self.user)
    else:
      # TODO: (madhu)
      # open home page directly
      pass
    
  def check_if_user_profile_exists(self, email):
    return app_tables.userprofile.get(email=email)
      