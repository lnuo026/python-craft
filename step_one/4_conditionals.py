age = 10
is_healthy = True

print()
print( age > 7 and is_healthy)
print(age > 7 or is_healthy)
print(not is_healthy)

if age > 7 and not is_healthy:
     print("old and not good, need to check")
if age > 7:
     print("old and health, but still need to check")
else:
     print("younth and health")

print(age > 7 and not is_healthy)
print()
print(not(age > 7 and is_healthy))
print()
print(not( age > 7) or not is_healthy)
