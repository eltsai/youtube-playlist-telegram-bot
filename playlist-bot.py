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
import argparse


token_src = './assets/token'
youtube_API_src = './assets/youtubeAPI'
intro_src = 'assets/intro'
playlist_intro_src = 'assets/playlist-intro'

# load assets
with open(token_src,'r') as token_file:
    token = token_file.read()
with open(youtube_API_src, 'r') as API_file:
    youtube_key = API_file.read()
with open(intro_src, 'r') as intro_file:
    intro = intro_file.read()
with open(playlist_intro_src, 'r') as playlist_intro_file:
    playlist_intro = playlist_intro_file.read()


def start(update, context):
    '''
    Start playlist bot
    '''
    logging.info('Received command massage: start: {'+\
        '\"id\":\"'+str(update.message.chat.id)+'\"}')
    context.bot.send_message(chat_id=update.effective_chat.id, 
    text=intro)


def playlist(update, context):
    '''
    List youtube playlist options
    '''
    logging.info('Received command massage: playlist: {'+\
        '\"id\":\"'+str(update.message.chat.id)+'\"}')
    context.bot.send_message(chat_id=update.effective_chat.id, text=playlist_intro)


def curiosity(update, context):
    '''
    Get playlists info and return a random one video
    '''
    logging.info('Received command massage: curiosity: {'+\
        '\"id\":\"'+str(update.message.chat.id)+'\"}')
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

def astrology(update, context):
    logging.info('Received command massage: astrology: {'+\
        '\"id\":\"'+str(update.message.chat.id)+'\"}')
    youtube = build('youtube', 'v3', developerKey=youtube_key, cache_discovery=False)
    request = youtube.playlistItems().list(
            part='snippet',
            maxResults=100,
            playlistId='PLtDeAt13yqViDj5F1O2MzBWD0s7ISgZFk'
        )
    response = request.execute()
    index = randint(0, len(response['items'])-1)
    context.bot.send_message(chat_id=update.effective_chat.id, text=\
        response['items'][index]['snippet']['title']+'\n'+\
        'https://www.youtube.com/watch?v='+\
        response['items'][index]['snippet']['resourceId']['videoId'])
        
def exurb1a(update, context):
    logging.info('Received command massage: exurb1a: {'+\
        '\"id\":\"'+str(update.message.chat.id)+'\"}')
    youtube = build('youtube', 'v3', developerKey=youtube_key, cache_discovery=False)
    request = youtube.playlistItems().list(
            part='snippet',
            maxResults=100,
            playlistId='PLGT9QN_DA9E9x2K0TKbsHMsQ3kAYLqnrt'
        )
    response = request.execute()
    index = randint(0, len(response['items'])-1)
    context.bot.send_message(chat_id=update.effective_chat.id, text=\
        response['items'][index]['snippet']['title']+'\n'+\
        'https://www.youtube.com/watch?v='+\
        response['items'][index]['snippet']['resourceId']['videoId'])

    
def musicjokes(update, context):
    logging.info('Received command massage: musicjokes: {'+\
        '\"id\":\"'+str(update.message.chat.id)+'\"}')
    youtube = build('youtube', 'v3', developerKey=youtube_key, cache_discovery=False)
    request = youtube.playlistItems().list(
            part='snippet',
            maxResults=100,
            playlistId='PL04aSBdSdgC3IIq97NJGtli0lpyEnHzNA'
        )
    response = request.execute()
    index = randint(0, len(response['items'])-1)
    context.bot.send_message(chat_id=update.effective_chat.id, text=\
        response['items'][index]['snippet']['title']+'\n'+\
        'https://www.youtube.com/watch?v='+\
        response['items'][index]['snippet']['resourceId']['videoId'])
        
def nihilism(update, context):
    logging.info('Received command massage: astrology: {'+\
        '\"id\":\"'+str(update.message.chat.id)+'\"}')
    youtube = build('youtube', 'v3', developerKey=youtube_key, cache_discovery=False)
    request = youtube.playlistItems().list(
            part='snippet',
            maxResults=100,
            playlistId='PLFs4vir_WsTxontcYm5ctqp89cNBJKNrs'
        )
    response = request.execute()
    index = randint(0, len(response['items'])-1)
    context.bot.send_message(chat_id=update.effective_chat.id, text=\
        response['items'][index]['snippet']['title']+'\n'+\
        'https://www.youtube.com/watch?v='+\
        response['items'][index]['snippet']['resourceId']['videoId'])
      
    
def record_noncommand(update, context):
    logging.info('Received non-command massage: {'+\
        '\'id\':\''+str(update.message.chat.id)+'\', '\
        '\'message\':\''+update.message.text+'\'}')


def main():

    # arg parse
    parser = argparse.ArgumentParser(description='A playlist telegram bot.')
    parser.add_argument('-log', action="store", dest="log", help="specify the dest of log file if wanted", default="")
    args = parser.parse_args()
    if args.log == "":
        logging.basicConfig(level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    else:
        logging.basicConfig(filename=args.log,
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # initialize tg bot
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    # run function when prompt matches
    start_handler = CommandHandler('start', start)
    playlist_handler = CommandHandler('playlist', playlist)
    curiosity_handler = CommandHandler('curiosity', curiosity)
    astrology_handler = CommandHandler('astrology', astrology)
    nihilism_handler = CommandHandler('nihilism', nihilism)
    exurb1a_handler = CommandHandler('exurb1a', exurb1a)
    musicjokes_handler = CommandHandler('musicjokes', musicjokes)

    record_noncommand_handler = MessageHandler(Filters.text & (~Filters.command), record_noncommand)

    # register it in the dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(playlist_handler)
    dispatcher.add_handler(curiosity_handler)
    dispatcher.add_handler(astrology_handler)
    dispatcher.add_handler(nihilism_handler)
    dispatcher.add_handler(exurb1a_handler)
    dispatcher.add_handler(musicjokes_handler)

    dispatcher.add_handler(record_noncommand_handler)


    updater.start_polling()

if __name__ == "__main__":
    main()
