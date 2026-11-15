### Max Water Container
---
Using two pointers, while the left pointer is less then the right, we find the area between the two bars 
`area = ((r-l) * min(height[l], height[r]))`.
Since water flows after the lower bar is submerged we use that as the height while the breath is diff between the two bars.
`res = max(res, area)`.
We return the max value between the current and previous area stored in the res var.
The pointer is moved away from the shorter bar.
