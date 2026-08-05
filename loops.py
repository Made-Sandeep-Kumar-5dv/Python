# Print all perfect square numbers between 1 and 100.
for n in range(1, 101):
    if int(n ** 0.5) == n ** 0.5:
        print(n)
        
# Print all Armstrong numbers between 1 and 100# Armstrong numbers between 1 and 100
for n in range(1, 101):
    digits = str(n)
    power = len(digits)
    total = 0
    # use for loop to calculate sum of powers
    for i in digits:
        total += int(i) ** power
    if total == n:
        print(i)

