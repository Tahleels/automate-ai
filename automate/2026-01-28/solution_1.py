The problem asks us to count the number of non-empty substrings `s[i...j]` where every character present in that substring has an exact frequency of `k`.

Let's analyze the requirements and constraints:
*   **String `s`:** lowercase English letters.
*   **Integer `k`:** positive.
*   **Substring `s[i...j]`:** non-empty.
*   **Condition:** For every character `c` that *appears* in `s[i...j]`, its frequency within `s[i...j]` must be exactly `k`. This implies that characters not present in the substring are irrelevant.

**Constraints:**
*   `1 <= s.length <= 1000`
*   `1 <= k <= s.length`

### Approach: Optimized Brute Force (Sliding Window for Inner Loop)

A straightforward brute-force approach would involve generating all `O(N^2)` substrings and, for each substring, iterating through its characters to count frequencies. This would lead to an `O(N^3)` time complexity, which is too slow for `N=1000` (`1000^3 = 10^9`).

We can optimize the frequency counting for each substring. For a fixed starting index `i`, as we extend the ending index `j` (i.e., `j` goes from `i` to `n-1`), we can incrementally update the character frequencies for the substring `s[i...j]`.

**Algorithm Steps:**

1.  Initialize `total_valid_substrings = 0`.
2.  Iterate `i` from `0` to `n-1` (representing the start index of the substring).
    *   For each `i`, initialize:
        *   `current_freq_map`: A frequency array/list of size 26 (for 'a' through 'z') to store character counts for the current substring `s[i...j]`. All counts are initially 0.
        *   `distinct_chars_in_window`: A counter for the number of unique characters currently present in `s[i...j]`.
        *   `chars_with_exact_k_freq`: A counter for the number of unique characters in `s[i...j]` whose frequency is *exactly* `k`.
    *   Iterate `j` from `i` to `n-1` (representing the end index of the substring).
        *   Let `char_current = s[j]`. Calculate `char_idx = ord(char_current) - ord('a')`.
        *   **Update `distinct_chars_in_window`:** If `current_freq_map[char_idx]` was 0 before incrementing, it means `char_current` is a new distinct character in `s[i...j]`. Increment `distinct_chars_in_window`.
        *   **Update `chars_with_exact_k_freq`:**
            *   If `current_freq_map[char_idx]` was `k` before incrementing, it means this character previously satisfied the `k`-frequency condition. After incrementing, its frequency will be `k+1`, so it no longer satisfies the condition. Decrement `chars_with_exact_k_freq`.
        *   **Increment frequency:** `current_freq_map[char_idx] += 1`.
        *   **Update `chars_with_exact_k_freq` again:** If `current_freq_map[char_idx]` is now `k`, it means this character now satisfies the `k`-frequency condition. Increment `chars_with_exact_k_freq`.
        *   **Check condition:** If `distinct_chars_in_window == chars_with_exact_k_freq`, it means all unique characters in the current substring `s[i...j]` have a frequency of exactly `k`. If this is true, increment `total_valid_substrings`.
3.  Return `total_valid_substrings`.

**Example Walkthrough (s = "aabbcc", k = 2):**

`total_valid_substrings = 0`

`i = 0`:
  `current_freq_map = [0]*26`, `distinct_chars_in_window = 0`, `chars_with_exact_k_freq = 0`
  `j = 0`: `s[0] = 'a'`
    `freq['a']` (0 -> 1). `distinct_chars_in_window = 1`.
    `Condition: 1 == 0`? No.
  `j = 1`: `s[1] = 'a'`
    `freq['a']` (1 -> 2). `chars_with_exact_k_freq` (0 -> 1, because `freq['a']` became `k=2`).
    `Condition: 1 == 1`? Yes. `total_valid_substrings = 1` (for "aa")
  `j = 2`: `s[2] = 'b'`
    `freq['b']` (0 -> 1). `distinct_chars_in_window = 2`.
    `Condition: 2 == 1`? No.
  `j = 3`: `s[3] = 'b'`
    `freq['b']` (1 -> 2). `chars_with_exact_k_freq` (1 -> 2, because `freq['b']` became `k=2`).
    `Condition: 2 == 2`? Yes. `total_valid_substrings = 2` (for "aabb")
  `j = 4`: `s[4] = 'c'`
    `freq['c']` (0 -> 1). `distinct_chars_in_window = 3`.
    `Condition: 3 == 2`? No.
  `j = 5`: `s[5] = 'c'`
    `freq['c']` (1 -> 2). `chars_with_exact_k_freq` (2 -> 3, because `freq['c']` became `k=2`).
    `Condition: 3 == 3`? Yes. `total_valid_substrings = 3` (for "aabbcc")

