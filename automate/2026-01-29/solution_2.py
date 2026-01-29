The problem asks us to find the length of the shortest non-empty substring where every character present in that substring appears an even number of times.

Let's break down the core idea:
1.  **Character Parity**: For each character ('a' through 'z'), we only care if its count is even or odd.
2.  **Substring `S[i...j]`**: The count of a character `c` in `S[i...j]` is `count(c, S[0...j]) - count(c, S[0...i-1])`.
3.  **Even Frequency Condition**: We need *all* characters present in `S[i...j]` to have an even count. If a character is not present, its count is 0, which is even. So, effectively, we need *all 26 lowercase English letters* to have an even count within the substring `S[i...j]`.

**Using Prefix XOR Mask**

We can represent the parity of character counts using a bitmask.
*   Since there are 26 lowercase letters, a 26-bit integer (an `int` in Python) can be used as a mask.
*   The `k`-th bit in the mask corresponds to the `k`-th letter of the alphabet (`'a'` at bit 0, `'b'` at bit 1, ..., `'z'` at bit 25).
*   If the `k`-th bit is `1`, it means the `k`-th character has appeared an odd number of times in the current prefix.
*   If the `k`-th bit is `0`, it means the `k`-th character has appeared an even number of times.

Let `prefix_mask[x]` be the mask representing the parities of character counts in the prefix `S[0...x]`.
When we extend the prefix from `S[0...x-1]` to `S[0...x]` by adding `S[x]`, we flip the bit corresponding to `S[x]` in the mask. This is done using the XOR operation: `new_mask = old_mask ^ (1 << char_code)`.

For a substring `S[i...j]`, its character counts can be derived from the prefix counts. The parity of `count(c, S[i...j])` is `parity(count(c, S[0...j])) XOR parity(count(c, S[0...i-1]))`.
Therefore, the mask for the substring `S[i...j]` is `prefix_mask[j] XOR prefix_mask[i-1]`.

We are looking for a substring `S[i...j]` where *all* characters have even frequencies. This means the mask for `S[i...j]` must be `0` (all bits are `0`).
So, we need to find `i` and `j` such that `prefix_mask[j] XOR prefix_mask[i-1] == 0`.
This equation simplifies to `prefix_mask[j] == prefix_mask[i-1]`.

**Algorithm**

1.  Initialize `min_len` to `sys.maxsize` (representing infinity).
2.  Initialize `current_mask = 0`. This mask represents the parities of counts for the current prefix `S[0...idx]`.
3.  Create a dictionary `seen_masks = {mask_value: first_index}`. This dictionary will store the *first* index at which a particular `mask_value` was encountered.
    *   Initialize `seen_masks = {0: -1}`. The mask `0` represents all even counts. The index `-1` represents the state before the string begins (an empty prefix). This handles cases where a valid substring starts from index `0`.
4.  Iterate through the string `S` from `idx = 0` to `len(S) - 1`:
    *   For each character `char_s = S[idx]`:
        *   Calculate its corresponding bit position: `char_code = ord(char_s) - ord('a')`.
        *   Update `current_mask` by flipping the bit for `char_code`: `current_mask ^= (1 << char_code)`.
        *   Check if `current_mask` is already in `seen_masks`:
            *   If `current_mask` is found, it means we have seen this exact parity configuration before at `prev_idx = seen_masks[current_mask]`.
            *   The substring `S[prev_idx+1 ... idx]` has all character counts even. Its length is `idx - prev_idx`.
            *   Update `min_len = min(min_len, idx - prev_idx)`.
        *   If `current_mask` is *not* in `seen_masks`:
            *   Store the current `idx` as the first occurrence for this `current_mask`: `seen_masks[current_mask] = idx`.
5.  After the loop, if `min_len` is still `sys.maxsize`, no valid substring was found, so return `-1`. Otherwise, return `min_len`.

**Example Trace (`S = "banana"`)**

-   `min_len = infinity`, `current_mask = 0`, `seen_masks = {0: -1}`
-   **idx = 0, char = 'b'**:
    -   `char_code` for 'b' is 1. `current_mask = 0 ^ (1 << 1) = 2`.
    -   `current_mask` (2) not in `seen_masks`. Add `seen_masks[2] = 0`.
    -   `seen_masks = {0: -1, 2: 0}`
-   **idx = 1, char = 'a'**:
    -   `char_code` for 'a' is 0. `current_mask = 2 ^ (1 << 0) = 3`.
    -   `current_mask` (3) not in `seen_masks`. Add `seen_masks[3] = 1`.
    -   `seen_masks = {0: -1, 2: 0, 3: 1}`
