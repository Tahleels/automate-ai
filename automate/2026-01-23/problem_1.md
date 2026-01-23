Here is a unique DSA problem:

---

### 1. Title: Adjacent Sum Purge

### 2. Problem Statement:

You are given a string `s` consisting only of digits '0' through '9'. You need to process this string by repeatedly applying a specific rule:

If any two *adjacent* digits in the string, say `x` and `y`, have an *even sum* (i.e., `x + y` is an even number), then both `x` and `y` are removed from the string. After removal, the remaining parts of the string are concatenated, and the process continues on the new string. This operation is performed repeatedly until no more such adjacent pairs can be removed.

Your task is to return the final string after all possible eliminations.

**Example Walkthrough:**
Consider `s = "1221"`:
1. Initially, `s = "1221"`.
2. Process from left to right. The first pair `1` and `2` has sum `1+2=3` (odd).
3. The next pair in the original string would be `2` and `2`. Their sum `2+2=4` is even. So, these two `2`s are removed. The string effectively becomes `"11"`.
4. Now `s = "11"`. The pair `1` and `1` has sum `1+1=2` (even). These two `1`s are removed. The string becomes `""`.
5. The string is empty. No more pairs to check or remove.
Final string: `""`.

### 3. Constraints:

*   `1 <= s.length <= 10^5`
*   `s` consists only of digits '0' through '9'.

### 4. Example:

| Input `s` | Output | Explanation (using implicit stack logic)                                            |
| :-------- | :----- | :---------------------------------------------------------------------------------- |
| `"1221"`  | `""`   | `1221` -> `1` then `12` then `1(2+2)` -> `11` -> `(1+1)` -> `""`                   |
| `"4321"`  | `"4321"` | No adjacent pair has an even sum. (4+3=7, 3+2=5, 2+1=3 are all odd).              |
| `"246"`   | `"6"`  | `246` -> `(2+4)6` -> `6`.                                                          |
| `"1357"`  | `"1357"` | All sums are odd.                                                                 |
| `"8802"`  | `""`   | `8802` -> `(8+8)02` -> `02` -> `(0+2)` -> `""`.                                    |
| `"7123"`  | `"23"` | `7123` -> `(7+1)23` -> `23`. (7+1=8 is even, so 7 and 1 are removed. Then 2 and 3 remain). |

---