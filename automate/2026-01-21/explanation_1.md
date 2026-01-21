The problem asks us to find the longest contiguous subarray where all distinct elements have distinct frequencies. This is a classic "longest subarray" problem, hinting at a sliding window approach.

### 1. Problem Understanding

Given an array `nums`, we need to find `[nums[l], ..., nums[r]]` such that if we list the counts of each unique number in this subarray, all these counts are unique themselves. For example, if numbers A, B, C are in the subarray with frequencies `f_A, f_B, f_C` respectively, then `f_A, f_B, f_C` must all be distinct.

### 2. Approach: Sliding Window

We will use a sliding window `[l, r]` to explore all possible contiguous subarrays.
1.  We expand the window by moving the right pointer `r` one step at a time.
2.  After each expansion, we check if the current window `[l, r]` is valid (i.e., satisfies the distinct frequency condition).
3.  If the window is invalid, we shrink it by moving the left pointer `l` one step at a time, until it becomes valid again.
4.  Whenever the window is valid, we update our `max_length` with the current window's length (`r - l + 1`).

This approach guarantees that both `l` and `r` pointers traverse the array at most once, leading to an efficient solution.

### 3. Data Structures for Efficient Checking

To efficiently maintain and check the distinct frequency condition, we need two hash maps and a counter:

1.  **`freq_map` (e.g., `collections.defaultdict(int)`):**
    *   Stores the frequency of each number *within the current window `[l, r]`*.
    *   `key`: A number from `nums`.
    *   `value`: Its current count in the window.
    *   Example: `{1: 2, 5: 1}` means number `1` appears twice, number `5` appears once.

2.  **`freq_counts` (e.g., `collections.defaultdict(int)`):**
    *   Stores how many *distinct numbers* in the window currently have a specific frequency.
    *   `key`: A frequency value (e.g., 1, 2, 3...).
    *   `value`: The count of distinct numbers in `freq_map` that have this frequency.
    *   Example: If `freq_map` is `{1: 2, 5: 1}`, then `freq_counts` would be `{2: 1, 1: 1}` (one number (1) has frequency 2, one number (5) has frequency 1).
    *   If `freq_map` is `{A: 2, B: 2, C: 1}`, then `freq_counts` would be `{2: 2, 1: 1}` (two numbers (A, B) have frequency 2, one number (C) has frequency 1).

3.  **`invalid_freq_count` (integer counter):**
    *   This counter tracks how many frequency values `k` exist such that `freq_counts[k]` is greater than 1.
    *   If `invalid_freq_count` is `0`, it means all frequency values in `freq_counts` have a count of `1`. This directly translates to the condition that all distinct numbers in the subarray have distinct frequencies, making the subarray **valid**.
    *   If `invalid_freq_count > 0`, it means at least one frequency value `k` is shared by two or more distinct numbers (`freq_counts[k] > 1`), making the subarray **invalid**.

### 4. Algorithm Steps

1.  **Initialization**:
    *   `l = 0`: Left pointer of the window.
    *   `max_length = 0`: Stores the maximum length found so far.
    *   `freq_map = collections.defaultdict(int)`
    *   `freq_counts = collections.defaultdict(int)`
    *   `invalid_freq_count = 0`

2.  **Iterate `r` from `0` to `n-1` (Expand Window)**:
    *   Let `num_r = nums[r]`.

    *   **a. Update `freq_counts` for `num_r`'s *old* frequency (if it existed)**:
        *   Get `old_freq_r = freq_map[num_r]`.
        *   If `old_freq_r > 0`: This `num_r` was already in the window. Its frequency is about to change.
            *   Decrement `freq_counts[old_freq_r]` because one number (which is `num_r`) is no longer at `old_freq_r`.
            *   If `freq_counts[old_freq_r]` becomes `1`: This means `old_freq_r` was previously shared by *more than one* number, but now it's only held by one. So, this frequency `old_freq_r` is no longer a "bad" (shared) frequency. Decrement `invalid_freq_count`.

    *   **b. Update `freq_map` and `freq_counts` for `num_r`'s *new* frequency**:
        *   Increment `freq_map[num_r]` (add `num_r` to window or increase its count).
        *   Let `new_freq_r = freq_map[num_r]`.
        *   Increment `freq_counts[new_freq_r]` because `num_r` now has this `new_freq_r`.
        *   If `freq_counts[new_freq_r]` becomes `2`: This means `new_freq_r` is now shared by *two* distinct numbers. This makes `new_freq_r` a "bad" (shared) frequency. Increment `invalid_freq_count`.

