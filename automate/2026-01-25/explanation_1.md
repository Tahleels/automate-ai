The problem asks us to count the number of ways to split an array `nums` into two non-empty contiguous subarrays, `left` and `right`, such that both subarrays have an equal number of unique elements. A split point `i` means `left` is `nums[0...i]` and `right` is `nums[i+1...n-1]`.

---

### 1. Problem Analysis and Constraints

*   `nums.length` up to `10^5`: This is a crucial constraint. An `O(N^2)` solution (where `N` is `nums.length`) would be too slow (`10^{10}` operations). We need an `O(N)` or `O(N log N)` approach.
*   `nums[i]` up to `10^9`: The values can be large, but this doesn't significantly impact the performance of `set` operations (hashing integers is efficient).

### 2. Naive Approach (and why it's inefficient)

A straightforward approach would be to iterate through all possible split points `i` from `0` to `n-2` (to ensure both `left` and `right` are non-empty). For each `i`:
1.  Extract `nums[0...i]` as `left`.
2.  Extract `nums[i+1...n-1]` as `right`.
3.  Calculate the number of distinct elements in `left` using a `set`.
4.  Calculate the number of distinct elements in `right` using a `set`.
5.  If these counts are equal, increment a counter.

**Complexity of Naive Approach:**
*   Each calculation of distinct elements for a subarray takes `O(subarray_length)` time. Since subarrays can be up to `O(N)` length, each split point check takes `O(N)` time.
*   There are `N-1` possible split points.
*   Total time complexity: `O(N * N) = O(N^2)`.
*   For `N=10^5`, this is `10^{10}` operations, which is too slow.

### 3. Optimized Approach: Precomputing Prefix and Suffix Distinct Counts

To achieve an `O(N)` solution, we can precompute the number of distinct elements for all possible prefixes and suffixes of the array. This allows us to determine the distinct counts for any `left` and `right` subarray in `O(1)` time after the initial precomputation.

Here's the detailed breakdown:

#### Step 1: Precompute Prefix Distinct Counts

*   Create an array `prefix_distinct` of size `N`.
*   `prefix_distinct[k]` will store the number of unique elements in the subarray `nums[0...k]`.
*   We iterate from the beginning of `nums` (index `0`) to the end (index `n-1`).
*   Maintain a `set` called `seen_elements_left`.
*   For each index `i`:
    *   Add `nums[i]` to `seen_elements_left`.
    *   `prefix_distinct[i]` is set to `len(seen_elements_left)`.

**Example:** `nums = [1, 2, 1, 3, 2]`
*   `i=0`: `nums[0]=1`. `seen_elements_left = {1}`. `prefix_distinct[0] = 1`.
*   `i=1`: `nums[1]=2`. `seen_elements_left = {1, 2}`. `prefix_distinct[1] = 2`.
*   `i=2`: `nums[2]=1`. `seen_elements_left = {1, 2}`. `prefix_distinct[2] = 2`.
*   `i=3`: `nums[3]=3`. `seen_elements_left = {1, 2, 3}`. `prefix_distinct[3] = 3`.
*   `i=4`: `nums[4]=2`. `seen_elements_left = {1, 2, 3}`. `prefix_distinct[4] = 3`.
Result: `prefix_distinct = [1, 2, 2, 3, 3]`

#### Step 2: Precompute Suffix Distinct Counts

*   Create an array `suffix_distinct` of size `N`.
*   `suffix_distinct[k]` will store the number of unique elements in the subarray `nums[k...n-1]`.
*   We iterate *backwards* from the end of `nums` (index `n-1`) to the beginning (index `0`).
*   Maintain a `set` called `seen_elements_right`.
*   For each index `i` (from `n-1` down to `0`):
    *   Add `nums[i]` to `seen_elements_right`.
    *   `suffix_distinct[i]` is set to `len(seen_elements_right)`.

**Example:** `nums = [1, 2, 1, 3, 2]`
*   `i=4`: `nums[4]=2`. `seen_elements_right = {2}`. `suffix_distinct[4] = 1`.
*   `i=3`: `nums[3]=3`. `seen_elements_right = {2, 3}`. `suffix_distinct[3] = 2`.
*   `i=2`: `nums[2]=1`. `seen_elements_right = {1, 2, 3}`. `suffix_distinct[2] = 3`.
*   `i=1`: `nums[1]=2`. `seen_elements_right = {1, 2, 3}`. `suffix_distinct[1] = 3`.
*   `i=0`: `nums[0]=1`. `seen_elements_right = {1, 2, 3}`. `suffix_distinct[0] = 3`.
Result: `suffix_distinct = [3, 3, 3, 2, 1]`

#### Step 3: Iterate and Compare

Now that we have both `prefix_distinct` and `suffix_distinct` arrays, we can iterate through all valid split points `i` and check the condition in `O(1)` time per split.

*   A split point `i` means the `left` subarray is `nums[0...i]` and the `right` subarray is `nums[i+1...n-1]`.
*   Both subarrays must be non-empty.
    *   `left` is non-empty if `i >= 0`.
    *   `right` is non-empty if `i+1 <= n-1`, which means `i <= n-2`.
*   Therefore, `i` can range from `0` to `n-2`.
*   Initialize `valid_splits_count = 0`.
*   Loop `i` from `0` to `n-2`:
    *   The number of distinct elements in the `left` subarray (`nums[0...i]`) is `prefix_distinct[i]`.
    *   The number of distinct elements in the `right` subarray (`nums[i+1...n-1]`) is `suffix_distinct[i+1]`.
    *   If `prefix_distinct[i] == suffix_distinct[i+1]`, increment `valid_splits_count`.

**Example Walkthrough (Cont.):** `nums = [1, 2, 1, 3, 2]`
`prefix_distinct = [1, 2, 2, 3, 3]`
`suffix_distinct = [3, 3, 3, 2, 1]`

*   `i=0`: `prefix_distinct[0]` (1) vs `suffix_distinct[1]` (3). Not equal.
*   `i=1`: `prefix_distinct[1]` (2) vs `suffix_distinct[2]` (3). Not equal.
*   **`i=2`**: `prefix_distinct[2]` (2) vs `suffix_distinct[3]` (2). **Equal!** `valid_splits_count = 1`.
*   `i=3`: `prefix_distinct[3]` (3) vs `suffix_distinct[4]` (1). Not equal.

Return `valid_splits_count = 1`. This matches the example.

### 4. Complexity Analysis

*   **Time Complexity:**
    *   Step 1 (Prefix Distincts): Iterating through `N` elements and performing `set.add()` and `len(set)` operations. On average, `set.add()` and `len()` are `O(1)`. So, `O(N)`.
    *   Step 2 (Suffix Distincts): Similar to Step 1, `O(N)`.
    *   Step 3 (Comparison): Iterating `N-1` times and performing `O(1)` array lookups and comparison. `O(N)`.
    *   Total Time Complexity: `O(N) + O(N) + O(N) = O(N)`.

*   **Space Complexity:**
    *   `prefix_distinct` array: `O(N)` space.
    *   `suffix_distinct` array: `O(N)` space.
    *   `seen_elements_left` set: At most `O(N)` distinct elements.
    *   `seen_elements_right` set: At most `O(N)` distinct elements.
    *   Total Space Complexity: `O(N) + O(N) + O(N) + O(N) = O(N)`.

This optimized approach satisfies the constraints and provides an efficient solution to the problem.

---
The provided Python code implements this exact optimized strategy.