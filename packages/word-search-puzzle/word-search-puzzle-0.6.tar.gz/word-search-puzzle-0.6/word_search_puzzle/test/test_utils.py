import unittest
from unittest.mock import MagicMock
from utils import *


class TestUtils(unittest.TestCase):

    def test_choose_position_distributor(self):
        position_distributor = choose_position_distributor()
        self.assertIsInstance(position_distributor, PositionDistributor)

    def test_choose_position(self):
        panel = Panel()
        expected_width = 10
        expected_height = 5
        panel.width = MagicMock(return_value=expected_width)
        panel.height = MagicMock(return_value=expected_height)

        position = choose_position(panel)

        self.assertIsInstance(position, Position)
        self.assertIn(position.r, range(expected_height))
        self.assertIn(position.c, range(expected_width))

    def test_produce_positions_du(self):
        length = 3
        position = Position(3, 5)
        position_distributor = PositionDistributor.DU

        expected_positions = [
            Position(3, 5),
            Position(2, 6),
            Position(1, 7)
        ]

        positions = produce_positions(position, length, position_distributor)

        self.assertIsNotNone(positions)
        self.assertEqual(list(positions), expected_positions)

    def test_produce_positions_dd(self):
        length = 3
        position = Position(3, 5)
        position_distributor = PositionDistributor.DD

        expected_positions = [
            Position(3, 5),
            Position(4, 6),
            Position(5, 7)
        ]

        positions = produce_positions(position, length, position_distributor)

        self.assertIsNotNone(positions)
        self.assertEqual(list(positions), expected_positions)

    def test_produce_positions_l2r(self):
        length = 3
        position = Position(3, 5)
        position_distributor = PositionDistributor.L2R

        expected_positions = [
            Position(3, 5),
            Position(3, 6),
            Position(3, 7)
        ]

        positions = produce_positions(position, length, position_distributor)

        self.assertIsNotNone(positions)
        self.assertEqual(list(positions), expected_positions)

    def test_produce_positions_u2d(self):
        length = 3
        position = Position(3, 5)
        position_distributor = PositionDistributor.U2D

        expected_positions = [
            Position(3, 5),
            Position(4, 5),
            Position(5, 5)
        ]

        positions = produce_positions(position, length, position_distributor)

        self.assertIsNotNone(positions)
        self.assertEqual(list(positions), expected_positions)

    def test_valid_positions_valid(self):
        panel = Panel()
        expected_width = 6
        expected_height = 6
        panel.width = MagicMock(return_value=expected_width)
        panel.height = MagicMock(return_value=expected_height)

        positions = [
            Position(3, 5),
            Position(4, 5),
            Position(5, 5)
        ]

        valid = valid_positions(positions, panel)

        self.assertTrue(valid)

    def test_valid_positions_invalid(self):
        panel = Panel()
        expected_width = 2
        expected_height = 3
        panel.width = MagicMock(return_value=expected_width)
        panel.height = MagicMock(return_value=expected_height)

        positions = [
            Position(3, 5),
            Position(4, 5),
            Position(5, 5)
        ]

        valid = valid_positions(positions, panel)

        self.assertFalse(valid)

    def test_insert_word(self):
        panel = Panel(height=6, width=6)
        word = Word(value='cat', positions=[Position(0, 0), Position(0, 1), Position(0, 2)])
        insert_word(word, panel)

        self.assertEqual(panel[0, 0], 'c')
        self.assertEqual(panel[0, 1], 'a')
        self.assertEqual(panel[0, 2], 't')

    def test_fill_remaining_cells(self):
        panel = Panel(height=6, width=6)
        word = Word(value='cat', positions=[Position(0, 0), Position(0, 1), Position(0, 2)])
        insert_word(word, panel)

        fill_remaining_cells(panel)
        for cell in panel.cells.values():
            self.assertNotEqual(cell, DEFAULT_IGNORE_CHARACTER)

    def test_display_panel(self):
        panel = Panel(height=6, width=6)
        display_panel(panel)

if __name__ == '__main__':
    unittest.main()