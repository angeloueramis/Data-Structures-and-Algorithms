Data Structures and Algorithms.

The folder "DSA GRAPHS" contains screenshots of the results of each equation plotted on a graph.

The folder named "DSA ASSIGNMENT" contains two files, namely "dsass1.py" and "input.txt". 
 - "dsass1.py" contains the code for solving equations with x values of 1-50. 
 - "input.txt" contains the input values for x and the results of each equation for each value.

This code is a Python script that allows users to select from a list of mathematical equations and plot the results of those equations using Matplotlib. A brief description of how the code works is as follows:

 - The code begins with importing the necessary libraries: matplotlib.pyplot for plotting and math for mathematical functions.
 - It prints out a menu of equations numbered from 1 to 10.
 - It prompts the user to choose a number corresponding to the equation they want to plot.
 - It defines 10 different functions (p1() to p10()), each representing one of the equations listed in the menu. These functions calculate       the results of their respective equations for a range of x-values.
 - The code then opens a file named "input.txt" in write mode.
 - Depending on the user's choice, it calls one of the equation functions, writes the results to the file, and plots the results using Matplotlib.
 - Finally, it displays the plot with appropriate labels and legends.
