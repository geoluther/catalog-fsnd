from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Item, Category, User

engine = create_engine('sqlite:///itemcatalog.db')
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

# Categories

cat1 = Category(name="Classic Keyboards")
session.add(cat1)
session.commit()

Item1 = Item(name = "Yamaha DX7", description = "Classic FM Synthesis", category = cat1)
session.add(Item1)
session.commit()

Item2 = Item(name = "microKORG", description = "Synthesizer + Vocoder", category = cat1)
session.add(Item2)
session.commit()

Item3 = Item(name = "ARP 2600", description = "In your dreams", category = cat1)
session.add(Item3)
session.commit()

Item4 = Item(name = "Roland Jupiter 4", description = "Her name is Rio", category = cat1)
session.add(Item4)
session.commit()

Item5 = Item(name = "Moog Modular", description = "Monophonic Nirvana", category = cat1)
session.add(Item5)
session.commit()

#KEEP ADDING STUFF

## add users here


print "added lots of items and users!"

