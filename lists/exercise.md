# Exercise 1

Create Python 3 program that:

- Declares an empty list

Hint for empty list:

```python
l = []
```

- Then a conditional loop, obtain integers from the user. The loop should stop asking when the user enters the value ```-1```.

Once the loop has finished its course, calculate and display average value of numbers.

## Pseudo-code

```
Variable: numbers, empty list of integers
Variable: n, integer
Variable: average, float

while n is not -1
    Set n to input "Please enter a number, -1 to stop."
    If n is not -1
       Append n to numbers
    End if
end while

Display numbers to screen
Set average to sum of all numbers divided by length of numbers
Display average to screen
```