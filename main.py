# Варианты по перемещению курсора
import os  # для запуска сторонних приложений (с операционной системы виндовс)
import win32api  # библиотека для получения информакии о курсоре
import time  # для задержек
import pyautogui  # комп зрение (скрин, и работа с ним)
import random  # рандомные числа (от до)

import win32gui

import confidentially  # мой доп файл для личных данных
import sys  # для завершения выполнения скрипта


def option_1(position_on_x, position_on_y):  # Динамическое прямолинейное
    flag = 0  # флаг для цикла вайл
    a = 0; b = 0  # для различий, повлиял ли пользователь на курсор во время програмного движения по иксу и игрику
    while flag == 0:  # пока флаг равен нулю выполняем цикл
        x, y = win32api.GetCursorPos()  # получаем текущее положение курсора
        if x == position_on_x and y == position_on_y:  # если курсор уже где нужно
            flag += 1  # возвести флаг
        else:  # курсор нужно перемещать
            if x == int(a) and y == int(b):  # пользователь не двигает курсор во время програмного движения
                distance_on_x = position_on_x - x  # дистанция по иксу между сейчас и надо
                distance_on_y = position_on_y - y  # дистанция по игрику между сейчас и надо
                step = ((distance_on_x ** 2) + (distance_on_y ** 2)) ** (1 / 2)  # количество шагов, которыми нужно будет дойти к назначенным координатам
                a += distance_on_x / step  # сместить курсор на один шаг
                b += distance_on_y / step  # сместить курсор на один шаг
                win32api.SetCursorPos((int(a), int(b)))  # установить курсор
            else:  # двинул или начало движения
                a = x; b = y  # если повлиял, или это начало
        # time.sleep(0.001)  # задержка чтобы курсор не слишком быстро двигался


# попробую сделать прогу для запуска приложения
if __name__ == '__main__':  # запуск файла как основной файл

    """Запуск приложения"""
    a1 = 0  # флаг для зацикливания
    while a1 == 0:  # цыкл запуска приложения
        if pyautogui.locateCenterOnScreen('on_of.png'):  # приложение запущено, окно активно, и курсор не над иконкой
            a1 = 1  # выход с цикла
        elif pyautogui.locateCenterOnScreen('on_on.png'):  # приложение запущено, окно активно, и курсор над иконкой
            a1 = 1  # выход с цикла
        elif pyautogui.locateCenterOnScreen('of_on.png'):  # приложение запущено, но окно не активно, и курсор над иконкой
            x, y = pyautogui.locateCenterOnScreen('of_on.png')  # получаем координаты фрагмента для клика
            option_1(random.randint(x - 8, x + 8), random.randint(y - 14, y + 14))  # рандомно расположим курсор в пределах иконки
            pyautogui.click()  # клик ЛКМ
            time.sleep(5)  # задержка 5 сек, чтобы дать появится окну по верх всех
        elif pyautogui.locateCenterOnScreen('of_of.png'):  # приложение запущено, но окно не активно, курсор не над иконкой
            x, y = pyautogui.locateCenterOnScreen('of_of.png')  # получаем координаты фрагмента для клика
            option_1(random.randint(x - 8, x + 8), random.randint(y - 15, y + 15))  # рандомно расположим курсор в пределах иконки
            pyautogui.click()  # клик ЛКМ
            time.sleep(5)  # задержка 5 сек, чтобы дать появится окну по верх всех
        else:  # иконка еще не появилась
            os.system(confidentially.address())  # запустить приложение по адресу
            print("выполнен пуск, ждем 15 сек")
            time.sleep(15)  # задержка 15 сек, чтобы дать появится иконке на панели задачь
    print("приложение запущено и выведено на верх всех остальных окон")

    """Первый ввод данных"""
    a2 = 0  # флаг для зацикливания
    while a2 == 0:  # первый цикл ввода данных
        okno1 = win32gui.FindWindow(None, confidentially.okno1())  # Функция получения хендла по заголовку
        win32gui.SetForegroundWindow(okno1)  # активация окна по хендлу (окно по верх всех окон)
        time.sleep(1)  # задержка 1 сек
        # найти виджет в окне (поле ввода почты и поле ввода пароля)
    sys.exit(0)  # прекратить выполнение скрипта







