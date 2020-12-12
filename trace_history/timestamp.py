from datetime import datetime


# example:
# 12:36:41 on Dec 8th, 2020 => '20201208-123641'
def timestamp():
    return datetime.today().strftime('%Y%m%d-%H%M%S')
