from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from wch_Sp import *

engine = create_engine('sqlite:///watches.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete Watchname if exisitng.
session.query(Watchname).delete()
# Delete Watchlist if exisitng.
session.query(Watchlist).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create Users1 data
User1 = User(
    name="Doredla Gayathri", email="gayathridoredla982@gmail.com")
session.add(User1)
session.commit()
print ("Successfully Add First User1")
# Create sample Watchnames
w1 = Watchname(
    name="Fashion Watches",
    user_id=1)
session.add(w1)
session.commit()
w2 = Watchname(
    name="Luxuary Watches", user_id=1)
session.add(w2)
session.commit()
w3 = Watchname(
    name="Italian Design Watches", user_id=1)
session.add(w3)
session.commit()
w4 = Watchname(
    name="Automatic Watches", user_id=1)
session.add(w4)
session.commit()
w5 = Watchname(
    name="Mechanical Watches", user_id=1)
session.add(w5)
session.commit()
print("added")
# Popular Watchnames with modelnames for testing
# Using different users for Watchlist models
list1 = Watchlist(
    modelname="Fastrak",
    description="good leather-strap,mineralglass",
    price="1375",
    rating="4stars",
    color="Brown",
    modelweight="209g",
    modellength="11.9mm",
    modelwidth="24mm",
    date=datetime.datetime.now(),
    watchnameid=1,
    user_id=1)
session.add(list1)
session.commit()
list2 = Watchlist(
    modelname="Casio",
    description="water resistance is good",
    price="4695",
    rating="4stars",
    color="silver",
    modelweight="231g",
    modellength="11.0mm",
    modelwidth="22mm",
    date=datetime.datetime.now(),
    watchnameid=1,
    user_id=1)
session.add(list2)
session.commit()
list3 = Watchlist(
    modelname="Sodial",
    description="It is suitable for hand",
    price="3100",
    rating="3stars",
    color="white",
    modelweight="210g",
    modellength="12mm",
    modelwidth="20mm",
    date=datetime.datetime.now(),
    watchnameid=1,
    user_id=1)
session.add(list3)
session.commit()
list4 = Watchlist(
    modelname="Rolex",
    description="stainless steel",
    price="2300",
    rating="4stars",
    color="gold",
    modelweight="215g",
    modellength="12.2mm",
    modelwidth="21mm",
    date=datetime.datetime.now(),
    watchnameid=2,
    user_id=1)
session.add(list4)
session.commit()
list5 = Watchlist(
    modelname="Fossil",
    description="waterproof",
    price="2350",
    rating="2stars",
    color="white",
    modelweight="218g",
    modellength="11.0mm",
    modelwidth="23mm",
    date=datetime.datetime.now(),
    watchnameid=2,
    user_id=1)
session.add(list5)
session.commit()
list6 = Watchlist(
    modelname="Titan",
    description="display is good",
    price="1900",
    rating="3stars",
    color="black",
    modelweight="220g",
    modellength="11.4mm",
    modelwidth="25mm",
    date=datetime.datetime.now(),
    watchnameid=2,
    user_id=1)
session.add(list6)
session.commit()
list7 = Watchlist(
    modelname="Timex",
    description="batteryresistance is good",
    price="4500",
    rating="4stars",
    color="grey",
    modelweight="240g",
    modellength="11.5mm",
    modelwidth="26mm",
    date=datetime.datetime.now(),
    watchnameid=3,
    user_id=1)
session.add(list7)
session.commit()
list8 = Watchlist(
    modelname="Richclub",
    description="available in less cost",
    price="1300",
    rating="2stars",
    color="red",
    modelweight="230g",
    modellength="11.8mm",
    modelwidth="20mm",
    date=datetime.datetime.now(),
    watchnameid=3,
    user_id=1)
session.add(list8)
session.commit()
list9 = Watchlist(
    modelname="Tedbaker",
    description="length is good",
    price="2300",
    rating="2stars",
    color="blue",
    modelweight="245g",
    modellength="11.6mm",
    modelwidth="22mm",
    date=datetime.datetime.now(),
    watchnameid=3,
    user_id=1)
session.add(list9)
session.commit()
list10 = Watchlist(
    modelname="Apple",
    description="good for hand",
    price="6300",
    rating="4stars",
    color="green",
    modelweight="280g",
    modellength="12.0mm",
    modelwidth="24mm",
    date=datetime.datetime.now(),
    watchnameid=4, user_id=1)
session.add(list10)
session.commit()
list11 = Watchlist(
    modelname="Skagen",
    description="color is suitable",
    price="1800",
    rating="3stars",
    color="white",
    modelweight="200g",
    modellength="12.4mm",
    modelwidth="21mm",
    date=datetime.datetime.now(),
    watchnameid=4,
    user_id=1)
session.add(list11)
session.commit()
list12 = Watchlist(
    modelname="Tommyhillfygur",
    description="good-leather",
    price="1450",
    rating="2stars",
    color="red",
    modelweight="180g",
    modellength="12.5mm",
    modelwidth="23mm",
    date=datetime.datetime.now(),
    watchnameid=4,
    user_id=1)
session.add(list12)
session.commit()
list13 = Watchlist(
    modelname="Diesel",
    description="battery power is good",
    price="2800",
    rating="3stars",
    color="black",
    modelweight="185g",
    modellength="12.6mm",
    modelwidth="25mm",
    date=datetime.datetime.now(),
    watchnameid=5,
    user_id=1)
session.add(list13)
session.commit()
list14 = Watchlist(
    modelname="Armaniexchange",
    description="waterresistance",
    price="850",
    rating="2stars",
    color="blue",
    modelweight="150g",
    modellength="12.8mm",
    modelwidth="26mm",
    date=datetime.datetime.now(),
    watchnameid=5,
    user_id=1)
session.add(list14)
session.commit()
list15 = Watchlist(
    modelname="Michaelkors",
    description="stainlesssteel is provided",
    price="1300",
    rating="3stars",
    color="white",
    modelweight="250g",
    modellength="11.4mm",
    modelwidth="28mm",
    date=datetime.datetime.now(),
    watchnameid=5,
    user_id=1)
session.add(list15)
session.commit()
print("Your watches database has been inserted!")
