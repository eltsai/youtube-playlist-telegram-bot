#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#__author__ = 'eltsai'

'''
A benign tg bot that returns youtube videos upon request
'''

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
from googleapiclient.discovery import build

from random import randint
import json
import logging

token_src = './assets/token'
youtube_API_src = './assets/youtubeAPI'
intro_src = 'assets/intro'
logs_dir = './logs/'


with open(token_src,'r') as tokenfile:
    token = tokenfile.read()
with open(youtube_API_src, 'r') as APIfile:
    youtube_key = APIfile.read()
with open(intro_src, 'r') as introfile:
    intro = introfile.read()
    

playlist_name_list =[
    'curiosity',
    ]

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(filename=logs_dir+'test.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def start(update, context):
    '''
    Start playlist bot
    '''
    logging.info('Received command massage: start: {'+\
        '\'username\':\''+update.message.chat.username+'\', '\
        '\'message\':\''+update.message.text+'\'}')
    context.bot.send_message(chat_id=update.effective_chat.id, 
    text=intro)


def playlist(update, context):
    '''
    List youtube playlist optionsS
    '''
    logging.info('Received command massage: playlist: {'+\
        '\'username\':\''+update.message.chat.username+'\', '\
        '\'message\':\''+update.message.text+'\'}')
    context.bot.send_message(chat_id=update.effective_chat.id, text=
    'In a mood for a video? Choose your playlist:\n'+\
    '> /curiosity - Random knowledge')


def curiosity(update, context):
    '''
    Get Playlist and return a random one from it
    '''
    logging.info('Received command massage: curiosity: {'+\
        '\'username\':\''+update.message.chat.username+'\', '\
        '\'message\':\''+update.message.text+'\'}')
    youtube = build('youtube', 'v3', developerKey=youtube_key, cache_discovery=False)
    request = youtube.playlistItems().list(
            part='snippet',
            maxResults=100,
            playlistId='PLtDeAt13yqVig-8QGSqOQB-3VA2BB-kkh'
        )
    response = request.execute()
    index = randint(0, len(response['items'])-1)
    context.bot.send_message(chat_id=update.effective_chat.id, text=\
        response['items'][index]['snippet']['title']+'\n'+\
        'https://www.youtube.com/watch?v='+\
        response['items'][index]['snippet']['resourceId']['videoId'])
    
def record_noncommand(update, context):
    logging.info('Received non-command massage: {'+\
        '\'username\':\''+update.message.chat.username+'\', '\
        '\'message\':\''+update.message.text+'\'}')
    #print(update)
    

# run function when prompt matches
start_handler = CommandHandler('start', start)
playlist_handler = CommandHandler('playlist', playlist)
curiosity_handler = CommandHandler('curiosity', curiosity)

record_noncommand_handler = MessageHandler(Filters.text & (~Filters.command), record_noncommand)

# register it in the dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(playlist_handler)
dispatcher.add_handler(curiosity_handler)

dispatcher.add_handler(record_noncommand_handler)


updater.start_polling()