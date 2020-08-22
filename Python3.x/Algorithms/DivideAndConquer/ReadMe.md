# About Divide And Conquer
![Img](https://res.cloudinary.com/practicaldev/image/fetch/s--0knuwIJs--/c_imagga_scale,f_auto,fl_progressive,h_500,q_auto,w_1000/https://cl.ly/5864a2a8d8ba/Image%25202019-03-31%2520at%25205.27.52%2520PM.png)
Divide and Conquer is an algorithmic paradigm. It is a technique to solve a complex problem by dividing it into 3 parts:
1. Divide : Divide the main problem into subproblems and keeps on dividing it.
2. Conquer : Solve each of the sub-problem as it becomes very short
3. Combine : then combine the subproblems to reach the real problem

### Algorithm :
    Divide_and_Conquer ( Array , start_index, end_index ) :
      if ( check_base_case(Array, start_index, end_index) ): 
          return solution(Array, start_index, end_index)
     
      else:
        mid_divide = divide(Array, start_index, end_index)
    
        part_left = Divide_and_Conquer(Array, start_index, mid)
    
        part_right = Divide_and_Conquer (Array, mid+1, end_index)
    
        combined_ans = Combine( left_part, right_part )
    
      return combined_ans


Implemenatation of DAC: Finding MinMax in an array program : [link](https://github.com/Mystery01092000/Algorithms_myWay/blob/master/Python3.x/Algorithms/DivideAndConquer/MinAndMaxOfArrayDAC.py)
### Main Algorithms which use Divide and Conquer Approach for solving problems :

1. Binary Search
2. Quick Sort
3. Merge Sort
4. Closest pair of points
5. Strassen's Algorithm for multiplication of two matrices
6. Karatsuba Algorithm for fast multiplication
