## Explanation of the Solution

The problem asks for the *shortest* non-empty subarray `[i...j]` that satisfies two conditions:
1.  Its average is exactly `K`: `sum(nums[i...j]) / (j - i + 1) == K`.
2.  All elements `nums[x]` within that subarray are within `[min_val, max_val]`.

### 1. Problem Transformation

The first condition, `sum(nums[i...j]) / (j - i + 1) == K`, can be rewritten as:
`sum(nums[i...j]) == K * (j - i + 1)`

Let `length = j - i + 1`. The equation becomes `sum(nums[i...j]) == K * length`.
This can be further transformed by subtracting `K` from each element:
`sum(nums[i...j]) - sum(K for _ in range(length)) == 0`
`sum(nums[x] - K for x in i...j) == 0`

So, the problem boils down to finding the shortest subarray `[i...j]` such that:
1.  `sum(nums[x] - K for x in i...j) == 0`.
2.  All `nums[x]` in `[i...j]` are within `[min_val, max_val]`.

### 2. Core Idea and Algorithm Breakdown

The key insight comes from the second condition (range constraint). If any element `nums[x]` is outside the `[min_val, max_val]` range, then *any* subarray containing `nums[x]` is invalid. This effectively **splits the original array `nums` into several independent "valid blocks"**. We can process each valid block separately to find the shortest subarray satisfying the conditions within that block, and then take the minimum of these lengths.

The algorithm proceeds in two main steps:

#### Step 1: Identify Valid Blocks (Main Function `range_constrained_average_subarray`)

This step iterates through the `nums` array to find contiguous segments where all elements satisfy `min_val <= nums[x] <= max_val`.

1.  Initialize `min_overall_length = infinity` (to track the shortest length found across all blocks).
2.  Maintain `current_block_start`, an index marking the beginning of the current valid block.
3.  Iterate `j` from `0` to `n-1` (where `n` is `len(nums)`):
    *   If `nums[j]` is *outside* the `[min_val, max_val]` range:
        *   The current valid block (if any) ends at `j-1`. If `current_block_start < j` (meaning the block is non-empty), call the helper function `_process_block` on `nums[current_block_start ... j-1]`.
        *   Update `min_overall_length` with the result from `_process_block`.
        *   Reset `current_block_start = j + 1` to start a new potential block after the invalid element.
4.  After the loop, there might be a remaining valid block extending from `current_block_start` to `n-1`. Process this block if `current_block_start < n`.

#### Step 2: Process Each Valid Block (`_process_block` Helper Function)

This function takes a slice of `nums` (`nums[block_start ... block_end]`) where all elements are guaranteed to be within the `[min_val, max_val]` range. Its goal is to find the shortest subarray `nums[i...j]` within this block such that `sum(nums[x] - K for x in i...j) == 0`. This is a classic "subarray sum equals zero" problem, solved efficiently using prefix sums and a hash map.

1.  Initialize `segment_min_len = infinity`.
2.  Initialize `current_sum_minus_K = 0`. This variable will accumulate the sum of `(nums[x] - K)` for the current prefix.
3.  Initialize a hash map `prefix_sum_to_index = {0: block_start - 1}`.
    *   This map stores `(prefix_sum_value : index)`. The `index` is the position *before* which that `prefix_sum_value` was achieved.
    *   The entry `{0: block_start - 1}` is crucial: it handles cases where a valid subarray *starts* at `block_start` itself (e.g., if `nums[block_start] - K == 0`, then `current_sum_minus_K` becomes 0, and `j - (block_start - 1)` will correctly give the length).
4.  Iterate `j` from `block_start` to `block_end`:
    *   Add `(nums[j] - K)` to `current_sum_minus_K`.
    *   Check if `current_sum_minus_K` is already in `prefix_sum_to_index`:
        *   If yes, it means we found a subarray `nums[i+1 ... j]` whose sum of `(value - K)` is zero. The `i` here is `prefix_sum_to_index[current_sum_minus_K]`.
        *   The length of this subarray is `j - i`. Update `segment_min_len = min(segment_min_len, j - i)`.
    *   If `current_sum_minus_K` is *not* in `prefix_sum_to_index`:
        *   Add it to the map: `prefix_sum_to_index[current_sum_minus_K] = j`.
        *   **Important**: We only store the *first* occurrence of each prefix sum. If a sum `S` has been seen at index `p1` and again at `p2` (`p1 < p2`), and we encounter `S` again at `p3` (`p2 < p3`), then `p3 - p1` will be a longer or equal length compared to `p3 - p2`. To find the *shortest* subarray, we must always use the earliest index for a given prefix sum.
