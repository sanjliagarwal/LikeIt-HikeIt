import anvil.users
import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
import stripe
import anvil.email
import pandas as pd
import anvil.media
from io import BytesIO


@anvil.server.callable
def LoadOffshoreAssets(file):
    print ("Hi")
    my_bytes=file.get_bytes()
    #print (my_bytes)
    df = pd.read_csv(BytesIO(my_bytes))
    #print(df)
    df = df.replace({pd.np.nan: None})
    
    for d in df.to_dict(orient="records"):
      print (d)
      app_tables.location_options.add_row(**d)
    
    print(df.to_dict())
    
    



    

@anvil.server.callable
def add_message(name, email, message):
  app_tables.contact.add_row(name=name, email=email, message=message, date=datetime.now())
  anvil.email.send(from_name="Contact Form", 
                   subject="New Web Contact",
                   text=f"New web contact from {name} ({email})\nMessage: {message}")
  
@anvil.server.callable

def add_subscriber(email):
  app_tables.subscribers.add_row(email=email)
  
@anvil.server.callable
def add_order(charge_id, cart_items):
  app_tables.orders.add_row(charge_id=charge_id, order=cart_items)
  
@anvil.server.callable
def ensure_user():
  me = anvil.users.get_user()
  if me is None:
    raise Exception('Not logged in')
  return me

