import unittest

def find_moves(checkers, dice1, dice2):
    # implementation of the find_moves function

class TestFindMoves(unittest.TestCase):
    def test_find_moves(self):
        checkers = {1: 3, 6: 1, 10: 2, 12: 1, 13: 1}
        self.assertEqual(find_moves(checkers, 6, 1), [(1, 7, 6), (6, 12, 6), (10, 16, 6)])
        self.assertEqual(find_moves(checkers, 5, 5), [(1, 6, 5), (1, 6, 5)])
        self.assertEqual(find_moves(checkers, 3, 4), [(1, 4, 3), (1, 4, 4)])
        self.assertEqual(find_moves(checkers, 1, 2), [(1, 3, 1), (1, 3, 2), (6, 8, 1), (10, 12, 1), (10, 12, 2)])

if __name__ == '__main__':
    unittest.main()
