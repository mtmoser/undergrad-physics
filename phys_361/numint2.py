# Numerical integration assignment #2 (evaluating log2)
# Miles Moser
# PHYS 361

# One-pointnu scheme
a1 = 1
print('a1 =', a1)

# Two-point scheme
a2 = (1/2)*(1/1) + (1/2)*(1/2)
print('a2 =', a2)

# Three-point scheme
a3 = (1/6)*((1/1)+4*(1/1.5)+(1/2))
print('a3 =', a3)

# Four-point scheme
a4 = (1/8)*((1/1)+3*(3/4)+3*(3/5)+(1/2))
print('a4 =', a4)