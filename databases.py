
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    "mysql://root:jil001_!@localhost/shopping?charset=utf8",
    echo=False,
    convert_unicode=True,
    pool_size=30, max_overflow=100
)

db_session = scoped_session(
    sessionmaker(
        autocommit=True,
        autoflush=True,
        bind=engine,
    )
)
Base = declarative_base()
Base.query = db_session.query_property()


def data_insert(data):
    db_session.add(data)
    try:
        db_session.commit()
    except:
        db_session.rollback()