3.  **Shrink Window (while `invalid_freq_count > 0`)**:
    *   If the window is currently invalid (`invalid_freq_count > 0`), we need to shrink it from the left.
    *   While `invalid_freq_count > 0`:
        *   Let `num_l = nums[l]`.

        *   **a. Update `freq_counts` for `num_l`'s *old* frequency (before removal)**:
            *   Get `old_freq_l = freq_map[num_l]`.
            *   Decrement `freq_counts[old_freq_l]`.
            *   If `freq_counts[old_freq_l]` becomes `1`: This means `old_freq_l` was previously a "bad" frequency, but now it's "good". Decrement `invalid_freq_count`.

        *   **b. Update `freq_map` and `freq_counts` for `num_l`'s *new* frequency (after removal)**:
            *   Decrement `freq_map[num_l]`.
            *   Let `new_freq_l = freq_map[num_l]`.
            *   If `new_freq_l > 0` (meaning `num_l` is still in the window but with a lower frequency):
                *   Increment `freq_counts[new_freq_l]`.
                *   If `freq_counts[new_freq_l]` becomes `2`: This means `new_freq_l` is now a "bad" frequency. Increment `invalid_freq_count`.
            *   Else (`new_freq_l == 0`, `num_l` is completely removed from the window):
                *   Optionally, `del freq_map[num_l]` to keep `freq_map` clean.

        *   Increment `l` (move left pointer).

4.  **Update `max_length`**:
    *   After the `while` loop (when `invalid_freq_count == 0`), the current window `[l, r]` is valid.
    *   Update `max_length = max(max_length, r - l + 1)`.

5.  **Return `max_length`**.

### 5. Example Walkthrough (`nums = [1, 2, 2, 1, 3]`)

