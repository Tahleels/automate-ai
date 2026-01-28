Here's a unique DSA problem:

---

### 1. Title
K-Frequency Anomaly Substrings

### 2. Problem Statement
Given a string `s` consisting of lowercase English letters and a positive integer `k`.
Your task is to find the number of non-empty substrings `s[i...j]` (where `0 <= i <= j < len(s)`) such that for every character `c` that appears in `s[i...j]`, its frequency (count) within that substring is **exactly equal to `k`**.

### 3. Constraints
*   `1 <= s.length <= 1000`
*   `1 <= k <= s.length`
*   `s` consists of lowercase English letters.

### 4. Example

**Example 1:**
`s = "aabbcc", k = 2`

**Output:** `6`

**Explanation:**
The substrings satisfying the condition are:
1.  `"aa"` (count of 'a' is 2)
2.  `"bb"` (count of 'b' is 2)
3.  `"cc"` (count of 'c' is 2)
4.  `"aabb"` (count of 'a' is 2, count of 'b' is 2)
5.  `"bbcc"` (count of 'b' is 2, count of 'c' is 2)
6.  `"aabbcc"` (count of 'a' is 2, count of 'b' is 2, count of 'c' is 2)

---

**Example 2:**
`s = "abacaba", k = 1`

**Output:** `15`

**Explanation:**
Substrings where every character appears exactly once (i.e., `k=1`):
*   Single character substrings (length 1):
    *   `"a"` (7 occurrences: `s[0]`, `s[2]`, `s[4]`, `s[6]`, etc.)
    *   `"b"` (2 occurrences: `s[1]`, `s[5]`)
    *   `"c"` (1 occurrence: `s[3]`)
    (Total = 7 + 2 + 1 = 10 substrings)
*   Substrings of length 2:
    *   `"ab"` (2 occurrences: `s[0..1]`, `s[4..5]`)
    *   `"ba"` (2 occurrences: `s[1..2]`, `s[5..6]`)
    *   `"ac"` (1 occurrence: `s[2..3]`)
    *   `"ca"` (1 occurrence: `s[3..4]`)
    (Total = 2 + 2 + 1 + 1 = 6 substrings)
*   Substrings of length 3:
    *   `"bac"` (1 occurrence: `s[1..3]`)
    *   `"cab"` (1 occurrence: `s[3..5]`)
    (Total = 1 + 1 = 2 substrings)

Any substring of length 4 or more, e.g., `"abac"` (`s[0..3]`), would have 'a' appearing twice, making its frequency 2, which is not equal to `k=1`. Thus, no longer substrings qualify.

Overall total: 10 + 6 + 2 = `18`. Wait, my trace was 15. Let me re-verify.

*   `s = "abacaba", k = 1`
*   `i=0`:
    * `j=0`: "a" (freq a:1). Count=1
    * `j=1`: "ab" (freq a:1, b:1). Count=2
    * `j=2`: "aba" (freq a:2). No.
*   `i=1`:
    * `j=1`: "b" (freq b:1). Count=3
    * `j=2`: "ba" (freq b:1, a:1). Count=4
    * `j=3`: "bac" (freq b:1, a:1, c:1). Count=5
    * `j=4`: "baca" (freq a:2). No.
*   `i=2`:
    * `j=2`: "a" (freq a:1). Count=6
    * `j=3`: "ac" (freq a:1, c:1). Count=7
    * `j=4`: "aca" (freq a:2). No.
*   `i=3`:
    * `j=3`: "c" (freq c:1). Count=8
    * `j=4`: "ca" (freq c:1, a:1). Count=9
    * `j=5`: "cab" (freq c:1, a:1, b:1). Count=10
    * `j=6`: "caba" (freq a:2). No.
*   `i=4`:
    * `j=4`: "a" (freq a:1). Count=11
    * `j=5`: "ab" (freq a:1, b:1). Count=12
    * `j=6`: "aba" (freq a:2). No.
*   `i=5`:
    * `j=5`: "b" (freq b:1). Count=13
    * `j=6`: "ba" (freq b:1, a:1). Count=14
*   `i=6`:
    * `j=6`: "a" (freq a:1). Count=15

My previous trace of 15 was correct, and the detailed breakdown for 18 (which I had in thoughts) was incorrect. The issue was with "bac" and "cab" not being considered. Oh, they *are* valid. `bac` for `s[1..3]` and `cab` for `s[3..5]` are valid.

Let's do the example trace for `s = "abacaba", k = 1` again:
`ans = 0`

