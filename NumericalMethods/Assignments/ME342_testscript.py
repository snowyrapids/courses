# This test script uses Python 3.4 or newer.  To run it, type
# "python3 ME342_testscript.py" into the command prompt (without the quotes)
# and push enter.

# Testing numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10)
line, = plt.plot(x, np.sin(x), '--', linewidth=2)

dashes = [10, 5, 100, 5]  # 10 points on, 5 off, 100 on, 5 off
line.set_dashes(dashes)

plt.show()

# You should see a plot of a sine wave appear


# Testing the Sympy library
import sympy as s
s.init_printing(use_unicode=True)

x, y, z = s.symbols('x y z')
print(s.simplify(s.gamma(x)/s.gamma(x - 2)))


# You might not see the sympy output when running this script.  If not, verify that
# sympy is working by typing the four code lines above directly into the interpreter.
# enter "exit()" without the quotes to exit the interpreter.



