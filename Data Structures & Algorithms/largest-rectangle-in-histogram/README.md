# Largest Rectangle in Histogram

## 1. Problem Overview

Given an array of integers `heights`, where each integer represents the height of a histogram bar and each bar has a width of `1`, return the area of the largest rectangle that can be formed within the histogram.

### Example 1

**Input:**

```python
heights = [2, 1, 5, 6, 2, 3]
```

**Output:**

```python
10
```

**Explanation:**

The largest rectangle is formed using the bars with heights `5` and `6`.

The rectangle has:
- Height = 5
- Width = 2

Therefore:

```python
Area = Height * Width
Area = 5 * 2
Area = 10
```

### Example 2

**Input:**

```python
heights = [2, 4]
```

**Output:**

```python
4
```

The possible rectangles are:

- Bar with height 2: Area = 2 × 1 = 2.
- Bar with height 4: Area = 4 × 1 = 4.

The maximum area is `4`.

---

# 2. Understanding the Core Concept

Before looking at the solution, we need to understand how rectangles are formed in a histogram.

Every bar has:
- A height.
- A width of 1.
- A position (index).

The area of a rectangle is:

```python
Area = Height * Width
```

The interesting part is determining how far a particular bar can extend horizontally.

For example:

```python
heights = [2, 5, 6, 3]
```

Consider the bar with height `5`.

It can form a rectangle with:
- Height = 5.
- Width = 2.

Why?

Because the bars at indices 1 and 2 both have heights greater than or equal to 5.

Therefore:

```python
Area = 5 * 2
Area = 10
```

However, it cannot extend to the bar with height `3`, because that bar is shorter.

This gives us our first important observation:

**A rectangle's height is limited by the shortest bar within its horizontal range.**

---

# 3. The Monotonic Stack Approach

We solve this problem using a data structure called a **Monotonic Increasing Stack**.

A monotonic increasing stack maintains elements in increasing order.

In our solution, the stack stores pairs:

```python
(start_index, height)
```

For example:

```python
stack = [
    (0, 1),
    (2, 3),
    (4, 5)
]
```

The heights are increasing:

```text
1 < 3 < 5
```

Each pair represents a bar and the earliest index from which its height can potentially extend.

### Why do we need a stack?

Imagine we encounter these heights:

```python
heights = [2, 5, 6, 2]
```

As we traverse the array, we encounter:

```text
2 → 5 → 6
```

The heights are increasing, so we cannot yet determine the maximum rectangle for the bars with heights 5 and 6.

However, when we encounter the final `2`, something interesting happens.

We now know that:
- The bar with height 6 cannot extend beyond the current index.
- The bar with height 5 cannot extend beyond the current index either.

We can finally calculate their maximum possible rectangle areas.

This is exactly what the stack helps us accomplish.

---

# 4. The Complete Python Solution

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea = 0
        stack = []

        for i, h in enumerate(heights):

            start = i

            while stack and stack[-1][1] > h:

                index, height = stack.pop()

                maxArea = max(maxArea, height * (i - index))

                start = index

            stack.append((start, h))

        for i, h in stack:

            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
