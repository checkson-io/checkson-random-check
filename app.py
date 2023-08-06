import sys
import random
import datetime
import os


def write_last_result(result):
    if not os.path.exists("checkson/persistent"):
        os.makedirs("checkson/persistent")

    with open("checkson/persistent/last_result.txt", "w") as f:
        f.write(f"Result: {result}, time: {datetime.datetime.now()}")


def read_last_result():
    if not os.path.exists("checkson/persistent/last_result.txt"):
        return "No previous results"
    with open("checkson/persistent/last_result.txt", "r") as f:
        return f.read()


def print_all_files():
    print("All files:")
    for root, dirs, files in os.walk("/"):
        for dir in dirs:
            try:
                for filename in os.listdir(os.path.join(root, dir)):
                    print(os.path.join(root, dir, filename))
            except Exception as e:
                print("Error reading directory")


def print_all_env_vars():
    print("All env vars:")
    for key, value in os.environ.items():
        print(f"{key}: {value}")


if random.random() > 0.5:
    print(f"Last result: {read_last_result()}")
    print("Check successful")
    write_last_result("success")
    # print_all_files()
    print_all_env_vars()
    sys.exit(0)
else:
    print(f"Last result: {read_last_result()}")
    print("Check unsuccessful")
    write_last_result("failure")
    # print_all_files()
    print_all_env_vars()
    sys.exit(1)
