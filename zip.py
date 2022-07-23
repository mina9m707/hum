from pyrogram.types import *
from pyrogram.handlers import *
from pyrogram import *
from pyromod import *
import pyromod.listen
import os
from zipfile import ZipFile
bot = Client(
    'x bot',
    api_id="2802662",
    api_hash="b8a41227faa9481313ecfa661ef50ef4",
    bot_token="5372597194:AAEj8WM4k-4Kb81sRyqoyx36dhf6U7aI9Fw"
    )

@bot.on_message(filters.command('start'))
async def start(client, message):
    ast = ReplyKeyboardMarkup([['زیپ فایل🗂️'], ['زیپ ویدیو🎬']],resize_keyboard=True)
    await bot.send_message(message.chat.id, "سلام کاربر گرامی🌀", reply_markup=ast)

@bot.on_message(filters.regex('زیپ فایل🗂️'))
async def zipfile(client, message):
    anb = ReplyKeyboardMarkup([['برگشت🔙']], resize_keyboard=True)
    fzi = await bot.ask(message.chat.id, "فایل خود را ارسال کنید", reply_markup=anb)
    if fzi.text == 'برگشت🔙':
       await start(client, message)
    else:
       await bot.download_media(fzi.document)
       z = ZipFile(f'{fzi.document.file_id}.zip' , 'w')
       z.write(f'downloads/{fzi.document.file_name}')
       z.close()
       await bot.send_document(message.chat.id,f'{fzi.document.file_id}.zip')
       os.remove(f"downloads/{fzi.document.file_name}")
       os.remove(f'{fzi.document.file_id}.zip')
       
       
@bot.on_message(filters.regex('زیپ ویدیو🎬'))
async def zipfile(client, message):
    anb = ReplyKeyboardMarkup([['برگشت🔙']], resize_keyboard=True)
    fzi = await bot.ask(message.chat.id, "فایل خود را ارسال کنید", reply_markup=anb)
    if fzi.text == 'برگشت🔙':
       await start(client, message)
    else:
       await bot.download_media(fzi.video)
       z = ZipFile(f'{fzi.video.file_id}.zip' , 'w')
       z.write(f'downloads/{fzi.video.file_name}')
       z.close()
       await bot.send_document(message.chat.id, f'{fzi.video.file_id}.zip')
       os.remove(f"downloads/{fzi.video.file_name}")
       os.remove(f'{fzi.video.file_id}.zip')
       
@bot.on_message(filters.regex('برگشت🔙'))
async def blk(client, message):
    await start(client, message)

bot.run()