

# CMPS 2200 Assignment 1

**Name:** Oliver Sanger


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
. Yes it is.
. 𝑓(𝑛) is said to be 𝑂(𝑔(𝑛)) if there exist constants 𝑐 and 𝑘 such that if 𝑙 ≥ 𝑘 then 𝑓(𝑙) ≤ 𝑐 × 𝑔(𝑙)
. 𝑓(𝑛) is 𝑂(𝑔(𝑛)) if eventually, a constant multiple of 𝑔 is bigger than or equal to 𝑓.  
. let's say we multiply 2^𝑛 by 2,then it is 2^(𝑛+1), which of course, is greater than or equal to 2^(𝑛+1)
. So with 𝑐 = 2 and 𝑘 = 1, we have 2 × 2^𝑛 ≥ 2^(𝑛+1) for all 𝑛≥1. Therefore , 2𝑛+1 is 𝑂(2𝑛).

  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  No it is not.
.  Let x = 2^n, then we are asking if 2^x = O(x) 
.  If this were the case there would exist a constant c such that 2^x <= cx for all x
.  => log(2^x) <= log(cx) 
   => x <= log(c) + log(x)
   => x - log(x) <= log(c) 
.  This is a contradiction since x - log(x) is an increasing function and will eventually pass the constant c as x tends to infinity

  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  No it is not
.  
.
.

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  Yes it is
.  
.  
.  

  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  Yes it is
.  
.  
.  

  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  Yes it is


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

.  The function recursively calls itself when it reaches a value smaller or equal to 1,
.  Once the function reaches that point it can return x to the sequence
.  This process recurs until there are no more values to check and a sum of the previous numbers is reached
.  
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  The work of this function is O(n) (n is the length of the input list)
.  The span is O(1) because there are no seperate parallels
.  
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  Work is O(n log(n)) (n is the length of the input list), this is because the list is being divided in half at each recursive call
.  Span is O(log(n)), this is because the levels of recursion can be performed in parallel
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  Work = T(1) = O(n): the work is the total number of operations performed by the algorithm, which is proportional to the length of the input list n. Each thread works on a sub-list of length n/k where k is the number of threads created. Since each thread performs a constant number of operations, the total work of the algorithm is O(n).
.  Span = O(log n): the span is the longest path of sequential operations in the parallel execution of the algorithm. In the case of longest_run_recursive, the span is determined by the height of the recursion tree. Since each recursive call splits the input list into two halves, the height of the recursion tree is log n. Therefore, the span of the algorithm is O(log n).
.  
.  
.  
.  
.  
.  

