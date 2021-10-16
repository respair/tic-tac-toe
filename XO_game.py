from tkinter import *
import random


class XO:
    # переменная главного окна
    __root = Tk()
    # root.title('tic-tac-toe')
    # индикатор конца/продолжения игры
    __game = True
    # список кнопок
    __field = []
    # количество крестиков на поле
    __cross_count = 0

    def __init__(self):
        self.__root.title('tic-tac-toe')

    def new_game(self):
        for row in range(3):
            for col in range(3):
                self.__field[row][col]['text'] = ' '
                self.__field[row][col]['background'] = 'white'
        self.__game = True
        self.__cross_count = 0
        new_button = Button(self.__root, text='new game', command=self.new_game)
        new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')

    def click(self, row, col):
        if self.__game and self.__field[row][col]['text'] == ' ':
            self.__field[row][col]['text'] = 'X'
            self.__cross_count += 1
            self.check_win('X')
            if self.__game and self.__cross_count < 5:
                self.system_move()

    # проверяет все поле
    def check_win(self, sign):
        for i in range(3):
            self.check_line(self.__field[i][0], self.__field[i][1], self.__field[i][2], sign)
            self.check_line(self.__field[0][i], self.__field[1][i], self.__field[2][i], sign)
        self.check_line(self.__field[0][0], self.__field[1][1], self.__field[2][2], sign)
        self.check_line(self.__field[2][0], self.__field[1][1], self.__field[0][2], sign)

    def check_line(self, el1, el2, el3, sign):
        if el1['text'] == sign and el2['text'] == sign and el3['text'] == sign:
            el1['background'] = el2['background'] = el3['background'] = 'gray'
            self.__game = False
            new_button = Button(self.__root, text='win!!', command=self.new_game)
            new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')

    # система делает 1 ход и выигрывает (приоритет) ИЛИ мешает выйграть игроку за его следующий ход
    def to_win_the_system(self, el1, el2, el3, sign):
        win = False
        if el1['text'] == sign and el2['text'] == sign and el3['text'] == ' ':
            el3['text'] = 'O'
            win = True
            if sign is 'O':
                self.check_line(el1, el2, el3, sign)
        if el1['text'] == sign and el2['text'] == ' ' and el3['text'] == sign:
            el2['text'] = 'O'
            win = True
            if sign is 'O':
                self.check_line(el1, el2, el3, sign)
        if el1['text'] == ' ' and el2['text'] == sign and el3['text'] == sign:
            el1['text'] = 'O'
            win = True
            if sign is 'O':
                self.check_line(el1, el2, el3, sign)
        return win

    def check_to_win(self, sign):
        for i in range(3):
            if self.to_win_the_system(self.__field[i][0], self.__field[i][1], self.__field[i][2], sign):
                return True
            if self.to_win_the_system(self.__field[0][i], self.__field[1][i], self.__field[2][i], sign):
                return True
        if self.to_win_the_system(self.__field[0][0], self.__field[1][1], self.__field[2][2], sign):
            return True
        if self.to_win_the_system(self.__field[2][0], self.__field[1][1], self.__field[0][2], sign):
            return True
        return False

    def system_move(self):
        time = self.check_to_win('O')
        if time is True:
            new_button = Button(self.__root, text='losing:(', command=self.new_game)
            new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
        if time is False:
            time = self.check_to_win('X')
            if time is False:
                # если система не может выйграть и следущий ход игрока не приносит ему победу
                # рандомный ход
                while True:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)
                    if self.__field[row][col]['text'] == ' ':
                        self.__field[row][col]['text'] = 'O'
                        break

    def the_end(self):
        exit()

    def interface(self):
        for row in range(3):
            arr = []
            for col in range(3):
                button = Button(self.__root, text=' ', width=7, height=3,
                                font=(30),
                                background='white',
                                command=lambda row=row, col=col: self.click(row, col))
                button.grid(row=row, column=col, sticky='nsew')
                arr.append(button)
            self.__field.append(arr)
        new_button = Button(self.__root, text='new game', command=self.new_game)
        new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
        new_button2 = Button(self.__root, text='finish game', command=self.the_end)
        new_button2.grid(row=4, column=0, columnspan=3, sticky='nsew')
        self.__root.mainloop()
