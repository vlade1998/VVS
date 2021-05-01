This code runs tests upon a silly pascal identifier validator. The equivalence classes for the problem are shown below:


|         | Input condition                 | Valid classes           | Invalid classes     |
|---------|---------------------------------|-------------------------|---------------------|
| Length  | Length of identifier            | 1 <= \|identifier\| < 7 | \|identifier\| >= 7 |
|         |                                 |                         | \|identifier\| = 0  |
| General | Starts with a letter?           | Yes                     | No                  |
|         | Contains only valid characters? | Yes                     | No                  |

How to run the code:

* Run the test_silly_pascal file (python test_silly_pascal.py)

or

* Run pytest inside the "Week 2" folder 