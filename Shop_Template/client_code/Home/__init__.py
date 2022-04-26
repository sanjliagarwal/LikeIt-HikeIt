from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.users
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Shop import Shop
from ..Contact import Contact
from ..About import About
from ..Profile import Profile


class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
#     self.cart_items = []
    
    for link in [self.home_link, self.hike_link, self.profile_link]:
      link.role = ['spaced-title', 'display-none-responsive']
    
  def add_to_cart(self, product, quantity):
    #if item is already in cart, just update the quantity
    for i in self.cart_items:
      if i['product'] == product:
        i['quantity'] += quantity
        break
    else:
      self.cart_items.append({'product': product, 'quantity': quantity})
    
  def navigate(self, active_link, form):
    for i in [self.home_link, self.hike_link, self.profile_link]:
      i.foreground = 'theme:Primary 700'
    active_link.foreground = 'theme:Secondary 500'
    self.column_panel_1.clear()
    self.column_panel_1.add_component(form, full_width_row=True)

  def home_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.navigate(self.home_link, Home())


  def hike_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.navigate(self.hike_link_link, Shop())

  def about_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.navigate(self.about_link, About())
    
  def profile_link_click(self, **event_args):
    """This method is called when the Link is shown on the screen"""
    self.navigate(self.profile_link_link, Contact())

  def cart_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.navigate(self.cart_link, Cart(items=self.cart_items))

  def subscribe_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    email = self.subscribe_textbox.text
    if email:
      anvil.server.call('add_subscriber', email)
      self.subscribe_textbox.text = None
      Notification("Thanks for subscribing!").show()

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def logo_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.navigate(self.logo, About())










