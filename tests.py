import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )

        num_cols = 50
        num_rows = 1
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m2._cells),
            num_cols
        )
        self.assertEqual(
            len(m2._cells[0]),
            num_rows
        )

    def test_maze_constructor(self):
        m1 = Maze(179, 74, 13, 3, 17, 56)
        self.assertEqual(m1._x1, 179)
        self.assertEqual(m1._y1, 74)
        self.assertEqual(m1._num_rows, 13)
        self.assertEqual(m1._num_cols, 3)
        self.assertEqual(m1._cell_size_x, 17)
        self.assertEqual(m1._cell_size_y, 56)
        self.assertEqual(m1._win, None)

    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[-1][-1].has_bottom_wall)

    def test_reset_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(m1._cells[0][0].visited)
        self.assertFalse(m1._cells[5][3].visited)
        self.assertFalse(m1._cells[2][9].visited)
        self.assertFalse(m1._cells[8][1].visited)
        self.assertFalse(m1._cells[11][9].visited)

if __name__ == "__main__":
    unittest.main()