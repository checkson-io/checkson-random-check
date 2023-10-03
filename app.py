import sys
import random
import os

checkson_dir = os.environ['CHECKSON_DIR']


def write_message(message):
    with open(f"{checkson_dir}/message", "w") as f:
        f.write(message)


def write_attachment(contents):
    os.makedirs(f"{checkson_dir}/attachments", exist_ok=True)
    with open(f"{checkson_dir}/attachments/example-attachment.txt", "w") as f:
        f.write(contents)


if random.random() > 0.5:
    print("Check successful")
    write_message("Check successful")
    write_attachment("This is an example attachment")
    sys.exit(0)
else:
    print("Check unsuccessful")
    write_message("Check unsuccessful")
    write_attachment("This is an example attachment")
    sys.exit(1)
