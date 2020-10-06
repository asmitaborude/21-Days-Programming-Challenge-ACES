import math
print('The Floor and Ceiling value of 23.56 are: ' + str(math.ceil(23.56)) + ', ' + str(math.floor(23.56)))
x = 10
y = -15
print('The value of x after copying the sign from y is: ' + str(math.copysign(x, y)))
print('Absolute value of -96 and 56 are: ' + str(math.fabs(-96)) + ', ' + str(math.fabs(56)))
my_list = [12, 4.25, 89, 3.02, -65.23, -7.2, 6.3]
print('Sum of the elements of the list: ' + str(math.fsum(my_list)))
print('The GCD of 24 and 56 : ' + str(math.gcd(24, 56)))
x = float('nan')
if math.isnan(x):
    print('It is not a number')
x = float('inf')
y = 45
if math.isinf(x):
    print('It is Infinity')
print(math.isfinite(x)) #x is not a finite number
print(math.isfinite(y)) #y is a finite number

# power and logarithmic functions

print('The value of 5^8: ' + str(math.pow(5, 8)))
print('Square root of 400: ' + str(math.sqrt(400)))
print('The value of 5^e: ' + str(math.exp(5)))
print('The value of Log(625), base 5: ' + str(math.log(625, 5)))
print('The value of Log(1024), base 2: ' + str(math.log2(1024)))
print('The value of Log(1024), base 10: ' + str(math.log10(1024)))

#trigonometric and angular conversion functions

print('The value of Sin(60 degree): ' + str(math.sin(math.radians(60))))
print('The value of cos(pi): ' + str(math.cos(math.pi)))
print('The value of tan(90 degree): ' + str(math.tan(math.pi/2)))
print('The angle of sin(0.8660254037844386): ' + str(math.degrees(math.asin(0.8660254037844386))))