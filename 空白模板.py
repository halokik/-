from telethon import TelegramClient

API_ID = 21332425
API_HASH = 'f5d0cddc784e3a7a09ea9714ed01f238'

client = TelegramClient('session_name',API_ID,API_HASH)

client.start()
