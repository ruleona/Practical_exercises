"""Программа, заменяющая значения в текстовом документе.
Перед стартом убедитесь, что файл закодирован в utf-8"""

print('Здравствуйте.')
while True:
    action = input('\nВыберите действие:\n 1 - Редактировать\n 2 - Выход\n')
    if action == '2':
        break
    elif action == '1':
        value_to_change = input('Значение, которое нужно изменить: \n ')
        new_value = input('Новое значение: \n')
        file_path = r"C:\Users\Елена\Desktop\edit.txt"

        with open(file_path, 'r', encoding='utf-8') as open_file:
            content = open_file.read()

        new = content.replace(value_to_change, new_value)
        print(new)

        with open(file_path, 'w', encoding='utf-8') as open_file:
            open_file.write(new)
    else:
        print('Неверная команда. Попробуйте еще раз.')
print("До свидания.")


