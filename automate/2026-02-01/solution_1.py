To solve the "Range-Constrained Average Subarray" problem, we need to find the shortest non-empty subarray `nums[i...j]` that satisfies two conditions:
1.  **Average is K**: `sum(nums[i...j]) / (j - i + 1) == K`. This can be rewritten as `sum(nums[i...j]) == K * (j - i + 1)`. Further manipulation gives `sum(nums[x] - K for x in i...j) == 0`.
2.  **Range Constraint**: All elements `nums[x]` within `[i...j]` must satisfy `min_val <= nums[x] <= max_val`.

The second condition is critical. If any element `nums[x]` is outside the `[min_val, max_val]` range, then any subarray containing `nums[x]` is invalid. This means we can effectively split the original array `nums` into several contiguous "valid blocks" separated by elements that violate the range constraint. We then need to solve the first condition independently for each valid block and find the overall shortest subarray.

### Algorithm Breakdown

1.  **Iterate and Identify Valid Blocks**:
    *   Initialize `min_overall_length = infinity`.
    *   Maintain `current_block_start`, which marks the beginning of the current contiguous segment where all elements satisfy the range constraint.
    *   Iterate through `nums` with index `j`.
    *   If `nums[j]` is *outside* `[min_val, max_val]`:
        *   The current valid block ends at `j-1`. If `current_block_start < j` (meaning the block is non-empty), call a helper function `_process_block` on `nums[current_block_start ... j-1]`.
        *   Update `min_overall_length` with the result from `_process_block`.
        *   Reset `current_block_start = j + 1` to start a new potential block after the invalid element.
    *   After the loop, there might be a remaining valid block from `current_block_start` to `n-1`. Process this block if `current_block_start < n`.

2.  **`_process_block` Function (for a single valid block)**:
    *   This function takes a slice of `nums` (defined by `block_start` and `block_end`), and `K`. All elements in this slice are guaranteed to be within `[min_val, max_val]`.
    *   The goal is to find the shortest subarray `nums[i...j]` (where `block_start <= i <= j <= block_end`) such that `sum(nums[x] - K for x in i...j) == 0`.
    *   This is a classic prefix sum problem:
        *   Let `b[x] = nums[x] - K`. We need to find `sum(b[i...j]) == 0`.
        *   Define `P[k]` as the cumulative sum of `b` up to index `k-1` (i.e., `P[k] = sum(b[0...k-1])`). Then `sum(b[i...j]) = P[j+1] - P[i]`.
        *   So we are looking for `P[j+1] == P[i]`.
        *   Use a hash map, `prefix_sum_to_index`, to store `(current_prefix_sum: index)`. The `index` stored will be the *first* index `p` such that `P[p+1]` equals `current_prefix_sum`.
        *   Initialize `prefix_sum_to_index = {0: block_start - 1}`. This signifies that a prefix sum of 0 exists conceptually *before* the `block_start` element. This handles cases where a subarray starting at `block_start` itself satisfies the sum-to-zero condition.
        *   Initialize `current_sum_minus_K = 0` and `segment_min_len = infinity`.
        *   Iterate `j` from `block_start` to `block_end`:
            *   Add `(nums[j] - K)` to `current_sum_minus_K`.
            *   If `current_sum_minus_K` is found in `prefix_sum_to_index`:
                *   Let `i = prefix_sum_to_index[current_sum_minus_K]`. This `i` is the index *before* which the same sum was achieved.
                *   The subarray `nums[i+1 ... j]` has `sum(nums[x]-K) == 0`.
                *   The length is `j - i`. Update `segment_min_len = min(segment_min_len, j - i)`.
            *   If `current_sum_minus_K` is *not* in `prefix_sum_to_index`, add it: `prefix_sum_to_index[current_sum_minus_K] = j`. (We only store the *first* occurrence to ensure we find the shortest length).
        *   Return `segment_min_len`.

3.  **Final Result**:
    *   If `min_overall_length` remains `infinity`, no such subarray exists, so return -1.
    *   Otherwise, return `min_overall_length`.

