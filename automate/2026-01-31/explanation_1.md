The problem asks us to find the longest subarray that satisfies two conditions simultaneously: it must be "alternating" and "balanced".

Let's break down these conditions and the solution approach.

### 1. Understanding the Conditions

*   **Alternating Subarray**: A subarray `[a, b, c, ...]` is alternating if `a != b`, `b != c`, and so on. In other words, no two adjacent elements are equal. A single-element subarray is always alternating.
*   **Balanced Subarray**: A subarray is balanced if the count of even numbers equals the count of odd numbers within it.

### 2. Core Idea: Decomposing the Problem

The solution leverages two key observations to efficiently tackle both conditions:

#### a. Breaking Down by Alternating Property

The alternating property (`nums[i] != nums[i+1]`) is local. If at any point `nums[i] == nums[i+1]`, then any subarray that includes both `nums[i]` and `nums[i+1]` *cannot* be alternating. This acts as a **hard break point**.

This observation allows us to decompose the original array into several **maximal alternating segments**. For example, in `[1, 2, 2, 3, 4]`, the `2, 2` break point means `[1, 2]` is one maximal alternating segment, and `[2, 3, 4]` is another. We can process each such segment independently. Any subarray *within* a maximal alternating segment is guaranteed to be alternating. Our problem then reduces to: for each maximal alternating segment, find the longest *balanced* subarray within it, and then take the maximum length across all segments.

#### b. Solving for Balanced Subarrays within a Segment (Zero-Sum Problem)

Once we have an alternating segment, we need to find the longest balanced subarray within it.
The "balanced" condition (equal count of even and odd numbers) can be rephrased as a "zero-sum" problem:
*   Represent each even number as `+1`.
*   Represent each odd number as `-1`.
*   A subarray is balanced if the sum of these `+1`s and `-1`s within it is `0`.

This is a classic problem: **find the longest subarray with a sum of zero**. It's efficiently solved using prefix sums and a hash map (dictionary).
We maintain a `current_sum` as we iterate through the segment. If `current_sum` is `S` at index `k_rel`, and we had previously encountered `S` at index `prev_k_rel`, then the subarray from `prev_k_rel + 1` to `k_rel` has a sum of `0` (i.e., `S - S = 0`). The length of this subarray is `k_rel - prev_k_rel`. We store the *first* occurrence of each `current_sum` to ensure we calculate the longest possible subarray.

### 3. Detailed Algorithm

The solution combines these two ideas:

1.  **Initialize `overall_max_len = 0`**. This will store our final answer.
2.  **Initialize `start_idx = 0`**. This pointer marks the beginning of the current maximal alternating segment.
3.  **Iterate `i` from `0` to `n-1` (where `n` is `len(nums)`)**:
    *   At each `i`, we check if `i` is the last element of the array (`i == n - 1`) OR if `nums[i] == nums[i+1]`. If either is true, it means `nums[i]` is the end of the current maximal alternating segment (which runs from `start_idx` to `i`).
    *   **Process the segment `nums[start_idx : i+1]`**:
        *   Initialize `current_max_len_block = 0` for this segment.
        *   Initialize `current_sum = 0`.
        *   Initialize a hash map `sum_map = {0: -1}`. This map stores `(prefix_sum: relative_index)` pairs. The `0: -1` entry is crucial: if a subarray starting from the beginning of the segment (relative index 0) has a sum of 0, `current_sum` will become 0, and `k_rel - sum_map[0]` will correctly give its length.
        *   **Iterate `k_rel` from `0` to `i - start_idx`**: (This `k_rel` is the 0-based index *within* the current segment).
            *   Get the actual value `val = nums[start_idx + k_rel]`.
            *   Update `current_sum`: `current_sum += (1 if val % 2 == 0 else -1)`.
            *   **Check `sum_map`**:
                *   If `current_sum` is already in `sum_map`: A balanced subarray is found. Its length is `k_rel - sum_map[current_sum]`. Update `current_max_len_block = max(current_max_len_block, length)`.
                *   Else (if `current_sum` is new for this segment): Store `sum_map[current_sum] = k_rel`. (We store the first occurrence to find the longest subarray).
        *   After processing the entire segment, update `overall_max_len = max(overall_max_len, current_max_len_block)`.
    *   **Update `start_idx`**: Set `start_idx = i + 1` to mark the beginning of the next potential alternating segment.
