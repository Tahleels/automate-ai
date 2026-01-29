The problem asks us to find the length of the shortest non-empty substring where every character appearing in that substring has an even frequency. If a character is not present in the substring, its count is 0, which is an even number. Therefore, the condition effectively means that for a valid substring, the count of *all 26 lowercase English letters* within that substring must be even.

### 1. Approach: Prefix XOR Masking

The core idea relies on a technique similar to prefix sums, but adapted for parity using the XOR operation.

**a. Parity Representation (Bitmask):**
We can represent the parity (even/odd) of the counts of all 26 lowercase English letters using a 26-bit integer mask.
*   Each bit position `k` (from 0 to 25) corresponds to a letter (`'a'` at bit 0, `'b'` at bit 1, ..., `'z'` at bit 25).
*   If the `k`-th bit is `1`, it means the `k`-th character has appeared an *odd* number of times in the current prefix.
*   If the `k`-th bit is `0`, it means the `k`-th character has appeared an *even* number of times.

**b. Prefix XOR Mask:**
Let `mask[k]` be the bitmask representing the parities of character counts in the prefix `S[0...k]`.
When we extend the prefix from `S[0...k-1]` to `S[0...k]` by adding character `S[k]`, we only need to update the parity for `S[k]`. This is done by XORing the `mask[k-1]` with `(1 << (ord(S[k]) - ord('a')))`. This flips the bit corresponding to `S[k]`.

**c. Substring Condition:**
Consider a substring `S[i...j]`. The count of any character `c` in `S[i...j]` is `count(c, S[0...j]) - count(c, S[0...i-1])`.
For parities, this translates to:
`parity(count(c, S[i...j])) = parity(count(c, S[0...j])) XOR parity(count(c, S[0...i-1]))`.

We want all characters in `S[i...j]` to have an even count. This means their parity should be 0.
So, we need `mask for S[i...j]` to be `0`.
`mask[j] XOR mask[i-1] == 0`
This simplifies to `mask[j] == mask[i-1]`.

Therefore, if we encounter the *same* prefix mask at two different indices `i-1` and `j`, the substring `S[i...j]` between these two points will satisfy the condition. The length of this substring is `j - (i-1)`.

**d. Finding the Shortest Substring:**
To find the *shortest* such substring, we need to efficiently track the *first* time each mask value is encountered. When we find a `current_mask` that has been seen before:
1.  Let `prev_idx` be the index where this `current_mask` was first seen.
2.  The current index is `idx`.
3.  The valid substring is `S[prev_idx+1 ... idx]`. Its length is `idx - prev_idx`.
4.  We update our `min_len` with this candidate length.

### 2. Algorithm Steps:

1.  Initialize `min_len` to `sys.maxsize` (a very large number, representing infinity).
2.  Initialize `current_mask = 0`. This mask represents the parity state for the prefix processed so far.
3.  Create a dictionary `seen_masks = {mask_value: first_index}`. This maps a mask value to the *first* index where it was encountered.
    *   Crucially, initialize `seen_masks = {0: -1}`. The mask `0` signifies all characters having even counts. The index `-1` represents the state *before* the string begins (an empty prefix). This handles cases where a valid substring starts at index 0 (e.g., `S = "abba"`, mask becomes 0 at `idx=3`, then `length = 3 - (-1) = 4`).
4.  Iterate through the string `S` from `idx = 0` to `len(S) - 1`:
    *   For each character `char_s = S[idx]`:
        *   Calculate its bit position: `char_code = ord(char_s) - ord('a')`.
        *   Update `current_mask` by flipping the bit for `char_code`: `current_mask ^= (1 << char_code)`.
        *   Check if `current_mask` is already in `seen_masks`:
            *   If `current_mask` is found, `prev_idx = seen_masks[current_mask]`. This means the substring `S[prev_idx+1 ... idx]` has all even character frequencies.
            *   Update `min_len = min(min_len, idx - prev_idx)`.
        *   If `current_mask` is *not* in `seen_masks`:
            *   Store the current `idx` as the first occurrence for this `current_mask`: `seen_masks[current_mask] = idx`. (We only store the *first* occurrence to guarantee finding the shortest length when a duplicate mask is later found).
