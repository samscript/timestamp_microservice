# Free Code Camp TimeStamp Microservice
# Using:
#   .https://dateparser.readthedocs.org/en/latest/index.html
#   .http://bottlepy.org/docs/dev/index.html

from bottle import route, run, template
import dateparser
import json
import datetime

def parsed_entry(entry):
    return dateparser.parse(entry)

def is_unix_stamp(entry):

    parsed = parsed_entry(entry)

    str1 = str(parsed)

    # 1st check if its an integer which should be a unix timestamp
    if entry.isdigit():
            return True

    # 2nd we are going to check if the string is not a natural date
    elif parsed == None:
        return None

    # if the string is a natural language we return False
    else:
        return False

def unix_stamp(parsed):
    unix_start_time = dateparser.parse(' 1970 1 1')
    return (parsed - unix_start_time).total_seconds()

def returned_date(parsed):
    month   = parsed.strftime("%B")
    day     = parsed.day
    year    = parsed.year

    return month + " " + str(day) + ", " + str(year)

def return_json(unix, date):
    return json.dumps({"unix":unix,"natural":date})

def processing_input_output(entry):

    if is_unix_stamp(entry) == True:
        # unix timestamp
        # return "unix timestamp"
        unix_to_date =  dateparser.parse(' 1970 1 1') + datetime.timedelta(0,int(entry))

        return return_json( str(entry), returned_date(unix_to_date) )

    elif  is_unix_stamp(entry) == False:
        # natural language date
        return return_json(unix_stamp(parsed_entry(entry)), returned_date(parsed_entry(entry)))
    else:
        # neither unix timestamp nor natural language date
        return return_json(None, None)


# str_entered = "2012"

@route('/')
@route('/datetime/<entry>')
def date_time(entry):
    return processing_input_output(entry)


# print processing_input_output(str_entered)

run(host='0.0.0.0', port=8080, debug=True)