```

---

# 5. Line-by-Line Explanation

## Step 1: Initialize maxArea

```python
maxArea = 0
```

This variable keeps track of the largest rectangle area discovered so far.

Initially, we have not calculated any areas.

Therefore:

```python
maxArea = 0
```

Whenever we discover a larger rectangle, we update this variable.

---

## Step 2: Initialize the stack

```python
stack = []
```

We create an empty stack.

The stack stores pairs:

```python
(start_index, height)
```

For example:

```python
stack = [(0, 2), (2, 5), (3, 6)]
```

This means:

- `(0, 2)`: A bar with height 2 that can potentially extend from index 0.
- `(2, 5)`: A bar with height 5 that can potentially extend from index 2.
- `(3, 6)`: A bar with height 6 that can potentially extend from index 3.

Notice that the heights are increasing:

```text
2 < 5 < 6
```

This is the monotonic property we maintain.

---

## Step 3: Traverse the histogram

```python
for i, h in enumerate(heights):
```

We iterate through every bar.

`enumerate()` gives us two values:

- `i`: The current index.
- `h`: The current bar's height.

For example:

```python
heights = [2, 1, 5, 6, 2, 3]
```

The iterations are:

| Index (i) | Height (h) |
|---|---|
| 0 | 2 |
| 1 | 1 |
| 2 | 5 |
| 3 | 6 |
| 4 | 2 |
| 5 | 3 |

We process the bars from left to right.

---

## Step 4: Initialize start

```python
start = i
```

This is one of the most important lines in the solution.

Initially, we assume that the current bar can only start at its own index.

For example:

```python
i = 4
h = 2
```

Initially:

```python
start = 4
```

However, this starting position might change.

Why?

Because the current bar might be able to extend further left than its own index.

We will see how this happens in the next step.

---

## Step 5: The while loop

```python
while stack and stack[-1][1] > h:
```

This is the heart of the algorithm.

Let's break it down.

### Condition 1: stack

```python
stack
```

Checks whether the stack is empty.

We cannot access the top element of an empty stack.

### Condition 2: stack[-1]

```python
stack[-1]
```

Gets the last element in the stack.

Remember, the stack follows the Last In, First Out (LIFO) principle.

### Condition 3: stack[-1][1]

```python
stack[-1][1]
```

Gets the height stored in the top element.

Remember:

```python
(start_index, height)
```

Index `0` represents the starting index.

Index `1` represents the height.

### Condition 4: stack[-1][1] > h

We check whether the height at the top of the stack is greater than the current height.

Why?

Because encountering a shorter bar tells us that taller bars cannot extend beyond the current position.

We can now calculate their maximum possible areas.

For example:

```python
stack = [(0, 2), (2, 5), (3, 6)]
```

Current bar:

```python
i = 4
h = 2
```

The top of the stack has height 6.

Since:

```python
6 > 2
```

We must pop it.

After that, we check the new top.

Its height is 5.

Since:

```python
5 > 2
```

We pop that too.

We continue until the stack is empty or its top height is less than or equal to the current height.

---

## Step 6: Pop the previous bar

```python
index, height = stack.pop()
```

We remove the top element from the stack.

The popped element contains:

```python
(start_index, height)
```

We store these values in:

- `index`: The starting index of the popped bar.
- `height`: The height of the popped bar.

For example:

```python
stack = [(0, 2), (2, 5), (3, 6)]
```

After:

```python
index, height = stack.pop()
```

We get:

```python
index = 3
height = 6
```

The stack becomes:

```python
[(0, 2), (2, 5)]
```

**Important distinction:**

`i` and `index` are not necessarily the same.

- `i` represents the current bar's index.
- `index` represents the starting index of the previously stored bar.

---

## Step 7: Calculate the rectangle area

```python
maxArea = max(maxArea, height * (i - index))
```

This calculates the maximum rectangle area for the popped bar.

Remember:

```python
Area = Height * Width
```

We already know the height:

```python
height
```

But how do we calculate the width?

```python
i - index
```

Why?

Because:

- `index` is where the popped bar's rectangle starts.
- `i` is the current index where we encountered a shorter bar.

The popped bar can extend from `index` up to `i - 1`.

Therefore:

```python
Width = i - index
```

### Example

Suppose:

```python
index = 2
i = 4
height = 5
```

Then:

```python
width = 4 - 2
width = 2
```

And:

```python
area = 5 * 2
area = 10
```

We update the maximum area:

```python
maxArea = max(maxArea, 10)
```

This ensures that we never lose a larger area discovered earlier.

---

## Step 8: Update start

```python
start = index
```

This is arguably the most important line to understand.

Why do we update `start`?

Because the current, shorter bar can potentially extend further left than its original index.

Let's look at an example.

Suppose:

```python
heights = [2, 1, 5, 6, 2, 3]
```

We are currently processing:

```python
i = 4
h = 2
```

Initially:

```python
start = 4
```

We pop:

```python
(3, 6)
```

Therefore:

```python
index = 3
start = 3
```

Next, we pop:

```python
(2, 5)
```

Therefore:

```python
index = 2
start = 2
```

Why does this matter?

Because the current bar with height 2 can extend backwards to index 2.

Look at the relevant bars:

```text
Index:    2   3   4
Height:   5   6   2
```

All three bars have heights greater than or equal to 2.

Therefore, we can form a rectangle with:

```python
height = 2
width = 3
area = 6
```

If we didn't update `start`, we would lose the ability to represent this wider rectangle.

**The key idea: The current shorter bar inherits the earliest starting position of the taller bars we pop.**

---

## Step 9: Push the current bar

```python
stack.append((start, h))
```

After processing all taller bars, we push the current bar onto the stack.

Notice that we append:

```python
(start, h)
```

NOT:

```python
(i, h)
```

Why?

Because `start` might be smaller than `i`.

For example:

```python
i = 4
h = 2
start = 2
```

We append:

```python
(2, 2)
```

Not:

```python
(4, 2)
```

This preserves the information that the current bar can extend further left.

---

# 6. Understanding the Second For Loop

After processing every bar, we execute:

```python
for i, h in stack:
    maxArea = max(maxArea, h * (len(heights) - i))
