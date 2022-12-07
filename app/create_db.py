from .database import Base, engine
from models import User, HoldingItem


print('creating database ....')

Base.metadata.create_all(engine)



