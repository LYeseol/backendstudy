#사용자 입력에서 list만들기

user_input_list = []
num_element = int(input("Enter Number of Element: "))
for i in range(num_element):
    user_input_list.append(input('enter element: '))

print('user input list: ')
for element in user_input_list:
    print(element)