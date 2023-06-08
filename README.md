# Health Data Point Capture and Classification

This program captures various health data points, rates them based on specified ranges, and prints the data fields and their classifications to an output file.

## Project Information

- Author: Will Maxcy
- Created: 6/30/2022
- Last Updated: 7/1/2022

## Requirements

- Python 3.x
- PyPDF2 library

## Usage

1. Place the input PDF files in the `Input` directory.
2. Run the program to capture and classify the health data points.
3. The output will be saved to the output file.

## Instructions

1. Import the required libraries:
   - PyPDF2
   - os
   - sys
   - re

2. Set the global variables:
   - `path`: Path to the input files directory.
   - `dirs`: Directories in the input files directory.
   - `files`: Files in the input files directory.

3. Define comparison functions:
   - `compare(reference, low, high)`: Compares a reference number to low and high values and returns a classification code.
   - `lessthan(reference, low)`: Compares a reference number to a low value and returns a classification code.
   - `greaterthan(reference, low)`: Compares a reference number to a low value and returns a classification code.
   - `compare3(reference, low, high)`: Compares a reference number to low and high values and returns a classification code.
   - `match(reference, comp)`: Checks if a reference value matches a comparable variable and returns a classification code.
   - `percentage(reference)`: Placeholder function.

4. Define the printer function:
   - `printer(name, rating)`: Prints the name and classification of a data field.

5. Define the page0 function:
   - `page0(text)`: Scans the first page and captures the required variables using regular expressions. Then, it applies the comparison functions to rate the variables and uses the printer function to print the results.

6. Define the page1 function:
   - `page1(text)`: Scans the second page and captures the required variables using regular expressions. Then, it applies the comparison functions to rate the variables and uses the printer function to print the results.

7. Define the page2 function:
   - `page2(text)`: Scans the third page and captures the required variables using regular expressions. Then, it applies the comparison functions to rate the variables and uses the printer function to print the results.

8. Initialize the `output` variable to store the program's output.

9. Call the page0, page1, and page2 functions for each input file.

10. The program will print the captured data fields and their classifications to the `output` variable.

11. Save the `output` to an output file.

## License

This project is licensed under the [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).
