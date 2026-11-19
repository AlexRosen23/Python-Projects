import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tic_tac_toe_blocker import tic_tac_toe_blocker  # noqa: E402

LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


class BlockerTests(unittest.TestCase):
    def test_every_line_every_pair_returns_third_square(self):
        for line in LINES:
            for i in range(3):
                for j in range(3):
                    if i == j:
                        continue
                    third = [s for k, s in enumerate(line) if k not in (i, j)][0]
                    self.assertEqual(
                        tic_tac_toe_blocker(line[i], line[j]), third,
                        f"line {line} pair {line[i]},{line[j]}",
                    )

    def test_documented_example(self):
        self.assertEqual(tic_tac_toe_blocker(0, 1), 2)

    def test_squares_not_sharing_a_line_return_minus_one(self):
        # 0 and 5, 1 and 3, 1 and 5, 3 and 8 share no winning line
        for a, b in [(0, 5), (1, 3), (1, 5), (3, 8), (0, 7), (6, 5)]:
            self.assertEqual(tic_tac_toe_blocker(a, b), -1, f"{a},{b}")

    def test_same_square_twice_is_minus_one(self):
        for s in range(9):
            self.assertEqual(tic_tac_toe_blocker(s, s), -1)

    def test_out_of_range_is_minus_one(self):
        for a, b in [(-1, 0), (0, 9), (9, 10), (4, -4), (0, 100)]:
            self.assertEqual(tic_tac_toe_blocker(a, b), -1, f"{a},{b}")


if __name__ == "__main__":
    unittest.main()
