'''Модуль реализующий игру крестики-нолики'''
from string import ascii_uppercase
from argparse import ArgumentParser


class TicTacGame:
    '''Класс реализующий консольную игру крестики-нолики'''

    PLAYER_NAME = {'o': 'нолик', 'x': 'крестик'}

    def __init__(self, size=3, col_width=3):
        if col_width < 1:
            raise ValueError('Ширина стобцов должна быть не менее 1')
        if size < 3 or size > 26:
            raise ValueError('Размер игрового поля должен быть от 3 до 26 клеток')

        self.size = size
        self.width = col_width
        self.board = []
        for _ in range(size):
            self.board.append([' '] * size)

    def show_board(self):
        '''Функция отрисовки игровой таблицы в консоли'''
        indent = ' ' * 3  # Отступ для размещения двузначного индекса и пробела слева
        delimiter = ' '
        print(indent + delimiter +
            delimiter.join(val.center(self.width) for val in ascii_uppercase[:self.size]) +
            delimiter)
        delimiter = '|'
        for row_number in range(self.size):
            print(indent + ('+' + '-'*self.width)*self.size + '+')
            print(str(row_number).rjust(2, ' ') + ' ' + delimiter +
                delimiter.join(str(val).center(self.width) for val in self.board[row_number]) +
                delimiter)
        print(indent + ('+' + '-'*self.width)*self.size + '+')

    def make_move(self, row, col, sign):
        '''Функция ставит символ в игровую клетку'''
        self.board[row][col] = sign

    def validate_input(self, coord: str):
        '''Функция валидирует введенную координату'''
        if not coord:
            raise ValueError('Ошибка. Координата не была введена')

        col = coord[0]
        row = coord[1:]
        if not col.isalpha() or len(col) != 1 or not row.isdecimal():
            raise ValueError('Ошибка. Ожидаемый формат координаты: БукваЧисло')

        col_index = ascii_uppercase[:self.size].find(col.upper())
        if col_index == -1:
            last_col = ascii_uppercase[self.size - 1]
            raise ValueError(f"Значение столбца должно быть от 'A' до '{last_col}'")

        row_index = int(row)
        if row_index >= self.size:
            raise ValueError(f"Значение строки должно быть от '0' до '{self.size - 1}'")

        if self.board[row_index][col_index] != ' ':
            raise ValueError('Выбранная клетка занята')

        return (row_index, col_index)

    def check_winner(self):
        '''Функция определяет победителя'''
        # Проверка по строкам
        winner = self.get_win_row_sign(self.board)
        if winner:
            return winner

        # Проверка по столбцам
        transposed_board = list(map(list, zip(*self.board)))
        winner = self.get_win_row_sign(transposed_board)
        if winner:
            return winner

        # Проверка по диагоналям
        diagonals = [[], []]
        for i in range(self.size):
            diagonals[0].append(self.board[i][i])
            diagonals[1].append(self.board[i][self.size - 1 - i])
        winner = self.get_win_row_sign(diagonals)
        if winner:
            return winner

        return None

    def get_win_row_sign(self, lst):
        '''Функция ищет символ, которым заполнена какая-либо строка'''
        for row in lst:
            if len(set(row)) == 1 and row[0] != ' ':
                return row[0]
        return None

    def start_game(self):
        '''Функция реализующая игровой цикл'''
        moves_left = self.size ** 2
        current_player = 'x'
        winner = None

        self.show_board()
        while moves_left and not winner:
            while True:
                coord_str = input(f"Ходит {self.PLAYER_NAME[current_player]}. " \
                    "Введите координату клетки: ")
                try:
                    coord = self.validate_input(coord_str)
                    self.make_move(coord[0], coord[1], current_player)
                    break
                except ValueError as ex:
                    print(ex)

            self.show_board()

            winner = self.check_winner()
            if winner:
                print(f"Победил {self.PLAYER_NAME[winner]}!")

            moves_left -= 1
            if not moves_left:
                print('Ничья!')

            current_player = 'o' if current_player == 'x' else 'x'


if __name__ == '__main__':
    try:
        parser = ArgumentParser()
        parser.add_argument('-s', '--size', type=int, default=3, help='Размерность игрового поля')
        parser.add_argument('-w', '--width', type=int, default=3, help='Ширина столбцов')
        args = parser.parse_args()

        game = TicTacGame(args.size, args.width)
        game.start_game()
    except ValueError as err:
        print(err)
