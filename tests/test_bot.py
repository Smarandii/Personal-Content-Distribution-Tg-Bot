from aiogram.utils.exceptions import ValidationError


def test_aiogram_is_installed():
    try:
        import aiogram
    except ImportError:
        assert False


def test_client_token_is_valid():
    try:
        from aiogram import Bot
        from PersonalContentDistributionTgBot.my_secrets import API_TOKEN
        bot = Bot(token=API_TOKEN)
    except ValidationError:
        assert False


def test_dispatcher_is_valid():
    try:
        from aiogram import Bot, Dispatcher
        from PersonalContentDistributionTgBot.my_secrets import API_TOKEN
        bot = Bot(token=API_TOKEN)
        dp = Dispatcher(bot)
    except TypeError:
        assert False


