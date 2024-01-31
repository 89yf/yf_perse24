# ----- Task 1 -----
x = int(input())
y = int(input())
z = int(input())

fee = x + y*z*12
print(fee)

# ----- Task 2 -----
money = int(input())
cost = int(input())

no_rides = money//cost # % gives remainder & // gives quotient
print(no_rides)

# ----- Task 3 -----
msg = str(input())

d = str(msg[2:] + msg[:2])
print(d)

# ----- Task 4 -----
f = str(input())
s = str(input())
t = str(input())

if f == s and s == t:
  print("OK")
elif f != s and f != t:
  print("BOTH MISMATCH")
elif f != s:
  print("ENTRY 2 MISMATCH")
elif f != t:
  print("ENTRY 3 MISMATCH")

# ----- Task 5 ----- 2/3 testcase1: runtime error
drink = str(input())
if drink == 't' or 'c':
  add = int(input())
else:
  add = 0
total = 1 + add
if total >= 10:
  print("10 is the maximum!")
else:
  print(total)

# ----- Task 6 -----
