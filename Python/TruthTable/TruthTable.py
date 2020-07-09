def truthtable (n):
  if n < 1:
    return [[]]
  subtable = truthtable(n-1)
  return [ row + [v] for row in subtable for v in [0,1] ]
"""
Reference : GeeksforGeeks

"""



arr = truthtable(3)

for i in range (0,len(arr)):
    arr[i] = "".join(arr[i])
print(arr)