| r | `nums[r]` | Action (`num_r`) | `freq_map` | `old_freq_r` | `new_freq_r` | `freq_counts` | `invalid_freq_count` | Window `[l, r]` | Valid? | `max_length` |
|---|---|---|---|---|---|---|---|---|---|---|
| Initial | | | `{}` | | | `{}` | 0 | `[]` | N/A | 0 |
| 0 | `1` | Add `1` | `{1:1}` | 0 | 1 | `{1:1}` | 0 | `[1]` | Y | 1 |
| 1 | `2` | Add `2` | `{1:1, 2:1}` | 0 | 1 | `{1:2}` | 1 (`1` is shared) | `[1,2]` | N | 1 |
|   |   | Shrink `l` (`nums[l]=1`) | `{2:1}` | 1 | 0 | `{1:1}` | 0 (`1` no longer shared) | `[2]` | Y | 1 |
| 2 | `2` | Add `2` | `{2:2}` | 1 | 2 | `{1:0}` `{2:1}` | 0 | `[2,2]` | Y | 2 |
| 3 | `1` | Add `1` | `{2:2, 1:1}` | 0 | 1 | `{2:1, 1:1}` | 0 | `[2,2,1]` | Y | 3 |
| 4 | `3` | Add `3` | `{2:2, 1:1, 3:1}` | 0 | 1 | `{2:1, 1:2}` | 1 (`1` is shared) | `[2,2,1,3]` | N | 3 |
|   |   | Shrink `l` (`nums[l]=2`) | `{2:1, 1:1, 3:1}` | 2 | 1 | `{2:0}` `{1:3}` | 1+1=2 (`1` new shared) | `[2,1,3]` | N | 3 |
|   |   | Shrink `l` (`nums[l]=2`) | `{1:1, 3:1}` | 1 | 0 | `{1:2}` | 2-1=1 (`1` still shared, from prev step, but now it's {1:2} in freq_counts (numbers 1 and 3 have freq 1)) | `[1,3]` | N | 3 |
|   |   | Shrink `l` (`nums[l]=1`) | `{3:1}` | 1 | 0 | `{1:1}` | 1-1=0 (`1` no longer shared) | `[3]` | Y | 3 |

**Note on trace logic for `invalid_freq_count`:**
When `r=4`, `num_r=3`.
`old_freq_r = freq_map[3]` is 0.
`freq_map` becomes `{2:2, 1:1, 3:1}`.
`new_freq_r = freq_map[3]` is 1.
`freq_counts[1]` becomes `2` (because `1` and `3` both have freq 1). So `invalid_freq_count` increases to 1.
Window `[2,2,1,3]` (l=0, r=4) is invalid. Length `5`. `max_length` remains `3`.

Shrink `l` (l=0, `nums[0]=2`):
`old_freq_l = freq_map[2]` is 2. `freq_counts[2]` decreases to 0. Since `freq_counts[2]` was 1 and became 0, `invalid_freq_count` doesn't change here. (My previous description had a slight error here. `freq_counts[2]` changing from 1 to 0 does not imply a reduction in `invalid_freq_count` because it was never `>1`).
The critical part is when `freq_counts[k]` goes from `2` to `1`.
In this step, `freq_counts[2]` goes from 1 to 0. No `invalid_freq_count` change.
`freq_map[2]` decreases to 1. `new_freq_l = 1`.
`freq_counts[1]` increases to 3 (because `1`, `2`, `3` now all have frequency 1). `invalid_freq_count` increases to 2 (because `freq_counts[1]` was 2 and became 3).
`l` becomes 1. Window `[2,1,3]` (l=1, r=4). `invalid_freq_count=2`.

Shrink `l` (l=1, `nums[1]=2`):
`old_freq_l = freq_map[2]` is 1. `freq_counts[1]` decreases to 2. Since `freq_counts[1]` was 3 and became 2, `invalid_freq_count` decreases to 1.
`freq_map[2]` decreases to 0. `del freq_map[2]`.
`l` becomes 2. Window `[1,3]` (l=2, r=4). `invalid_freq_count=1`. Still invalid.

Shrink `l` (l=2, `nums[2]=1`):
`old_freq_l = freq_map[1]` is 1. `freq_counts[1]` decreases to 1. Since `freq_counts[1]` was 2 and became 1, `invalid_freq_count` decreases to 0.
`freq_map[1]` decreases to 0. `del freq_map[1]`.
`l` becomes 3. Window `[3]` (l=3, r=4). Valid. `invalid_freq_count=0`.
`max_length = max(3, r-l+1 = 4-3+1 = 2) = 3`.

Final `max_length` is 3. This matches the example. The logic for updating `invalid_freq_count` is critical and must be precise.

### 6. Complexity Analysis

*   **Time Complexity: O(N)**
    *   Both the left pointer `l` and the right pointer `r` traverse the `nums` array at most once, each visiting each element a constant number of times.
    *   Operations on `freq_map` and `freq_counts` (insertion, deletion, lookup, update) typically take `O(1)` on average for hash maps (`defaultdict` in Python is based on hash tables).
    *   Therefore, the total time complexity is linear with respect to the input array size `N`.

*   **Space Complexity: O(N)**
    *   `freq_map`: In the worst case, all numbers in `nums` are unique. This map would store up to `N` entries, each `(number -> count)`. So, `O(N)`.
    *   `freq_counts`: In the worst case, all frequency values from `1` to `N` could be present (e.g., if we had `[1, 2, 2, 3, 3, 3, ..., k, ..., k]` where `k` appears `k` times). This map would store up to `N` entries, each `(frequency_value -> count_of_numbers_with_this_frequency)`. So, `O(N)`.
    *   Therefore, the total space complexity is `O(N)`.

This approach provides an optimal solution for the problem within the given constraints.