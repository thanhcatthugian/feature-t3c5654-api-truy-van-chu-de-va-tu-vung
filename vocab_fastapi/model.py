from sqlalchemy import Column,String,Integer,ForeignKey,Enum
from database import Base
from sqlalchemy.orm import relationship
class Language(Base):
    __tablename__ = "languages"
    id = Column(Integer,primary_key=True,autoincrement=True)
    language_name = Column(String(255),nullable=False)
    topics = relationship("Topic",back_populates="language")

class Topic(Base):
    __tablename__ = "topics"
    id = Column(Integer,primary_key=True,autoincrement=True)
    topic_name = Column(String(255),nullable=False)
    language_id = Column(Integer,ForeignKey("languages.id"))
    language = relationship("Language",back_populates="topics")
    wts = relationship("Word_and_topic",back_populates="topics")


class Word(Base):
    __tablename__ = "words"
    id = Column(Integer,primary_key=True,autoincrement=True)
    word_name = Column(String(255),nullable=False)
    hardness_ranking = Column(Enum("easy","normal","hard"))
    wts = relationship("Word_and_topic",back_populates="words")

class Word_and_topic(Base):
    __tablename__ = "word_topics"
    id = Column(Integer,primary_key=True,autoincrement=True)
    words = relationship("Word",back_populates="wts")
    topics = relationship("Topic",back_populates="wts")
    word_id = Column(Integer,ForeignKey("words.id"))
    topic_id = Column(Integer,ForeignKey("topics.id"))
