import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ECGSequence import ecg_seq_index  # noqa: E402

# OEIS A064413: 1, 2, 4, 6, 3, 9, 12, 8, 10, 5, 15, 18, 14, 7, 21, 24, 16, 20, 22, 11
EKG = [1, 2, 4, 6, 3, 9, 12, 8, 10, 5, 15, 18, 14, 7, 21, 24, 16, 20, 22, 11]


class EcgSeqIndexTests(unittest.TestCase):
    def test_matches_known_terms(self):
        for index, value in enumerate(EKG):
            self.assertEqual(ecg_seq_index(value), index, f"value {value}")

    def test_documented_examples(self):
        self.assertEqual(ecg_seq_index(3), 4)
        self.assertEqual(ecg_seq_index(5), 9)
        self.assertEqual(ecg_seq_index(7), 13)

    def test_primes_appear_after_two_times_prime_then_prime_times_three(self):
        # Known EKG property: prime p appears right after 2p (then 3p follows).
        # 11 sits at index 19 (after 22 at index 18); 13 follows 26.
        self.assertEqual(ecg_seq_index(11), 19)
        self.assertEqual(ecg_seq_index(13), ecg_seq_index(26) + 1)

    def test_starting_terms_need_no_generation(self):
        self.assertEqual(ecg_seq_index(1), 0)
        self.assertEqual(ecg_seq_index(2), 1)

    def test_rejects_non_positive(self):
        for bad in (0, -1, -100):
            with self.assertRaises(ValueError):
                ecg_seq_index(bad)


if __name__ == "__main__":
    unittest.main()