4.  **Return `overall_max_len`**.

### 4. Example Walkthrough (`nums = [1, 2, 2, 3, 4]`)

1.  `overall_max_len = 0`, `start_idx = 0`.

2.  **`i = 0`**: `nums[0]=1`, `nums[1]=2`. `nums[0] != nums[1]`. No break.
3.  **`i = 1`**: `nums[1]=2`, `nums[2]=2`. `nums[1] == nums[2]`. **BREAK POINT!**
    *   Process segment `nums[0:2]` (`[1, 2]`).
    *   `current_max_len_block = 0`, `current_sum = 0`, `sum_map = {0: -1}`.
    *   `k_rel = 0` (for `nums[0]=1`): `val=1` (odd). `current_sum = -1`. `sum_map = {0: -1, -1: 0}`.
    *   `k_rel = 1` (for `nums[1]=2`): `val=2` (even). `current_sum = -1 + 1 = 0`.
        *   `current_sum` (0) is in `sum_map`. `length = 1 - sum_map[0] = 1 - (-1) = 2`.
        *   `current_max_len_block = max(0, 2) = 2`.
    *   End segment processing. `overall_max_len = max(0, 2) = 2`.
    *   `start_idx = 1 + 1 = 2`.

4.  **`i = 2`**: `nums[2]=2`, `nums[3]=3`. `nums[2] != nums[3]`. No break.
5.  **`i = 3`**: `nums[3]=3`, `nums[4]=4`. `nums[3] != nums[4]`. No break.
6.  **`i = 4`**: `i == n - 1`. **END OF ARRAY!**
    *   Process segment `nums[2:5]` (`[2, 3, 4]`).
    *   `current_max_len_block = 0`, `current_sum = 0`, `sum_map = {0: -1}`.
    *   `k_rel = 0` (for `nums[2]=2`): `val=2` (even). `current_sum = 1`. `sum_map = {0: -1, 1: 0}`.
    *   `k_rel = 1` (for `nums[3]=3`): `val=3` (odd). `current_sum = 1 + (-1) = 0`.
        *   `current_sum` (0) is in `sum_map`. `length = 1 - sum_map[0] = 1 - (-1) = 2`.
        *   `current_max_len_block = max(0, 2) = 2`.
    *   `k_rel = 2` (for `nums[4]=4`): `val=4` (even). `current_sum = 0 + 1 = 1`.
        *   `current_sum` (1) is in `sum_map`. `length = 2 - sum_map[1] = 2 - 0 = 2`.
        *   `current_max_len_block = max(2, 2) = 2`.
    *   End segment processing. `overall_max_len = max(2, 2) = 2`.
    *   `start_idx = 4 + 1 = 5`.

7.  Loop finishes. Return `overall_max_len = 2`.

### 5. Complexity Analysis

*   **Time Complexity: O(N)**
    *   The outer `for i in range(n)` loop iterates `N` times.
    *   Inside this loop, when a segment is processed, the inner `for k_rel in range(...)` loop iterates through the elements of that segment.
    *   Crucially, each element of the original `nums` array belongs to exactly one maximal alternating segment. Therefore, the total number of operations performed in all `k_rel` loops combined across all segments will be `N`.
    *   Hash map operations (insertion and lookup) take `O(1)` time on average.
    *   Thus, the total time complexity is linear, `O(N)`.

*   **Space Complexity: O(N)**
    *   In the worst case (e.g., if the entire `nums` array is one single maximal alternating segment, like `[1, 2, 1, 2, ...]`), the `sum_map` could potentially store up to `N` distinct prefix sums.
    *   Therefore, the space complexity is `O(N)`.