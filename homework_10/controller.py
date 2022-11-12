import operation as op
import log


def ask_user():
    choise = input('Записать, найти или удалить данные (w/r/d): ')
    if choise == 'w':
        log.write_log(op.add_data(), 'w')
    elif choise == 'r':
        log.write_log(op.find_data(), 'r')
    elif choise == 'd':
        log.write_log(op.delete_data(), 'd')
    else:
        print('Неизвестная команда')
