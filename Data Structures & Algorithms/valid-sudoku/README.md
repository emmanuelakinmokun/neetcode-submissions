### Valid Sudoku

+ Use three `defaultdict(set)` dictionaries to track numbers in rows, columns, and 3×3 boxes.
- Loop through all 81 cells using nested loops (`r` for rows, `c` for columns).
* Skip empty cells (`"."`) using `continue`.
+ Use `rows[r]`, `cols[c]`, and `squares[(r//3, c//3)]` to check for duplicates. The formula `(r//3, c//3)` uniquely identifies each of the nine 3×3 boxes.
_ If a duplicate exists, return `False`; otherwise, add the number to all three sets. If all cells pass, return `True`.
