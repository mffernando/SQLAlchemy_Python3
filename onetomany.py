#One to Many, is used when an instance of a class can be associated with many instances of another class.
#Example: 'Article' class could be associated with many instances of the 'Comment' class.

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    comments = relationship("Comment")

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey('articles.id'))