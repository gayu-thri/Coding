## Job Sequence with maximum profit 
Geeks for geeks - https://youtu.be/R6Skj4bT1HE
### Input:
Five Jobs with following deadlines and profits
JobID | Deadline | Profit
--- | --- | ---
   a  |   2   |    100
   b  |   1   |    19
   c  |   2   |    27
   d  |   1   |    25
   e  |   3   |    15
  
### Sorted:
  JobID | Deadline | Profit
--- | --- | ---
   a  |   2   |    100
   c  |   2   |    27
   d  |   1   |    25
   b  |   1   |    19
   e  |   3   |    15
   
### Result :
1. A having the highest profit with deadline 2<br>
` ` | `a` | ` ` | ` ` | ` ` | ` `
2. Next C has to be completed before 2, hence search for 
an empty slot before 2.
Since 0th position is a free slot,
`c` | `a` | ` ` | ` ` | ` ` | ` `
3. D cannot be inserted as no empty slot is available 
before 1(D's deadline), similarly also B can't be added.
4. E's deadline is 3 and free slot is available
`c` | `a` | `e ` | ` ` | ` ` | ` `
  
Output: Following is maximum profit sequence of jobs:
       c, a, e
