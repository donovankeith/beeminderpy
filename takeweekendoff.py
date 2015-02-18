"""Take Weekends Off
Will schedule the next weekend off for you.

To Do
-----

- [ ] Get basic version working
"""

import settings
import beeminderpy
import json
import datetime
import time
import sys

def main():
    bm = beeminderpy.Beeminder(goalname=settings.BEEMINDER_GOALNAME)
    user_data = bm.get_user()
    goal_data = bm.get_goal()
    data_points = bm.get_datapoints()

    print "user: ", user_data
    print "goal_data: ", goal_data
    print "data_points: ", data_points

if __name__ == '__main__':
    main()