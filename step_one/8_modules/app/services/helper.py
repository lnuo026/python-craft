
# method
def say_name(name):
     print(f"Hello, {name}, from hepler module!")
     print()




# test
print(f",helper.py loaded, __name__ is {__name__}")

if __name__ == "__main__":
     print("I was run directly")
     print()
else:
     print("I was imported by another file")
     print()