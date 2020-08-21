# Binary Search :

Binary search works on sorted arrays. Binary search begins by comparing an element in the middle of the array with the target value. If the target value matches the element, its position in the array is returned. If the target value is less than the element, the search continues in the lower half of the array. If the target value is greater than the element, the search continues in the upper half of the array. By doing this, the algorithm eliminates the half in which the target value cannot lie in each iteration.

![gif](https://stackabuse.s3.amazonaws.com/media/binary-search-in-java-1.gif)

The above animation image shows how a binary search works.

Pseudo-code For the Algorithm:

                  function binary_search(A, n, T) is
                      L := 0
                      R := n − 1
                      while L ≤ R do
                          m := floor((L + R) / 2)
                          if A[m] < T then
                              L := m + 1
                          else if A[m] > T then
                              R := m − 1
                          else:
                              return m
                      return unsuccessful
                      
 In worst case, the binary search algorithm takes O(logn) for an array of size n.
 
 The python code for Binary Search : [link](https://github.com/Mystery01092000/Algorithms_myWay/blob/master/Python3.x/Algorithms/DivideAndConquer/BinarySearch.py)
 
 References : [Wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm)
