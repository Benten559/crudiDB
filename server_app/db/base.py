from .session import Base, engine
from server_app.models.item import Item

# Import all models here for Alembic
def init_db():
    Base.metadata.create_all(bind=engine)
