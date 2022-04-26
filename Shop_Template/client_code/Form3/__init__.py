from ._anvil_designer import Form3Template
from anvil import *
import anvil.server
import anvil.users
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.drop_down_1_dd.items = [(r['Location'], r) for r in app_tables.location_options.search()]
    self.drop_down_2_dd.items = [(r['Radius'], r) for r in app_tables.radius_options.search()]


  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    app_tables.hardfilters.add_row(location=self.drop_down_1_dd.selected_value, radius=self.drop_down_2_dd.selected_value, user_id=my_email)
    pass

