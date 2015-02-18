import settings
import beeminderpy
import json
import datetime
import time
import sys

def main():
    bm = beeminderpy.Beeminder()
    user_data = bm.get_user()
    goal_data = bm.get_goal()

if __name__ == '__main__':
    main()