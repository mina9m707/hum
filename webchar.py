import requests
from bs4 import BeautifulSoup
from pyrogram import *
from pyrogram.handlers import *
from pyrogram.types import *
from pyrogram import client
import pyrogram
import os
import wget
###
bot = Client(
    'x bot',
    api_id="2802662",
    api_hash="b8a41227faa9481313ecfa661ef50ef4",
    bot_token="2019198313:AAHB4hToJYmDoGDH9o-Lc3-Lw8CkC2--15k"
    )

@bot.on_message(filters.command('get'))
async def getone(client, message):
    aa = message.text[4:].strip()
    aaget = aa[:-2].strip("/")
    aagetnum = aa[-2:].strip("/")
    urlone = 'https://xvideos.com/?k={}&p={}'.format(aaget,aagetnum)
    reone = requests.get(urlone)
    html = reone.content
    listone = []
    listtwo = []
    soupone = BeautifulSoup(html, "html.parser")
    for findone in soupone.find_all('div', {'class':'thumb'}):
        for allone in findone.find_all('a', href=True):
            reuone = allone['href']
            listone.append(reuone)
            bb = len(listone)
            for yel in soupone.find_all('img'):
                b = (yel.get('data-src'))
                listtwo.append(b)
    for i in range(1,bb):
        aslone = ("https://xvideos.com{}".format(listone[i]))
        geeet = (listtwo[i])
        filename = wget.download(geeet)
        await bot.send_photo(message.chat.id,photo=filename ,caption="""Video Download Link: {}""".format(aslone))
        os.remove(filename)



# ['Amateur', 'Anal', 'Arab', 'Asian', 'Babe', 'Babysitter', 'BBW', 'Big Ass', 'Big Dick', 'Big Tits', 'Bisexual Male', 'Blonde', 'Blowjob', 'Bondage', 
# 'Brazilian', 'British', 'Bukkake', 'Cartoon', 'College', 'Compilation', 'Cosplay', 'Creampie', 'Cumshot', 'Dp', 'Ebnoy', 'Orgasm', 'Fetish', 'Fingering', 
# 'Fisting', 'Gangbang', 'Gay', 'Handjob', 'Hardcore', 'Hentai', 'Interracial', 'Japanese', 'Lesbian', 'Massage', 'Masturbation', 'Milf', 'Orgy', 'Public', 'Pov', 
# 'Role Play', 'School', 'Squirt', 'Teen', 'Threesome', 'Toys', 'Transgender', 'Webcam']
#
@bot.on_message(filters.command('list'))
async def callstart(client, message):
    textcall = 'Select 👇'
    calll = InlineKeyboardMarkup(
[
        
    [
        InlineKeyboardButton('lesbian', callback_data="lesbian"),
        InlineKeyboardButton('gay', callback_data="gay")
                                                                ],
                                                                [
        InlineKeyboardButton('Hentai', callback_data="Hentai"),
        InlineKeyboardButton('Milf', callback_data="Milf")
                                                                ],
                                                                [
        InlineKeyboardButton('Amateur', callback_data="Amateur"),
        InlineKeyboardButton('Anal', callback_data="Anal")
                                                                ],
                                                                [
        InlineKeyboardButton('Arab', callback_data="Arab"),
        InlineKeyboardButton('Asian', callback_data="Asian")
                                                                ],
                                                                [
        InlineKeyboardButton('Babe', callback_data="Babe"),
        InlineKeyboardButton('Babysitter', callback_data="Babysitter")
                                                                ],
                                                                [
        InlineKeyboardButton('Big Ass', callback_data="Big Ass"),
        InlineKeyboardButton('Big Dick', callback_data="Big Dick")
                                                                ],
                                                                [
        InlineKeyboardButton('Big Tits', callback_data="Big Tits"),
        InlineKeyboardButton('Bisexual Male', callback_data="Bisexual Male")
                                                                ],
                                                                [
        InlineKeyboardButton('Blonde', callback_data="Blonde"),
        InlineKeyboardButton('Blowjob', callback_data="Blowjob")
                                                                ],
                                                                [
        InlineKeyboardButton('Bondage', callback_data="Bondage"),
        InlineKeyboardButton('Cartoon', callback_data="Cartoon")
                                                                ],
                                                                [
        InlineKeyboardButton('College', callback_data="College"),
        InlineKeyboardButton('College', callback_data="College")
                                                                ],
                                                                [
        InlineKeyboardButton('Cumshot', callback_data="Cumshot"),
        InlineKeyboardButton('Dp', callback_data="Dp")
                                                                ],
                                                                [
        InlineKeyboardButton('Orgasm', callback_data="Orgasm"),
        InlineKeyboardButton('Fetish', callback_data="Fetish")
                                                                ],
                                                                [
        InlineKeyboardButton('Fisting', callback_data="Fisting"),
        InlineKeyboardButton('Japanese', callback_data="Japanese")
                                                                ],
                                                                [
        InlineKeyboardButton('Hardcore', callback_data="Hardcore"),
        InlineKeyboardButton('Handjob', callback_data="Handjob")
                                                                ],
                                                                [
        InlineKeyboardButton('Masturbation', callback_data="Masturbation"),
        InlineKeyboardButton('Orgy', callback_data="Orgy")
                                                                ],
                                                                [
        InlineKeyboardButton('Public', callback_data="Public"),
        InlineKeyboardButton('Pov', callback_data="Pov")
                                                                ],
                                                                [
        InlineKeyboardButton('Role Play', callback_data="Role Play"),
        InlineKeyboardButton('School', callback_data="School")
                                                                ],
                                                                [
        InlineKeyboardButton('Teen', callback_data="Teen"),
        InlineKeyboardButton('Webcam', callback_data="Webcam")
                                                                ]
    ])
    await bot.send_message(message.chat.id,text = textcall,reply_markup=calll)

@bot.on_callback_query()
def callback_query(client, CallbackQuery):
    CallbackQuery.edit_message_text(text='OK')
    aa = CallbackQuery.data
    urlone = 'https://xvideos.com/?k={}&p=1'.format(aa)
    reone = requests.get(urlone)
    html = reone.content
    listone = []
    listtwo = []
    soupone = BeautifulSoup(html, "html.parser")
    for findone in soupone.find_all('div', {'class':'thumb'}):
        for allone in findone.find_all('a', href=True):
            reuone = allone['href']
            listone.append(reuone)
            bb = len(listone)
            for yel in soupone.find_all('img'):
                b = (yel.get('data-src'))
                listtwo.append(b)
    for i in range(1,bb):
        aslone = ("https://xvideos.com{}".format(listone[i]))
        geeet = (listtwo[i])
        filename = wget.download(geeet)
        bot.send_photo(CallbackQuery.from_user.id,photo=filename ,caption="""Video Download Link: {}""".format(aslone))
        os.remove(filename)
print("run")
bot.run()