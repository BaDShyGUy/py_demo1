# py_demo1

## compute_data
Takes a file as input and find the max, min, and average salaries in the file. <br/>
Also, finds the number of satisfied respondents.

### Steps to build "compute_data":
* Declare some local scope variables for temporary assignment.
* Open the file.
  * Read all lines in the file and assign to a variable. 
* Loop through all the lines (slicing first line since it's headers for the data).
  * Strip and split all the lines on the character ' | '.
  * Append the desired piece of data as float (index 4 out of the split which returns a list).
* If second piece of desired data is not in satisfaction dictionary set dictionary key with value equal to 0.
  * If it exists increment it by +1.
* Break out from under loop, assign max to the max() of the salaries list, do the same for the min() method.
  * Calculate the average by sum() of the salaries and divide by the len() of the salaries.
* Loop through local dictionary variable for .items().
  * If the key with .lower() NOT contains 'dissatisfied' (would pick-up both satisfied and dissatisfied if looking for just 'satisfied') then add the value of that key (number of respondents who selected that response) to satisfied variable.
* Return desired data in a tuple.
