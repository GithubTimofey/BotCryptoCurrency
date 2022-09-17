import requests
from bs4 import BeautifulSoup
import datetime
import time
from aiogram import types, executor, Dispatcher, Bot

TOKEN = ''
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['help'])
async def help(m: types.Message):
    await bot.send_message(m.chat.id,'''
Список команд:

/start - Вы получаете курс Монет.
/author - Информация о том кто издал.
/help - Выводит Список Команд''')

@dp.message_handler(commands=['author'])
async def author(m: types.Message):
    await bot.send_message(m.chat.id,'''
Этот БОТ был создан 16 апреля 2022.
Тимофеем Корзниковым благодаря сайту coinmarketcap.com.
И сайту www.banki.ru.''')

@dp.message_handler(commands=["start"])
async def start(m: types.Message):
    markupreply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("💲Валюта")
    btn2 = types.KeyboardButton("🪙Монеты")
    btn3 = types.KeyboardButton("👟STEP'N")
    btn4 = types.KeyboardButton('💵Полный Список')
    btn5 = types.KeyboardButton('🏹Сайт')
    btn6 = types.KeyboardButton('🎖️LetMeSpeak')
    btn7 = types.KeyboardButton('🐻Walken')
    markupreply.add(btn1, btn2,btn3,btn4,btn5,btn6,btn7)
    url = 'https://coinmarketcap.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quete = soup.find_all('a',class_='cmc-link')
    await bot.send_message(m.chat.id,'''
Привет *{0.first_name}*! Я КриптоБот. 

*Капитализация рынка: {1} трлн*,
*Доминация Bitcoin:{2}*,
*Всего крипты: {3}*.

А теперь давайте узнаем пoподробнее!'''.format(m.from_user,quete[2].text[:-16:],quete[4].text[4:-11:],quete[0].text),reply_markup=markupreply,parse_mode='Markdown')



    
@dp.message_handler(content_types=['text'])
async def general(message: types.Message):
    if (message.text == '💲Валюта'):
        now1 = time.strftime("%H:%M:%S", time.localtime()) 
        now = datetime.datetime.now()
        #Получаем сколько стоит Евро
        url_eur = 'https://www.banki.ru/products/currency/eur/'
        response_eur = requests.get(url_eur)
        soup_eur = BeautifulSoup(response_eur.text,'lxml')
        quete_eur = soup_eur.find_all('div',class_='currency-table__large-text')

        #Получаем китайский Юяань
        url_cny = 'https://www.banki.ru/products/currency/cny/'
        response_cny = requests.get(url_cny)
        soup_cny = BeautifulSoup(response_cny.text,'lxml')
        quete_cny = soup_cny.find_all('div',class_='currency-table__large-text')

        #Получает сколько стоит Доллар(USD)
        url_usd = 'https://www.banki.ru/products/currency/usd/'
        response_usd = requests.get(url_usd)
        soup_usd = BeautifulSoup(response_usd.text, 'lxml')
        quete_usd = soup_usd.find_all('div',class_='currency-table__large-text')

        await bot.send_message(message.chat.id,text = f'''
*Сегодня: {now.strftime('%d-%m-%Y').replace('-','/')}.
Время: {now1}.
________________

Валюты:
_________________
Доллар: ${quete_usd[0].text}.
Евро: €{quete_eur[0].text}.
Юань: ¥{quete_cny[0].text}*
        ''',parse_mode="Markdown")
    elif (message.text == '🪙Монеты'):
        now1 = time.strftime("%H:%M:%S", time.localtime()) 
        now = datetime.datetime.now()
        #Получаем сколько стоит NEAR
        url_near = 'https://coinmarketcap.com/currencies/near-protocol/'
        response_near = requests.get(url_near)
        soup_near = BeautifulSoup(response_near.text, 'lxml')
        quete_near = soup_near.find_all('div',class_='priceValue')
        for price in quete_near:
            NEAR = price.find('span').text
        
        #Получаем сколько стоит Polkadot
        url_DOT = 'https://coinmarketcap.com/currencies/polkadot-new/'
        response_DOT = requests.get(url_DOT)
        soup_DOT = BeautifulSoup(response_DOT.text, 'lxml')
        quete_DOT = soup_DOT.find_all('div',class_='priceValue')
        for price6 in quete_DOT:
            DOT = price6.find('span').text

        #Получаем стоимость BTC(Bitcoin) Later
        url_BTC = 'https://coinmarketcap.com/currencies/bitcoin/'
        response_BTC = requests.get(url_BTC)
        soup_BTC = BeautifulSoup(response_BTC.text, 'lxml')
        quete_BTC = soup_BTC.find_all('div',class_='priceValue')
        for price1 in quete_BTC:
            BTC = price1.find('span').text

        #Получаем стоимоть ETH Later
        url_ETH = 'https://coinmarketcap.com/currencies/ethereum/'
        response_ETH = requests.get(url_ETH)
        soup_ETH = BeautifulSoup(response_ETH.text, 'lxml')
        quete_ETH = soup_ETH.find_all('div',class_='priceValue')
        for price2 in quete_ETH:
            ETH = price2.find('span').text
        
        #Получаем стоимоть FIL
        url_fil = 'https://coinmarketcap.com/currencies/filecoin/'
        response_fil = requests.get(url_fil)
        soup_fil = BeautifulSoup(response_fil.text, 'lxml')
        quete_fil = soup_fil.find_all('div',class_='priceValue')
        for price7 in quete_fil:
            Filecoin = price7.find('span').text
        
        #Получаем стоимоть Polygon
        url_polygon = 'https://coinmarketcap.com/currencies/polygon/'
        response_polygon = requests.get(url_polygon)
        soup_polygon = BeautifulSoup(response_polygon.text, 'lxml')
        quete_polygon = soup_polygon.find_all('div',class_='priceValue')
        for i4 in quete_polygon:
            Polygon = i4.find('span').text

        #Получаем сколько стоит Cardana
        url_car = 'https://coinmarketcap.com/currencies/cardano/'
        response_car = requests.get(url_car)
        soup_car = BeautifulSoup(response_car.text, 'lxml')
        quete_car = soup_car.find_all('div',class_='priceValue')
        for i2 in quete_car:
            Cardana = i2.find('span').text
        await bot.send_message(message.chat.id,f'''
*Сегодня: {now.strftime('%d-%m-%Y').replace('-','/')}.
Время: {now1}.
________________

Монеты:
_________________

Монета NEAR: {NEAR}.
Монета BTC: {BTC}.
Монета ETH: {ETH}.
Монета Cardano: {Cardana}.
Монета PolkaDOT: {DOT}.
Монета Filecoin: {Filecoin}.
Монета Polygon: {Polygon}.*
''',parse_mode="Markdown")
    elif (message.text == "👟STEP'N"):
        now1 = time.strftime("%H:%M:%S", time.localtime()) 
        now = datetime.datetime.now()
        url_sol = 'https://coinmarketcap.com/currencies/solana/'
        response_sol = requests.get(url_sol)
        soup_sol = BeautifulSoup(response_sol.text, 'lxml')
        quete = soup_sol.find_all('div',class_='priceValue')
        for n in quete:
            SOL = n.find('span').text
        #Получаем сколько стоит GMT
        url_gmt = 'https://coinmarketcap.com/currencies/green-metaverse-token/'
        response_gmt = requests.get(url_gmt)
        soup_gmt = BeautifulSoup(response_gmt.text, 'lxml')
        quete_gmt = soup_gmt.find_all('div',class_='priceValue')
        for i3 in quete_gmt:
            GMT = i3.find('span').text
    
        #Получаем сколько стоит GST
        url_gst = 'https://coinmarketcap.com/currencies/green-satoshi-token/'
        response_gst = requests.get(url_gst)
        soup_gst = BeautifulSoup(response_gst.text, 'lxml')
        quete_gst = soup_gst.find_all('div',class_='priceValue')
        for i4 in quete_gst:
            GST = i4.find('span').text
        
        #Получаем стоимоть BNB
        url_bnb = 'https://coinmarketcap.com/currencies/bnb/'
        response_bnb = requests.get(url_bnb)
        soup_bnb = BeautifulSoup(response_bnb.text, 'lxml')
        quete_bnb = soup_bnb.find_all('div',class_='priceValue')
        for price4 in quete_bnb:
            BNB = price4.find('span').text
        
        url_gst_bsc = 'https://coinmarketcap.com/currencies/green-satoshi-token-bsc/'
        response_gst_bsc = requests.get(url_gst_bsc)
        soup_gst_bsc = BeautifulSoup(response_gst_bsc.text, 'lxml')
        quete_gst_bsc = soup_gst_bsc.find_all('div',class_='priceValue')
        for i4 in quete_gst_bsc:
            GST_BSC = i4.find('span').text
        
        url_gsterc = 'https://coinmarketcap.com/currencies/green-satoshi-token-eth/'
        response_gsterc = requests.get(url_gsterc)
        soup_gsterc = BeautifulSoup(response_gsterc.text, 'lxml')
        quete_gsterc = soup_gsterc.find_all('div',class_='priceValue')
        for gstercvalue in quete_gsterc:
            GSTERC = gstercvalue.find('span').text

        await bot.send_message(message.chat.id,f'''
*Сегодня: {now.strftime('%d-%m-%Y').replace('-','/')}.
Время: {now1}.
________________

Монеты для STEP'N
_________________

Монета SOL: {SOL}.
Монета GMT: {GMT}.
Монетa GST: {GST}.
Монета BNB: {BNB}.
Монета GST(BSC): {GST_BSC}
Монета GST(ERC): {GSTERC} *''',parse_mode="Markdown")
    elif (message.text == '💵Полный Список'):
        now1 = time.strftime("%H:%M:%S", time.localtime()) 
        now = datetime.datetime.now()
        url_sol = 'https://coinmarketcap.com/currencies/solana/'
        response_sol = requests.get(url_sol)
        soup_sol = BeautifulSoup(response_sol.text, 'lxml')
        quete = soup_sol.find_all('div',class_='priceValue')
        for n in quete:
            SOL = n.find('span').text
        
        url_gsterc = 'https://coinmarketcap.com/currencies/green-satoshi-token-eth/'
        response_gsterc = requests.get(url_gsterc)
        soup_gsterc = BeautifulSoup(response_gsterc.text, 'lxml')
        quete_gsterc = soup_gsterc.find_all('div',class_='priceValue')
        for gstercvalue in quete_gsterc:
            GSTERC = gstercvalue.find('span').text

        #Получает сколько стоит Доллар(USD)
        url_usd = 'https://www.banki.ru/products/currency/usd/'
        response_usd = requests.get(url_usd)
        soup_usd = BeautifulSoup(response_usd.text, 'lxml')
        quete_usd = soup_usd.find_all('div',class_='currency-table__large-text')

        #Получаем сколько стоит NEAR
        url_near = 'https://coinmarketcap.com/currencies/near-protocol/'
        response_near = requests.get(url_near)
        soup_near = BeautifulSoup(response_near.text, 'lxml')
        quete_near = soup_near.find_all('div',class_='priceValue')
        for price in quete_near:
            NEAR = price.find('span').text

        #Получаем стоимость BTC(Bitcoin) Later
        url_BTC = 'https://coinmarketcap.com/currencies/bitcoin/'
        response_BTC = requests.get(url_BTC)
        soup_BTC = BeautifulSoup(response_BTC.text, 'lxml')
        quete_BTC = soup_BTC.find_all('div',class_='priceValue')
        for price1 in quete_BTC:
            BTC = price1.find('span').text
        
        #Получаем стоимоть FIL
        url_fil = 'https://coinmarketcap.com/currencies/filecoin/'
        response_fil = requests.get(url_fil)
        soup_fil = BeautifulSoup(response_fil.text, 'lxml')
        quete_fil = soup_fil.find_all('div',class_='priceValue')
        for price7 in quete_fil:
            Filecoin = price7.find('span').text
        
        #Получаем сколько стоит Polkadot
        url_DOT = 'https://coinmarketcap.com/currencies/polkadot-new/'
        response_DOT = requests.get(url_DOT)
        soup_DOT = BeautifulSoup(response_DOT.text, 'lxml')
        quete_DOT = soup_DOT.find_all('div',class_='priceValue')
        for price6 in quete_DOT:
            DOT = price6.find('span').text

        #Получаем стоимоть ETH Later
        url_ETH = 'https://coinmarketcap.com/currencies/ethereum/'
        response_ETH = requests.get(url_ETH)
        soup_ETH = BeautifulSoup(response_ETH.text, 'lxml')
        quete_ETH = soup_ETH.find_all('div',class_='priceValue')
        for price2 in quete_ETH:
            ETH = price2.find('span').text


        #Получаем сколько стоит Евро
        url_eur = 'https://www.banki.ru/products/currency/eur/'
        response_eur = requests.get(url_eur)
        soup_eur = BeautifulSoup(response_eur.text,'lxml')
        quete_eur = soup_eur.find_all('div',class_='currency-table__large-text')

        #Получаем китайский Юяань
        url_cny = 'https://www.banki.ru/products/currency/cny/'
        response_cny = requests.get(url_cny)
        soup_cny = BeautifulSoup(response_cny.text,'lxml')
        quete_cny = soup_cny.find_all('div',class_='currency-table__large-text')

        #Получаем сколько стоит Cardana
        url_car = 'https://coinmarketcap.com/currencies/cardano/'
        response_car = requests.get(url_car)
        soup_car = BeautifulSoup(response_car.text, 'lxml')
        quete_car = soup_car.find_all('div',class_='priceValue')
        for i2 in quete_car:
            Cardana = i2.find('span').text
    
        #Получаем сколько стоит GMT
        url_gmt = 'https://coinmarketcap.com/currencies/green-metaverse-token/'
        response_gmt = requests.get(url_gmt)
        soup_gmt = BeautifulSoup(response_gmt.text, 'lxml')
        quete_gmt = soup_gmt.find_all('div',class_='priceValue')
        for i3 in quete_gmt:
            GMT = i3.find('span').text

        #Получаем сколько стоит GST
        url_gst = 'https://coinmarketcap.com/currencies/green-satoshi-token/'
        response_gst = requests.get(url_gst)
        soup_gst = BeautifulSoup(response_gst.text, 'lxml')
        quete_gst = soup_gst.find_all('div',class_='priceValue')
        for i4 in quete_gst:
            GST = i4.find('span').text

        #Получаем стоимоть BNB
        url_bnb = 'https://coinmarketcap.com/currencies/bnb/'
        response_bnb = requests.get(url_bnb)
        soup_bnb = BeautifulSoup(response_bnb.text, 'lxml')
        quete_bnb = soup_bnb.find_all('div',class_='priceValue')
        for price4 in quete_bnb:
            BNB = price4.find('span').text
        
        url_lstar = 'https://www.coincarp.com/currencies/letmespeak/'
        response_lstar = requests.get(url_lstar)
        soup_lstar = BeautifulSoup(response_lstar.text,'lxml')
        quete_lstar = soup_lstar.find_all('span',class_='h2 mr-2 mb-2 price')


        #Получаем стоимоть Polygon
        url_polygon = 'https://coinmarketcap.com/currencies/polygon/'
        response_polygon = requests.get(url_polygon)
        soup_polygon = BeautifulSoup(response_polygon.text, 'lxml')
        quete_polygon = soup_polygon.find_all('div',class_='priceValue')
        for i4 in quete_polygon:
            Polygon = i4.find('span').text

        #WLKN
        url_wlkn = 'https://coinmarketcap.com/currencies/walken/'
        response_wlkn = requests.get(url_wlkn)
        soup_wlkn = BeautifulSoup(response_wlkn.text, 'lxml')
        quete_wlkn = soup_wlkn.find_all('div',class_='priceValue')
        for i4 in quete_wlkn:
            WLKN = i4.find('span').text

        url_gst_bsc = 'https://coinmarketcap.com/currencies/green-satoshi-token-bsc/'
        response_gst_bsc = requests.get(url_gst_bsc)
        soup_gst_bsc = BeautifulSoup(response_gst_bsc.text, 'lxml')
        quete_gst_bsc = soup_gst_bsc.find_all('div',class_='priceValue')
        for i4 in quete_gst_bsc:
            GST_BSC = i4.find('span').text

        await bot.send_message(message.chat.id,f'''
*Сегодня: {now.strftime('%d-%m-%Y').replace('-','/')}.
Время: {now1}. 

Валюта
___________________________

Доллар: ${quete_usd[0].text}.
Евро: €{quete_eur[0].text}.
Юань: ¥{quete_cny[0].text}

Монеты
_________________________

Монета NEAR: {NEAR}.
Монета BTC: {BTC}.
Монета ETH: {ETH}.
Монета Cardano: {Cardana}.
Монета PolkaDOT: {DOT}.
Монета Filecoin: {Filecoin}.
Монета Polygon: {Polygon}.

For app STEP'N
_________________________

Монета SOL: {SOL}.
Монета GMT: {GMT}.
Монета GST: {GST}.
Монета BNB: {BNB}.
Монета GST(BSC): {GST_BSC}.
Монета GST(ERC): {GSTERC}.

For app LetMeSpeak
_________________________

Монета: LSTAR: {quete_lstar[0].text}

For app Walken
_________________________

Монета WLKN: {WLKN}.
*''',parse_mode="Markdown")
    elif (message.text == '🏹Сайт'):
        await bot.send_message(message.chat.id,'Сайт https://coinmarketcap.com/ Просмотр 🪙Монет')
    elif (message.text == '🎖️LetMeSpeak'):
        now1 = time.strftime("%H:%M:%S", time.localtime()) 
        now = datetime.datetime.now()
        url_lstar = 'https://www.coincarp.com/currencies/letmespeak/'
        response_lstar = requests.get(url_lstar)
        soup_lstar = BeautifulSoup(response_lstar.text,'lxml')
        quete_lstar = soup_lstar.find_all('span',class_='h2 mr-2 mb-2 price')

        await bot.send_message(message.chat.id,f'''
*Сегодня: {now.strftime('%d-%m-%Y').replace('-','/')}.
Время: {now1}.
________________

Монеты для LetMeSpeak
_________________

Монеты LSTAR: {quete_lstar[0].text}*
''',parse_mode="Markdown")



    elif (message.text == '🐻Walken'):
        now1 = time.strftime("%H:%M:%S", time.localtime()) 
        now = datetime.datetime.now()
        url_wlkn = 'https://coinmarketcap.com/currencies/walken/'
        response_wlkn = requests.get(url_wlkn)
        soup_wlkn = BeautifulSoup(response_wlkn.text, 'lxml')
        quete_wlkn = soup_wlkn.find_all('div',class_='priceValue')
        for i4 in quete_wlkn:
            WLKN = i4.find('span').text

        await bot.send_message(message.chat.id,f'''
*Сегодня: {now.strftime('%d-%m-%Y').replace('-','/')}.
Время: {now1}.
________________

Монеты для Walken
_________________

Монета WLKN: {WLKN}*''',parse_mode="Markdown")


def main():
    executor.start_polling(dp)

if __name__ == '__main__':
    main()
