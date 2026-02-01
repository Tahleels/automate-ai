Here is a unique DSA problem:

---

### 1. Title
**Range-Constrained Average Subarray**

### 2. Problem Statement
Given an array of integers `nums`, an integer `K`, and a range `[min_val, max_val]`, find the length of the *shortest* non-empty subarray `[i...j]` (where `i <= j`) that satisfies two conditions:

1.  Its average is exactly `K`: `sum(nums[i...j]) / (j - i + 1) == K`.
2.  All elements `nums[x]` within that subarray (for `i <= x <= j`) satisfy `min_val <= nums[x] <= max_val`.

If no such subarray exists, return -1.

### 3. Constraints
*   `1 <= nums.length <= 10^5`
*   `0 <= nums[i] <= 10^9`
*   `1 <= K <= 10^9`
*   `0 <= min_val <= max_val <= 10^9`
*   The sum of elements in a subarray can exceed standard 32-bit integer limits, so use `long long` for sums.

### 4. Example

**Input:**
```
nums = [10, 2, 5, 8, 30, 4]
K = 5
min_val = 1
max_val = 10
```

**Output:**
```
1
```

**Explanation:**

Let's examine subarrays that satisfy the range constraint `[1, 10]` and check their averages:

*   **Subarray `[10]`**:
    *   All elements in range `[1, 10]`.
    *   Sum = 10, Length = 1. Average = 10 / 1 = 10. (Not `K=5`)
*   **Subarray `[2]`**:
    *   All elements in range `[1, 10]`.
    *   Sum = 2, Length = 1. Average = 2 / 1 = 2. (Not `K=5`)
*   **Subarray `[5]`**:
    *   All elements in range `[1, 10]`.
    *   Sum = 5, Length = 1. Average = 5 / 1 = 5. (**Matches `K=5`!**)
    *   This subarray has length **1**.
*   **Subarray `[8]`**:
    *   All elements in range `[1, 10]`.
    *   Sum = 8, Length = 1. Average = 8 / 1 = 8. (Not `K=5`)
*   **Subarray `[30]`**:
    *   Element `30` is **OUT** of range `[1, 10]`. Any subarray containing `30` is invalid.
*   **Subarray `[4]`**:
    *   All elements in range `[1, 10]`.
    *   Sum = 4, Length = 1. Average = 4 / 1 = 4. (Not `K=5`)
*   **Subarray `[10, 2]`**:
    *   All elements in range `[1, 10]`.
    *   Sum = 12, Length = 2. Average = 12 / 2 = 6. (Not `K=5`)
*   **Subarray `[2, 5]`**:
    *   All elements in range `[1, 10]`.
    *   Sum = 7, Length = 2. Average = 7 / 2 = 3.5. (Not `K=5`)
*   **Subarray `[5, 8]`**:
    *   All elements in range `[1, 10]`.
    *   Sum = 13, Length = 2. Average = 13 / 2 = 6.5. (Not `K=5`)
*   **Subarray `[8, 4]`**:
    *   All elements in range `[1, 10]`.
    *   Sum = 12, Length = 2. Average = 12 / 2 = 6. (Not `K=5`)
*   **Subarray `[2, 5, 8]`**:
    *   All elements in range `[1, 10]`.
    *   Sum = 15, Length = 3. Average = 15 / 3 = 5. (**Matches `K=5`!**)
    *   This subarray has length **3**.

Comparing all valid subarrays (those matching `K=5` and meeting range constraints), the shortest length is **1** (from subarray `[5]`).