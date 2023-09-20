m = {"A","B","C", "A"}
print("1: ", m)
m.add("E")
print("2: ",m)
m.update("A","F","G")
print("3: ",m)
m.discard("A")
print("4: ",m)
m.union({"W","F","H"})
print("5: ",m)
m.intersection({"A","B","C"})
print("6: ",m)

