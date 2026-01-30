Here is a unique DSA problem:

---

### 1. Title
**Token Grouping Score**

### 2. Problem Statement
You are given a string `s` consisting of uppercase English letters (`A-Z`) and an integer `k`. Your task is to calculate the "grouping score" of the string.

The score is calculated by identifying and "removing" consecutive "valid groups" of characters. A "valid group" is defined as a substring `s[i...j]` (from the currently processed string, which is dynamically changing) where:
1. All characters within the substring `s[i...j]` are **distinct**.
2. The length of the substring `s[i...j]` is exactly `k`.

When a valid group is found at the end of the current sequence of characters:
- It is "removed" from the sequence (i.e., conceptually deleted, and the remaining parts of the string are concatenated).
- The grouping score increases by 1.

This process of finding and removing groups is repeated on the modified string until no more valid groups can be formed. The total number of groups removed is the final grouping score.

**Example of removal:** If the current sequence of characters is `X Y Z P Q` and `P Q` forms a valid group, it is removed, and the sequence becomes `X Y Z`. New groups might then form with `Z`.

### 3. Constraints
*   `1 <= s.length <= 10^5`
*   `1 <= k <= 26` (since characters must be distinct, `k` cannot exceed the number of unique English letters)
*   `s` consists only of uppercase English letters (`'A'` through `'Z'`).

### 4. Example

**Example 1:**
*   `s = "ABBCADEF"`
*   `k = 3`

**Explanation:**

We can simulate the process using a stack to keep track of the characters that haven't been removed yet.

1.  Read 'A': `stack = ['A']`
2.  Read 'B': `stack = ['A', 'B']`
3.  Read 'B': `stack = ['A', 'B', 'B']`
    *   The current stack length is 3. Check the last `k=3` elements: `['A', 'B', 'B']`.
    *   Are all characters distinct? No, 'B' appears twice. Not a valid group.
4.  Read 'C': `stack = ['A', 'B', 'B', 'C']`
    *   The current stack length is 4. Check the last `k=3` elements: `['B', 'B', 'C']`.
    *   Are all characters distinct? No, 'B' appears twice. Not a valid group.
5.  Read 'A': `stack = ['A', 'B', 'B', 'C', 'A']`
    *   The current stack length is 5. Check the last `k=3` elements: `['B', 'C', 'A']`.
    *   Are all characters distinct? Yes (`B`, `C`, `A` are all unique).
    *   This is a valid group! Increment `score` to `1`. Pop 3 elements from the stack.
    *   `stack = ['A', 'B']`
6.  Read 'D': `stack = ['A', 'B', 'D']`
    *   The current stack length is 3. Check the last `k=3` elements: `['A', 'B', 'D']`.
    *   Are all characters distinct? Yes (`A`, `B`, `D` are all unique).
    *   This is a valid group! Increment `score` to `2`. Pop 3 elements from the stack.
    *   `stack = []`
7.  Read 'E': `stack = ['E']`
8.  Read 'F': `stack = ['E', 'F']`

End of string. No more groups can be formed.

**Final Score: 2**

---