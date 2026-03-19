from __future__ import annotations


class NotVerifiedException(Exception):
    def __init__(self, user_id: str | None = None):
        self.user_id = user_id
        self.verification_link = (
            f"https://t.me/itd_verification_bot?start={user_id}"
            if user_id else "https://t.me/itd_verification_bot"
        )
        super().__init__(
            f"Аккаунт не верифицирован. "
            f"Подтвердите через Telegram: {self.verification_link}"
        )
