from database import *
from sqlalchemy.orm import Session
from model import *

def take_topics_through_language_id(language_id: int, db:Session):
    information = db.query(Topic).filter(Topic.language_id==language_id).all()
    if not information:
        return None
    else:
        return information

def take_words_through_topic_or_hardness(hardness:str,topic_id:int,db:Session):
    if hardness is None and topic_id is not None:
        information = db.query(Word_and_topic).filter(Word_and_topic.topic_id == topic_id).all()
    elif hardness is not None and topic_id is None:
        information = db.query(Word).filter(Word.hardness_ranking==hardness).all()
    elif hardness is not None and topic_id is not None:
        information  = db.query(Word).join(Word_and_topic,Word.id==Word_and_topic.word_id).filter(Word.hardness_ranking==hardness,Word_and_topic.topic_id==topic_id).all()
    else:
        return None
    return information

    
