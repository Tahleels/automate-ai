Here is a unique DSA problem:

---

### 1. Title
Group Cyclically Shifted Anagrams

### 2. Problem Statement
Given a list of `N` words, `words`, group them into lists such that words within each group are "cyclically shifted anagrams" of each other.

Two words, `w1` and `w2`, are considered "cyclically shifted anagrams" if `w1` can be transformed into `w2` by applying the *same* cyclic character shift to *every* character in `w1`. For example, if we shift 'a' by 1 to 'b', then 'b' must shift by 1 to 'c', 'c' to 'd', and so on, with 'z' cyclically shifting to 'a'. This shift amount must be uniform across all characters of the word.

All words consist of lowercase English letters ('a'-'z'). The order of the groups and the order of words within each group does not matter.

### 3. Constraints
*   `1 <= words.length <= 10^4`
*   `1 <= words[i].length <= 50`
*   `words[i]` consists of lowercase English letters.

### 4. Example
Input: `words = ["abc", "bcd", "ace", "cde", "zab"]`

Output:
`[["abc", "bcd", "cde", "zab"], ["ace"]]`

*Explanation:*
Let's analyze the words and their relationships:

1.  **"abc"**: This can be considered a base word.
2.  **"bcd"**:
    *   'a' shifted by `+1` becomes 'b'.
    *   'b' shifted by `+1` becomes 'c'.
    *   'c' shifted by `+1` becomes 'd'.
    Since every character in "abc" is shifted by `+1` to get "bcd", "bcd" is a cyclically shifted anagram of "abc".
3.  **"cde"**:
    *   'a' shifted by `+2` becomes 'c'.
    *   'b' shifted by `+2` becomes 'd'.
    *   'c' shifted by `+2` becomes 'e'.
    Since every character in "abc" is shifted by `+2` to get "cde", "cde" is a cyclically shifted anagram of "abc".
4.  **"zab"**:
    *   'a' shifted by `-1` (or `+25` cyclically) becomes 'z'.
    *   'b' shifted by `-1` (or `+25` cyclically) becomes 'a'.
    *   'c' shifted by `-1` (or `+25` cyclically) becomes 'b'.
    Since every character in "abc" is shifted by `-1` to get "zab", "zab" is a cyclically shifted anagram of "abc".
5.  **"ace"**:
    *   To get 'a' from 'a', the shift is `0`.
    *   To get 'c' from 'b', the shift is `+1`.
    *   To get 'e' from 'c', the shift is `+2`.
    Since the required shift amount is not uniform across all characters (`0`, `+1`, `+2`), "ace" is *not* a cyclically shifted anagram of "abc". Thus, "ace" forms its own group.

Therefore, the words are grouped as shown in the output.