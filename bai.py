from telethon import TelegramClient, events
import asyncio

API_ID = 21332425
API_HASH = 'f5d0cddc784e3a7a09ea9714ed01f238'
BOT_TOKEN = '7258082736:AAEof4V0c7vGL5ZlOboQ-PKjZCuftB4Dzag'  # 替换为你的机器人token

# 创建两个客户端
bot = TelegramClient('bot_session', API_ID, API_HASH)
user = TelegramClient('user_session', API_ID, API_HASH)

# 处理 /start 命令
@bot.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    await event.reply('123')

async def main():
    # 启动机器人
    print('正在启动机器人...')
    await bot.start(bot_token=BOT_TOKEN)
    print('机器人启动成功!')
    
    # 启动用户账号
    print('正在启动用户账号...')
    await user.start()
    print('用户账号启动成功!')
    
    # 发送测试消息给自己
    await user.send_message('me', 'Hello, myself!')
    
    # 同时运行两个客户端
    await asyncio.gather(
        bot.run_until_disconnected(),
        user.run_until_disconnected()
    )

# 运行主程序
asyncio.run(main())
