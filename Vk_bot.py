#!/usr/bin/env python
# -*- coding: utf-8 -*-
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import time
from datetime import datetime
import data
import random 
#import func

def get(vk_session, id_group, vk):
    try:
        attachment = ''
        #print ('До всего ' + str(time.ctime(time.time())))
        max_num = vk.wall.get(owner_id = id_group, count = 0) ['count']
        #print("Смотрим время после получения количества всех картинок" + str(time.ctime(time.time())))
        num = random.randint(1, max_num)
        #print("Время до получения пикчи" + str(time.ctime(time.time())))
        walls = vk.wall.get(owner_id = str(id_group), count = 5, offset = num)['items']
        buf = []
        
        elements = str(input(""))
        for element in walls:
            buf.append('wall' + str(id_group) + '_' + str(element['id']))
        attachment = ','.join(buf)
        #print("Время после получения пикчи" + str(time.ctime(time.time())))
        #print (attachment)
        return attachment
    except:
        return get(vk_session, id_group, vk)

login, password = "89817762764","мойботномер1"
vk_session = vk_api.VkApi(login, password, app_id=2685278)
vk_session.auth(token_only = True)
# token = "ЗдесьЕстьВашТокен"
# vk_session = vk_api.VkApi(token=token)
#vk = vk_api.VkApi(token = "f1fff50eefe81bd537dcbb5e49d50c41f81e36c590098e57eef58058458307749819917439f7c4ef2c79f")
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
    #главный цикл
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print ("Что то странное", session_api)
        print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print("Текст сообщения: " + str(event.text))
        print(event.user_id)
        response = event.text.lower()
        if event.from_user and not (event.from_me):
            if response == "привет":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Что это?..', 'random_id': 0})
            elif response == "салам алейкум":
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Ваалейкум салам, брат', 'random_id': 0})
            elif response == "непредсказуемый":
                #name_film = event.text
                post = get(vk_session, -69139588, session_api)
                print("ccылка: ", post)
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Держи, фильм!', 'random_id': 0, "attachment":post})
            else:
                vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Поздаровайся вац!', 'random_id': 0})
    time.sleep(1)
#While True здесь оказался не нужен. Его функцию выполняет for event in longpoll.listen():

   

                              
        