`i=0`:
  `j=0`: "a" -> {'a':1}. OK. `ans=1`.
  `j=1`: "ab" -> {'a':1, 'b':1}. OK. `ans=2`.
  `j=2`: "aba" -> {'a':2, 'b':1}. NOT OK. (a's freq is 2, not 1)

`i=1`:
  `j=1`: "b" -> {'b':1}. OK. `ans=3`.
  `j=2`: "ba" -> {'b':1, 'a':1}. OK. `ans=4`.
  `j=3`: "bac" -> {'b':1, 'a':1, 'c':1}. OK. `ans=5`.
  `j=4`: "baca" -> {'b':1, 'a':2, 'c':1}. NOT OK.

`i=2`:
  `j=2`: "a" -> {'a':1}. OK. `ans=6`.
  `j=3`: "ac" -> {'a':1, 'c':1}. OK. `ans=7`.
  `j=4`: "aca" -> {'a':2, 'c':1}. NOT OK.

`i=3`:
  `j=3`: "c" -> {'c':1}. OK. `ans=8`.
  `j=4`: "ca" -> {'c':1, 'a':1}. OK. `ans=9`.
  `j=5`: "cab" -> {'c':1, 'a':1, 'b':1}. OK. `ans=10`.
  `j=6`: "caba" -> {'c':1, 'a':2, 'b':1}. NOT OK.

`i=4`:
  `j=4`: "a" -> {'a':1}. OK. `ans=11`.
  `j=5`: "ab" -> {'a':1, 'b':1}. OK. `ans=12`.
  `j=6`: "aba" -> {'a':2, 'b':1}. NOT OK.

`i=5`:
  `j=5`: "b" -> {'b':1}. OK. `ans=13`.
  `j=6`: "ba" -> {'b':1, 'a':1}. OK. `ans=14`.

`i=6`:
  `j=6`: "a" -> {'a':1}. OK. `ans=15`.

My repeated trace gives 15. The detailed breakdown example above summing to 18 was indeed incorrect. I will update the example explanation to align with the correct output of 15.

**Corrected Explanation for Example 2:**
`s = "abacaba", k = 1`

**Output:** `15`

**Explanation:**
Substrings where every character appears exactly once (i.e., `k=1`):
*   `s[0..0] = "a"`
*   `s[0..1] = "ab"`
*   `s[1..1] = "b"`
*   `s[1..2] = "ba"`
*   `s[1..3] = "bac"`
*   `s[2..2] = "a"`
*   `s[2..3] = "ac"`
*   `s[3..3] = "c"`
*   `s[3..4] = "ca"`
*   `s[3..5] = "cab"`
*   `s[4..4] = "a"`
*   `s[4..5] = "ab"`
*   `s[5..5] = "b"`
*   `s[5..6] = "ba"`
*   `s[6..6] = "a"`
(Total 15 substrings).
Substrings like `"aba"` (`s[0..2]`) are not included because 'a' appears twice (frequency is 2), which is not equal to `k=1`.

---

**Example 3:**
`s = "topcoder", k = 1`

**Output:** `8`

**Explanation:**
All 8 single-character substrings qualify: "t", "o", "p", "c", "o", "d", "e", "r". No other substrings qualify, as any substring of length 2 or more would have at least one character with frequency 1 (which is `k`), but it would also contain multiple distinct characters, each with frequency 1. The problem requires *all* characters in the substring to have frequency `k`.
This example is confusing. Let's re-evaluate "topcoder", k=1.
"t", "o", "p", "c", "d", "e", "r" are valid (7 single chars).
`s[1]='o'`, `s[4]='o'`.
So "o" (s[1..1]) is valid. "o" (s[4..4]) is valid. Total 2 'o's.
The problem: "topcoder", 'o' appears twice in the string.
Substrings:
"t" (s[0..0]): {'t':1}. OK.
"o" (s[1..1]): {'o':1}. OK.
"p" (s[2..2]): {'p':1}. OK.
"c" (s[3..3]): {'c':1}. OK.
"o" (s[4..4]): {'o':1}. OK.
"d" (s[5..5]): {'d':1}. OK.
"e" (s[6..6]): {'e':1}. OK.
"r" (s[7..7]): {'r':1}. OK.
This is 8 substrings.

Now, consider "to" (s[0..1]): {'t':1, 'o':1}. OK. `ans=9`.
"op" (s[1..2]): {'o':1, 'p':1}. OK. `ans=10`.
... This means the example output of 8 is likely wrong.

Let's stick to the previous trace of "abacaba", k=1 outputting 15 and remove Example 3, as it seems to be generating confusion. Example 1 is clear. Example 2 (with corrected explanation) is also clear.

---

**Final Example Set:**

**Example 1:**
`s = "aabbcc", k = 2`
**Output:** `6`
**Explanation:**
The substrings satisfying the condition are:
1.  `"aa"` (count of 'a' is 2)
2.  `"bb"` (count of 'b' is 2)
3.  `"cc"` (count of 'c' is 2)
4.  `"aabb"` (count of 'a' is 2, count of 'b' is 2)
5.  `"bbcc"` (count of 'b' is 2, count of 'c' is 2)
6.  `"aabbcc"` (count of 'a' is 2, count of 'b' is 2, count of 'c' is 2)

**Example 2:**
`s = "abacaba", k = 1`
**Output:** `15`
**Explanation:**
Substrings where every character appears exactly once (i.e., `k=1`):
*   `s[0..0] = "a"`
*   `s[0..1] = "ab"`
*   `s[1..1] = "b"`
*   `s[1..2] = "ba"`
*   `s[1..3] = "bac"`
*   `s[2..2] = "a"`
*   `s[2..3] = "ac"`
*   `s[3..3] = "c"`
*   `s[3..4] = "ca"`
*   `s[3..5] = "cab"`
*   `s[4..4] = "a"`
*   `s[4..5] = "ab"`
*   `s[5..5] = "b"`
*   `s[5..6] = "ba"`
*   `s[6..6] = "a"`
(Total 15 substrings).
Any other substring (e.g., `"aba"`, which is `s[0..2]`) would not qualify because 'a' appears twice (frequency is 2), which is not equal to `k=1`.

**Example 3:**
`s = "abcabc", k = 2`
**Output:** `1`
**Explanation:**
Only the entire string `"abcabc"` qualifies, because 'a' appears twice, 'b' appears twice, and 'c' appears twice, all matching `k=2`. No shorter substring meets this condition (e.g., `"abca"` has 'a' twice, 'b' once, 'c' once - not all frequencies are 2).

---