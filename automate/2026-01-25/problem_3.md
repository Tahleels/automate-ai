Here's a unique DSA problem:

---

### 1. Title
**K-Frequent Subarray**

### 2. Problem Statement
You are given an array of positive integers `nums` and a positive integer `k`.

Your task is to find the shortest *contiguous* subarray `nums[i...j]` such that for *every unique element* `x` present within that subarray `nums[i...j]`, its frequency within `nums[i...j]` is at least `k`.

If no such subarray exists, return -1.

### 3. Constraints
*   `1 <= nums.length <= 10^5`
*   `1 <= nums[i] <= 10^9`
*   `1 <= k <= nums.length`

### 4. Example
**Input:**
`nums = [1, 2, 1, 2]`
`k = 2`

**Output:**
`4`

**Explanation:**

Let's analyze the subarrays of `nums`:
*   `[1]` : Unique element is `1`. Its frequency is `1`. `1 < k (2)`. Invalid.
*   `[1, 2]` : Unique elements are `1, 2`. Frequency of `1` is `1`. Frequency of `2` is `1`. Both `1 < k (2)`. Invalid.
*   `[1, 2, 1]` : Unique elements are `1, 2`. Frequency of `1` is `2`. Frequency of `2` is `1`. `1 < k (2)`. Invalid.
*   `[1, 2, 1, 2]` : Unique elements are `1, 2`. Frequency of `1` is `2`. Frequency of `2` is `2`. Both `2 >= k (2)`. Valid. Length = 4.

In this example, `[1, 2, 1, 2]` is the only subarray that satisfies the condition, and its length is `4`. Therefore, the shortest length is `4`.