Here's a unique DSA problem:

---

### 1. Title
**Distinct Frequency Subarray**

### 2. Problem Statement
Given an array of integers `nums`, find the length of the longest contiguous subarray `[nums[l], nums[l+1], ..., nums[r]]` such that all distinct elements within that subarray appear a distinct number of times.

In simpler terms, for a chosen subarray, calculate the frequency of each unique number present in it. If all these calculated frequencies are themselves unique (i.e., no two distinct numbers in the subarray have the same frequency), then the subarray is valid. Your task is to find the maximum possible length of such a valid subarray.

**Example Explanation:**
- Consider the subarray `[1, 2, 2, 3, 3, 3]`:
  - `1` appears `1` time.
  - `2` appears `2` times.
  - `3` appears `3` times.
  The frequencies are `[1, 2, 3]`. Since `1`, `2`, and `3` are all distinct, this subarray is **valid**.

- Consider the subarray `[1, 2, 2, 3]`:
  - `1` appears `1` time.
  - `2` appears `2` times.
  - `3` appears `1` time.
  The frequencies are `[1, 2, 1]`. Since `1` appears twice in this list of frequencies, this subarray is **not valid**.

### 3. Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- The answer will always be at least 1 (a single-element subarray is always valid, as its only element appears once).

### 4. Example

**Input:**
`nums = [1, 2, 2, 1, 3]`

**Output:**
`3`

**Explanation:**
Let's analyze some subarrays:
- `[1]` : Frequencies: `{1:1}`. Valid. Length 1.
- `[1, 2]` : Frequencies: `{1:1, 2:1}`. The frequencies `[1, 1]` are not distinct. Invalid.
- `[1, 2, 2]` : Frequencies: `{1:1, 2:2}`. The frequencies `[1, 2]` are distinct. Valid. Length 3.
- `[2, 2, 1]` : Frequencies: `{2:2, 1:1}`. The frequencies `[2, 1]` are distinct. Valid. Length 3.
- `[2, 2, 1, 3]` : Frequencies: `{2:2, 1:1, 3:1}`. The frequencies `[2, 1, 1]` are not distinct (1 appears twice). Invalid.
- `[1, 3]` : Frequencies: `{1:1, 3:1}`. The frequencies `[1, 1]` are not distinct. Invalid.

The longest valid subarrays are `[1, 2, 2]` and `[2, 2, 1]`, both of length 3. Therefore, the maximum length is 3.

---