import os

from aiogram import types as aiogram_types
import urllib.parse
import httpx


class Validator:

    def __init__(self, message: aiogram_types):
        self.user_id = message.chat.id

    def user_is_admin(self):
        return self.user_id == 523055322 or self.user_id == 231584958

    @staticmethod
    def add_content_syntax_satisfied_in(message: aiogram_types.Message):
        return message

    async def is_user_in_channel(self, channel_id: int = "@theimaria_personalbrand") -> bool:
        """Returns True if user `user_id` in `channel_id` now"""
        url = self._get_tg_url(method="getChatMember", chat_id=channel_id, user_id=self.user_id)
        async with httpx.AsyncClient() as client:
            json_response = (await client.get(url)).json()
        try:
            return json_response["result"]["status"] in (
                "member",
                "creator",
                "administrator",
            )
        except KeyError:
            return False

    @staticmethod
    def _get_tg_url(method: str, **params) -> str:
        """Returns URL for Telegram Bot API method `method`
        and optional key=value `params`"""
        url = f"https://api.telegram.org/bot{os.environ['API_TOKEN']}/{method}"
        if params:
            url += "?" + urllib.parse.urlencode(params)
        return url