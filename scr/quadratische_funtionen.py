# how to calculate roots

import math

a,b,c = 1,8,3 # Koeffizienten von ax^2 + bx + c

discriminant = math.pow(b,2) - 4 * a * c

if discriminant < 0:
    print("Keine reele Lösung")
else:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b + math.sqrt(discriminant)) / (2*a)
    print("x1 = ", round(x1,3), "x2 = ", round(x2,3))


