import crud

Base = declarative_base()

class Appearances(Base):

     __tablename__ = 'appearances'

     id = Column(Integer, primary_key=True)
     name = Column(String)
     fullname = Column(String)
     nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>"\
               % (self.name, self.fullname, self.nickname)


class CommentFacts(Base):

     __tablename__ = 'comment_facts'

     id = Column(Integer, primary_key=True)
     name = Column(String)
     fullname = Column(String)
     nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>"\
               % (self.name, self.fullname, self.nickname)

class User(Base):

     __tablename__ = 'users'

     id = Column(Integer, primary_key=True)
     name = Column(String)
     fullname = Column(String)
     nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>"\
               % (self.name, self.fullname, self.nickname)

