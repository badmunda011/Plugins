from PbxConfig import Config
from PbxConfig import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


def start() -> scoped_session:
    engine = create_engine(postgres://u94bvurcphj34k:p88947d7eef18ddde09311863e892248be33064faa453b5a7792270e9ab27c7c5@c4jpa9p9eiug0j.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d5phr18iooe2k0)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    # this is a dirty way for the work-around required for #23
    print(
        "DATABASE_URL is not configured. Features depending on the database might have issues."
    )
    print(str(e))
