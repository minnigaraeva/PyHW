import time
import itertools


class TrafficLight:
    def __init__(self):
        self._color = ['red', 'yellow', 'green']

    def running(self):
        sleep_time = itertools.cycle([7, 2, 9])
        cycler = itertools.cycle(['red', 'yellow', 'green'])
        while True:
            print(next(cycler))
            time.sleep(next(sleep_time))


first = TrafficLight()
first.running()
