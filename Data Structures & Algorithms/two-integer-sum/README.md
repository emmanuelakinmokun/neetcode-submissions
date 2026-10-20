#  Two sum

### Submission 1

We loop through the range for nums before running a loop through a nested loop through nums except the current `i` using `i + 1` before comparing `num[i] + num[j]` to `target`

### Submission 2

Storing the `num` in `nums` as keys and index as values, the difference between the `target` and `num`is calculated on a second pass. By checking if this complement exists in the hash map, the solution avoids nested loops and efficiently finds the matching pair in O(n) time.
