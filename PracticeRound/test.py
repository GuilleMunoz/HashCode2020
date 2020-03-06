import unittest
from PracticeRound.main import chose_slices

class TestChoseSlices(unittest.TestCase):

    def test_small_1(self):
        self.assertEqual([0, 2, 3], chose_slices(17, 4, ['2', '5', '6', '8']))

    def test_small_2(self):
        self.assertEqual([0, 1, 2, 3], chose_slices(17, 4, ['1', '2', '3', '4']))

    def test_small_3(self):
        self.assertEqual([2, 3], chose_slices(17, 4, ['1', '2', '3', '14']))

    def test_small_4(self):
        self.assertEqual([2, 3], chose_slices(17, 5, ['1', '2', '3', '14', '43']))

    def test_100_types(self):
        self.assertEqual([2, 3], chose_slices(17, 100, ['1', '2', '3', '14'] + [str(i) for i in range(43, 43 + 100 - 4)]))


if __name__ == '__main__':
    unittest.main()