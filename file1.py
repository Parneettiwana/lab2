l = 0
#declaring input from user
num = int(input("enter year: "))
while (l < num):
  j = 0
  k = 0
  total = 0
  while (j < 12):
    print("enter the name of the  month:", j + 1, "")
    k = int(input())
    total = total + k
    j += 1
  l = l + 1
  #total
avg = total / 12
print("totally :", total, "")
#finding average
print("Average of monthly rainfall:",avg,"")