import unittest
import maximal_repeats as mr


class TestMaximalRepeats(unittest.TestCase):


  def test_maximal_repeats(self):
    self.assertEqual(mr.maximal_repeats("abaababa"), {"aba"})


  def test_suffix_and_lcp_array(self):
    SA, LCP = mr.suffix_and_lcp_array("abaababa")
    sa_lcp = list(zip(SA, LCP))
                                         # Summary of expected output:
                                         # i  sa[i]  lcp[i] suf[sa[i]]
    self.assertEqual(sa_lcp[0], (7, 0))  # 0  7      0      a
    self.assertEqual(sa_lcp[1], (2, 1))  # 1  2      1      aababa
    self.assertEqual(sa_lcp[2], (5, 1))  # 2  5      1      aba
    self.assertEqual(sa_lcp[3], (0, 3))  # 3  0      3      abaababa
    self.assertEqual(sa_lcp[4], (3, 3))  # 4  3      3      ababa
    self.assertEqual(sa_lcp[5], (6, 0))  # 5  6      0      ba
    self.assertEqual(sa_lcp[6], (1, 2))  # 6  1      2      baababa
    self.assertEqual(sa_lcp[7], (4, 2))  # 7  4      2      baba


  def test_get_singletons(self):
    self.assertEqual(mr.get_singletons("a"), {"a"})
    self.assertEqual(mr.get_singletons("ab"), {"a", "b"})
    self.assertEqual(mr.get_singletons("aba"), {"b"})
    self.assertEqual(mr.get_singletons("aab"), {"b"})
    self.assertEqual(mr.get_singletons("abb"), {"a"})
    self.assertEqual(mr.get_singletons("aabcc"), {"b"})
    self.assertEqual(mr.get_singletons("aabccdee"), {"b", "d"})
    self.assertEqual(mr.get_singletons("abab"), set())


  def test_split_at_singletons(self):
    self.assertEqual(mr.split_at_singletons("abab"), ["abab"])
    self.assertEqual(mr.split_at_singletons("aba"), ["a", "a"])
    self.assertEqual(mr.split_at_singletons("bacabafab"), ["ba", "aba", "ab"])
    self.assertEqual(mr.split_at_singletons("abc"), [])


  # def test_maximal_repeats_with_singleton_characters(self):
  #   self.assertEqual(mr.maximal_repeats_with_singleton_characters(
  #     "papototalatalatota"), {"tota", "talat", "ot"})
  #   self.assertEqual(mr.maximal_repeats_with_singleton_characters(
  #     "patalatalota"), {"atal", "ta"})


if __name__ == '__main__':
    unittest.main()
