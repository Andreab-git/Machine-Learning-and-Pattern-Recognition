# Laboratory 1
Exercise 1 (adapted from Computer Sciences exam 03/09/2012) <br>
Write a program able to handle the scores of an artistic gymnastic event. The event scores are contained in a file whose name is passed from the command line.<br>Every line of the file contains: the competitors name and surname, competitors nationality, and the assigned evaluations provided by 5 judges.<br>
For example, the file (score.txt) contains:

Donald Duck ITA 9.3 8.9 9.7 9.7 9.8<br>
Mickey Mouse ITA 9.0 9.0 9.0 9.2 9.5<br>
Bugs Bunny USA 8.4 8.7 8.5 8.6 9.0<br>
Daffy Duck RUS 8.3 8.8 9.5 9.6 9.0<br>
Charlie Brown GRB 8.2 8.9 8.9 8.6 9.3<br>

## Assumptions:
• The total number of records (lines) is not known <br>
• The competitors name and surname do not contain spaces <br>
• There are always 5 evaluations for every competitor, and these numbers are separated by a space <br>

### The program should show: <br>
• The final ranking for the best 3 competitors: consider that for computing the final records, the highest and lowest evaluations are ignored and the score is determined by the sum of the remaining
3 values. <br>
• The best country: the one that obtained the best score considering the sum of all the competitors of this country (always ignoring for every competitor the highest and lower evaluations).<br>
<br>
### For the provided file, the program output should be<br>
final ranking:<br>
1: Donald Duck -- Score: 28.7 <br>
2: Daffy Duck Score: 27.3 <br>
3: Mickey Mouse Score: 27.2 <br>
<br>
Best Country: <br>
ITA Total score: 55.9
