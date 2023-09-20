vals = [(x+1)**2 for x in range(1,5)]
print(vals)

vals2 = [1,2,3]
vals2 = [i*2 for i in vals2]
print(vals2)

vals3 = [7,2,19,8,5]
vals3 = [k for k in vals3 if k<7]
print(vals3)

vals4 = [7,2,19,8,5]
vals4= [k-10 for k in vals4 if k>=7]
print(vals4)