from bs4 import BeautifulSoup
import re
import time
import requests


def getRating(review):
    
    rating='NA'
    ratingChunk=review.find('div', {'class':re.compile('rotten')})
    if not ratingChunk:
        ratingChunk= ratingChunk=review.find('div', {'class':re.compile('fresh')})
        if not ratingChunk:
            rating ='NA'
        else: rating='fresh'
    else: rating='rotten'
    
    return rating 

def getCritic(review):
    
    critic='NA' # initialize critic and text 
    criticChunk=review.find('a',{'href':re.compile('/critic/')})
    if criticChunk: 
        critic=criticChunk.text#.encode('ascii','ignore')
    
    return critic

        
def getSource(review):
    
    source='NA'
    sourceChunk=review.find('em', {'class':'subtle'})
    if sourceChunk: source=sourceChunk.text
    
    return source
    

def getDate(review):
    
    date='NA'
    dateChunk=review.find('div', {'class':re.compile('review_date')})
    if dateChunk: date=dateChunk.text
    
    return date


def getTextLen(review):
    
    text='NA'
    textChunk=review.find('div',{'class':'the_review'})
    if textChunk: text=textChunk.text
    
    return len(text)
