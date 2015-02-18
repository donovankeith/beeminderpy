import settings
import beeminderpy
import json
import datetime
import time
import sys

def main():
    bm = beeminderpy.Beeminder(goalname="cloth")
    user_data = bm.get_user()
    goal_data = bm.get_goal()

    print user_data
    print goal_data

if __name__ == '__main__':
    main()