```

Why do we need this?

Some bars might never encounter a shorter bar while traversing the histogram.

For example:

```python
heights = [2, 3, 4, 5]
```

Every new bar is taller than the previous one.

Nothing gets popped.

At the end:

```python
stack = [(0, 2), (1, 3), (2, 4), (3, 5)]
```

We still need to calculate their maximum possible areas.

Since no shorter bar appeared to their right, they can all extend to the end of the histogram.

### Understanding the width

```python
len(heights) - i
```

The length of the array represents the position immediately after the last index.

For example:

```python
heights = [2, 3, 4, 5]
```

Array length:

```python
len(heights) = 4
```

For the bar at index 1:

```python
width = 4 - 1
width = 3
```

It can extend across indices 1, 2 and 3.

Therefore:

```python
area = 3 * 3
area = 9
```

We repeat this calculation for every remaining bar.

Finally:

```python
return maxArea
```

Returns the largest rectangle area.

---

# 7. Complete Dry Run

Let's walk through the entire algorithm.

Input:

```python
heights = [2, 1, 5, 6, 2, 3]
```

Initially:

```python
maxArea = 0
stack = []
```

### Iteration 1: Index 0, Height 2

Current values:

```python
i = 0
h = 2
start = 0
```

The stack is empty.

Therefore, we skip the while loop.

Push:

```python
stack.append((0, 2))
```

Result:

```python
stack = [(0, 2)]
maxArea = 0
```

### Iteration 2: Index 1, Height 1

Current values:

```python
i = 1
h = 1
start = 1
```

The top of the stack is:

```python
(0, 2)
```

Since:

```python
2 > 1
```

We pop it.

```python
index = 0
height = 2
```

Calculate:

```python
area = 2 * (1 - 0)
area = 2
```

Update:

```python
maxArea = 2
```

Update start:

```python
start = 0
```

Push:

```python
stack.append((0, 1))
```

Result:

```python
stack = [(0, 1)]
maxArea = 2
```

### Iteration 3: Index 2, Height 5

Current values:

```python
i = 2
h = 5
start = 2
```

The top of the stack is:

```python
(0, 1)
```

Since:

```python
1 > 5
```

is false, we don't pop.

Push:

```python
stack.append((2, 5))
```

Result:

```python
stack = [(0, 1), (2, 5)]
maxArea = 2
```

### Iteration 4: Index 3, Height 6

Current values:

```python
i = 3
h = 6
start = 3
```

The top of the stack has height 5.

Since:

```python
5 > 6
```

is false, we don't pop.

Push:

```python
stack.append((3, 6))
```

Result:

```python
stack = [(0, 1), (2, 5), (3, 6)]
maxArea = 2
```

### Iteration 5: Index 4, Height 2

This is the most important iteration.

Current values:

```python
i = 4
h = 2
start = 4
```

Our stack:

```python
[(0, 1), (2, 5), (3, 6)]
```

**First pop:**

The top element is:

```python
(3, 6)
```

Since:

```python
6 > 2
```

We pop it.

Calculate:

```python
area = 6 * (4 - 3)
area = 6
```

Update:

```python
maxArea = 6
```

Update start:

```python
start = 3
```

Stack:

```python
[(0, 1), (2, 5)]
```

**Second pop:**

The top element is:

```python
(2, 5)
```

Since:

```python
5 > 2
```

We pop it.

Calculate:

```python
area = 5 * (4 - 2)
area = 10
```

Update:

```python
maxArea = 10
```

Update start:

```python
start = 2
```

Stack:

```python
[(0, 1)]
```

**Check again:**

The top height is 1.

Since:

```python
1 > 2
```

is false, we exit the while loop.

Now push:

```python
stack.append((2, 2))
```

Notice that we push `(2, 2)` instead of `(4, 2)`.

Why?

Because the current bar can potentially extend back to index 2.

Result:

```python
stack = [(0, 1), (2, 2)]
maxArea = 10
```

### Iteration 6: Index 5, Height 3

Current values:

```python
i = 5
h = 3
start = 5
```

The top element is:

```python
(2, 2)
```

Since:

```python
2 > 3
```

is false, we don't pop.

Push:

```python
stack.append((5, 3))
```

Result:

```python
stack = [(0, 1), (2, 2), (5, 3)]
maxArea = 10
```

---

# 8. Processing the Remaining Stack

We have finished traversing the histogram.

Our stack contains:

```python
stack = [(0, 1), (2, 2), (5, 3)]
```

Some bars have not yet had their maximum possible areas calculated.

We process them using:

```python
for i, h in stack:
    maxArea = max(maxArea, h * (len(heights) - i))
