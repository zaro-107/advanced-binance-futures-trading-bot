class TradingBotException(Exception):
    pass

class ValidationException(TradingBotException):
    pass

class APIException(TradingBotException):
    pass