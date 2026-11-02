### Car Fleet

 The position and speed for each vehicle is stored in an ordered list. The time taken to get to the target is calculated and stored in the stack starting from the closest to the target. 
 When the `len(stack)>=2`, we compare the items to each other and if the subsequent time is greater than the previous, we add to the stack to form a new fleet and if not, we pop.
