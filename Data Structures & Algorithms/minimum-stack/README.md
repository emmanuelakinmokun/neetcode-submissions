# MINIMUM STACK
So, to get the minimum number in 0(1) time, we simple create two stacks, a second stack `minStack` that stores the minimum number from the main stack at the `minStack[-1]` position. 
This was achieved by updating val to the minimum number between the stack and the previous `minStack` so the lower number can only get append to `minStack`  
