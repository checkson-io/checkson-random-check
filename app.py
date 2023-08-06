import sys
import random
import datetime
import os


base = os.environ['CI_PROJECT_DIR']


def write_last_result(result):
    if not os.path.exists(f"{base}/checkson/persistent"):
        os.makedirs(f"{base}/checkson/persistent")

    with open(f"{base}/checkson/persistent/last_result.txt", "w") as f:
        f.write(f"Result: {result}, time: {datetime.datetime.now()}")


def read_last_result():
    if not os.path.exists(f"{base}/checkson/persistent/last_result.txt"):
        return "No previous results"
    with open(f"{base}/checkson/persistent/last_result.txt", "r") as f:
        return f.read()


if random.random() > 0.5:
    print(f"Last result: {read_last_result()}")
    print("Check successful")
    write_last_result("success")
    sys.exit(0)
else:
    print(f"Last result: {read_last_result()}")
    print("Check unsuccessful")
    write_last_result("failure")
    sys.exit(1)
