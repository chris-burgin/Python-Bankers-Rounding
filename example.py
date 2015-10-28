# Import 'Rounding' from 'rounding.py'
from rounding import Rounding

# Create a new instance of the 'Rounding' class
rounding = Rounding()

# Examples

number1 = 2.966
number1 = rounding.BankersRounding(number1)
print('Number 1: ' + str(number1))
# Result: 2.97

number2 = 2.965
number2 = rounding.BankersRounding(number2)
print('Number 2: ' + str(number2))
# Result: 2.96

number3 = 2.975
number3 = rounding.BankersRounding(number3)
print('Number 3: ' + str(number3))
# Result: 2.98

number4 = 2.9735
number4 = rounding.BankersRounding(number4, 3)
print('Number 4: ' + str(number4))
# Result: 2.974

number5 = 2.999
number5 = rounding.BankersRounding(number5)
print('Number 5: ' + str(number5))
# Result: 3.0

number6 = 2.909015
number6 = rounding.BankersRounding(number6, 5)
print('Number 6: ' + str(number6))
# Result: 2.90902
