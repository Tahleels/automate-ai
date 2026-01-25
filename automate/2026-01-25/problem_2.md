Here's a unique DSA problem:

---

### 1. Title
**Smart Text Editor**

### 2. Problem Statement
You are tasked with implementing a simplified text editor that supports three types of operations. The editor starts with an empty string. You need to process a given sequence of operations represented as a string `s` and return the final state of the editor's string.

The operations are:
1.  **Lowercase English letters (`'a'-'z'`):** Append the character to the current string.
2.  **`'#'` (Backspace):** If the current string is not empty, delete the last character. If the string is empty, this operation does nothing.
3.  **`'@'` (Undo):** Reverse the effect of the *last successful character modification*.
    *   If the last successful modification was adding a character `C` (by typing a letter), `C` is removed from the string.
    *   If the last successful modification was deleting a character `C` (by using '#'), `C` is re-added to the string.
    *   If there were no prior successful character modifications to undo, or if the last operation was an '@' or a failed '#' (on an empty string), this operation does nothing.

A "successful character modification" is defined as any operation that actually alters the content of the editor's string (e.g., adding 'a', or deleting 'b' with '#'). Operations that do not change the string (like '#' on an empty string, or '@' when there's nothing to undo) are not considered successful modifications and do not count towards the "last successful modification" for future '@' operations.

### 3. Constraints
*   `1 <= s.length <= 10^5`
*   `s` consists of lowercase English letters, `'#'`, and `'@'`.

### 4. Example

**Input:**
`s = "ab#c@de"`

**Trace and Output:**

Let's simulate the editor's state and history:

| Step | Character | Current String Stack | History Stack (Op, Char) | Explanation                                                                                                 |
| :--- | :-------- | :------------------- | :----------------------- | :---------------------------------------------------------------------------------------------------------- |
| 1    | `'a'`     | `['a']`              | `[('ADD', 'a')]`         | Add 'a'. Record `ADD 'a'`.                                                                                  |
| 2    | `'b'`     | `['a', 'b']`         | `[('ADD', 'a'), ('ADD', 'b')]` | Add 'b'. Record `ADD 'b'`.                                                                                  |
| 3    | `'#'`     | `['a']`              | `[('ADD', 'a'), ('ADD', 'b'), ('DELETE', 'b')]` | Backspace removes 'b'. Record `DELETE 'b'`.                                                                 |
| 4    | `'c'`     | `['a', 'c']`         | `[('ADD', 'a'), ('ADD', 'b'), ('DELETE', 'b'), ('ADD', 'c')]` | Add 'c'. Record `ADD 'c'`.                                                                                  |
| 5    | `'@'`     | `['a', 'b']`         | `[('ADD', 'a'), ('ADD', 'b'), ('DELETE', 'b')]` | Undo. Last successful modification was `ADD 'c'`. So, remove 'c'. History stack pops `('ADD', 'c')`. String stack pops 'c'. |
| 6    | `'d'`     | `['a', 'b', 'd']`    | `[('ADD', 'a'), ('ADD', 'b'), ('DELETE', 'b'), ('ADD', 'd')]` | Add 'd'. Record `ADD 'd'`.                                                                                  |
| 7    | `'e'`     | `['a', 'b', 'd', 'e']` | `[('ADD', 'a'), ('ADD', 'b'), ('DELETE', 'b'), ('ADD', 'd'), ('ADD', 'e')]` | Add 'e'. Record `ADD 'e'`.                                                                                  |

**Final string:** `"abde"`

---