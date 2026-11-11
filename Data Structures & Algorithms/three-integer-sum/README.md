# 3Sum (LeetCode 15)

## Approach: Sorting + Two Pointers

### Problem
Given an integer array `nums`, find all unique triplets `[a, b, c]` such that:

`a + b + c == 0`

Duplicate triplets are not allowed.

### How It Works

1. **Sort the array:** Sorting allows us to use two pointers efficiently and skip duplicates.

2. **Fix one number:** Iterate through the array using `i` as the first number of each potential triplet.

3. **Skip duplicates:** If the current number is the same as the previous number, skip it to avoid duplicate triplets.

4. **Initialize two pointers:**
   - `left = i + 1`
   - `right = len(nums) - 1`

5. **Find the remaining two numbers:** While `left < right`, calculate the sum of the three numbers:
   - If `total < 0`, move `left` forward to increase the sum.
   - If `total > 0`, move `right` backward to decrease the sum.
   - If `total == 0`, add the triplet to the result.

6. **Skip duplicates:** After finding a valid triplet, move past duplicate values on both sides before moving both pointers inward.

7. **Return the result:** Return all unique triplets found.

### Complexity Analysis

- **Time Complexity:** `O(n²)`
  - Sorting takes `O(n log n)`.
  - The outer loop runs `O(n)` times.
  - The two-pointer traversal takes `O(n)` per iteration.

- **Space Complexity:** `O(1)` auxiliary space, excluding sorting implementation overhead and the output list.

### Key Takeaway

The main idea is to transform the 3Sum problem into a Two Sum problem by fixing one number and using two pointers to find the remaining pair.

**Pointer movement rule:**
- Negative sum → Move left forward.
- Positive sum → Move right backward.
- Zero sum → Store the triplet and skip duplicates.

This approach avoids the brute-force `O(n³)` solution and achieves `O(n²)` time complexity.
