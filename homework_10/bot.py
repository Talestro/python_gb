import logging
import log
import operation

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove



TOKEN = '5669367414:AAG0NQNbNDDXpFG3D1ZCyrIVv-fNbWj74Uk'
dp = Dispatcher()
logger = logging.getLogger(__name__)


class Form(StatesGroup):
    main_menu = State()
    phonebook_menu = State()
    add_type_menu = State()
    test_answer = State()
    get_one_line_add = State()
    find_data = State()
    dell_data = State()
    #get_mult_line_add = State()
    city_name =State()


@dp.message(Command(commands=['start']))
async def command_start_handler(message: Message) -> None:
    await message.answer(f'Здравствуйте, <b>{message.from_user.full_name}!</b>\n'
                         f'Чтобы узнать возможности бота введите: /help')


@dp.message(Command(commands=['help']))
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.main_menu)
    await message.reply(f'Список комманд:\n'
                         f'Для доступа к работе с телефонным справочником введите /phonebook\n'
                         f'В телефонном справочнике ыв можете добавлять, удалять и искать записи\n\n'
                         f'Также можно посмотреть погоду в любом городе, для этого нужно ввести /weather\n\n'
                         f'Для получения лога всех операций введите: /log')



@dp.message(Command(commands=['weather']))
async def get_city(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Form.city_name)
    await message.reply(' В каком городе нужно узнать погоду? '
                        'введите наименование города на английском языке ',
                         reply_markup=ReplyKeyboardRemove())
    
@dp.message(Form.city_name)
async def weather_message(message: Message, state: FSMContext) -> None:
    record = await state.update_data(answer=message.text)
    record = record['answer']
    await message.reply(operation.get_weather(record))


@dp.message(Command(commands=['phonebook']))
async def cmd_dialog_root(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Form.phonebook_menu)
    await message.reply(
        f'Выберите десйтвия для работы с записями',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[
                    KeyboardButton(text='Добавить'),
                    KeyboardButton(text='Найти'),
                    KeyboardButton(text='Удалить'),
                ]], resize_keyboard=True,),)


# @dp.message(Form.phonebook_menu, F.text.contains('Добавить'))
# async def cmd_dialog_phonebook(message: types.Message, state: FSMContext) -> None:
#     await state.set_state(Form.add_type_menu)
#     await message.reply(
#         f'Выбирите тип ввода',
#         reply_markup=ReplyKeyboardMarkup(
#             keyboard=[[
#                     KeyboardButton(text='Однострочный'),
#                     KeyboardButton(text='Многострочный'),
#                 ]], resize_keyboard=True,),)


#@dp.message(Form.add_type_menu, F.text.contains('Однострочный'))
@dp.message(Form.phonebook_menu, F.text.contains('Добавить'))
async def one_line_add(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.get_one_line_add)
    await message.reply('Введите фамилию, имя, номер телефона, '
                        'должность, заработную плату через запятую в одну строку: ',
                         reply_markup=ReplyKeyboardRemove())


@dp.message(Form.get_one_line_add)
async def process_message(message: Message, state: FSMContext) -> None:
    record = await state.update_data(answer=message.text)
    record = record['answer'].split(',')
    await message.reply(operation.add_data(record))

 


@dp.message(Form.phonebook_menu, F.text.contains('Найти'))
async def cmd_dialog1(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.find_data)
    await message.reply('Введите данные для поиска: ', reply_markup=ReplyKeyboardRemove())


@dp.message(Form.find_data)
async def process_message(message: Message, state: FSMContext) -> None:
    find_request = await state.update_data(answer=message.text)
    await message.reply(operation.find_data(find_request['answer']))


@dp.message(Form.phonebook_menu, F.text.contains('Удалить'))
async def cmd_dialog1(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.dell_data)
    await message.reply('Введите данные для удаления', reply_markup=ReplyKeyboardRemove())


@dp.message(Form.dell_data)
async def process_message(message: Message, state: FSMContext) -> None:
    dell_request = await state.update_data(answer=message.text)
    await message.reply(operation.delete_data(dell_request['answer']))


@dp.message(Command(commands=['log']))
async def command_start_handler(message: Message) -> None:
    await message.reply(log.get_log())


def main() -> None:
    bot = Bot(TOKEN, parse_mode='HTML')
    dp.run_polling(bot)


if __name__ == '__main__':
    print('Сервер запущен')
    main()
