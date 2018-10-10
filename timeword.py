"""Turn a string of 24h time into words.

You can trust that you'll be given a valid string (it will
always have a two-digit hour 00-23, and a two-digit minute
00-59). Hours 0-11 are am, and hours 12-23 are pm.

Handle noon and midnight specially:

    >>> time_word("00:00")
    'midnight'

    >>> time_word("12:00")
    'noon'

Otherwise, covert times to text:

    >>> time_word("01:00")
    "one o'clock am"

    >>> time_word("06:01")
    'six oh one am'

    >>> time_word("06:10")
    'six ten am'

    >>> time_word("06:18")
    'six eighteen am'

    >>> time_word("06:30")
    'six thirty am'

    >>> time_word("10:34")
    'ten thirty four am'

Don't forget to handle early morning properly:

    >>> time_word("00:12")
    'twelve twelve am'

For times after noon, add 'pm'

    >>> time_word("12:09")
    'twelve oh nine pm'

    >>> time_word("23:23")
    'eleven twenty three pm'

By Joel Burton <joel@joelburton.com>.
"""


def time_word(time):
    """Convert time to text."""

    if time == "00:00":
        return('midnight')
    if time == "12:00":
        return("noon")


    time = time.split(":")
    hours = time[0]
    minutes = time[1]
    written_time = ""

    if hours == "00" or hours == "12":
        written_time = "twelve"

    elif hours == "01" or hours == "13":
        written_time = "one"

    elif hours == "02" or hours == "14":
        written_time = "two"

    elif hours == "03" or hours == "15":
        written_time = "three"

    elif hours == "04" or hours == "16":
        written_time = "four"

    elif hours == "05" or hours == "17":
        written_time = "five"

    elif hours == "06" or hours == "18":
        written_time = "six"

    elif hours == "07" or hours == "19":
        written_time = "seven"

    elif hours == "08" or hours == "20":
        written_time = "eight"

    elif hours == "09" or hours == "21":
        written_time = "nine"

    elif hours == "10" or hours == "22":
        written_time = "ten"
    
    elif hours == "11" or hours == "23":
        written_time = "eleven"


    numbers = { "20":"twenty", "30":"thirty", "40":"fourty", "50":"fifty",
        "1":"one", "2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven",
        "8":"eight","9":"nine", "10":"ten", "11":"eleven","12":"twelve","13":"thirteen",
        "14":"fourteen","15":"fifteen","16":"sixteen","17":"seventeen","18":"eighteen",
        "19":"nineteen"}
    if minutes == "00":
        written_time += " o'clock"
    elif minutes[0] == "0":
        written_time += " oh " + numbers[minutes[1]]
    elif minutes[0] == "1":
        written_time += " " + numbers[minutes]
    else:
        n = int(minutes[0]) * 10
        if minutes[1] == "0":
            written_time += " " + numbers[str(n)]
        else:
            written_time += " " + numbers[str(n)] + " " + numbers[minutes[1]]

    if int(hours) < 12:
        written_time += " am"
    else:
        written_time += " pm"

    return written_time



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. YOU'RE A TIME WIZARD!\n")