from telethon import TelegramClient, events

API_ID = 21332425
API_HASH = 'f5d0cddc784e3a7a09ea9714ed01f238'

# 创建客户端并登录
client = TelegramClient('session_name', API_ID, API_HASH)

@client.on(events.NewMessage(from_users='apk4nbot'))
async def handler(event):
    # 打印收到的消息
    print(f'收到消息: {event.message.text}')

# 启动客户端
client.start()
print('登录成功! 正在监听消息...')

# 持续运行直到断开连接
client.run_until_disconnected()
