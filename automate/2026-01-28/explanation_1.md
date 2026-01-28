The problem asks us to count the number of non-empty substrings `s[i...j]` such that for every character `c` that appears in `s[i...j]`, its frequency within that substring is **exactly equal to `k`**.

Let's break down the solution step by step.

---

### 1. Understanding the Problem and Constraints

*   **Input:** A string `s` (lowercase English letters, length `1` to `1000`) and a positive integer `k` (`1` to `s.length`).
*   **Output:** Count of qualifying substrings.
*   **Condition:** For a substring `sub`, if a character `c` is present in `sub`, its count in `sub` must be exactly `k`. Characters not in `sub` are ignored.

For example, if `s = "aabbcc"`, `k = 2`:
*   `"aa"`: 'a' appears 2 times. Valid.
*   `"aabb"`: 'a' appears 2 times, 'b' appears 2 times. Both are exactly `k`. Valid.
*   `"aab"`: 'a' appears 2 times, 'b' appears 1 time. 'b's count (1) is not `k` (2). Invalid.

The maximum length of `s` is 1000. An `O(N^2)` solution would be `1000^2 = 10^6` operations, which is acceptable. An `O(N^3)` solution would be `1000^3 = 10^9`, which is too slow.

---

### 2. Approach: Optimized Brute Force (Sliding Window for Inner Loop)

A naive brute-force approach would be:
1.  Iterate `i` from `0` to `n-1` (start of substring).
2.  Iterate `j` from `i` to `n-1` (end of substring).
3.  For each substring `s[i...j]`:
    a.  Calculate frequencies of all characters within this substring. This takes `O(j - i + 1)` time, which is `O(N)`.
    b.  Check if all characters that appear in the substring have a frequency of exactly `k`. This also takes `O(1)` (max 26 characters) after frequency calculation.
This results in an `O(N^3)` solution (`N` choices for `i`, `N` choices for `j`, `N` to count frequencies).

We can optimize the frequency counting. For a fixed starting index `i`, as we extend the ending index `j` from `i` to `n-1`, we can efficiently update character frequencies and check the condition in `O(1)` time for each `j`. This transforms the inner `O(N)` frequency counting into `O(1)`, making the overall complexity `O(N^2)`.

**Key Idea for Optimization:**
When extending the substring from `s[i...j-1]` to `s[i...j]` by adding `s[j]`, we only need to update the frequency of `s[j]`. We also need to keep track of two important counters to quickly check the condition:
1.  `distinct_chars_in_window`: The number of unique characters currently present in `s[i...j]`.
2.  `chars_with_exact_k_freq`: The number of unique characters in `s[i...j]` whose frequency is *exactly* `k`.

The condition "for every character `c` that appears in `s[i...j]`, its frequency is `k`" is met if and only if `distinct_chars_in_window == chars_with_exact_k_freq`.

---

### 3. Algorithm Steps

1.  Initialize `total_valid_substrings = 0`.
2.  Iterate `i` from `0` to `n-1` (outer loop, fixes the starting character of the substring):
    *   Initialize `current_freq_map = [0] * 26` (to store counts for 'a' through 'z' for the current substring `s[i...j]`).
    *   Initialize `distinct_chars_in_window = 0`.
    *   Initialize `chars_with_exact_k_freq = 0`.
3.  Iterate `j` from `i` to `n-1` (inner loop, extends the substring to `s[i...j]`):
    *   Let `char_current = s[j]`. Calculate its 0-25 index: `char_idx = ord(char_current) - ord('a')`.

    *   **Step 1: Update `distinct_chars_in_window`**
        *   If `current_freq_map[char_idx]` was `0` before incrementing (meaning this character is new to the window), increment `distinct_chars_in_window`.

    *   **Step 2: Update `chars_with_exact_k_freq` (before incrementing `current_freq_map`)**
        *   If `current_freq_map[char_idx]` was exactly `k`, it means this character *previously* satisfied the `k`-frequency condition. After we increment its count, it will become `k+1`, no longer satisfying the condition. So, decrement `chars_with_exact_k_freq`.

    *   **Step 3: Increment character frequency**
        *   `current_freq_map[char_idx] += 1`.

    *   **Step 4: Update `chars_with_exact_k_freq` (after incrementing `current_freq_map`)**
        *   If `current_freq_map[char_idx]` is now exactly `k`, it means this character *now* satisfies the `k`-frequency condition. So, increment `chars_with_exact_k_freq`.

    *   **Step 5: Check condition and update total count**
        *   If `distinct_chars_in_window == chars_with_exact_k_freq`, it implies that all unique characters present in the current substring `s[i...j]` have a frequency of exactly `k`. Increment `total_valid_substrings`.

4.  Return `total_valid_substrings`.

---

### 4. Example Walkthrough (s = "aabbcc", k = 2)

`total_valid_substrings = 0`

