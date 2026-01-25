The problem asks us to find the number of ways to split an array `nums` into two non-empty contiguous subarrays, `left` and `right`, such that the number of distinct elements in `left` is equal to the number of distinct elements in `right`.

A split point `i` defines `left = nums[0...i]` and `right = nums[i+1...n-1]`, where `n` is the length of `nums`.

**Constraints Analysis:**
- `1 <= nums.length <= 10^5`: This suggests that an `O(N^2)` solution would be too slow (`10^{10}` operations). We need an `O(N)` or `O(N log N)` solution.
- `0 <= nums[i] <= 10^9`: The values can be large, so we should use data structures that handle arbitrary integer values efficiently, like Python's `set`.

**Naive Approach (and why it's too slow):**
A straightforward approach would be to iterate through all possible split points `i` from `0` to `n-2` (to ensure both `left` and `right` subarrays are non-empty). For each `i`:
1. Extract `left_subarray = nums[0:i+1]`.
2. Extract `right_subarray = nums[i+1:n]`.
3. Calculate `distinct_left = len(set(left_subarray))`.
4. Calculate `distinct_right = len(set(right_subarray))`.
5. If `distinct_left == distinct_right`, increment a counter.

Calculating distinct elements using a `set` takes `O(length_of_subarray)` time. Since `left_subarray` and `right_subarray` can each be up to `O(N)` elements long, each split point takes `O(N)` time. With `N-1` possible split points, the total time complexity becomes `O(N^2)`, which is too slow for `N=10^5`.

**Optimized Approach (Prefix and Suffix Distinct Counts):**
To achieve `O(N)` time complexity, we can precompute the number of distinct elements for all possible prefix and suffix subarrays.

1.  **Precompute Prefix Distinct Counts:**
    Create an array `prefix_distinct` of size `N`. `prefix_distinct[k]` will store the number of distinct elements in `nums[0...k]`.
    We can populate this array by iterating from `i = 0` to `n-1`, maintaining a `set` of elements encountered so far. For each `i`, add `nums[i]` to the set, and `prefix_distinct[i]` will be the current size of the set.
    This step takes `O(N)` time and `O(N)` space (for the `prefix_distinct` array and the `set`).

2.  **Precompute Suffix Distinct Counts:**
    Similarly, create an array `suffix_distinct` of size `N`. `suffix_distinct[k]` will store the number of distinct elements in `nums[k...n-1]`.
    We can populate this array by iterating *backwards* from `i = n-1` down to `0`, maintaining a `set` of elements encountered so far. For each `i`, add `nums[i]` to the set, and `suffix_distinct[i]` will be the current size of the set.
    This step also takes `O(N)` time and `O(N)` space.

3.  **Iterate and Compare:**
    After precomputation, we can iterate through all valid split points `i`.
    A split at index `i` means:
    - The `left` subarray is `nums[0...i]`. Its distinct count is `prefix_distinct[i]`.
    - The `right` subarray is `nums[i+1...n-1]`. Its distinct count is `suffix_distinct[i+1]`.

    The `left` subarray must be non-empty, which means `i` must be at least `0`.
    The `right` subarray must be non-empty, which means `i+1` must be at most `n-1`, so `i` must be at most `n-2`.
    Therefore, we iterate `i` from `0` to `n-2`.
    For each `i`, we compare `prefix_distinct[i]` with `suffix_distinct[i+1]`. If they are equal, we increment our `valid_splits_count`.

    This final comparison step takes `O(N)` time.

**Total Complexity:**
-   **Time Complexity:** `O(N)` for prefix calculation + `O(N)` for suffix calculation + `O(N)` for comparison = **`O(N)`**.
-   **Space Complexity:** `O(N)` for `prefix_distinct` array + `O(N)` for `suffix_distinct` array + `O(N)` for sets used in precomputation = **`O(N)`**.

This optimized approach meets the requirements for the given constraints.

**Example Walkthrough (from problem statement):**
`nums = [1, 2, 1, 3, 2]`

1.  **Prefix Distinct Counts (`prefix_distinct`):**
    -   `i=0`: `nums[0]=1`. `set={1}`. `prefix_distinct[0]=1`.
    -   `i=1`: `nums[1]=2`. `set={1,2}`. `prefix_distinct[1]=2`.
    -   `i=2`: `nums[2]=1`. `set={1,2}`. `prefix_distinct[2]=2`.
    -   `i=3`: `nums[3]=3`. `set={1,2,3}`. `prefix_distinct[3]=3`.
    -   `i=4`: `nums[4]=2`. `set={1,2,3}`. `prefix_distinct[4]=3`.
    `prefix_distinct = [1, 2, 2, 3, 3]`

2.  **Suffix Distinct Counts (`suffix_distinct`):**
    -   `i=4`: `nums[4]=2`. `set={2}`. `suffix_distinct[4]=1`.
    -   `i=3`: `nums[3]=3`. `set={2,3}`. `suffix_distinct[3]=2`.
    -   `i=2`: `nums[2]=1`. `set={1,2,3}`. `suffix_distinct[2]=3`.
    -   `i=1`: `nums[1]=2`. `set={1,2,3}`. `suffix_distinct[1]=3`.
    -   `i=0`: `nums[0]=1`. `set={1,2,3}`. `suffix_distinct[0]=3`.
    `suffix_distinct = [3, 3, 3, 2, 1]`

3.  **Iterate and Compare:**
    `valid_splits_count = 0`
    Possible `i` values: `0, 1, 2, 3` (since `n=5`, `i` goes up to `n-2 = 3`).
    -   `i=0`: `prefix_distinct[0]` (1) vs `suffix_distinct[1]` (3). Not equal.
    -   `i=1`: `prefix_distinct[1]` (2) vs `suffix_distinct[2]` (3). Not equal.
    -   `i=2`: `prefix_distinct[2]` (2) vs `suffix_distinct[3]` (2). Equal! `valid_splits_count = 1`.
    -   `i=3`: `prefix_distinct[3]` (3) vs `suffix_distinct[4]` (1). Not equal.
    Return `1`.

This matches the example output.

```python
import collections

class Solution:
    def balancedUniqueSplit(self, nums: list[int]) -> int:
        """
        Calculates the number of ways to split an array into two non-empty
        contiguous subarrays (left and right) such that the number of distinct
        elements in 'left' equals the number of distinct elements in 'right'.

        Args:
            nums: A list of integers.

        Returns:
            The total count of valid split points.
        """
        n = len(nums)

        # Base case: To split into two non-empty subarrays, we need at least 2 elements.
        # If n=1, left=nums[0] and right would be empty, which is not allowed.
        if n < 2:
            return 0

        # --- Step 1: Precompute prefix distinct counts ---
        # `prefix_distinct[i]` stores the number of unique elements
        # in the subarray `nums[0...i]`.
        prefix_distinct = [0] * n
        seen_elements_left = set()
        for i in range(n):
            seen_elements_left.add(nums[i])
            prefix_distinct[i] = len(seen_elements_left)

        # --- Step 2: Precompute suffix distinct counts ---
        # `suffix_distinct[i]` stores the number of unique elements
        # in the subarray `nums[i...n-1]`.
        suffix_distinct = [0] * n
        seen_elements_right = set()
        # Iterate backwards from the end of the array to the beginning
        for i in range(n - 1, -1, -1):
            seen_elements_right.add(nums[i])
            suffix_distinct[i] = len(seen_elements_right)

        # --- Step 3: Iterate through all possible split points and compare counts ---
        # A split point `i` means:
        #   - The `left` subarray is `nums[0]` to `nums[i]`.
        #   - The `right` subarray is `nums[i+1]` to `nums[n-1]`.
        #
        # Both subarrays must be non-empty.
        # - `left` is non-empty if `i >= 0`. This is always true for loop values.
        # - `right` is non-empty if `i+1 <= n-1`, which simplifies to `i <= n-2`.
        # So, valid split points `i` range from `0` to `n-2`.
        
        valid_splits_count = 0
        # The loop iterates `i` from 0 up to `n-2` (inclusive).
        # For example, if n=2, range(1) means i=0.
        #   left = nums[0], right = nums[1]. This is the only valid split.
        for i in range(n - 1): 
            # Number of distinct elements in the left subarray (nums[0...i])
            num_distinct_left = prefix_distinct[i]
            
            # Number of distinct elements in the right subarray (nums[i+1...n-1])
            num_distinct_right = suffix_distinct[i + 1]
            
            # Check if the counts of distinct elements are equal
            if num_distinct_left == num_distinct_right:
                valid_splits_count += 1
                
        return valid_splits_count

```