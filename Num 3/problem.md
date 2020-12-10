# Number 3:
Create a function that takes in a string and returns a string. You are allowed to assume that the input will always be a string. This function should invert the case of every other character in the string. Characters that do not have alternate cases (?,!,.,etc) should be kept the same.

##### example input and output:

```
input:
Hello there!
output:
HElLo tHeRe!
```

please note that the output
```
heLlO ThErE!
```
is also valid.

Send me your code (just make sure I don't have to indent anything manually to make it work please) and I will check it and point out issues.
My solution is 11 lines long.

# Relevant information
This is information that will likely be helpful or even necessary when solving this problem.

## upper method:
the `upper` method in python returns the string that is called on with all characters that have a corresponding case in their uppercase form. It will leave already uppercase characters as uppercase.

##### example:
```python
print("Yeet".upper())
```

##### output:
```
YEET
```

## lower method:
the `lower` method in python returns the string that is called on with all characters that have a corresponding case in their lowercase form. It will leave already lowercase characters as uppercase.

##### example:
```python
print("YEEt".lower())
```

##### output:
```
yeet
```