**`i = 0` (substrings starting with `s[0] = 'a'`):**
  `current_freq_map = [0]*26`, `distinct_chars_in_window = 0`, `chars_with_exact_k_freq = 0`

  *   **`j = 0` (`s[0] = 'a'`)**:
      *   `char_idx` for 'a' is 0. `current_freq_map[0]` was 0, so `distinct_chars_in_window` becomes 1.
      *   `current_freq_map[0]` was 0 (not `k`), `chars_with_exact_k_freq` remains 0.
      *   `current_freq_map[0]` becomes 1.
      *   `current_freq_map[0]` is 1 (not `k`), `chars_with_exact_k_freq` remains 0.
      *   Condition `distinct_chars_in_window (1) == chars_with_exact_k_freq (0)`? No.
      *   Substring: "a"

  *   **`j = 1` (`s[1] = 'a'`)**:
      *   `char_idx` for 'a' is 0. `current_freq_map[0]` was 1 (not 0), `distinct_chars_in_window` remains 1.
      *   `current_freq_map[0]` was 1 (not `k`), `chars_with_exact_k_freq` remains 0.
      *   `current_freq_map[0]` becomes 2.
      *   `current_freq_map[0]` is 2 (equals `k`), so `chars_with_exact_k_freq` becomes 1.
      *   Condition `distinct_chars_in_window (1) == chars_with_exact_k_freq (1)`? Yes. `total_valid_substrings` becomes 1.
      *   Substring: "aa"

  *   **`j = 2` (`s[2] = 'b'`)**:
      *   `char_idx` for 'b' is 1. `current_freq_map[1]` was 0, so `distinct_chars_in_window` becomes 2.
      *   `current_freq_map[1]` was 0 (not `k`), `chars_with_exact_k_freq` remains 1.
      *   `current_freq_map[1]` becomes 1.
      *   `current_freq_map[1]` is 1 (not `k`), `chars_with_exact_k_freq` remains 1.
      *   Condition `distinct_chars_in_window (2) == chars_with_exact_k_freq (1)`? No.
      *   Substring: "aab"

  *   **`j = 3` (`s[3] = 'b'`)**:
      *   `char_idx` for 'b' is 1. `current_freq_map[1]` was 1 (not 0), `distinct_chars_in_window` remains 2.
      *   `current_freq_map[1]` was 1 (not `k`), `chars_with_exact_k_freq` remains 1.
      *   `current_freq_map[1]` becomes 2.
      *   `current_freq_map[1]` is 2 (equals `k`), so `chars_with_exact_k_freq` becomes 2.
      *   Condition `distinct_chars_in_window (2) == chars_with_exact_k_freq (2)`? Yes. `total_valid_substrings` becomes 2.
      *   Substring: "aabb"

  *   **`j = 4` (`s[4] = 'c'`)**:
      *   `char_idx` for 'c' is 2. `current_freq_map[2]` was 0, so `distinct_chars_in_window` becomes 3.
      *   `current_freq_map[2]` was 0 (not `k`), `chars_with_exact_k_freq` remains 2.
      *   `current_freq_map[2]` becomes 1.
      *   `current_freq_map[2]` is 1 (not `k`), `chars_with_exact_k_freq` remains 2.
      *   Condition `distinct_chars_in_window (3) == chars_with_exact_k_freq (2)`? No.
      *   Substring: "aabbc"

  *   **`j = 5` (`s[5] = 'c'`)**:
      *   `char_idx` for 'c' is 2. `current_freq_map[2]` was 1 (not 0), `distinct_chars_in_window` remains 3.
      *   `current_freq_map[2]` was 1 (not `k`), `chars_with_exact_k_freq` remains 2.
      *   `current_freq_map[2]` becomes 2.
      *   `current_freq_map[2]` is 2 (equals `k`), so `chars_with_exact_k_freq` becomes 3.
      *   Condition `distinct_chars_in_window (3) == chars_with_exact_k_freq (3)`? Yes. `total_valid_substrings` becomes 3.
      *   Substring: "aabbcc"

**`i = 1` (substrings starting with `s[1] = 'a'`)** - No new valid substrings are found.
    For example, `s[1...1]="a"`. `freq['a'] = 1`. Not `k=2`.
    `s[1...2]="ab"`. `freq['a']=1, freq['b']=1`. Not `k=2`.

**`i = 2` (substrings starting with `s[2] = 'b'`):**
  `current_freq_map = [0]*26`, `distinct_chars_in_window = 0`, `chars_with_exact_k_freq = 0`

  *   **`j = 2` (`s[2] = 'b'`)**: ... (freq 'b' = 1). Condition No. Substring: "b"
  *   **`j = 3` (`s[3] = 'b'`)**:
      *   `freq['b']` becomes 2. `distinct_chars_in_window = 1`, `chars_with_exact_k_freq = 1`.
      *   Condition `1 == 1`? Yes. `total_valid_substrings` becomes 4.
      *   Substring: "bb"
  *   **`j = 4` (`s[4] = 'c'`)**: ... Condition No. Substring: "bbc"
  *   **`j = 5` (`s[5] = 'c'`)**:
      *   `freq['c']` becomes 2. `distinct_chars_in_window = 2` ('b', 'c'), `chars_with_exact_k_freq = 2` (both 'b', 'c' are freq 2).
      *   Condition `2 == 2`? Yes. `total_valid_substrings` becomes 5.
      *   Substring: "bbcc"

