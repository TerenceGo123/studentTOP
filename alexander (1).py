import tkinter as tk
from settings import *
import random


def click1():
    if len(hand) == 0:
        hand.append(random.choice(cards))
    hand.append(random.choice(cards))
    button['text'] = 'Добавить карту'
    label_2['text'] = hand

def click2():
    button['text'] = 'Начать игру'
    hand.clear()
    


cards = [6, 7, 8, 9, 10, "Валет", "Дама", "Король", "Туз"]

# Превращение слов в списке cards в переменные с числами
Валет = 2
Дама = 3
Король = 4
Туз = 11

# Попытка сумировать числа, находящиеся в списке hand, но не получается)

# print(total)   total - это сумма чисел(очки) в списке 


win = tk.Tk()
win.title('21')
win.geometry(F'{W}x{H}')
win.configure(bg =COLOR_1)

button = tk.Button(text="Начать игру", command=lambda:click1())
button.place(x=110, y=100, width=200, height=100)

button2 = tk.Button(text="Сбросить руку", command=lambda:click2())
button2.place(x=110, y=220, width=200, height=100)

label_1 = tk.Label(text = 'Список карт')
label_1.place(x=150, y=320, width=120, height=70)

label_2 = tk.Label(text=0)
label_2.place(x=150, y=390, width=100, height=40)

label_3 = tk.Label(text = 'Сумма очков' )
label_3.place(x=110, y=430, width=200, height=100)

hand = []
total = 0
for number in hand:
    total += number 
label_4 = tk.Label(text=total)

label_4.place(x=110, y=500, width=200, height=100)


# Проверка на количество очков
if total > 21:
    print('Перебор')
else:
    print('Победа')

win.mainloop()