### Example Walkthrough (from problem statement)

`nums = [10, 2, 5, 8, 30, 4]`, `K = 5`, `min_val = 1`, `max_val = 10`

1.  `min_overall_length = infinity`, `current_block_start = 0`.
2.  **`j = 0` to `3`**: `nums[0]=10, nums[1]=2, nums[2]=5, nums[3]=8` are all in `[1, 10]`.
3.  **`j = 4`**: `nums[4]=30`. This is `OUT` of range `[1, 10]`.
    *   A valid block `nums[0...3]` exists (`current_block_start=0 < j=4`).
    *   Call `_process_block(nums, 5, 0, 3)`:
        *   `segment_min_len = infinity`, `current_sum_minus_K = 0`, `prefix_sum_to_index = {0: -1}`.
        *   `j_internal = 0` (`nums[0]=10`): `current_sum_minus_K = 5`. `prefix_sum_to_index = {0: -1, 5: 0}`.
        *   `j_internal = 1` (`nums[1]=2`): `current_sum_minus_K = 2`. `prefix_sum_to_index = {0: -1, 5: 0, 2: 1}`.
        *   `j_internal = 2` (`nums[2]=5`): `current_sum_minus_K = 2`. `2` is in map. `i = prefix_sum_to_index[2] = 1`. `length = 2 - 1 = 1`. `segment_min_len = min(infinity, 1) = 1`. (Don't update map as `2` already present).
        *   `j_internal = 3` (`nums[3]=8`): `current_sum_minus_K = 5`. `5` is in map. `i = prefix_sum_to_index[5] = 0`. `length = 3 - 0 = 3`. `segment_min_len = min(1, 3) = 1`. (Don't update map).
        *   `_process_block` returns `1`.
    *   `min_overall_length = min(infinity, 1) = 1`.
    *   `current_block_start = 4 + 1 = 5`.
4.  **`j = 5`**: `nums[5]=4`. This is `IN` range `[1, 10]`.
5.  Loop ends.
6.  Remaining block check: `current_block_start = 5 < n=6`.
    *   Call `_process_block(nums, 5, 5, 5)`:
        *   `segment_min_len = infinity`, `current_sum_minus_K = 0`, `prefix_sum_to_index = {0: 4}`.
        *   `j_internal = 5` (`nums[5]=4`): `current_sum_minus_K = -1`. `prefix_sum_to_index = {0: 4, -1: 5}`.
        *   `_process_block` returns `infinity`.
    *   `min_overall_length = min(1, infinity) = 1`.
7.  Return `1`.

This matches the example output.

### Constraints & Data Types

*   `nums.length` up to `10^5`.
*   `nums[i]` and `K` up to `10^9`.
*   `current_sum_minus_K` can accumulate up to `10^5 * 10^9 = 10^14`, which fits within Python's arbitrary-precision integers.

### Complexity

*   **Time Complexity**: O(N), where N is the length of `nums`. Each element is visited a constant number of times (once in the main loop, and once in `_process_block` across all calls). Hash map operations are O(1) on average.
*   **Space Complexity**: O(N). In the worst case, the `prefix_sum_to_index` hash map could store up to N distinct prefix sums.

```python
import math

class Solution:
    def range_constrained_average_subarray(self, nums: list[int], K: int, min_val: int, max_val: int) -> int:
        """
        Finds the length of the shortest non-empty subarray whose average is K
        and all elements are within [min_val, max_val].

        The problem transforms into finding a subarray [i...j] such that:
        1. sum(nums[i...j]) / (j - i + 1) == K
           This simplifies to sum(nums[i...j]) == K * (j - i + 1),
           or sum(nums[x] - K for x in i...j) == 0.
        2. All elements nums[x] within [i...j] satisfy min_val <= nums[x] <= max_val.

        The second condition means we can only consider subarrays that lie entirely
        within contiguous segments of `nums` where all elements meet the range constraint.
        Any element outside [min_val, max_val] acts as a separator.

        Args:
            nums: The input array of integers.
            K: The target average.
            min_val: The minimum allowed value for elements in the subarray.
            max_val: The maximum allowed value for elements in the subarray.

        Returns:
            The length of the shortest such subarray, or -1 if no such subarray exists.
        """
        n = len(nums)
        min_overall_length = math.inf

        current_block_start = 0
        for j in range(n):
            # Check if current element violates the range constraint
            if not (min_val <= nums[j] <= max_val):
                # If there was a valid block ending at j-1, process it
                # current_block_start < j ensures the block is non-empty
                if current_block_start < j:
                    length_in_block = self._process_block(nums, K, current_block_start, j - 1)
                    min_overall_length = min(min_overall_length, length_in_block)
                # An invalid element breaks the current valid block.
                # Start searching for a new valid block from the next element.
                current_block_start = j + 1
        
        # After the loop, process any remaining valid block that extends to the end of the array.
        # This handles cases where the last element(s) are valid.
        if current_block_start < n:
            length_in_block = self._process_block(nums, K, current_block_start, n - 1)
            min_overall_length = min(min_overall_length, length_in_block)

        # If min_overall_length is still infinity, no valid subarray was found.
        return int(min_overall_length) if min_overall_length != math.inf else -1

    def _process_block(self, nums: list[int], K: int, block_start: int, block_end: int) -> int:
        """
        Helper function to find the shortest subarray with average K within a valid block.
        All elements in nums[block_start...block_end] are guaranteed to be within [min_val, max_val].

        This function uses the prefix sum technique. We're looking for a subarray `nums[i...j]`
        within the block such that `sum(nums[x] - K for x in i...j) == 0`.
        This is equivalent to `P[j+1] - P[i] == 0`, where `P[k]` is the prefix sum
        of `(nums[x]-K)` up to `x=k-1`. So, `P[j+1] == P[i]`.

        We use a hash map to store the *first* occurrence of each prefix sum encountered.
        When a current prefix sum `current_sum_minus_K` is found in the map, it means
        we've found a subarray whose sum (of `nums[x]-K`) is zero. The length of this subarray
        is `j - i`, where `i` is the index *before* which that same prefix sum was last seen.

        Args:
            nums: The input array.
            K: The target average.
            block_start: The starting index of the current valid block (inclusive).
            block_end: The ending index of the current valid block (inclusive).

        Returns:
            The length of the shortest such subarray within this block, or math.inf if none found.
        """
        segment_min_len = math.inf
        current_sum_minus_K = 0
        
        # prefix_sum_to_index maps a prefix sum value to the *index* (relative to original array)
        # *before* which that sum was achieved.
        # {0: block_start - 1} initializes the map. It signifies that a sum of 0 exists
        # logically before the first element of the current block (at index `block_start - 1`).
        # This allows detection of subarrays starting at `block_start` itself, e.g., if `nums[block_start] - K == 0`.
        prefix_sum_to_index = {0: block_start - 1}

        for j in range(block_start, block_end + 1):
            # Calculate the cumulative sum of (nums[x] - K) for elements up to index j
            current_sum_minus_K += (nums[j] - K)

            # If current_sum_minus_K is already in the map, it means we found a subarray
            # with a sum of 0 for (nums[x] - K) values.
            # The subarray starts at `i + 1` and ends at `j`.
            if current_sum_minus_K in prefix_sum_to_index:
                # `i` is the index *before* which this `current_sum_minus_K` was previously accumulated.
                i = prefix_sum_to_index[current_sum_minus_K]
                length = j - i  # Length of the subarray nums[i+1 ... j]
                segment_min_len = min(segment_min_len, length)
            
            # Store the *first* occurrence of this prefix sum.
            # We only add to the map if `current_sum_minus_K` has not been seen before.
            # This is critical for finding the *shortest* subarray. If a sum repeats,
            # using the index of its first occurrence will always yield a shorter
            # or equal length subarray when `current_sum_minus_K` is matched later.
            if current_sum_minus_K not in prefix_sum_to_index:
                prefix_sum_to_index[current_sum_minus_K] = j
                
        return segment_min_len

```