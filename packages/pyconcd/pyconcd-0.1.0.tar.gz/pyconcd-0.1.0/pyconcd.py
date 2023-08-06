"""Countdown until the next PyCon."""

from pyfiglet import Figlet
from datetime import datetime
from dateutil import tz

__version__ = "0.1.0"

PYCON_DATE = datetime(2020, 4, 15, 8, 00, 00, tzinfo=tz.gettz("America/New_York"))


def main():
    timezone = tz.gettz("America/New_York")
    f = Figlet()
    now = datetime.now(tz=timezone)
    countdown = now - PYCON_DATE
    print(f.renderText(str(countdown)))


if __name__ == "__main__":
    main()
