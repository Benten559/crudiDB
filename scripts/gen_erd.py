import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from server_app.db.session import Base
from server_app.models.item import Item
from server_app.core.config import settings
from sqlalchemy_schemadisplay import create_schema_graph
from sqlalchemy_schemadisplay import create_uml_graph

# Database setup
SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Reflect the database
Base.metadata.create_all(engine)

# Generate the ERD
graph = create_schema_graph(
    engine=engine,
    metadata=Base.metadata,
    show_datatypes=True,  # Show datatypes
    show_indexes=True,    # Show index names
    rankdir='LR',         # Left to right direction
    concentrate=False     # If true, multiple edges between same nodes will be merged
)
graph.write_png(f'{settings.PROJECT_NAME}_schema_erd.png')  # Save the ERD as a PNG file