**`i = 3` (substrings starting with `s[3] = 'b'`)** - No new valid substrings.

**`i = 4` (substrings starting with `s[4] = 'c'`):**
  `current_freq_map = [0]*26`, `distinct_chars_in_window = 0`, `chars_with_exact_k_freq = 0`

  *   **`j = 4` (`s[4] = 'c'`)**: ... (freq 'c' = 1). Condition No. Substring: "c"
  *   **`j = 5` (`s[5] = 'c'`)**:
      *   `freq['c']` becomes 2. `distinct_chars_in_window = 1`, `chars_with_exact_k_freq = 1`.
      *   Condition `1 == 1`? Yes. `total_valid_substrings` becomes 6.
      *   Substring: "cc"

**`i = 5` (substrings starting with `s[5] = 'c'`)** - No new valid substrings.

Final `total_valid_substrings = 6`. This matches Example 1.

---

### 5. Complexity Analysis

*   **Time Complexity: O(N^2)**
    *   The outer loop runs `N` times (for `i` from `0` to `n-1`).
    *   The inner loop runs up to `N` times (for `j` from `i` to `n-1`).
    *   Inside the inner loop, all operations (character to index conversion, array lookups, increments, decrements, and comparisons) take constant time, `O(1)`, because the size of the frequency map (26 for lowercase English letters) is constant.
    *   Therefore, the total time complexity is `N * N * O(1) = O(N^2)`. Given `N <= 1000`, `N^2 = 10^6`, which is efficient enough for typical time limits (usually around `10^8` operations per second).

*   **Space Complexity: O(1)**
    *   We use a `current_freq_map` (an array of 26 integers) and a few integer counters (`total_valid_substrings`, `distinct_chars_in_window`, `chars_with_exact_k_freq`).
    *   The size of the `current_freq_map` is constant (26) regardless of the input string length `N`.
    *   Thus, the space complexity is `O(1)`.

---

### 6. Python Implementation

```python
import collections

class Solution:
    def k_frequency_anomaly_substrings(self, s: str, k: int) -> int:
        """
        Calculates the number of non-empty substrings where every character
        present in the substring has a frequency exactly equal to k.

        Args:
            s (str): The input string consisting of lowercase English letters.
            k (int): The target frequency for each character.

        Returns:
            int: The total count of such valid substrings.
        """
        
        n = len(s)
        total_valid_substrings = 0

        # Outer loop iterates through all possible starting indices 'i' of a substring.
        # A substring will be of the form s[i...j].
        for i in range(n):
            # For each starting index 'i', we need to reset our counters and frequency map
            # because we are starting a new potential substring sequence.
            
            # current_freq_map: An array of size 26 (for 'a' through 'z') to store 
            # frequencies of characters within the current substring s[i...j].
            # 'ord(char) - ord('a')' gives the 0-25 index for a character.
            current_freq_map = [0] * 26
            
            # distinct_chars_in_window: Counts the number of unique characters
            # that have appeared at least once in the current substring s[i...j].
            distinct_chars_in_window = 0
            
            # chars_with_exact_k_freq: Counts the number of distinct characters
            # in s[i...j] whose frequency is currently exactly 'k'.
            chars_with_exact_k_freq = 0

            # Inner loop iterates through all possible ending indices 'j' for the 
            # substring starting at 'i'. This effectively expands the window [i...j].
            for j in range(i, n):
                char_current = s[j]
                char_idx = ord(char_current) - ord('a')

                # Step 1: Update distinct_chars_in_window.
                # If the current character's frequency was 0 before adding it, 
                # it means it's a new distinct character entering the window.
                if current_freq_map[char_idx] == 0:
                    distinct_chars_in_window += 1
                
                # Step 2: Update chars_with_exact_k_freq (before incrementing freq).
                # If the current character's frequency was exactly 'k' before this
                # increment, it will become 'k+1' after incrementing. So, it will
                # no longer satisfy the 'k'-frequency condition. Decrement the counter.
                if current_freq_map[char_idx] == k:
                    chars_with_exact_k_freq -= 1
                
                # Step 3: Increment the frequency of the current character.
                current_freq_map[char_idx] += 1
                
                # Step 4: Update chars_with_exact_k_freq (after incrementing freq).
                # If the current character's frequency is now exactly 'k' after this
                # increment, it means it now satisfies the 'k'-frequency condition.
                # Increment the counter.
                if current_freq_map[char_idx] == k:
                    chars_with_exact_k_freq += 1
                
                # Step 5: Check if the current substring s[i...j] satisfies the condition.
                # The condition "for every character c that appears in s[i...j], 
                # its frequency is exactly k" is met if and only if:
                # the total number of distinct characters in the window 
                # is equal to the number of distinct characters whose frequency is exactly 'k'.
                if distinct_chars_in_window == chars_with_exact_k_freq:
                    total_valid_substrings += 1
        
        return total_valid_substrings

```