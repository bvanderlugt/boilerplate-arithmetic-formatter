# Reflecting on this project

Wow this project took me way longer than expected and the reason was becuase of
the string formatting of the output. I knew that I needed to get neat table like
output for this challenge so I went back to a resource I used in the past that
had good string formatting. In David Beasle's Practical Python course he takes
you through an excercise to create a stock price table. He uses a tiny bit of
the python [string formatting mini-language](https://docs.python.org/2/library/string.html#formatstrings)
to create nice spacing between columns. This is just I needed for this challenge
because of the dynamic nature of the alignment. The total width of each problem
is dependent on the length of the inputs plus the operand. Also, the numbers
have to be right justified. Python's formatting language lets you control this
easily.

For example to print the integer '10' right-justified in a string padded to length 20 you can run:
```
>>> f"{10:>20}"
'                  10'
```

Python let's you make the padding dynamic using the same syntax for variables.

```
>>> width = 4
>>> f"{10:>{width}}"
'  10'
```

Great! The next issue I ran into was that I needed to dynamically set the
spacing between the operator and the lower operand. Also, These two should be
right-justified and have the same padding as the other rows. This created a kind
of nested formatting that I couldn't achieve in one line but I was able to
define one f-string and then call it from inside another one. 

```

```

The next problem was that I needed to align the problems horizontally rather
than printing them line by line so they were laid out vertically. I tried some
techniques to split zip and join the problems but in the end I created an array
for each row and joined the problems together with the requisite four spaces.
Then joined each row with a new line. 

This challenge was conceptually simple but the challenge was in the string
formatting. I learned a lot about string formating in Python. Its really
powerful and I think was worth the time exploring. Now if only I could paste my
clipboard contents in vim...



