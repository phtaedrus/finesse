
import sqlalchemy

from datetime import date
from sqlalchemy import Column, Integer, String, schema
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Date, Text

Base = declarative_base()
engine = create_engine('sqlite:///finesse_db', echo=False)


class TopAppearances(Base):

    __tablename__ = 'hashtag_top_appearances'

    id = Column(Integer, primary_key=True)
    post_url = Column(String, nullable=False)
    segment_id = Column(String)
    days_top_hashtag = Column("days_in_hashtag_top_section", Integer)


class PostMetricsAndComments(Base):

    __tablename__ = 'post_metrics_and_comments'

    id = Column(Integer, primary_key=True)
    post_url = Column(String)
    segment_id = Column(String)
    username = Column(String)
    date_posted = Column(Date)
    img_urls = Column(Text)
    caption = Column(Text)
    max_likes = Column(Integer)
    max_views = Column(Integer)
    followers_total = Column(Integer)
    following_total = Column(Integer)
    concat_comments = Column(Text)


class RawMetrics(Base):

    __tablename__ = 'raw_post_metrics'

    id = Column(Integer, primary_key=True)
    post_url = Column(String)
    segment_id = Column(String)
    num_like = Column(Integer, nullable=True)
    num_comments = Column(Integer, nullable=True)
    num_views = Column(Integer, nullable= True)
    date_time_collected = Column(Date)

try:
    Base.metadata.create_all(engine)
    print('Database Schema Instantiated')
except sqlalchemy.exc.DatabaseError as db_error:
    print(db_error)





