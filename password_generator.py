import random
import datetime
import string
import os
def get_password_len():
    while True:
        try:
            password_len = int(input("Введите длину пароля (от 8 до 62): ")) 
            if 8 <= password_len <= 62:
                return password_len
            else:
                print("Введите число в интервале (от 8 до 62).") 
        except ValueError:
            print("ERROR: Введите числовое значение.")
def is_special_symbol():
    while True:
        is_there_symbol = input("Хотите добавить спец. символы? Да/Нет\n").strip().lower()
        if is_there_symbol in ['да', 'нет']:
            return is_there_symbol == 'да'
        else:
            print("Введите корректный ответ (да/нет).")         
def generate_password(pass_len, use_special_symbol):  
    uppercase_letters = list(string.ascii_uppercase)
    lowercase_letters = list(string.ascii_lowercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation) if use_special_symbol else []
    all_characters = uppercase_letters + lowercase_letters + digits + punctuation 
    total_unique_chars = len(all_characters)
    if pass_len > total_unique_chars:
        print("Ошибка: запрашиваемая длина пароля превышает количество доступных уникальных символов.") 
        return None
    password = []
    if use_special_symbol:
        num_each_type = pass_len // 4
        extras = pass_len % 4
    else:
        num_each_type = pass_len // 3
        extras = pass_len % 3     
    if num_each_type > 0:
        password.extend(random.sample(uppercase_letters, min(num_each_type, len(uppercase_letters))))
        password.extend(random.sample(lowercase_letters, min(num_each_type, len(lowercase_letters))))
        password.extend(random.sample(digits, min(num_each_type, len(digits))))      
        if use_special_symbol:
            password.extend(random.sample(punctuation, min(num_each_type, len(punctuation))))
    all_characters = uppercase_letters + lowercase_letters + digits + punctuation
    password.extend(random.sample(all_characters, extras))  
    random.shuffle(password)  
    final_password = ''.join(password) 
    print("Сгенерированный пароль:", final_password)  
    return final_password
def save_password(password):
    while True:
        want_to_save = input("Хотите ли сохранить пароль? Да/Нет\n").strip().lower()
        if want_to_save in ['да', 'нет']:
            break
        else:
            print("Введите корректный ответ (да/нет).")
    if want_to_save != 'да':
        print("Хорошо, удачи запомнить пароль!")
        return
    website = input("Для какой платформы создали данный пароль?\n").strip()
    if not website:
        print("ERROR: Веб-сайт не может быть пустым.")  
        return
    date_now = datetime.datetime.now().strftime("|  %d-%m-%Y %H:%M")
    file_path = "passwords.txt"
    file_exists = os.path.exists(file_path)  
    try:
        with open(file_path, "a", encoding="utf-8") as file:
            if not file_exists:
                file.write(f"{'| №':<5} {'|  Пароль':<62} {'|  Дата и Время':<30} {'|  Веб-сайт':<30}\n") 
                file.write("-" * 130 + "\n")     
            record_number = sum(1 for line in open(file_path, "r", encoding="utf-8") if line.strip() and line[0].isdigit()) 
            result = f"{record_number + 1:<5} {password:<62} {date_now:<30} {website:<30}\n" 
            file.write(result)             
        print("Пароль успешно сохранён в файл 'passwords.txt'.")
    except Exception as err:
        print("Ошибка при сохранении пароля:", err)

def main():
    password_len = get_password_len()
    use_special_symbols = is_special_symbol()
    final_password = generate_password(password_len, use_special_symbols)
    if final_password:  
        save_password(final_password)

main()