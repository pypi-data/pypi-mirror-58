import unittest
from algorithms import create_panel
from exceptions import PermutationsExceededException
from models import DEFAULT_IGNORE_CHARACTER


class TestAlgorithms(unittest.TestCase):
    def test_create_panel_successful(self):
        words = ['Cat', 'Bear', 'Tiger', 'Lion']

        result = create_panel(height=5, width=5, words_value_list=words)

        self.assertLessEqual(result.get('attempts'), 25)
        self.assertTrue(result.get('found'))

        panel = result.get('panel')

        for cell in panel.cells.values():
            self.assertNotEqual(cell, DEFAULT_IGNORE_CHARACTER)

    def test_create_panel_fail(self):
        words = ['Cat', 'Bear', 'Tiger', 'Lion']

        try:
            result = create_panel(height=4, width=3, words_value_list=words)
        except Exception as exception:
            self.assertIsInstance(exception, PermutationsExceededException)

