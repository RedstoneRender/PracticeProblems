# Number 2:
Your program will have a string variable defined at the very beginning of the program. The contents of this variable will text that can include spaces and uppercase characters as well as punctuation. Your program must count the amount of times that any character appears in this text and calculate the percentage of the text which includes this character.
for every unique character in the text, you must print the times it occurs and its frequency and what character it is.

##### example format:
```
The character '<character here>' appears in the text <times it appears> times. It makes up <percentage>% of the text.
```

Send me your code (just make sure I don't have to indent anything manually to make it work please) and I will check it and point out issues.
My solution is 9 lines long.

# Relevant information
This is information that will likely be helpful or even necessary when solving this problem.

## The len function
The len function returns the amount of characters in a string or the number of values in a list.

##### example:
```python
print(len("yeet"))
```

##### output:
```
4
```

##### example:
```python
print(len([1,2,3,4,5]))
```

##### output:
```
5
```

## dictionaries
Dictionaries are a datatype in python. Rather than using indices to address the data in a list, you can use any datatype as the key for a bit of data in a dictionary.

##### example:
```python
dictionary = {"a": 1500, "b": 26}
print(dictionary["a"])
print(dictionary["b"])
dictionary["b"] = 2000
print(dictionary["b"])
dictionary["c"] = 25
print(dictionary["c"])
```

##### output:
```
1500
26
2000
25
```

you can check if a key already exists in a dictionary like this:

##### example:
```python
dictionary = {"a": 1500, "b": 26}
print("a" in dictionary)
print("c" in dictionary)
```

##### output:
```
True
False
```

## String indices
string characters can be accessed like the values of a list.

##### indices of a string:

| y | e | e | t |
|---|---|---|---|
| 0 | 1 | 2 | 3 |

##### example:
```python
x = "why the fuck did you ask me for help an hour before the test like seriously what the fuck, exactly how many pot brownies did you have?"
print(x[0])
print(x[4])
print(x[8])
```

##### output:
```
w
t
f
```

## Strings in for loops
strings can be used in place of the range function in for loops.

##### example:
```python
x = "ur high lol"
for i in x:
  print(i)
```

##### output:
```
u
r

h
i
g
h

l
o
l
```

## Concatenating numbers with strings
in python you need to explicitly concatenate strings with numbers in print statements.

##### example:
```python
x = 10
y = "yeet "
print(y + x)
```

##### output:
```
it errors I don't remember the error exactly
```

##### example:
```python
x = 10
y = "yeet "
print(y + str(x))
```

##### output:
```
yeet 10
```

## Doing decimal math with integers
before doing decimal math with integers you should convert them to floats first.

##### example:
```python
x = 20
y = 299
print(float(20)/float(299))
```
##### output:
```
0.06688963210702341
```
