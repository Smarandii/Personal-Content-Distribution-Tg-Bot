from . import bot, dp, executor, aiogram_types, defined_messages, ContentType
from ContentManagementSystem.content_management_system import ContentManagementSystem
from user_input_validation import Validator


@dp.message_handler(commands=['start'])
async def send_welcome(message: aiogram_types.Message):
    await bot.send_message(message.chat.id, defined_messages.GREETING)


@dp.message_handler(content_types=ContentType.DOCUMENT)
async def add_content(message: aiogram_types.Message):
    validator = Validator(message)
    if validator.user_is_admin() and cms_conn.map_file_id_to_trigger_word(message):
        await bot.send_message(message.chat.id, defined_messages.ADD_CONTENT_SUCCESS)
    else:
        await bot.send_message(message.chat.id, defined_messages.ADD_CONTENT_FAIL)


@dp.message_handler(content_types=ContentType.TEXT)
async def get_content(message: aiogram_types.Message):
    validator = Validator(message)
    user_in_channel = await validator.is_user_in_channel()
    if cms_conn.trigger_word_exists(message.text) and user_in_channel:
        file_id, trigger_word, description = cms_conn.get_file_id_mapped_to(message.text)
        await bot.send_document(message.chat.id, file_id, caption=trigger_word)
    if not user_in_channel:
        await bot.send_message(message.chat.id, defined_messages.NOT_MEMBER)

if __name__ == '__main__':
    while True:
        try:
            cms_conn = ContentManagementSystem()
            executor.start_polling(dp, skip_updates=True)
        except Exception as e:
            print(e)
