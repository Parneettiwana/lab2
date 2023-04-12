#declaring inputs
x = float(input("Starting number of organism:"))
# average
per = float(input("Average daily percentage increase:"))
# declaring results
total = int(input("Enter the number of days to display the final data:"))
print("day approximate", "       ", "population")
c = x
print(x)
for i in range(1, total):
  #for increament
  c = x + (x * (per / 100))
  print(i, "                ", c, "\n")
  x = c