```

Remember:

```python
len(heights) = 6
```

### First element: (0, 1)

```python
area = 1 * (6 - 0)
area = 6
```

Current maximum remains 10.

### Second element: (2, 2)

```python
area = 2 * (6 - 2)
area = 8
```

Current maximum remains 10.

### Third element: (5, 3)

```python
area = 3 * (6 - 5)
area = 3
```

Current maximum remains 10.

Final result:

```python
return 10
```

---

# 9. Complete Dry Run Table

| i | h | Operation | Stack after iteration | maxArea |
|---|---|---|---|---|
| 0 | 2 | Push (0,2) | [(0,2)] | 0 |
| 1 | 1 | Pop (0,2), area = 2; push (0,1) | [(0,1)] | 2 |
| 2 | 5 | Push (2,5) | [(0,1),(2,5)] | 2 |
| 3 | 6 | Push (3,6) | [(0,1),(2,5),(3,6)] | 2 |
| 4 | 2 | Pop (3,6), area = 6 | [(0,1),(2,5)] | 6 |
| 4 | 2 | Pop (2,5), area = 10; push (2,2) | [(0,1),(2,2)] | 10 |
| 5 | 3 | Push (5,3) | [(0,1),(2,2),(5,3)] | 10 |

Final stack processing:

| Starting index | Height | Width | Area |
|---|---|---|---|
| 0 | 1 | 6 | 6 |
| 2 | 2 | 4 | 8 |
| 5 | 3 | 1 | 3 |

Final answer:

```python
10
```

---

# 10. Understanding i, index, and start

These three variables are easy to confuse.

Let's distinguish them.

| Variable | Meaning |
|---|---|
| `i` | Index of the current bar being processed |
| `index` | Starting index of a previously popped bar |
| `start` | Earliest index the current bar can potentially extend to |

### Example

Suppose:

```python
i = 4
h = 2
```

Initially:

```python
start = 4
```

We pop:

```python
(index, height) = (3, 6)
```

Now:

```python
index = 3
start = 3
```

We pop again:

```python
(index, height) = (2, 5)
```

Now:

```python
index = 2
start = 2
```

Finally:

```python
stack.append((start, h))
```

We append:

```python
(2, 2)
```

The current bar is at index 4, but its earliest possible starting position is index 2.

**Remember:**

- `i` tells us where we are.
- `index` tells us where a popped bar started.
- `start` remembers how far left the current bar can potentially extend.

---

# 11. Why Don't We Lose the Horizontal Width When Popping?

This is an important concept.

When we pop a bar, we calculate its maximum possible rectangle area.

For example, at index 4:

The bar with height 6:

```python
area = 6 * (4 - 3)
area = 6
```

The bar with height 5:

```python
area = 5 * (4 - 2)
area = 10
```

We then preserve the earliest starting position:

```python
start = 2
```

And push:

```python
(2, 2)
```

This allows the current bar with height 2 to extend across indices 2, 3 and 4.

In other words, popping a bar does not mean that we discard all information about its horizontal position.

We calculate its area and transfer the relevant starting-position information to the shorter bar.

---

# 12. Why Does the Second Loop Exist?

Consider:

```python
heights = [2, 3, 4, 5]
```

The heights continuously increase.

Therefore, the while loop never pops anything.

At the end:

```python
stack = [(0, 2), (1, 3), (2, 4), (3, 5)]
```

If we didn't have the second loop, we would miss rectangles that extend all the way to the end of the histogram.

The second loop calculates those remaining areas.

For each remaining bar:

```python
width = len(heights) - i
```

This gives us the maximum possible width because no shorter bar appeared to its right.

---

# 13. Time and Space Complexity

Let `n` represent the number of bars in the histogram.

### Time Complexity: O(n)

We traverse the array once.

Each element:
- Gets pushed onto the stack at most once.
- Gets popped from the stack at most once.

Although we have a nested `while` loop, the total number of pop operations across the entire algorithm cannot exceed `n`.

The second loop also processes at most `n` elements.

Therefore:

```text
O(n) + O(n) = O(n)
```

### Space Complexity: O(n)

In the worst case, the stack can contain every element.

For example:

```python
heights = [1, 2, 3, 4, 5, 6]
```

Every new height is greater than the previous one.

Nothing gets popped.

Therefore, the stack grows to size `n`.

Space complexity:

```text
O(n)
```

---

# 14. Common Mistakes and Things to Remember

### Mistake 1: Thinking i and index are the same

They are different.

```python
i
```

Is the current index.

```python
index
```

Is the starting index of a previously popped element.

### Mistake 2: Forgetting to update start

This line is essential:

```python
start = index
```

Without it, the current shorter bar would lose its ability to extend further left.

### Mistake 3: Appending (i, h) instead of (start, h)

Incorrect:

```python
stack.append((i, h))
```

Correct:

```python
stack.append((start, h))
```

The current bar might be able to extend further left.

### Mistake 4: Forgetting the second loop

The second loop handles bars that never encountered a shorter bar to their right.

Without it, we would miss valid rectangles.

### Mistake 5: Thinking the nested while loop makes the algorithm O(n²)

It doesn't.

Each element is pushed once and popped at most once.

Therefore, the total time complexity remains O(n).

---

# 15. The Algorithm in Plain English

Imagine you're walking through the histogram from left to right.

1. Pick the current bar.
2. Assume its rectangle starts at its own index.
3. Look at the top of your stack.
4. If the previous bar is taller than the current bar, calculate the previous bar's maximum possible rectangle area.
5. Remove that taller bar from the stack.
6. Inherit its starting index because the current, shorter bar can potentially extend further left.
7. Repeat until the stack is empty or the top bar is shorter than or equal to the current bar.
8. Push the current bar into the stack using its earliest possible starting index.
9. Continue until every bar has been processed.
10. Calculate the areas of any bars remaining in the stack by extending them to the end of the histogram.
11. Return the maximum area.

---

# 16. Final Takeaways

The entire solution revolves around three important ideas.

**1. Monotonic Increasing Stack**

We maintain bars in increasing order of height so that we can efficiently identify when a taller bar's maximum rectangle has been reached.

**2. Calculate Area When Popping**

When we encounter a shorter bar, we know that taller bars cannot extend any further to the right.

We calculate their areas using:

```python
area = height * (i - index)
```

**3. Preserve the Starting Index**

When we pop a taller bar, we transfer its starting position to the current shorter bar:

```python
start = index
```

This allows the shorter bar to potentially form a wider rectangle.

### The Most Important Formulas

When popping:

```python
area = height * (i - index)
```

When processing the remaining stack:

```python
area = height * (len(heights) - i)
```

Both follow the same fundamental formula:

```python
Area = Height * Width
```

The only difference is how we determine the right boundary.

**Final complexity:**

| Complexity | Value |
|---|---|
| Time | O(n) |
| Space | O(n) |

**The key lesson:** A monotonic stack helps us efficiently find the boundaries within which each bar can form a rectangle. Once we understand how the left and right boundaries are determined, the entire problem becomes much easier.
