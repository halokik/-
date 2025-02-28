from telethon import TelegramClient, events
import asyncio

API_ID = 21332425
API_HASH = 'f5d0cddc784e3a7a09ea9714ed01f238'

# 创建客户端
client = TelegramClient('user_session', API_ID, API_HASH)

# 设置来源群和目标群
SOURCE_CHANNEL = -1002229433020  # 替换为来源群ID
TARGET_CHANNEL = -1002297134028  # 替换为目标群ID

# 监听相册消息
@client.on(events.Album(chats=[SOURCE_CHANNEL]))
async def handle_album(event):
    # 获取相册中的所有媒体文件
    files = []
    for message in event.messages:
        if message.media:
            files.append(message.media)
    
    # 发送相册
    if files:
        await client.send_file(
            TARGET_CHANNEL,
            files,
            caption=event.text
        )

# 监听普通消息
@client.on(events.NewMessage(chats=[SOURCE_CHANNEL]))
async def handle_message(event):
    message = event.message
    
    # 如果不是相册的一部分
    if not message.grouped_id:
        if message.media:
            await client.send_file(
                TARGET_CHANNEL,
                message.media,
                caption=message.text
            )
        elif message.text:
            await client.send_message(
                TARGET_CHANNEL,
                message.text
            )

# 启动客户端
client.start()
client.run_until_disconnected()
