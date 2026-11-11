"""
RECORD CHECK  -  my version
===========================

Name  : Ronak Nai
Lane  :  AI  
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here
def parse_line(raw_line):

    clean_line = raw_line.strip().lower()

    hostname_part, rest = clean_line.split(",", 1)

    hostname = hostname_part.strip()

    data = {}

    for piece in rest.split(","):
        key, value = piece.split("=")

        key = key.strip()
        value = float(value.strip())

        data[key] = value

    return {
        "hostname": hostname,
        **data
    }



# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

records = [
    "  Survey_2026 , rating=2 , age=21  ",
    "survey_2027, rating=4, age=23",
    "  SURVEY_2028,  rating=6, age=22 ",
    "Survey_2029 ,RATING=8, AGE=24",
    "  survey_2030 , rating=7 , age=25  "
]

for record in records:
    print(record)   # replace with your code


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

for record in records:
    record = record.strip()
    parts = record.split(",")
    label = parts[0].strip().lower()

    rating = int(parts[1].strip().split("=")[1])

    age = int(parts[2].strip().split("=")[1])
    cleaned = {
        "label": label,
        "rating": rating,
        "age": age
    }

    print(cleaned)   # replace with your code


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
