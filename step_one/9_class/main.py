from app.People.people import person
from app.Students.student import studing

s1 = studing("aaaa", 2, "A")
s2 = studing("bbb", 5, "B")
s1.show_detail()
s2.show_detail()
print()

s1.greet()
print()

print(s1)
print()

from app.services.services import build_pet, check_all_pets, all_detail

pets_infor = [
     {"species":"dog", "name":"aa", "age":"5", "temperature":39},
     {"species":"dog", "name":"bb", "age":"7", "temperature":37},
     {"species":"cat", "name":"cc", "age":"8", "mood":"bad", "temperature":39.5},
     {"species":"cat", "name":"dd", "age":"9", "mood":"good", "temperature":39},
     ]

# pet_infor 传给services
pets = build_pet(pets_infor)
# pet_infor 传给services 处理完，调用check_all_pets ,传进去的是 pets(上一行已经造好的对象列表),不是 pet_infor 本身。
check_all_pets(pets)
all_detail(pets)
