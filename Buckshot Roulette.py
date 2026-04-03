from random import choice, shuffle, randint
from time import sleep, time
import os
import sys
import msvcrt
import subprocess
import winsound
winsound.PlaySound("before_every_load.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
if "idlelib" in sys.modules:
    subprocess.Popen(['cmd', '/k', 'py', __file__], creationflags=subprocess.CREATE_NEW_CONSOLE)
    sys.exit() 
os.system('')
sys.stdout.write("\x1b]2;Buckshot Roulette\x07")
RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"
def timing():
    start_time = time()
    while True:
        if (time() - start_time) > 20:
            return None
        if msvcrt.kbhit():
            char = msvcrt.getch().decode('cp866').lower()
            if char in ('\x00', '\xe0'):
                msvcrt.getch()
                continue
            return char
        sleep(0.01) 
def clear():
    os.system('cls')
def reload():
    '''Перезарядка дробовика и раздача предметов игрокам. Максимум можно получить 4 предмета, максимум предметов у одного игрока 8'''
    global item1, item2, buck
    buck = choice(buckshot)
    shuffle(buck)
    Print('Перезарядка...')
    sleep(3) #Задержка (для реалистичности)
    Print(f'Новая комбинация: {buck.count(0)} {BLUE}холостых{RESET} и {buck.count(1)} {RED}боевых{RESET}')
    if len(item1) <= 4: #Тут начинаются проверки, т.к. поставлено ограничение в 8 предметов максимум, и если предметов больше 4, то уменьшаем добавление
        item1 += [choice(all_item) for i in range(4)]
        Print('Игрок 1:')
        for i in range(len(item1)): Print(f'{i+1}. {item1[i]}')
    else:
        item1 += [choice(all_item) for i in range(8-len(item1))]
        Print('Игрок 1:')
        for i in range(len(item1)): Print(f'{i+1}. {item1[i]}')
    if len(item2) <= 4:
        item2 += [choice(all_item) for i in range(4)]
        Print('Игрок 2:')
        for i in range(len(item2)): Print(f'{i+1}. {item2[i]}')
    else:
        item2 += [choice(all_item) for i in range(8-len(item2))]
        Print(f'Игрок 2:')
        for i in range(len(item2)): Print(f'{i+1}. {item2[i]}')
    clear()
def Print(text):
    """Выводит текст посимвольно с задержкой"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.02)
    print()
player1 = player2 = 5 #Сделал 1 раунд вместо 3 и всем сделал 5 хп
buckshot = [[0,1],
            [0,0,1],
            [0,0,1,0],
            [0,0,1,1],
            [1,1,1,0,0],
            [1,1,0,0,0],
            [0,0,0,1,1,1],
            [1,1,0,0,0,0],
            [1,1,1,0,0,0,0],
            [1,1,1,1,0,0,0],
            [0,0,0,0,1,1,1,1],
            [1,1,1,0,0,0,0,0]] #Комбинации (1 - боевой, 0 - холостой). Выбираются случайно и перемешиваются
buck = choice(buckshot) #Выбор комбинации.
shuffle(buck) #Перемешивание комбинации
turn = randint(1,2) #Выбор игрока, который ходит первым
x2dmg = 0 #Двойной урон (от ножа)
all_item = ['Сигареты','Лупа','Пиво','Нож','Инвертор', 'Адреналин'] #Все предметы в игре на данный момент
Print(f'Первый ход игрока {turn}.')
Print(f'Начальная комбинация: {buck.count(0)} {BLUE}холостых{RESET} и {buck.count(1)} {RED}боевых{RESET}')
Print('Предметы:')
item1 = [choice(all_item) for i in range(4)] #Выбор предметов для игрока 1
Print('Игрок 1:')
for i in range(len(item1)): Print(f'{i+1}. {item1[i]}')
item2 = [choice(all_item) for i in range(4)] #Выбор предметов для игрока 2
Print('Игрок 2:')
for i in range(len(item2)): Print(f'{i+1}. {item2[i]}')
sleep(1)
clear()
while player1>0 and player2>0:
    sleep(1)
    clear()
    Print(f'Текущее количество зарядов: игрок 1 - {player1}, игрок 2 - {player2}')
    if turn==1:
        pov=False
        Print('Ход игрока 1')
        while True:
            if not buck:
                reload()
            if not pov:
                Print('Выбор:')
                for i in range(len(item1)):
                    if item1[i] == 'Сигареты': Print(f'{i+1}. Сигареты: +1 заряд. {RED}Не действует, если сейчас у игрока 5 зарядов{RESET}')
                    if item1[i] == 'Лупа': Print(f'{i+1}. Лупа: посмотреть текущий патрон')
                    if item1[i] == 'Пиво': Print(f'{i+1}. Пиво: пропустить текущий патрон')
                    if item1[i] == 'Нож': Print(f'{i+1}. Нож: увеличивает урон вдвойне')
                    if item1[i] == 'Инвертор': Print(f'{i+1}. Инвертор: меняет патрон на противоположный')
                    if item1[i] == 'Адреналин': Print(f'{i+1}. Адреналин: забрать любой предмет кроме другого Адреналина и использовать его')
                Print(f'0. Дробовик: противник пропустит ход, если вы выстрелите в себя {BLUE}холостым{RESET}')
            Print('Выберите предмет')
            try:
                choise=int(msvcrt.getch().decode('utf-8'))
            except:
                pov=True
                continue
            if choise>len(item1) or choise<0:
                pov=True
                continue
            pov=False
            if choise==0: #Дробовик
                Print('В противника - 1, в себя - 2, отменить - любая другая клавиша')
                try:
                    answer=int(msvcrt.getch().decode('utf-8'))
                except:
                    pov=True
                    continue
                if answer!=1 and answer!=2:
                    pov=True
                    continue 
                if answer == 1: #В противника (в любом случае переход хода)
                    Print('Вы стреляете в противника...')
                    sleep(3)
                    if buck[0] == 1: #Боевой
                        if x2dmg == 1: #Двойной урон :)
                            if player2==1:
                                player2=0
                            else:
                                player2 -= 2
                        else: player2 -= 1
                        Print(f'Это {RED}боевой{RESET} патрон! У противника осталось {player2} зарядов')
                    else: Print(f'Это {BLUE}холостой{RESET} патрон!')
                    x2dmg=0
                    turn += 1
                    del buck[0]
                    break
                elif answer == 2: #В себя (переход хода только если боевой)
                    Print('Вы стреляете в себя...')
                    sleep(3)
                    if buck[0] == 1:
                        if x2dmg == 1: #Без понятия, кто так будет делать
                            if player1==1:
                                player1=0
                            else:
                                player1 -= 2
                        else: player1 -= 1
                        turn += 1
                        Print(f'Это {RED}боевой{RESET} патрон! У вас осталось {player1} зарядов')
                    else: Print(f'Это {BLUE}холостой{RESET} патрон! Вы ходите еще раз')
                    x2dmg=0
                    del buck[0]
                    break
            elif item1[choise-1] == 'Адреналин':
                if not item2:
                    Print('У противника нет предметов!')
                    del item1[choise-1]
                    clear()
                    continue
                clear()
                Print('Выбор:')
                for i in range(len(item2)):
                    if item2[i] == 'Сигареты': Print(f'{i+1}. Сигареты: +1 заряд. {RED}Не действует, если сейчас у игрока 5 зарядов{RESET}')
                    if item2[i] == 'Лупа': Print(f'{i+1}. Лупа: посмотреть текущий патрон')
                    if item2[i] == 'Пиво': Print(f'{i+1}. Пиво: пропустить текущий патрон')
                    if item2[i] == 'Нож': Print(f'{i+1}. Нож: увеличивает урон вдвойне')
                    if item2[i] == 'Инвертор': Print(f'{i+1}. Инвертор: меняет патрон на противоположный')
                    if item2[i] == 'Адреналин': Print(f'{i+1}. Адреналин: забрать любой предмет кроме другого Адреналина и использовать его {RED}(невозможно забрать!){RESET}')
                while True:
                    Print('Выберите предмет, который хотите забрать')
                    answer=timing()
                    if not answer:
                        Print(f'{RED}Действие андреналина закончилось!{RESET}')
                        del item1[choise-1]
                        break
                    else:
                        try:
                            answer=int(answer)
                        except:
                            continue
                    if answer>len(item2) or answer<=0:
                        continue
                    if item2[answer-1] == 'Адреналин':
                        Print(f'{RED}Невозможно забрать!{RESET}')
                        continue
                    elif item2[answer-1] == 'Сигареты':
                        if player1 == 5:
                            Print(f'Вы использовали сигареты. {RED}Вы не получаете никакого эффекта, потому что у вас максимальное количество зарядов{RESET}')
                        else:
                            player1 += 1
                            Print(f'Вы использовали сигареты. Теперь у вас {player1} зарядов')
                    elif item2[answer-1] == 'Лупа':
                        if buck[0] == 1: Print(f'Вы использовали лупу. Текущий патрон {RED}боевой{RESET}')
                        else: Print(f'Вы использовали лупу. Текущий патрон {BLUE}холостой{RESET}')
                    elif item2[answer-1] == 'Пиво':
                        if buck[0] == 1: Print(f'Вы использовали пиво. Вы пропускаете текущий патрон. Этот патрон {RED}боевой{RESET}')
                        else: Print(f'Вы использовали пиво. Вы пропускаете текущий патрон. Этот патрон {BLUE}холостой{RESET}')
                        del buck[0]
                    elif item2[answer-1] == 'Инвертор':
                        Print('Вы использовали инвертор. Текущий патрон меняется на противоположный')
                        buck[0] = 0 if buck[0] == 1 else 1
                    elif item2[answer-1] == 'Нож':
                        Print(f'Вы использовали нож. {RED}В этот ход дробовик будет наносить x2 урона{RESET}')
                        x2dmg = 1
                    del item2[answer-1]
                    del item1[choise-1]
                    sleep(2)
                    clear()
                    break
                if not buck:
                    reload()
            elif item1[choise-1]=='Сигареты':
                if player1==5:Print(f'Вы использовали сигареты. {RED}Вы не получаете никакого эффекта, потому что у вас максимальное количество зарядов{RESET}')
                else:
                    player1+=1
                    Print(f'Вы использовали сигареты. Теперь у вас {player1} зарядов')
                del item1[choise-1]
            elif item1[choise-1]=='Лупа':
                if buck[0]==1:Print(f'Вы использовали лупу. Текущий патрон {RED}боевой{RESET}')
                else:Print(f'Вы использовали лупу. Текущий патрон {BLUE}холостой{RESET}')
                del item1[choise-1]
            elif item1[choise-1]=='Пиво':
                if buck[0]==1: Print(f'Вы использовали пиво. Вы пропускаете текущий патрон. Этот патрон {RED}боевой{RESET}')
                else: Print(f'Вы использовали пиво. Вы пропускаете текущий патрон. Этот патрон {BLUE}холостой{RESET}')
                del buck[0]
                del item1[choise-1]
            elif item1[choise-1]=='Инвертор':
                Print('Вы использовали инвертор. Текущий патрон меняется на противоположный')
                buck[0]=0 if buck[0]==1 else 1
                del item1[choise-1]
            elif item1[choise-1]=='Нож':
                Print(f'Вы использовали нож. {RED}В этот ход дробовик будет наносить x2 урона{RESET}')
                x2dmg=1
                del item1[choise-1]
            sleep(2)
            clear()
            if not buck:
                reload()
    else:
        #Тут тоже самое. Мне лень сносить все в одну функцию, да и зачем
        Print('Ход игрока 2')
        pov=False
        while True:
            if not buck:
                reload()
            if not pov:
                Print('Выбор:')
                for i in range(len(item2)):
                    if item2[i]=='Сигареты': Print(f'{i+1}. Сигареты: +1 заряд. {RED}Не действует, если сейчас у игрока 5 зарядов{RESET}')
                    if item2[i]=='Лупа': Print(f'{i+1}. Лупа: посмотреть текущий патрон')
                    if item2[i]=='Пиво': Print(f'{i+1}. Пиво: пропустить текущий патрон')
                    if item2[i]=='Нож': Print(f'{i+1}. Нож: увеличивает урон вдвойне')
                    if item2[i]=='Инвертор': Print(f'{i+1}. Инвертор: меняет патрон на противоположный')
                    if item2[i]=='Адреналин': Print(f'{i+1}. Адреналин: забрать любой предмет кроме другого Адреналина и использовать его')
                Print(f'0. Дробовик: противник пропустит ход, если вы выстрелите в себя {BLUE}холостым{RESET}')
            Print('Выберите предмет')
            try:
                choise=int(msvcrt.getch().decode('utf-8'))
            except:
                pov=True
                continue
            if choise>len(item2) or choise<0:
                pov=True
                continue
            if choise==0:
                Print('В противника - 1, в себя - 2, отменить - любая другая клавиша')
                try:
                    answer=int(msvcrt.getch().decode('utf-8'))
                except:
                    pov=True
                    continue
                if answer!=1 and answer!=2:
                    pov=True
                    continue
                if answer==1:
                    Print('Вы стреляете в противника...')
                    sleep(3)
                    if buck[0]==1:
                        if x2dmg==1:
                            if player1==1:
                                player1=0
                            else:
                                player1-=2
                        else: player1-=1
                        Print(f'Это {RED}боевой{RESET} патрон! У противника осталось {player1} зарядов')
                    else: Print(f'Это {BLUE}холостой{RESET} патрон!')
                    x2dmg=0
                    turn-=1
                    del buck[0]
                    break
                elif answer==2:
                    Print('Вы стреляете в себя...')
                    sleep(3)
                    if buck[0]==1:
                        if x2dmg==1:
                            if player2==1:
                                player2=0
                            else:
                                player2-=2
                        else: player2-=1
                        turn-=1
                        Print(f'Это {RED}боевой{RESET} патрон! У вас осталось {player2} зарядов')
                    else: Print(f'Это {BLUE}холостой{RESET} патрон! Вы ходите еще раз')
                    x2dmg=0
                    del buck[0]
                    break
            elif item2[choise-1]=='Адреналин':
                if not item1:
                    Print('У противника нет предметов!')
                    del item2[choise-1]
                    clear()
                    continue
                clear()
                Print('Выбор:')
                for i in range(len(item1)):
                    if item1[i]=='Сигареты': Print(f'{i+1}. Сигареты: +1 заряд. {RED}Не действует, если сейчас у игрока 5 зарядов{RESET}')
                    if item1[i]=='Лупа': Print(f'{i+1}. Лупа: посмотреть текущий патрон')
                    if item1[i]=='Пиво': Print(f'{i+1}. Пиво: пропустить текущий патрон')
                    if item1[i]=='Нож': Print(f'{i+1}. Нож: увеличивает урон вдвойне')
                    if item1[i]=='Инвертор': Print(f'{i+1}. Инвертор: меняет патрон на противоположный')
                    if item1[i]=='Адреналин': Print(f'{i+1}. Адреналин: забрать любой предмет кроме другого Адреналина и использовать его {RED}(невозможно забрать!){RESET}')
                while True:
                    Print('Выберите предмет, который хотите забрать')
                    answer=timing()
                    if not answer:
                        Print(f'{RED}Действие андреналина закончилось!{RESET}')
                        del item2[choise-1]
                        break
                    else:
                        try:
                            answer=int(answer)
                        except:
                            continue
                    if answer>len(item1) or answer<=0:
                        continue
                    if item1[answer-1]=='Адреналин':
                        Print(f'{RED}Невозможно забрать!{RESET}')
                        continue
                    elif item1[answer-1]=='Сигареты':
                        if player2==5: Print(f'Вы использовали сигареты. {RED}Вы не получаете никакого эффекта, потому что у вас максимальное количество зарядов{RESET}')
                        else:
                            player2+=1
                            Print(f'Вы использовали сигареты. Теперь у вас {player2} зарядов')
                    elif item1[answer-1]=='Лупа':
                        if buck[0]==1: Print(f'Вы использовали лупу. Текущий патрон {RED}боевой{RESET}')
                        else: Print(f'Вы использовали лупу. Текущий патрон {BLUE}холостой{RESET}')
                    elif item1[answer-1]=='Пиво':
                        if buck[0]==1: Print(f'Вы использовали пиво. Вы пропускаете текущий патрон. Этот патрон {RED}боевой{RESET}')
                        else: Print(f'Вы использовали пиво. Вы пропускаете текущий патрон. Этот патрон {BLUE}холостой{RESET}')
                        del buck[0]
                    elif item1[answer-1] == 'Инвертор':
                        Print('Вы использовали инвертор. Текущий патрон меняется на противоположный')
                        buck[0]=0 if buck[0]==1 else 1
                    elif item1[answer-1]=='Нож':
                        Print(f'Вы использовали нож. {RED}В этот ход дробовик будет наносить x2 урона{RESET}')
                        x2dmg=1
                    del item2[choise-1]
                    del item1[answer-1]
                    sleep(2)
                    clear()
                    break
                if not buck:
                    reload()
            elif item2[choise-1]=='Сигареты':
                if player2==5: Print(f'Вы использовали сигареты. {RED}Вы не получаете никакого эффекта, потому что у вас максимальное количество зарядов{RESET}')
                else:
                    player2+=1
                    Print(f'Вы использовали сигареты. Теперь у вас {player2} зарядов')
                del item2[choise-1]
            elif item2[choise-1]=='Лупа':
                if buck[0]==1: Print(f'Вы использовали лупу. Текущий патрон {RED}боевой{RESET}')
                else: Print(f'Вы использовали лупу. Текущий патрон {BLUE}холостой{RESET}')
                del item2[choise-1]
            elif item2[choise-1]=='Пиво':
                if buck[0]==1: Print(f'Вы использовали пиво. Вы пропускаете текущий патрон. Этот патрон {RED}боевой{RESET}')
                else: Print(f'Вы использовали пиво. Вы пропускаете текущий патрон. Этот патрон {BLUE}холостой{RESET}')
                del buck[0]
                del item2[choise-1]
            elif item2[choise-1]=='Инвертор':
                Print('Вы использовали инвертор. Текущий патрон меняется на противоположный')
                buck[0]=0 if buck[0]==1 else 1
                del item2[choise-1]
            elif item2[choise-1]=='Нож':
                Print(f'Вы использовали нож. {RED}В этот ход дробовик будет наносить x2 урона{RESET}')
                x2dmg=1
                del item2[choise-1]
            sleep(2)
            clear()
            if not buck:
                reload()
clear()
Print('Игрок 1 победил!') if player1 else Print('Игрок 2 победил!')
sleep(5)
