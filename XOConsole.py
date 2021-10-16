"""tic-tac-toe plus some useful function"""
import sys


def get_input(text):
    """input function made for good testing"""
    return input(text)


class XOConsole:
    """tic-tac-toe"""

    def __init__(self):
        self.board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.sign = 'X'

    def new_game(self):
        """start a new game or end it"""
        answer = get_input("Хотите начать игру заново? Введите 'yes' или 'no'")
        try:
            if not answer:
                raise ValueError('empty input')
            if not isinstance(answer, str):
                raise ValueError('incorrect input')
        except ValueError:
            print("Некорректный ответ: игра завершается..")
            sys.exit()
        if answer == "yes":
            self.board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            self.sign = 'X'
            self.main()
        else:
            print("Спасибо за игру!")
            sys.exit()

    def draw_board(self):
        """draw the field for the game"""
        print("-" * 13)
        for i in range(3):
            print("|", self.board[0 + i * 3], "|", self.board[1 + i * 3], "|",
                  self.board[2 + i * 3], "|")
            print("-" * 13)

    def check_win(self):
        """check for the current player's win or a draw"""
        for i in range(3):
            if self.board[0 + i * 3] == self.sign and self.board[1 + i * 3] == self.sign and \
                    self.board[2 + i * 3] == self.sign:
                print(self.sign + " is WINNER!")
                self.new_game()
        for i in range(3):
            if self.board[i] == self.sign and self.board[i + 3] == self.sign and \
                    self.board[i + 6] == self.sign:
                print(self.sign + " is WINNER!")
                self.new_game()
        if self.board[0] == self.sign and self.board[4] == self.sign and self.board[8] == self.sign:
            print(self.sign + " is WINNER!")
            self.new_game()
        if self.board[2] == self.sign and self.board[4] == self.sign and self.board[6] == self.sign:
            print(self.sign + " is WINNER!")
            self.new_game()
        count_x = 0
        for i in range(9):
            if self.board[i] == 'X':
                count_x += 1
        if count_x == 5:
            print("НИЧЬЯ!")
            self.new_game()

    def move(self):
        """player turn"""
        start = 0
        while start == 0:
            string_input = "куда поставите " + self.sign + "? "
            value = get_input(string_input)
            try:
                if not value:
                    raise ValueError('empty input')
                if (int(value) < 1) or (int(value) > 9):
                    raise ValueError('incorrect input')
                if (int(value) > 0) or (int(value) < 10):
                    start = 1
            except ValueError:
                print("Некорректный ввод: введите номер клетки.")
            if start == 1:
                if self.board[int(value) - 1] == 'X' or self.board[int(value) - 1] == 'O':
                    print("Эта клетка уже занята!")
                    start = 0
                else:
                    self.board[int(value) - 1] = self.sign
                    self.check_win()
                    if self.sign == 'X':
                        self.sign = 'O'
                    else:
                        self.sign = 'X'

    def main(self):
        """beginning of the game"""
        while True:
            self.draw_board()
            self.move()
