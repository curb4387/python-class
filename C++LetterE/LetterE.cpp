// LetterE.cpp - This program prints the letter E with 3 asterisks
// across and 5 asterisks down. 
// Input:  None
// Output: Prints the outline of the letter E. 

#include <iostream>
#include <string>
using namespace std;
int main()
{
   const int NUM_ACROSS = 3;  // Number of asterisks to print across
   const int NUM_DOWN = 5;    // Number of asterisks to print down
   int row; // Loop control for row number
   int column;    // Loop control for column number

   row = 1;
   while(row <= NUM_DOWN) {
      column = 1;
      while(column <= NUM_ACROSS) {
         if (row == 1 || row == 3 || row == 5) {
               cout << "*";
               } else if (column == 1) {
                     cout << "*";
               } else {
                     cout << " "; 
               }
         column++;
      }                      
   // Figure out where to place this statement that prints a newline.    
      cout << endl;
      row++;
   }
   return 0; 
}