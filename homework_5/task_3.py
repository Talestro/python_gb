# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_encode(sourse_str):
    coded_str, item = "", 0
    while item < len(sourse_str):
        count = 1
        while item + 1 < len(sourse_str) and sourse_str[item] == sourse_str[item + 1]:
            count += 1
            item += 1
        coded_str += str(count) + sourse_str[item]
        item += 1
    return coded_str


def rle_decode(rle_str):
    decoded_str, count = '', ''
    for char in rle_str:
        if char.isdigit():
            count += char
        else:
            decoded_str += char * int(count)
            count = ''
    return decoded_str


def ask_user():
    operation = input('Type a letter for what operations you want:\n'
                      'e - encode\n'
                      'd - decode\n')
    if operation == 'e':
        with open('for_encode.txt', 'r') as f:
            source_data = f.read()
        with open('coded_file.txt', 'w') as f:
            f.write(rle_encode(source_data))
        print(f'Your data encoded')
    elif operation == 'd':
        with open('coded_file.txt', 'r') as f:
            coded_content = f.read()
        with open('decoded_file.txt', 'w') as f:
            f.write(rle_decode(coded_content))
        print(f'Your data decoded')
    else:
        print(f'Unknown operation try again')


ask_user()
