Here's a unique DSA problem:

---

### 1. Title: Longest Subarray with Unique Element Frequencies

### 2. Problem Statement:

Given an array of integers `nums`, find the length of the longest contiguous subarray `[nums[left], ..., nums[right]]` such that for every unique number `X` present in that subarray, its frequency (count) within that subarray is unique among all other distinct numbers' frequencies in the same subarray.

In simpler terms: If a valid subarray contains distinct numbers $X_1, X_2, \ldots, X_k$ with frequencies $F_1, F_2, \ldots, F_k$ respectively, then all frequencies $F_1, F_2, \ldots, F_k$ must be distinct. For example, if $X_1$ appears 2 times and $X_2$ appears 2 times, this would be invalid because the frequency `2` is not unique (it's shared by $X_1$ and $X_2$).

### 3. Constraints:

*   $1 \le nums.length \le 10^5$
*   $1 \le nums[i] \le 10^9$ (The values of numbers can be large, but the number of distinct elements in the array is at most `nums.length`).

### 4. Example:

**Input:**
`nums = [1, 2, 1, 3, 2, 4]`

**Expected Output:**
`3`

**Explanation:**

Let's analyze some subarrays and their validity:

*   `[1]`
    *   Numbers & Frequencies: `{1:1}`
    *   Set of Frequencies: `{1}`
    *   Valid. Length = 1.

*   `[1, 2]`
    *   Numbers & Frequencies: `{1:1, 2:1}`
    *   Set of Frequencies: `{1, 1}` (Frequency `1` is present for both `1` and `2`)
    *   Invalid (frequency `1` is not unique).

*   `[1, 1]`
    *   Numbers & Frequencies: `{1:2}`
    *   Set of Frequencies: `{2}`
    *   Valid. Length = 2.

*   `[1, 2, 1]`
    *   Numbers & Frequencies: `{1:2, 2:1}`
    *   Set of Frequencies: `{2, 1}` (Frequency `2` for number `1`, Frequency `1` for number `2`)
    *   Valid (all frequencies in the set `{1, 2}` are distinct). Length = 3.

*   `[1, 1, 2, 2]`
    *   Numbers & Frequencies: `{1:2, 2:2}`
    *   Set of Frequencies: `{2, 2}` (Frequency `2` is present for both `1` and `2`)
    *   Invalid (frequency `2` is not unique).

For the given `nums = [1, 2, 1, 3, 2, 4]`:
The longest valid subarray is `[1, 2, 1]`, which has a length of 3.
Other valid subarrays like `[2, 3]` (frequencies `{1, 1}` -> invalid) or `[2, 4, 4]` (frequencies `{1, 2}` -> valid, length 3).
Subarray `[2,4,4]` has `num_freq = {2:1, 4:2}`. Frequencies are `{1,2}`. Valid. Length 3.
There might be multiple subarrays of maximal length. We just need to return the length.