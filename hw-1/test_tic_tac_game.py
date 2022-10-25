'''Модуль тестирующий игру крестики-нолики'''
import unittest

from tic_tac_game import TicTacGame


class TestTicTacGame(unittest.TestCase):
    '''Класс тестирующий игру крестики-нолики'''
    def setUp(self):
        self.game = TicTacGame()

    def test_validate_input(self):
        '''Тестирование функции валидации введенной координаты'''
        # Пользователь не ввел координату
        with self.assertRaises(ValueError):
            self.game.validate_input('')

        # Неправильный формат координаты
        with self.assertRaises(ValueError):
            self.game.validate_input('qwerty')

        # Значение столбца выходит за рамки игрового поля
        with self.assertRaises(ValueError):
            self.game.validate_input('F1')

        # Значение строки выходит за рамки игрового поля
        with self.assertRaises(ValueError):
            self.game.validate_input('A22')

        # Выбранная клетка занята
        with self.assertRaises(ValueError):
            self.game.board[0][0] = 'x'
            self.game.validate_input('A0')

        # Корректный ввод координаты
        self.assertEqual(self.game.validate_input('B1'), (1, 1))

    def test_check_winner(self):
        '''Тестирование функции, проверяющей победителя в игре'''
        # Проверка на победителя в строке
        self.game.board = [
            ['x', 'o', 'o'],
            ['x', 'x', 'x'],
            ['o', ' ', 'o'],
        ]
        self.assertEqual(self.game.check_winner(), 'x')

        self.game.board = [
            ['x', ' ', 'x'],
            ['x', 'x', 'o'],
            ['o', 'o', 'o'],
        ]
        self.assertEqual(self.game.check_winner(), 'o')

        # Проверка на победителя в столбце
        self.game.board = [
            ['x', 'x', 'o'],
            ['x', 'o', 'x'],
            ['x', 'o', 'o'],
        ]
        self.assertEqual(self.game.check_winner(), 'x')

        self.game.board = [
            ['x', 'o', 'o'],
            ['o', 'o', 'x'],
            ['x', 'o', 'o'],
        ]
        self.assertEqual(self.game.check_winner(), 'o')

        # Проверка на победителя в диагонали
        self.game.board = [
            ['x', 'o', 'o'],
            ['o', 'x', 'x'],
            ['o', 'o', 'x'],
        ]
        self.assertEqual(self.game.check_winner(), 'x')

        self.game.board = [
            ['x', 'x', 'o'],
            ['x', 'o', 'x'],
            ['o', 'x', 'o'],
        ]
        self.assertEqual(self.game.check_winner(), 'o')

        # Поверка незаполненной игровой доски
        self.game.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        self.assertIsNone(self.game.check_winner())
        self.game.board = [
            [' ', ' ', ' '],
            ['o', 'x', 'o'],
            ['x', ' ', 'x'],
        ]
        self.assertIsNone(self.game.check_winner())

    def test_get_win_row_sign(self):
        '''Тестирование функции ищущей символ, которым заполнена какая-либо строка'''
        # Строка заполнена крестиками
        case1 = [
            ['o', 'x', ' '],
            ['x', 'x', 'x'],
            ['o', 'o', ' '],
        ]

        # Строка заполнена ноликами
        case2 = [
            ['x', ' ', 'x'],
            ['x', ' ', 'x'],
            ['o', 'o', 'o'],
        ]

        # Строка заполнена пробелами
        case3 = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]

        self.assertEqual(self.game.get_win_row_sign(case1), 'x')
        self.assertEqual(self.game.get_win_row_sign(case2), 'o')
        self.assertEqual(self.game.get_win_row_sign(case3), None)

if __name__ == '__main__':
    unittest.main()
