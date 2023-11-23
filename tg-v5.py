from telethon import TelegramClient, events
from telethon.tl.custom import message
from telethon.tl.types import MessageMediaPhoto
import asyncio

api_id = 21965304
api_hash = '726bd7960b0ccaf56010b7204c5369da'

my_channel_id = [-1001837825846, -1001538842585] #айди канала приватки (-1001538842585 это тестовый) 
channels_to = [-1001947945341, -1001908722524] #наш канал (PRIVATE CALLS) + с2

client = TelegramClient('Session', api_id, api_hash, system_version="4.16.30-vxCUSTOM")

print("Resend - Started")

@client.on(events.NewMessage(chats=my_channel_id))
async def my_event_handler(event):
    if event.message:
        for channel_id in channels_to:
            await client.send_message(channel_id, event.message)


client.start()
client.run_until_disconnected()
