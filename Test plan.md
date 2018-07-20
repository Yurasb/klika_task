## Test scope
Only main, atomic calculator operations are considered for functional testing.

## Out of scope
+ boundary testing (e.g. how long could be operands)
+ compound operations (e.g. `5 + 3 * 7 / 2`)
+ operand position - e.g. `5+3` and `3+5`. Such cases are possible and could be 
important in cases of subtraction and division, but considered as extension
+ non-functional requirements - e.g. displaying of floats and negative numbers, 
displaying of operators
+ service actions, e.g. `Clear` and `Clear All`, `Equality`, are considered as functionally valid

## Test techniques
Two main techniques are used:
+ equivalence classes
+ all-pairs

I considered following equivalence classes for operations:
+ addition (`+`)
+ subtract (`-`)
+ division (`/`)
+ multiplication (`*`)

For operands (numbers), I extracted next classes:
+ positive integers
+ negative integers
+ positive floats
+ negative floats
+ zero

All-pairs gives us combination of these clasess as test cases - combine all 
operands classes for each operation class.

## Test cases
Because operand position is not considered as part of testing, this helped to 
reduce number of combinations - e.g. `add positive int to negative int` and 
`add negative int to positive int` are considered as equal.
+ Addition
1. add positive int to positive int
2. add negative int to positive int
3. add positive float to positive int
4. add negative float to positive int
5. add zero to positive int
6. add negative int to negative int
7. add positive float to negative int
8. add negative float to negative int
9. add zero to negative int
10. add positive float to positive float
11. add negative float to positive float
12. add zero to positive float
13. add negative float to negative float
14. add zero to negative float
+ Subtraction
1. subtract positive int from positive int
2. subtract negative int from positive int
3. subtract positive float from positive int
4. subtract negative float from positive int
5. subtract zero from positive int
6. subtract negative int from negative int
7. subtract positive float from negative int
8. subtract negative float from negative int
9. subtract zero from negative int
10. subtract positive float from positive float
11. subtract negative float from positive float
12. subtract zero from positive float
13. subtract negative float from negative float
14. subtract zero from negative float
+ Multiplication
1. multiply positive int by positive int
2. multiply positive int by negative int
3. multiply positive int by positive float
4. multiply positive int by negative float
5. multiply positive int by zero
6. multiply negative int by negative int
7. multiply negative int by positive float
8. multiply negative int by negative float
9. multiply negative int by zero
10. multiply positive float by positive float
11. multiply positive float by negative float
12. multiply positive float by zero
13. multiply negative float by negative float
14. multiply negative float by zero
+ Division
1. divide positive int by positive int
2. divide positive int by negative int
3. divide positive int by positive float
4. divide positive int by negative float
5. divide positive int by zero
6. divide negative int by negative int
7. divide negative int by positive float
8. divide negative int by negative float
9. divide negative int by zero
10. divide positive float by positive float
11. divide positive float by negative float
12. divide positive float by zero
13. divide negative float by negative float
14. divide negative float by zero

## Issue areas
1. precision - headache for operations with float due to difference in float processing
2. subtraction - works fine only with positive integers
    + subtract zero return zero
    + subtract negative number return this number
3. multiplication by negative numbers
4. division by negative numbers
5. division of negative number by zero return `-Infinity`, which is considered 
as bug, but most likely is related to JS feature

## Summary
Majority of issues are found in area of operations with negative numbers.
Only addition works fine in that area. With that I assume compound operations 
would be invalid as well.
Also, flaky tests due to precision are also one of the complex issue on border 
between application implementation and test framework solution.
Only add operations are valid (with regard of precision constraints).
Medium error rate is about 50%, which means that majority of cases out from 
addition are usually failed.
 