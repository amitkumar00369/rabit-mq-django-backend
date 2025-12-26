from asgiref.sync import sync_to_async
import asyncio
from dotenv import load_dotenv

from rabbit.producer import public_message

load_dotenv()
import os

from django.core.cache import cache
async def chatMessageData(userType,message,groupId):
    public_message({'message':message,'userType':userType,'groupId':groupId})

async def liveMessageData(userType)->str:
    message = None
    if userType=="sender":
        message = cache.get(os.getenv('CACHE_NAME_REC'))
    else:
        message = cache.get(os.getenv('CACHE_NAME_SENDER'))
    return message

