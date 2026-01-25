The problem asks us to find the shortest *contiguous* subarray `nums[i...j]` such that every unique element `x` within that subarray has a frequency of at least `k` *within that same subarray*. If no such subarray exists, we return -1.

This is a classic "shortest subarray with a property" problem, perfectly suited for the **Sliding Window** technique.

---

### Approach: Sliding Window

We use a two-pointer approach, `left` and `right`, to define our current window `nums[left...right]`. The `right` pointer expands the window by including new elements, and the `left` pointer shrinks it to find the shortest valid subarray or to try and make an invalid window valid again.

To efficiently check the condition ("every unique element's frequency is at least `k`"), we need to maintain specific counts and states for the elements within our current window:

1.  **`window_counts`**: A hash map (Python's `collections.defaultdict(int)` is ideal) to store the frequency of each number currently within `nums[left...right]`.
2.  **`total_unique_elements`**: This variable keeps track of the total number of *distinct* (unique) elements present in the current window. For example, in `[1, 2, 1]`, `total_unique_elements` would be 2 (for 1 and 2).
3.  **`good_elements_count`**: This crucial variable counts how many of the `total_unique_elements` currently satisfy the frequency requirement, i.e., their count in `window_counts` is `>= k`.

The core idea is:
*   Expand the window using `right`.
*   Maintain `window_counts`, `total_unique_elements`, and `good_elements_count` as elements are added.
*   Once the window becomes "valid" (meaning `good_elements_count == total_unique_elements`), we have a candidate subarray. We record its length and then try to shrink the window from the `left` side to find an even shorter valid subarray.
*   As we shrink from `left`, we update the counts and metrics accordingly, continuing to shrink as long as the window remains valid.

---

### Detailed Algorithm Steps

1.  **Initialization:**
    *   `left = 0`: The left boundary of our sliding window.
    *   `min_length = math.inf`: Stores the minimum length of a valid subarray found so far. Initialized to infinity.
    *   `window_counts = collections.defaultdict(int)`: Frequency map for elements in the current window.
    *   `total_unique_elements = 0`: Count of distinct elements in the window.
    *   `good_elements_count = 0`: Count of distinct elements whose frequency is `>= k`.

2.  **Expanding the Window (`right` pointer loop):**
    *   Iterate `right` from `0` to `len(nums) - 1`.
    *   Let `num_r = nums[right]`. This is the element being added to the window.
    *   **Update `total_unique_elements`**: If `window_counts[num_r]` was `0` *before* incrementing it, `num_r` is a new unique element in the window. Increment `total_unique_elements`.
    *   **Update `good_elements_count`**: If `window_counts[num_r]` was `k - 1` *before* incrementing it, its frequency will become `k`. This means `num_r` now satisfies the frequency condition, so increment `good_elements_count`.
    *   Increment `window_counts[num_r]`.

3.  **Shrinking the Window (`left` pointer loop):**
    *   After adding `num_r`, check if the current window `[left, right]` is valid:
        *   A window is valid if `good_elements_count == total_unique_elements` (all unique elements meet the `k`-frequency requirement) AND `total_unique_elements > 0` (to ensure we consider non-empty subarrays).
    *   While the window is valid:
        *   **Record length**: Update `min_length = min(min_length, right - left + 1)`.
        *   Let `num_l = nums[left]`. This is the element being removed from the window.
        *   **Update `good_elements_count`**: If `window_counts[num_l]` was `k` *before* decrementing it, its frequency will become `k - 1`. This means `num_l` no longer satisfies the frequency condition, so decrement `good_elements_count`.
        *   Decrement `window_counts[num_l]`.
        *   **Update `total_unique_elements`**: If `window_counts[num_l]` becomes `0` *after* decrementing, `num_l` is no longer present in the window. Decrement `total_unique_elements`.
        *   Increment `left` to shrink the window.

4.  **Final Result:**
    *   After the `right` pointer finishes iterating through all elements, if `min_length` is still `math.inf`, it means no valid subarray was ever found. Return -1.
    *   Otherwise, return the `min_length`.

---

### Example Walkthrough (`nums = [1, 2, 1, 2], k = 2`)

Initialize: `left = 0`, `min_length = inf`, `window_counts = {}`, `total_unique_elements = 0`, `good_elements_count = 0`

| `right` | `nums[right]` | `window_counts` (before) | `total_unique_elements` (before) | `good_elements_count` (before) | Add `nums[right]` Updates | `window_counts` (after) | `total_unique_elements` (after) | `good_elements_count` (after) | Window `[L,R]` | Valid? | `min_length` | Shrink (if valid) |
| :------ | :------------ | :----------------------- | :------------------------------- | :----------------------------- | :------------------------ | :---------------------- | :------------------------------ | :---------------------------- | :------------- | :----- | :----------- | :------------------ |
| -       | -             | `{}`                     | `0`                              | `0`                            | -                         | `{}`                    | `0`                             | `0`                           | -              | -      | `inf`        | -                   |
| `0`     | `1`           | `{1:0}`                  | `0`                              | `0`                            | `total_unique_elements` becomes `1` (`1` was new). `good_elements_count` no change (count becomes 1, not `k`). `window_counts[1]` becomes `1`. | `{1:1}`                 | `1`                             | `0`                           | `[1]`          | `F`    | `inf`        | -                   |
| `1`     | `2`           | `{2:0}`                  | `1`                              | `0`                            | `total_unique_elements` becomes `2` (`2` was new). `good_elements_count` no change. `window_counts[2]` becomes `1`. | `{1:1, 2:1}`            | `2`                             | `0`                           | `[1,2]`        | `F`    | `inf`        | -                   |
| `2`     | `1`           | `{1:1}`                  | `2`                              | `0`                            | `total_unique_elements` no change. `good_elements_count` becomes `1` (`1` count was `1` (`k-1`), now `2` (`k`)). `window_counts[1]` becomes `2`. | `{1:2, 2:1}`            | `2`                             | `1`                           | `[1,2,1]`      | `F`    | `inf`        | -                   |
| `3`     | `2`           | `{2:1}`                  | `2`                              | `1`                            | `total_unique_elements` no change. `good_elements_count` becomes `2` (`2` count was `1` (`k-1`), now `2` (`k`)). `window_counts[2]` becomes `2`. | `{1:2, 2:2}`            | `2`                             | `2`                           | `[1,2,1,2]`    | `T`    | `4`          |
|         |               |                          |                                  |                                |                                   |                                 |                                 |                               |                |        |              | **Shrink:** `num_l=nums[0]=1`. `window_counts[1]` was `2` (`k`), so `good_elements_count` becomes `1`. `window_counts[1]` becomes `1`. `window_counts[1]` is not `0`, `total_unique_elements` no change. `left` becomes `1`. |
|         |               | `{1:1, 2:2}`             | `2`                              | `1`                            | (after `left` moves)      | `{1:1, 2:2}`            | `2`                             | `1`                           | `[2,1,2]`      | `F`    | `4`          | Stop shrinking (window no longer valid: `good_elements_count (1) != total_unique_elements (2)`). |

End of `right` loop.
Return `min_length = 4`.

---

### Complexity Analysis

*   **Time Complexity: O(N)**
    *   The `right` pointer iterates through the `nums` array exactly once (`N` steps).
    *   The `left` pointer also moves forward, and in the worst case, it processes each element at most once across all iterations of the inner `while` loop.
    *   Dictionary operations (`window_counts[num]`, `len(window_counts)`) take O(1) time on average.
    *   Therefore, the overall time complexity is linear, O(N).

*   **Space Complexity: O(U)**
    *   `window_counts` stores frequencies for all unique elements within the current window. In the worst case, all elements in `nums` could be unique, so `window_counts` might store up to `N` entries.
    *   Therefore, the space complexity is O(U), where U is the number of unique elements in `nums`. In the worst case, U can be N, so it's O(N).

---