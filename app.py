import sys
import random
import os

checkson_dir = os.environ['CHECKSON_DIR']


def write_message(message):
    with open(f"{checkson_dir}/message", "w") as f:
        f.write(message)


if random.random() > 0.5:
    print("Check successful")
    write_message("Check successful")
    sys.exit(0)
else:
    print("Check unsuccessful")
    write_message("Check unsuccessful")
    sys.exit(1)
