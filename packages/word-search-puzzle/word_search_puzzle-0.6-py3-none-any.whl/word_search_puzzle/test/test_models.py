import unittest
from models import *


class TestModels(unittest.TestCase):

    def test_position_distributor_get_values(self):
        values = PositionDistributor.get_values()
        self.assertIn(PositionDistributor.L2R, values)
        self.assertIn(PositionDistributor.U2D, values)
        self.assertIn(PositionDistributor.DD, values)
        self.assertIn(PositionDistributor.DU, values)

    def test_panel_width(self):
        panel = Panel(10, 11)
        self.assertEqual(panel.width(), 11)

    def test_panel_height(self):
        panel = Panel(10, 11)
        self.assertEqual(panel.height(), 10)
