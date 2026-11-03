### Approach: Length-Prefix Encoding

- **Encode:** Iterate through each string and concatenate its length, a `#` delimiter, and the original string.
- This produces a single encoded string while preserving the original string boundaries.
- **Decode:** Use two pointers (`i` and `j`) to identify the length prefix and locate the `#` delimiter.
- Convert the length prefix to an integer to determine how many characters to extract.
- Extract the original string using Python slicing and append it to the result list.
- Update `i` to the beginning of the next encoded string and repeat until the end.
- Using length prefixes ensures the solution works even when strings contain special characters or delimiters.

**Time Complexity:** O(n) for both encoding and decoding, where n is the total number of characters.

**Space Complexity:** O(n) for storing the encoded string and decoded result.
