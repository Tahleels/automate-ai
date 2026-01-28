Here's a unique DSA problem:

---

### 1. Title
**Anagrammatic Partition**

### 2. Problem Statement
You are given two strings, `S` (the main string) and `W` (the target word). Your task is to determine if `S` can be perfectly partitioned into a sequence of contiguous substrings, such that:

1.  Each substring has the same length as `W`.
2.  Each substring is an anagram of `W`.

Return `true` if `S` can be partitioned this way, `false` otherwise.

### 3. Constraints
*   `1 <= len(W) <= len(S) <= 10^5`
*   Both `S` and `W` consist of lowercase English letters only.

### 4. Examples

**Example 1:**
*   **Input:**
    `S = "catact"`
    `W = "act"`
*   **Output:** `true`
*   **Explanation:**
    `len(S) = 6`, `len(W) = 3`.
    `S` can be partitioned into two substrings of length 3: `"cat"` and `"act"`.
    - `"cat"` is an anagram of `"act"`.
    - `"act"` is an anagram of `"act"`.
    Since both partitions are anagrams of `W`, the result is `true`.

**Example 2:**
*   **Input:**
    `S = "abcabcab"`
    `W = "bca"`
*   **Output:** `false`
*   **Explanation:**
    `len(S) = 8`, `len(W) = 3`.
    `len(S)` is not perfectly divisible by `len(W)` (`8 % 3 != 0`). Therefore, `S` cannot be partitioned into equal-length substrings of `W`, and the result is `false`.

**Example 3:**
*   **Input:**
    `S = "listenilentt"`
    `W = "silent"`
*   **Output:** `false`
*   **Explanation:**
    `len(S) = 12`, `len(W) = 6`.
    `S` would be partitioned into two substrings of length 6: `"listen"` and `"ilentt"`.
    - The first partition, `"listen"`, is an anagram of `"silent"` (both contain one 's', 'i', 'l', 'e', 'n', 't').
    - The second partition, `"ilentt"`, is NOT an anagram of `"silent"` (e.g., `"ilentt"` has two 't's and no 's', while `"silent"` has one 't' and one 's').
    Since not all partitions are anagrams of `W`, the result is `false`.