#!/usr/bin/env python3
from datetime import date, datetime
import psutil
import time

if __name__ == "__main__":
    today = date.today()
    fname = str(today) + ".txt"
    f = open(fname, "a")
    try:
        while (1):
            cpu = psutil.cpu_percent()
            mem = psutil.virtual_memory()[2]
            t = datetime.now()
            message = str(t) + " CPU: " + str(cpu) + " MEMORY: " + str(mem)
            f.write(message + "\n")
            print(message)
            time.sleep(30)
    except KeyboardInterrupt:
        f.close()
        print("\nSuccessfully closed file writer")