-   **idx = 2, char = 'n'**:
    -   `char_code` for 'n' is 13. `current_mask = 3 ^ (1 << 13)`. (Let's represent 'n' as 2 for simpler trace, assuming alphabet is a,b,n). `current_mask = 3 ^ (1 << 2) = 7`.
    -   `current_mask` (7) not in `seen_masks`. Add `seen_masks[7] = 2`.
    -   `seen_masks = {0: -1, 2: 0, 3: 1, 7: 2}`
-   **idx = 3, char = 'a'**:
    -   `char_code` for 'a' is 0. `current_mask = 7 ^ (1 << 0) = 6`.
    -   `current_mask` (6) not in `seen_masks`. Add `seen_masks[6] = 3`.
    -   `seen_masks = {0: -1, 2: 0, 3: 1, 7: 2, 6: 3}`
-   **idx = 4, char = 'n'**:
    -   `char_code` for 'n' is 2. `current_mask = 6 ^ (1 << 2) = 2`.
    -   `current_mask` (2) *is* in `seen_masks`. `prev_idx = seen_masks[2] = 0`.
    -   Length of substring `S[0+1 ... 4]` (`"anan"`) is `4 - 0 = 4`.
    -   `min_len = min(infinity, 4) = 4`.
-   **idx = 5, char = 'a'**:
    -   `char_code` for 'a' is 0. `current_mask = 2 ^ (1 << 0) = 3`.
    -   `current_mask` (3) *is* in `seen_masks`. `prev_idx = seen_masks[3] = 1`.
    -   Length of substring `S[1+1 ... 5]` (`"nana"`) is `5 - 1 = 4`.
    -   `min_len = min(4, 4) = 4`.

-   Loop finishes. `min_len` is 4. Return 4.

**Time and Space Complexity**

*   **Time Complexity**: `O(N)`, where `N` is the length of string `S`. We iterate through the string once. Each operation inside the loop (character conversion, bitwise XOR, dictionary lookup/insertion) takes `O(1)` on average.
*   **Space Complexity**: `O(min(N, 2^A))`, where `A` is the size of the alphabet (26 for lowercase English letters). In the worst case, all prefix masks could be unique, storing up to `N` entries. However, the number of distinct masks is bounded by `2^26`. Since `N = 10^5` and `2^26` is approximately `6.7 * 10^7`, the space complexity is effectively `O(N)` because `N` is smaller than the maximum possible mask values.

```python
import sys

class Solution:
    def shortestEvenFrequencySubstring(self, S: str) -> int:
        """
        Finds the length of the shortest non-empty substring of S such that every
        character present within that substring appears an even number of times.

        Args:
            S: The input string consisting of lowercase English letters.

        Returns:
            The length of the shortest valid substring, or -1 if no such substring exists.
        """

        # Initialize min_len to a very large value to easily find the minimum length.
        # sys.maxsize is a good choice for representing infinity in this context.
        min_len = sys.maxsize

        # current_mask will store the XOR sum of parities of character counts
        # for the prefix S[0...idx].
        # Each bit in the mask corresponds to a character ('a' to 'z').
        # If the k-th bit is 1, it means the k-th character has appeared an odd number of times.
        # If the k-th bit is 0, it means the k-th character has appeared an even number of times.
        # A mask of 0 means all characters have appeared an even number of times.
        current_mask = 0

        # seen_masks will store the first index at which a particular mask value was encountered.
        # Key: mask value (integer)
        # Value: index (integer)
        # We initialize with mask 0 at index -1. This represents the state before the string
        # begins (an empty prefix), where all character counts are 0 (even). This is crucial
        # for correctly identifying substrings that start from index 0 and satisfy the condition.
        seen_masks = {0: -1}

        # Iterate through the string S with its indices.
        for idx, char_s in enumerate(S):
            # Calculate the bit position for the current character.
            # 'a' corresponds to bit 0, 'b' to bit 1, ..., 'z' to bit 25.
            char_code = ord(char_s) - ord('a')

            # Flip the bit corresponding to the current character in the mask.
            # This updates the parity of its count in the prefix S[0...idx].
            current_mask ^= (1 << char_code)

            # The core logic:
            # A substring S[i...j] has all even character frequencies if and only if
            # the parity mask for S[0...j] is the same as the parity mask for S[0...i-1].
            # In our loop, `idx` is `j` and `prev_idx` is `i-1`.
            # So, if `current_mask` (for S[0...idx]) has been seen before at `prev_idx`,
            # it means the substring `S[prev_idx+1 ... idx]` has all character counts even.
            # This also implicitly covers characters not present in the substring, as their
            # count of 0 is an even number.
            if current_mask in seen_masks:
                prev_idx = seen_masks[current_mask]
                # The length of this valid substring is `idx - prev_idx`.
                # We update `min_len` with the shortest length found so far.
                min_len = min(min_len, idx - prev_idx)
            else:
                # If this `current_mask` value is encountered for the first time,
                # store its index. We store the *first* occurrence to ensure
                # that when we later find the same mask, `idx - prev_idx`
                # yields the shortest possible length for that specific mask pairing.
                seen_masks[current_mask] = idx

        # After iterating through the entire string, if `min_len` is still `sys.maxsize`,
        # it means no valid substring was found. In that case, return -1.
        # Otherwise, return the `min_len` found.
        return min_len if min_len != sys.maxsize else -1

```