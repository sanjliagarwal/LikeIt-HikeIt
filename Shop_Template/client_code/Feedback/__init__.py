from ._anvil_designer import FeedbackTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

me = anvil.users.get_user(allow_remembered=True)
my_email = me['email']

class Feedback(FeedbackTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.drop_down_feedback.items = [(r['Description_feedback'], r) for r in app_tables.rating_options.search()]

  def send_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    app_tables.feedback.add_row(Feedback_rating=self.drop_down_feedback.selected_value,
                                Comments=self.message_box.text,
                                User_email=my_email)