5.  Return `segment_min_len`.

#### Final Result

After processing all blocks, if `min_overall_length` is still `infinity`, it means no such subarray exists, so return -1. Otherwise, return `min_overall_length`.

### Example Walkthrough (from problem statement)

`nums = [10, 2, 5, 8, 30, 4]`, `K = 5`, `min_val = 1`, `max_val = 10`

1.  `min_overall_length = inf`, `current_block_start = 0`.
2.  **`j = 0`**: `nums[0]=10` is in `[1,10]`.
3.  **`j = 1`**: `nums[1]=2` is in `[1,10]`.
4.  **`j = 2`**: `nums[2]=5` is in `[1,10]`.
5.  **`j = 3`**: `nums[3]=8` is in `[1,10]`.
6.  **`j = 4`**: `nums[4]=30` is **OUT** of `[1,10]`.
    *   A valid block `nums[0...3]` exists (`current_block_start=0 < j=4`).
    *   Call `_process_block(nums, 5, 0, 3)`:
        *   `prefix_sum_to_index = {0: -1}`. `current_sum_minus_K = 0`. `segment_min_len = inf`.
        *   `j_internal = 0` (`nums[0]=10`): `current_sum_minus_K = (10-5) = 5`. `prefix_sum_to_index = {0: -1, 5: 0}`.
        *   `j_internal = 1` (`nums[1]=2`): `current_sum_minus_K = 5 + (2-5) = 2`. `prefix_sum_to_index = {0: -1, 5: 0, 2: 1}`.
        *   `j_internal = 2` (`nums[2]=5`): `current_sum_minus_K = 2 + (5-5) = 2`. `2` is in map (`prefix_sum_to_index[2] = 1`). `length = 2 - 1 = 1`. `segment_min_len = min(inf, 1) = 1`.
        *   `j_internal = 3` (`nums[3]=8`): `current_sum_minus_K = 2 + (8-5) = 5`. `5` is in map (`prefix_sum_to_index[5] = 0`). `length = 3 - 0 = 3`. `segment_min_len = min(1, 3) = 1`.
        *   `_process_block` returns `1`.
    *   `min_overall_length = min(inf, 1) = 1`.
    *   `current_block_start = 4 + 1 = 5`.
7.  **`j = 5`**: `nums[5]=4` is in `[1,10]`.
8.  Loop ends.
9.  Post-loop block check: `current_block_start = 5 < n=6`.
    *   Call `_process_block(nums, 5, 5, 5)`:
        *   `prefix_sum_to_index = {0: 4}`. `current_sum_minus_K = 0`. `segment_min_len = inf`.
        *   `j_internal = 5` (`nums[5]=4`): `current_sum_minus_K = (4-5) = -1`. `prefix_sum_to_index = {0: 4, -1: 5}`.
        *   `_process_block` returns `inf`.
    *   `min_overall_length = min(1, inf) = 1`.
10. Final result: `1`.

### Complexity Analysis

*   **Time Complexity: O(N)**
    *   The main loop iterates through the `nums` array once (O(N)).
    *   Inside the loop, calls to `_process_block` are made. Crucially, each element of `nums` is part of *at most one* call to `_process_block`.
    *   Within `_process_block`, another loop iterates through the elements of that specific block once.
    *   Hash map (dictionary in Python) operations (insertion and lookup) take O(1) time on average.
    *   Therefore, the total time complexity is proportional to the number of elements in `nums`, making it O(N).

*   **Space Complexity: O(N)**
    *   In the worst case, all elements of `nums` could be valid and form a single large block.
    *   The `prefix_sum_to_index` hash map could potentially store up to `N` distinct prefix sum values, each mapping to an index.
    *   Thus, the space complexity is O(N) due to the hash map.

### Data Types

The problem statement specifies that sums can exceed standard 32-bit integer limits. Python's integers handle arbitrary precision automatically, so `long long` is implicitly managed. In languages like C++ or Java, `long long` would be required for `current_sum_minus_K` and `K` if calculations like `nums[j] - K` or the cumulative sum could overflow `int`. Given `nums[i]` and `K` up to `10^9` and `N` up to `10^5`, `current_sum_minus_K` could be up to `10^5 * 10^9 = 10^{14}`, which definitely requires a 64-bit integer type.