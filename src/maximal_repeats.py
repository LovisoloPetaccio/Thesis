# Maximal repeats algorithm as per Lucian Ilie's paper. Requires input string
# not to have any singleton characters.
def maximal_repeats(w):
  assert get_singletons(w) == set()

  SA, LCP = suffix_and_lcp_array(w)
  max_rep = [len(w)] * len(w)
  for i in range(len(w)):
    lcp = max(LCP[i], LCP[i + 1]) if i < len(w) - 1 else LCP[i]
    max_rep[SA[i] + lcp - 1] = min(max_rep[SA[i] + lcp - 1], SA[i])

  # Build list with actual substrings.
  max_rep_str = [w[max_rep[j]:(j+1)]
                 for j in range(len(w))
                 if max_rep[j] < j]

  return set(max_rep_str)  # Return strings as set.


# Builds SA and LCP arrays as per Lucian Ilie's paper.
# Note: This is a naive implementation of the algorithms. A linear time
# implementation should be possible.
def suffix_and_lcp_array(w):
  # Generate all suffixes of w. The suffix of w that starts at position i is
  # denoted suf[i] = w[i:n]
  suf = [w[i:len(w)] for i in range(len(w))]

  # Build suffix array SA containing positions 0, ..., n-1 sorted in increasing
  # lexicographical order of the corresponding suffixes suf[i], i = 0, ..., n.
  SA = [(i, suf[i]) for i in range(len(w))]
  SA.sort(key = lambda s: s[1])
  SA = [i for i, _ in SA]

  # Build longest common prefix array LCP, containing in its i-th position the
  # length of the longest common prefix of suf[SA[i]] and suf[SA[i − 1]]. The
  # zeroth position is defined as LCP[0] = 0.
  LCP = [0] + [longest_common_prefix_length(suf[SA[i - 1]], suf[SA[i]])
               for i in range(1, len(w))]

  # Print out contents of both arrays.
  # for i in range(len(w)):
  #   print("%d\t%d\t%s\t%d" % (i, SA[i],
  #                                suf[SA[i]],
  #                                LCP[i]))

  return SA, LCP


# Returns the length of the longest common prefix among two strings.
def longest_common_prefix_length(v, w):
  l = 0
  for a, b in zip(v, w):
    if a != b: break
    l += 1
  return l


# Returns a set of singleton characters in a string.
def get_singletons(w):
  count = {}
  for c in w:
    if c not in count: count[c] = 0
    count[c] = count[c] + 1
  return {c for c in count if count[c] == 1}


# Splits a string at singleton characters.
# Example input: "aabcc".
# Expected output: ["aa", "cc"]
def split_at_singletons(w):
  singletons = [(c, w.index(c)) for c in get_singletons(w)]
  singletons.sort(key = lambda ci: ci[1])  # Sorted array [(singleton, index)]
  splits = []
  for c, _ in singletons:
    substring, tail = w.split(c)
    if len(substring) > 0: splits.append(substring)
    w = tail
  if len(w) > 0: splits.append(w)
  return splits


# Failed idea to adapt maximal repeats algorithm to support strings with
# singleton characters.
def maximal_repeats_with_singleton_characters(w):
  substrings = split_at_singletons(w)
  mr = set()
  for s in substrings:
    mr = mr.union(maximal_repeats_no_singletons(s))
  return mr


if __name__ == "__main__":
  pass
