The problem asks us to simulate a text editor with three operations: appending a character, backspace, and undo. The core challenge lies in correctly implementing the `undo` operation, which must reverse the *last successful character modification*.

### Approach

To handle the operations efficiently, especially the undo feature, we utilize two stack-like data structures:

1.  **`current_text_stack` (Type: `collections.deque`):**
    *   This stack stores the characters that currently form the editor's string.
    *   `collections.deque` (double-ended queue) is chosen because it provides O(1) time complexity for appending (`append`) and removing (`pop`) elements from its ends, making it ideal for simulating a stack.
    *   When a character is appended, it's pushed onto this stack.
    *   When backspace is pressed, the last character is popped from this stack.
    *   When an "undo add" operation occurs, the last character is popped.
    *   When an "undo delete" operation occurs, the character is pushed back onto this stack.

2.  **`history_stack` (Type: `collections.deque`):**
    *   This stack keeps a record of every *successful character modification*.
    *   Each entry in this stack is a tuple: `(operation_type, character_involved)`.
        *   `operation_type` can be `OP_ADD` (for character additions) or `OP_DELETE` (for character deletions via backspace).
        *   `character_involved` is the character that was either added or deleted.
    *   This stack is crucial for the `undo` operation. When `@` is encountered, we look at the top of this stack to determine what action to reverse.

### Operation Logic Breakdown

We iterate through the input string `s` character by character:

1.  **Lowercase English letters (`'a'-'z'`):**
    *   The character is appended to `current_text_stack`.
    *   A record `(OP_ADD, char)` is pushed onto `history_stack`. This is always a successful modification.

2.  **`'#'` (Backspace):**
    *   **If `current_text_stack` is not empty:**
        *   The last character is popped from `current_text_stack`.
        *   A record `(OP_DELETE, removed_char)` is pushed onto `history_stack`. This is a successful modification.
    *   **If `current_text_stack` is empty:**
        *   The operation does nothing. No record is added to `history_stack` because it wasn't a successful modification.

3.  **`'@'` (Undo):**
    *   **If `history_stack` is not empty (i.e., there's something to undo):**
        *   The last recorded modification `(op_type, char_involved)` is popped from `history_stack`.
        *   **If `op_type` was `OP_ADD`:** This means `char_involved` was previously added. To reverse this, we pop the last character from `current_text_stack`. (Since characters are always added to the end, undoing an add means removing from the end).
        *   **If `op_type` was `OP_DELETE`:** This means `char_involved` was previously deleted. To reverse this, we re-append `char_involved` to `current_text_stack`.
    *   **If `history_stack` is empty:**
        *   The operation does nothing. No record is added to `history_stack` because it wasn't a successful modification.

Finally, after processing all operations, the characters in `current_text_stack` are joined to form the final string.

### Example Trace (`s = "ab#c@de"`) and Discrepancy

Let's trace `s = "ab#c@de"` with the strict logic:

| Step | Char | `current_text_stack` | `history_stack`                  | Explanation                                     |
| :--- | :--- | :------------------- | :------------------------------- | :---------------------------------------------- |
| Initial |      | `[]`                 | `[]`                             | Editor starts empty.                            |
| 1    | `a`  | `['a']`              | `[('ADD', 'a')]`                 | Add 'a'.                                        |
| 2    | `b`  | `['a', 'b']`         | `[('ADD', 'a'), ('ADD', 'b')]`   | Add 'b'.                                        |
| 3    | `#`  | `['a']`              | `[('ADD', 'a'), ('ADD', 'b'), ('DELETE', 'b')]` | Backspace: pops 'b'. Record `DELETE 'b'`.      |
| 4    | `c`  | `['a', 'c']`         | `[..., ('DELETE', 'b'), ('ADD', 'c')]` | Add 'c'.                                        |
| 5    | `@`  | `['a']`              | `[('ADD', 'a'), ('ADD', 'b'), ('DELETE', 'b')]` | Undo: Pops `('ADD', 'c')`. Reverse by popping 'c' from current text. |
| 6    | `d`  | `['a', 'd']`         | `[..., ('DELETE', 'b'), ('ADD', 'd')]` | Add 'd'.                                        |
| 7    | `e`  | `['a', 'd', 'e']`    | `[..., ('ADD', 'd'), ('ADD', 'e')]` | Add 'e'.                                        |

**Final string (by strict logic):** `"ade"`

**Note on Example Discrepancy:** The problem's example output for `"ab#c@de"` is `"abde"`. This implies that after the `@` operation (Step 5), the `current_text_stack` went from `['a', 'c']` to `['a', 'b']`. However, based on the explicit rules ("reverse the effect of the *last successful character modification*", and if it was `ADD 'C'`, then `C` is removed), undoing `ADD 'c'` should simply remove 'c', resulting in `['a']`. The example's `Current String Stack` column in the trace is inconsistent with its own `Explanation` and `History Stack` columns. This solution adheres strictly to the problem's textual rules, which yields `"ade"`.

### Complexity Analysis

*   **Time Complexity: O(N)**
    *   `N` is the length of the input string `s`.
    *   We iterate through `s` exactly once.
    *   Each operation (`append`, `pop` on `collections.deque`) takes amortized O(1) time.
    *   The final `"".join(current_text_stack)` operation takes O(L) time, where `L` is the length of the final string (at most `N`).
    *   Therefore, the overall time complexity is dominated by iterating through `s` and stack operations, resulting in O(N).

*   **Space Complexity: O(N)**
    *   In the worst case (e.g., all append operations without backspace or undo), `current_text_stack` can store up to `N` characters.
    *   Similarly, `history_stack` can store up to `N` entries, each being a small tuple.
    *   Thus, the total space complexity is O(N).

These complexities are efficient enough for the given constraint `s.length <= 10^5`.