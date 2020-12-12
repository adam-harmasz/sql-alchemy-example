from speak_and_fly.config import engine
from speak_and_fly.models import Base


def create_tables():
    Base.metadata.create_all(bind=engine)
