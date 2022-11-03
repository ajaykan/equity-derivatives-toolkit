import matplotlib.pyplot as plt

class Option:
    def __init__(self, strike, type):
        self.strike = strike
        self.type = type # type either 'call' or 'put'

    def isITM(self, price):
        if self.type == 'call' and self.strike < price:
            return True
        elif self.type == 'put' and self.strike > price:
            return True
        else:
            return False

positions = [
            (Option(65, 'call'), 3),
            (Option(65, 'call'), 2),
            (Option(70, 'call'), 2),
            (Option(70, 'put'), -4),
            (Option(75, 'call'), -5),
            (Option(75, 'put'), 3),
            (Option(80, 'call'), 3),
            ]

minimum = 50
maximum = 100
increment = 5
input_prices = []
output_prices = []

for input in range(minimum, maximum+increment, increment):
    input_prices.append(input)
    output = 0
    for option, quantity in positions:
        if option.isITM(input):
            output += abs(option.strike - input) * quantity
    output_prices.append(output)


plt.plot(input_prices, output_prices)
plt.show()