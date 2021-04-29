import datetime


def transfer_date(raw_date: str) -> datetime.date:
    """
    Example:
    "2021-04-20" => datetime(year=2021, month=04, day=20)
    :param raw_date: str
    :return: datetime.date
    """
    date_obj = datetime.datetime.strptime(raw_date, '%Y-%m-%d').date()
    return date_obj
