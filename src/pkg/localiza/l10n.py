import datetime

import flask_babel as fb
from flask import g, request, current_app, Flask


class L10n:

    def __init__(self, app: Flask):
        self.babel = fb.Babel(app=app)

        @self.babel.localeselector
        def get_locale():
            user = getattr(g, "user", None)
            if user is not None:
                return user.locale
            return request.accept_languages.best_match(["en", "vi"])

        @self.babel.timezoneselector
        def get_timezone():
            user = getattr(g, "user", None)
            if user is not None:
                return user.timezone
            return current_app.config["BABEL_DEFAULT_TIMEZONE"]


def format_datetime(date_time: datetime.datetime, *args, **kwargs):
    return fb.format_datetime(datetime=date_time, *args, **kwargs)


def format_date(date: datetime.date, *args, **kwargs):
    return fb.format_date(date=date, *args, **kwargs)


def format_currency(price: int | float, *args, **kwargs):
    return fb.format_currency(price, currency=current_app.config["CURRENCY_TYPE"],
                              format=u"{format}".format(format=current_app.config["CURRENCY_FORMAT"]), *args, **kwargs)


def format_percent(percent: int | float, *args, **kwargs) -> str:
    """
       Format percent.
       :param str percent: the percent will be formatted ( min: 0, max: 1 )
       :param *args
       :param **kwargs
       :rtype: str
       :raises ValueError: if the message_body exceeds 160 characters
       :raises TypeError: if the message_body is not a basestring
       """

    return fb.format_percent(number=percent)
