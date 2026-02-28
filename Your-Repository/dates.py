from datetime import date, datetime, timedelta, timezone


def today_date():
    return date.today()


def current_datetime_utc():
    return datetime.now(timezone.utc)


def add_days(start_date, days):
    return start_date + timedelta(days=days)


def days_between(date1, date2):
    return abs((date2 - date1).days)


def format_datetime(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def parse_datetime(value):
    return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")


def convert_timezone(dt, hours_offset):
    return dt.astimezone(timezone(timedelta(hours=hours_offset)))


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def next_weekday(start, weekday):
    days_ahead = weekday - start.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start + timedelta(days=days_ahead)


if __name__ == "__main__":
    today = today_date()
    print("Today:", today)

    now_utc = current_datetime_utc()
    print("UTC now:", now_utc)

    future = add_days(today, 10)
    print("After 10 days:", future)

    print("Days between:", days_between(today, future))

    formatted = format_datetime(now_utc)
    print("Formatted:", formatted)

    parsed = parse_datetime("2026-01-01 12:00:00")
    print("Parsed:", parsed)

    print("UTC+6:", convert_timezone(now_utc, 6))

    print("Leap year 2024:", is_leap_year(2024))

    print("Next Monday:", next_weekday(today, 0))