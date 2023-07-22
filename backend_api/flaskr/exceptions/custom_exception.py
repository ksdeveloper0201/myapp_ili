"""カスタム例外クラス"""


class IsNotFound(Exception):
    """データがみつからない時のエラー

    Args:
        Exception (_type_): _description_
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class LoginProhibitingException():
    """ログイン禁止エラー
    """

    def __init__(self, *args: object) -> None:
        super().__init(*args)
