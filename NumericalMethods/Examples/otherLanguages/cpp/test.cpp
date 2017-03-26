#include <iostream>
#include <cmath>
using namespace std;

// Declarations
void printMe(int firstInt, int secondInt);
void printMe(int firstInt, double firstDouble);


int main()
{
   // Variable Declarations
   int int1 = 1;
   int int2 = 2;
   double d1 = 2;

   cout << "Hello World!\n";
   printMe(int1,int2);
   printMe(int1,d1);

   return 0;
}

// Functions
void printMe(int firstInt, int secondInt)
{
   cout << "int1/int2: " << firstInt/secondInt << endl;
}

void printMe(int firstInt, double firstDouble)
{
   cout << "int1/d1: " << firstInt/firstDouble << endl;
}

