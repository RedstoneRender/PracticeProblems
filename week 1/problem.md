# Week 1:
Write a program that will print out the numbers 0 through 99. When the program prints a number that is a multiple of 3, print out fizz in addition to the number. When the program prints a number that is a multiple of 5, print out buzz in addition to the number. when the program prints a number that is a multiple of 3 and 5, print out fizzbuzz in addition to the number.

You may not print out fizz or buzz more than once per number-I.e:

##### valid outputs:
```
15
fizzbuzz
```

```
10
buzz
```

##### invalid outputs:
```
15
fizz
buzz
fizzbuzz
```

```
10
fizzbuzz
```

Send me your code (just make sure I don't have to indent anything manually to make it work please) and I will check it and point out issues.
My solution is 8 lines long and was written in probably 45 seconds.

# Relevant information
This is information that will likely be helpful or even necessary when solving this problem.

## The modulus operator (%):
the modulus operator returns the remainder of a division operation.

10 % 2 gives 0 (10 divided by 2 has a remainder of 0)\
21 % 8 gives 5 (21 divided by 8 has a remainder of 5)\
1 % 2 gives 1 (1 divided by 2 has a remainder of 1)

##### example:
```python
x = 5 % 2
print(x)
```

##### output:
```
1
```

## If statements:
If statements evaluate the expression after the if keyword and before the ':' symbol and execute the code in the block if the expression evaluates to true.

##### example:
```python
if 2 > 1:
    print(10)

if 10 < 5:
    print(20)
```

##### output:
```
10
```

## Elif statements:
Elif statements are short for else if. They are only evaluated if the condition preceding them evaluates to false and if their condition evaluates to true.

##### example:
```python
if 2 > 1:
    print(10)
elif 10 > 2:
    print(20)
```

##### output:
```
10
```

##### example 2:
```python
if 2 < 1:
    print(10)
elif 10 > 2:
    print(20)
```

##### output:
```
20
```

## Else statements:
Else statements only run the code in the block if the none of the if and elif statements preceding them evaluated to true.

##### example:
```python
if 2 > 1:
    print(10)
elif 10 > 2:
    print(20)
else:
    print(30)
```

##### output:
```
10
```

##### example 2:
```python
if 2 < 1:
    print(10)
elif 10 > 2:
    print(20)
else:
    print(30)
```

##### output:
```
20
```

##### example 3:
```python
if 2 < 1:
    print(10)
elif 1 > 2:
    print(20)
else:
    print(30)
```
##### output:
```
30
```
