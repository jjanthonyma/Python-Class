#p21.py
#Jose Melgar
#9/25/2024
#Python 3.12.5
#program  the sum of negative positive and all numbers

# penny value
pennyValue = 0.01

# Day 
day = 30

# Double penny value
for day in range(1, day + 1):
    pennyValue *= 2

# amount ($1,000,000)
amount = 1000000

# difference penny value and amount
difference = pennyValue - amount


print(f"Value of the penny after {day} days: ${pennyValue:.2f}")

# conditions
if difference > 0:
    print(f"The penny is ${difference:.2f} more valuable than the fixed amount.")
elif difference < 0:
    print(f"The penny is ${abs(difference):.2f} less valuable than the fixed amount.")
else:
    print("The cent has the same value as the fixed amount.")


"========== RESTART: C:/Users/janth/Desktop/phyton class/class4/p21.py =========="
"Value of the penny after 30 days: $10737418.24"
"The penny is $9737418.24 more valuable than the fixed amount."
