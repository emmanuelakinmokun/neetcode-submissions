## Products of Array Except Self

This answer returns a list of the product of a list except the index. 

FIrstly, we multiply the non-zero elements of the list and count the zeros in the list. If the number of zeros > 1, our resulting list will be zeros. 

In case of zero count = 1, when our index is 0, we get the product of the other numbers and when it isn't we return 0 because the zero will cancel out the other numbers. 
If zero_count = 0, we simply floor divide the product by the current index to eliminate the number.
