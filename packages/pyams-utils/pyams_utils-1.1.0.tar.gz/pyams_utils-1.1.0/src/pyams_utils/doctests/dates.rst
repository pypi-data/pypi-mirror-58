
Dates functions
---------------

Dates functions are used to convert dates from/to string representation:

    >>> import pytz
    >>> from datetime import datetime
    >>> from pyams_utils import date
    >>> gmt = pytz.timezone('GMT')
    >>> now = datetime.fromtimestamp(1205000000, gmt)
    >>> now
    datetime.datetime(2008, 3, 8, 18, 13, 20, tzinfo=<StaticTzInfo 'GMT'>)

You can get an unicode representation of a date in ASCII format using 'unidate' fonction ; date is
converted to GMT:

    >>> udate = date.unidate(now)
    >>> udate
    '2008-03-08T18:13:20+00:00'

'parse_date' can be used to convert ASCII format into datetime:

    >>> ddate = date.parse_date(udate)
    >>> ddate
    datetime.datetime(2008, 3, 8, 18, 13, 20, tzinfo=<StaticTzInfo 'GMT'>)

'date_to_datetime' can be used to convert a 'date' type to a 'datetime' value ; if a 'datetime' value
is used as argument, it is returned 'as is':

    >>> ddate.date()
    datetime.date(2008, 3, 8)
    >>> date.date_to_datetime(ddate)
    datetime.datetime(2008, 3, 8, 18, 13, 20, tzinfo=<StaticTzInfo 'GMT'>)
    >>> date.date_to_datetime(ddate.date())
    datetime.datetime(2008, 3, 8, 0, 0)


Timezones handling
------------------

Timezones handling gave me headaches at first. I finally concluded that the best way (for me !) to handle
TZ data was to store every datetime value in GMT timezone.
As far as I know, there is no easy way to know the user's timezone from his request settings. So you can:
- store this timezone in user's profile,
- define a static server's timezone
- create and register a ServerTimezoneUtility to handle server default timezone.

My current default user's timezone is set to 'Europe/Paris'; you should probably update this setting in
'timezone.py' if you are located elsewhere.

    >>> from pyams_utils import timezone
    >>> timezone.tztime(ddate)
    datetime.datetime(2008, 3, 8, 18, 13, 20, tzinfo=<StaticTzInfo 'GMT'>)

'gmtime' function can be used to convert a datetime to GMT:

    >>> timezone.gmtime(now)
    datetime.datetime(2008, 3, 8, 18, 13, 20, tzinfo=<StaticTzInfo 'GMT'>)
