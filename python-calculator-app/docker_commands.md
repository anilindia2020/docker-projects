## Commands used
cd python-calculator-app/

docker build -t python-calculator .

docker run -it --rm python-calculator



## OUTPUT

$  pwd

/home/admin/python-calculator-app

$  docker run -it --rm python-calculator

--- Simple Python Calculator ---

Enter 'q' at any time to quit

Enter the first number: 45

Enter an operator (+, -, *, /): *

Enter the second number: 2

✅ Result: 45.0 * 2.0 = 90.0

Enter the first number: q

Calculator exiting. Goodbye!
