#whole list
a = []
b = int(input("Enter Number: "))
i = 0
while (i < b):
  a.append(int(input("Enter Element : ")))
  i = i + 1
print(a)

c = []
i = 0
#for getting output greater than 12
while (i < b):
  if (a[i] > 12):
    c.append(a[i])
  else:
    pass

  i = i + 1
print("lists of number larger than 12", c)
