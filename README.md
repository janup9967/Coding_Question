# 🧠 Coding Questions — Python

A curated collection of Python solutions covering data structures, algorithms, dynamic programming, and real-world problem-solving patterns.

---

## 📁 Project Structure

```
coding_question/
├── Linked List/
│   ├── base_linked_list.py         # Node & LinkedList class with insert + display
│   ├── insert_at_beg.py            # Insert at beginning
│   ├── insert_at_end.py            # Insert at end (O(1) with tail pointer)
│   ├── insert_any_pos.py           # Insert at any position
│   ├── display_linked_list.py      # Traverse and display
│   ├── detect_cycles.py            # Floyd's cycle detection (slow & fast pointer)
│   ├── middle_elements.py          # Find middle node (two-pointer technique)
│   ├── delete_node_beg.py          # Delete first node (head)
│   ├── delete_node_end.py          # Delete last node (tail)
│   ├── delete_node_pos.py          # Delete node at any position (0-based)
│   ├── delete_all_node_values.py   # Remove all nodes with a given value
│   ├── reverse_node.py             # Reverse list (stack O(n) & in-place O(1))
│   ├── reverse_node_betw.py        # Reverse sublist between positions left–right
│   ├── odd_even_linked_list.py     # Regroup odd/even indexed nodes (O(n), O(1))
│   ├── palindrome.py               # Check if linked list is palindrome
│   ├── length_of_loop.py           # Find length of cycle (Floyd's + count)
│   └── remove_nth_element.py       # Remove nth node from end (one-pass)
├── Doubly Linked List/
│   ├── insert_doubly_linked.py     # Insert at beginning, end, or any position
│   ├── display_doubly_linked.py    # Forward & backward traversal
│   ├── delete_doubly_linked.py     # Delete at beginning, end, or any position
│   ├── delete_all_occurence.py     # Delete all nodes with a given value
│   └── reverse_doubly_linked.py   # Reverse DLL by swapping next/prev pointers
├── Stack_Queues/
│   ├── stack.py                    # Stack (push, pop, peek, size, is_empty)
│   └── valid_paranthesis.py        # Valid parentheses using stack
├── 3Sum.py                         # Find all unique triplets summing to zero
├── twosum.py                       # Two Sum in O(n) using hash map
├── missing_number_array.py         # Find missing number using sum formula
├── max_subset_sum.py               # Max subset sum ≤ maxSum (memoized recursion)
├── maxprod_subarray.py             # Maximum product subarray
├── longest_0_1_subarray.py         # Longest subarray with equal 0s and 1s
├── longest_substring.py            # Longest substring without repeating chars (sliding window)
├── merge_overlapping.py            # Merge overlapping intervals
├── Leader_in_array.py              # Find leaders in array (right-to-left scan)
├── chocolate_distribution.py       # Min difference in chocolate distribution (sliding window)
├── duplicate_char.py               # Remove duplicates / find first non-repeating char
├── reverse_string.py               # Reverse a string
├── spam_safe.py                    # Detect spam (3 consecutive identical chars)
├── heap_sort.py                    # Heap sort with shiftDown (in-place)
├── Sort_pair.py                    # Sort pairs by (first, second) using selection sort logic
├── Spanning_tree.py                # Minimum & Second Minimum Spanning Tree (Kruskal/Prim)
├── prime_number.py                 # Prime check in O(√n)
├── min_max_digits_in_number.py     # Min and max digit in a number
├── Pattern_problem.py              # Star patterns (pyramid, diamond, inverted)
├── king_army.py                    # Count valid army arrangements (DP)
├── bus_passenger_tracking.py       # Max passengers on bus at any station
├── library_fine_calculation.py     # Total library fine for overdue books
├── parking_fine.py                 # Parking fine based on hours
├── gym.py                          # Gym membership cost calculator
├── transaction_monitor.py          # Detect duplicate/fraud transactions
├── lambda_late_binding.py          # Python closure & lambda late binding explained
└── inputs.py                       # Input parsing patterns & utility snippets
```

---

## 🗂️ Topics Covered

| Category | Problems / Concepts |
|---|---|
| **Arrays** | 3Sum `O(n²)`, Two Sum `O(n)`, Missing Number, Max Subset Sum, Max Product Subarray, Longest 0-1 Subarray, Merge Overlapping Intervals, Leader in Array, Chocolate Distribution |
| **Strings** | Longest Substring (Sliding Window), Remove Duplicates, First Non-Repeating Char, Reverse String, Spam Detection |
| **Singly Linked List** | Insert (Begin / End / Any Position), Display, Delete (Begin / End / Position / All Values), Reverse (Stack & In-place), Reverse Between Positions, Detect Cycle (Floyd's), Loop Length, Middle Element, Odd-Even Regroup, Palindrome Check, Remove Nth From End |
| **Doubly Linked List** | Insert (Begin / End / Any Position), Display (Forward & Backward), Delete (Begin / End / Position / All Occurrences), Reverse |
| **Stack & Queue** | Stack Implementation (LIFO), Valid Parentheses |
| **Sorting** | Heap Sort, Sort Pairs |
| **Graphs** | Minimum Spanning Tree, Second Minimum Spanning Tree |
| **Dynamic Programming** | Max Subset Sum (Memoization), King's Army Arrangements |
| **Patterns** | Right/Left/Full Pyramid, Inverted Pyramid, Half Diamond, Diamond |
| **Math** | Prime Check `O(√n)`, Min/Max Digits in Number |
| **Real-World Simulations** | Bus Passenger Tracking, Gym Membership, Library Fine, Parking Fine, Transaction Monitor (Fraud Detection) |
| **Python Internals** | Lambda Late Binding, Closure Behavior, Input Parsing Patterns |

---

## 🚀 Getting Started

```bash
git clone https://github.com/<your-username>/coding_question.git
cd coding_question
python <filename>.py
```

> Requires Python 3.x — no external dependencies.

---

## 💡 Highlights

- **Two Sum** — O(n) hash map approach, no nested loops
- **3Sum** — Sorted + two-pointer, avoids duplicates
- **Heap Sort** — In-place with manual `shiftDown`, no library used
- **Detect Cycle** — Floyd's slow/fast pointer algorithm
- **Loop Length** — Floyd's detection + counter in O(n), O(1)
- **Reverse Between** — Single-pass in-place partial reversal using dummy node
- **Odd Even List** — O(n) time, O(1) space index-based regroup
- **Remove Nth From End** — One-pass two-pointer solution
- **Palindrome Check** — Reverse second half in-place, then compare
- **Reverse DLL** — Swap next/prev for each node in O(n), O(1)
- **Valid Parentheses** — Stack-based bracket matching
- **Max Subset Sum** — Top-down DP with memoization
- **King's Army** — DP with rolling state array
- **Transaction Monitor** — Duplicate + fraud detection in single pass
- **Lambda Late Binding** — Explains Python closure pitfall with fix

---

## 🤝 Contributing

Pull requests are welcome! Feel free to add new problems or optimize existing solutions.

---

## 📄 License

[MIT](LICENSE)