`i = 1`: (Starting at `s[1] = 'a'`)
  ... (similar logic, no valid substrings starting at `s[1]`)

`i = 2`: (Starting at `s[2] = 'b'`)
  `current_freq_map = [0]*26`, `distinct_chars_in_window = 0`, `chars_with_exact_k_freq = 0`
  `j = 2`: `s[2] = 'b'`
    `freq['b']` (0 -> 1). `distinct_chars_in_window = 1`.
    `Condition: 1 == 0`? No.
  `j = 3`: `s[3] = 'b'`
    `freq['b']` (1 -> 2). `chars_with_exact_k_freq` (0 -> 1).
    `Condition: 1 == 1`? Yes. `total_valid_substrings = 4` (for "bb")
  `j = 4`: `s[4] = 'c'`
    `freq['c']` (0 -> 1). `distinct_chars_in_window = 2`.
    `Condition: 2 == 1`? No.
  `j = 5`: `s[5] = 'c'`
    `freq['c']` (1 -> 2). `chars_with_exact_k_freq` (1 -> 2).
    `Condition: 2 == 2`? Yes. `total_valid_substrings = 5` (for "bbcc")

`i = 3`: (Starting at `s[3] = 'b'`)
  ... (similar logic, no valid substrings starting at `s[3]`)

`i = 4`: (Starting at `s[4] = 'c'`)
  `current_freq_map = [0]*26`, `distinct_chars_in_window = 0`, `chars_with_exact_k_freq = 0`
  `j = 4`: `s[4] = 'c'`
    `freq['c']` (0 -> 1). `distinct_chars_in_window = 1`.
    `Condition: 1 == 0`? No.
  `j = 5`: `s[5] = 'c'`
    `freq['c']` (1 -> 2). `chars_with_exact_k_freq` (0 -> 1).
    `Condition: 1 == 1`? Yes. `total_valid_substrings = 6` (for "cc")

`i = 5`: (Starting at `s[5] = 'c'`)
  ... (similar logic, no valid substrings starting at `s[5]`)

The final count is `6`, matching Example 1.

### Complexity Analysis:

*   **Time Complexity:** `O(N^2)`. The outer loop runs `N` times. The inner loop runs up to `N` times. Inside the inner loop, all operations (array access, increment/decrement, comparison) take `O(1)` time because the alphabet size (26) is constant. So, `N * N * 1 = O(N^2)`. For `N=1000`, `N^2 = 10^6`, which is efficient enough.
*   **Space Complexity:** `O(1)`. We use a frequency map (list of 26 integers) and a few counters, all of which consume constant space regardless of the input string's length.

### Python Implementation:

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
        for i in range(n):
            # For each starting index 'i', we build substrings s[i...j] by extending 'j'
            # from 'i' to 'n-1'. We maintain character frequencies and related counts
            # for the current window [i...j].
            
            # current_freq_map: An array of size 26 to store frequencies of characters
            # 'a' through 'z' in the current substring s[i...j].
            # char_idx = ord(char) - ord('a') gives the 0-25 index for a character.
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

                # Step 1: Update distinct_chars_in_window
                # If the current character's frequency was 0, it means it's a new
                # distinct character entering the window.
                if current_freq_map[char_idx] == 0:
                    distinct_chars_in_window += 1
                
                # Step 2: Update chars_with_exact_k_freq (before incrementing freq)
                # If the current character's frequency was exactly 'k' before this
                # increment, it will no longer be 'k' after incrementing (it becomes k+1).
                # So, we decrement chars_with_exact_k_freq.
                if current_freq_map[char_idx] == k:
                    chars_with_exact_k_freq -= 1
                
                # Step 3: Increment the frequency of the current character.
                current_freq_map[char_idx] += 1
                
                # Step 4: Update chars_with_exact_k_freq (after incrementing freq)
                # If the current character's frequency is now exactly 'k' after this
                # increment, it means it now satisfies the 'k'-frequency condition.
                # So, we increment chars_with_exact_k_freq.
                if current_freq_map[char_idx] == k:
                    chars_with_exact_k_freq += 1
                
                # Step 5: Check if the current substring s[i...j] satisfies the condition.
                # The condition is met if and only if all unique characters present
                # in the substring have a frequency of exactly 'k'.
                # This is true when the total number of distinct characters in the window
                # is equal to the number of distinct characters whose frequency is exactly 'k'.
                if distinct_chars_in_window == chars_with_exact_k_freq:
                    total_valid_substrings += 1
        
        return total_valid_substrings

```