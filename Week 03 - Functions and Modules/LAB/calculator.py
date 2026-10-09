print('hello')
"""
1. Define a function `add(n1, n2)` that returns `n1 + n2`.
2. Define a function `subtract(n1, n2)` that returns `n1 - n2`.
3. Define a function `multiply(n1, n2)` that returns `n1 * n2`.
4. Define a function `divide(n1, n2)` that returns `n1 / n2`.
5. Use `input()` to ask for the first number. Convert it with `float()` and
   store it in `n1`.
6. Create a variable `keep_going` and set it to `True`.
7. Start a `while keep_going:` loop.
8. Inside the loop, ask for an operator (`+ - * /`) and store it in
   `operator`.
9. Ask for the second number, convert it with `float()`, and store it in `n2`.
10. Use `if`/`elif` to call the matching function and store the answer in
    `result`. For example, if `operator == "+"`, then `result = add(n1, n2)`.
11. Print the calculation and the result.
12. Ask the user: `"Type 'y' to continue with the result, or 'n' to start over:"`
13. If they type `"y"`, set `n1 = result`.
14. Otherwise, ask for a new first number and store it in `n1`.
   """

def add(n1 , n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multioly(n1 ,n2):
    return n1 * n2

def divide(n1 , n2):
    return n1 / n2

n1 = float(input('Enter 1st value:'))

keep_going = True

while keep_going:
    operator = input('Enter one of the operators (+ - * /)')
    n2 = float (input('Enter 2nd value:'))

    if operator == '+':
        result = add(n1 , n2)
        print(f'{n1} {operator} {n2} = {result}')

        choice = input("Type 'y' to continue, 'n' to start over, 'q' to quit")

        if choice == 'y':
            n1 = result
        elif choice == 'q':
             print(f'{n1} {operator} {n2} = {result}')
             keep_going = False

             

