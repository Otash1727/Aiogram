import asyncio
from aiogram import Bot,Dispatcher
from .handlers import *
from create_bot import bot,dp 



async def main():
    print('Bot online....')
    dp.include_router(client.router)
    await dp.start_polling(bot,close_bot_session=True) 


    






if __name__=='__main__':
    asyncio.run(main())