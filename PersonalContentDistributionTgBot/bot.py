from PersonalContentDistributionTgBot import bot, dp, executor, aiogram_types, defined_messages, ContentType
from PersonalContentDistributionTgBot.ContentManagementSystem.content_management_system import ContentManagementSystem


@dp.message_handler(commands=['start'])
async def send_welcome(message: aiogram_types.Message):
    await bot.send_message(message.chat.id, defined_messages.GREETING)


@dp.message_handler(content_types=ContentType.DOCUMENT)
async def add_content(message: aiogram_types.Message):
    if cms_conn.map_file_id_to_trigger_word(message):
        await bot.send_message(message.chat.id, defined_messages.ADD_CONTENT_SUCCESS)
    else:
        await bot.send_message(message.chat.id, defined_messages.ADD_CONTENT_FAIL)


@dp.message_handler(content_types=ContentType.TEXT)
async def get_content(message: aiogram_types.Message):
    if cms_conn.trigger_word_exists(message.text):
        file_id, trigger_word, description = cms_conn.get_file_id_mapped_to(message.text)
        await bot.send_document(message.chat.id, file_id, caption=trigger_word)


if __name__ == '__main__':
    while True:
        try:
            cms_conn = ContentManagementSystem()
            executor.start_polling(dp, skip_updates=True)
        except Exception as e:
            print(e)
