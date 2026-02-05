def condition_one(age):
    if age >= 18:
        print(True)
    else:
        print(False)

condition_one(1)
condition_one(19)


for number in [1, 2 ,3]:
    print(number)

#------------------------------------------------
user_input = "" # Надо определить переменную
while user_input != "exit":
    user_input = input()

#------------Альтернатива--------------------------

while True: # Запустили цикл, и не надо инициализировать переменную перед циклом
    user_input = input()
    if user_input == "exit":
        break
#--------------------------------------------------

