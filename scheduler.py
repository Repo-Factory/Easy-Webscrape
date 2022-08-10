import sched
import time
from webscrape import scrape


class Tracker:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Tracker, cls).__new__(cls)
            return cls.instance
    def __init__(self):
        self.interval = 3
    def getInterval(self):
        return self.interval
tracker = Tracker()


def trigger():
    scrape()
    event_schedule.enter(interval, 1, trigger)

interval = 6000
event_schedule = sched.scheduler(time.time, time.sleep)
event_schedule.enter(interval, 1, trigger)
event_schedule.run()