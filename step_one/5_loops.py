
for i in range(10):
     print(i)
print("------")


count = 0 
while count < 11:
     print(count)
     count += 1
print("-------")


for i in range(12):
     if i == 2:
          continue
     if i == 4:
          continue
     if i == 6:
          continue
     if i == 8:
          break
     print(i)
print("------")

a = 2
for i in range(102):
     a +=1
     print(i)
print("------")
print()

for i in range(3, 10):
     print(i)
     print("------")
     i  += 1
     print(i)
     print("+++++")
print()

for i in range(2,15,3):
     print(i)


     