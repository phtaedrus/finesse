import process_data

from date import datetime
from sqlalchemy import create_engine, Column, Integer, String, schema
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
ENGINE = create_engine('sqlite:///finesse.db')


class TopAppearances(Base):
    __tablename__ = 'top_appearances'

    id = Column(Integer, primary_key=True)
    url_hash = Column(String, nullable=True)
    post_url = Column(String, nullable=False)
    days_top_hashtag = Column(Integer)


    def __repr__(self):
        return f"TopAppearances->(url_hash={self.url_hash},\
                                  post_url={self.post_url},\
                                  days_top_hashtag={self.days_top_hashtag})"


class PostMetricsAndComments(Base):

    __tablename__ = 'post_metrics_and_comments'

    id = Column(Integer, primary_key=True)
    url_hash = Column(String)
    post_url = Column(String)
    username = Column(String)
    date_posted = Column(DATE)
    img_urls = Column(Text)
    caption = Column(Text, length=None, convert_unicode=True)
    max_likes = Column(Integer)
    max_views = Column(Integer)
    followers_total = Column(Integer)
    following_total = Column(Integer)
    concat_comments = Column(Text, length=None, convert_unicode=True)


    def __repr__(self):
        return f"PostMetricsAndComments->(  url_hash={self.url_hash},\
                                            post_url={self.post_url},\
                                            username={self.username},\
                                            date_posted = {self.date_posted},\
                                            img_urls= {self.img_urls},\
                                            caption = {self.caption},\
                                            max_likes = {self.max_likes},\
                                            max_views = {self.max_views},\
                                            followers_total = {self.followers_total},\
                                            following_total = {self.following_total},\
                                            concat_comments = {self.concat_comments})"

class RawMetrics(Base):

    __tablename__ = 'raw_metrics'

    id = Column(Integer, primary_key=True)
    url_hash = Column(String)
    post_url = Column(String)
    num_like = Column(Integer, nullable=True)
    num_comments = Column(Integer, nullable=True)
    num_views = Column(Integer, nullable= True)
    date_time_collected = Column(TIMESTAMP)


    def __repr__(self):
        return f"RawMetrics->( url_hash={self.url_hash},\
                               post_url={self.post_url},\
                               num_like={self.num_like},\
                               num_comments={self.num_comments},\
                               num_views={self.num_views},\
                               date_time_collected={self.date_time_collected})"