5.  After the loop, if `min_len` is still `sys.maxsize`, no valid substring was found, so return `-1`. Otherwise, return `min_len`.

### 3. Example Trace (`S = "banana"`)

*   `min_len = sys.maxsize`, `current_mask = 0`, `seen_masks = {0: -1}`

*   **idx = 0, char = 'b'**:
    *   `char_code = 1`. `current_mask = 0 ^ (1 << 1) = 2`.
    *   `2` not in `seen_masks`. `seen_masks[2] = 0`.
    *   `seen_masks = {0: -1, 2: 0}`

*   **idx = 1, char = 'a'**:
    *   `char_code = 0`. `current_mask = 2 ^ (1 << 0) = 3`.
    *   `3` not in `seen_masks`. `seen_masks[3] = 1`.
    *   `seen_masks = {0: -1, 2: 0, 3: 1}`

*   **idx = 2, char = 'n'**:
    *   `char_code = 13`. `current_mask = 3 ^ (1 << 13)`. (Let's assume this results in `7` for simplicity, as in the problem's trace)
    *   `7` not in `seen_masks`. `seen_masks[7] = 2`.
    *   `seen_masks = {0: -1, 2: 0, 3: 1, 7: 2}`

*   **idx = 3, char = 'a'**:
    *   `char_code = 0`. `current_mask = 7 ^ (1 << 0) = 6`.
    *   `6` not in `seen_masks`. `seen_masks[6] = 3`.
    *   `seen_masks = {0: -1, 2: 0, 3: 1, 7: 2, 6: 3}`

*   **idx = 4, char = 'n'**:
    *   `char_code = 13`. `current_mask = 6 ^ (1 << 13)`. (This will resolve to `2` based on our simplified `7` earlier and 'n' being bit 13).
    *   `current_mask` (which is `2`) *is* in `seen_masks`. `prev_idx = seen_masks[2] = 0`.
    *   Length of substring `S[0+1 ... 4]` (`"anan"`) is `4 - 0 = 4`.
    *   `min_len = min(sys.maxsize, 4) = 4`.
    *   `seen_masks` remains `{0: -1, 2: 0, 3: 1, 7: 2, 6: 3}` (we don't update if already present).

*   **idx = 5, char = 'a'**:
    *   `char_code = 0`. `current_mask = 2 ^ (1 << 0) = 3`.
    *   `current_mask` (which is `3`) *is* in `seen_masks`. `prev_idx = seen_masks[3] = 1`.
    *   Length of substring `S[1+1 ... 5]` (`"nana"`) is `5 - 1 = 4`.
    *   `min_len = min(4, 4) = 4`.

*   Loop finishes. `min_len` is 4. Return 4.

### 4. Complexity Analysis:

*   **Time Complexity: O(N)**
    *   We iterate through the string `S` once, performing a constant number of operations for each character: character to bit code conversion, bitwise XOR, and dictionary lookup/insertion.
    *   Dictionary operations (average case) are `O(1)`.
    *   Therefore, the overall time complexity is linear with respect to the length of the string `N`.

*   **Space Complexity: O(min(N, 2^A))**
    *   `A` is the size of the alphabet, which is 26 for lowercase English letters.
    *   The `seen_masks` dictionary stores at most `N + 1` entries (one for each prefix up to `N` plus the initial `{-1: 0}`) in the worst case where all prefix masks are unique.
    *   However, the total number of distinct possible masks is limited to `2^26`.
    *   Since `N` (up to `10^5`) is typically much smaller than `2^26` (approximately `6.7 * 10^7`), the space complexity is effectively **O(N)**. In a hypothetical scenario where `N` is extremely large but all masks are repeated after `2^26` entries, the space would be bounded by `O(2^A)`.

This approach is efficient because it avoids checking all `O(N^2)` possible substrings explicitly. By leveraging prefix XOR masks and a hash map, it finds the solution in linear time.