from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.users
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

me = anvil.users.get_user(allow_remembered=True)
my_email = me['email']
diff_row = app_tables.userprofile.get(email=my_email)
diff_input = diff_row['difficulty_level']

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
    self.drop_down_1.items = [(r['Rating'], r) for r in app_tables.rating_options.search()]
    self.drop_down_2.items = [(r['Rating'], r) for r in app_tables.rating_options.search()]
    self.drop_down_3.items = [(r['Rating'], r) for r in app_tables.rating_options.search()]
    self.drop_down_4.items = [(r['Rating'], r) for r in app_tables.rating_options.search()]
    self.drop_down_5.items = [(r['Rating'], r) for r in app_tables.rating_options.search()]
    infor = anvil.server.call('get_top_5', diff_input)
    self.option01.text = infor[0]
    self.option02.text = infor[1]
    self.option03.text = infor[2]
    self.option04.text = infor[3]
    self.option05.text = infor[4]

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    app_tables.user_ratings.add_row(Difficulty_level=diff_input, 
                                    Rating=self.drop_down_1.selected_value,
                                    Trail_Name=self.option01.text,
                                    User_email=my_email)
    app_tables.user_ratings.add_row(Difficulty_level=diff_input, 
                                    Rating=self.drop_down_2.selected_value,
                                    Trail_Name=self.option02.text,
                                    User_email=my_email)
    app_tables.user_ratings.add_row(Difficulty_level=diff_input, 
                                    Rating=self.drop_down_3.selected_value,
                                    Trail_Name=self.option03.text,
                                    User_email=my_email)
    app_tables.user_ratings.add_row(Difficulty_level=diff_input, 
                                    Rating=self.drop_down_4.selected_value,
                                    Trail_Name=self.option04.text,
                                    User_email=my_email)
    app_tables.user_ratings.add_row(Difficulty_level=diff_input, 
                                    Rating=self.drop_down_5.selected_value,
                                    Trail_Name=self.option05.text,
                                    User_email=my_email)
    open_form('Feedback')