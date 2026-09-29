#!/usr/bin/env python3
"""
Say hello from whichever computer this runs on, then count for a while.

    python3 hello.py          # counts for 60 seconds
    python3 hello.py 5        # counts for 5 seconds

The counting is there so the job lives long enough for you to watch it in
squeue, read its log while it runs, and kill it on purpose.
"""

import os
import socket
import sys
import time

seconds = int(sys.argv[1]) if len(sys.argv) > 1 else 60
user = os.environ.get("USER", "someone")
host = socket.gethostname()
job = os.environ.get("SLURM_JOB_ID")

cpu = "unknown CPU"
with open("/proc/cpuinfo") as f:
    for line in f:
        if line.startswith("model name"):
            cpu = line.split(":", 1)[1].strip()
            break

# flush=True: without it, output sits in a buffer and the log file stays empty
# until the program ends. That confuses everyone the first time.
print(f"Hello, {user}! This is {host} speaking.", flush=True)
print(f"My CPU is: {cpu}", flush=True)
if job:
    print(f"I am Slurm job {job}.", flush=True)
else:
    print("I am not inside a Slurm job.", flush=True)

for t in range(1, seconds + 1):
    time.sleep(1)
    if t % 10 == 0 or t == seconds:
        print(f"  still counting... {t}/{seconds} s", flush=True)

print("Done.", flush=True)
