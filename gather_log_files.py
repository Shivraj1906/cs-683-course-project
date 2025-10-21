import os
import sys
import shutil
config_name = input("ENTER SIMULATION CONFIG NAME: " )

# check if directory already exists
if os.path.isdir(config_name):
    print("CONFIG ALREADY EXISTS")
    sys.exit()

# create config folder
try:
    os.mkdir(config_name)
    print("config folder created...")
    print()
except Exception as e:
    printf(f"SOMETHING WENT WRONG, TERMINATING...")
    sys.exit()

# copy the content
scenes = ['FOX', 'FRST', 'LANDS', 'PARK', 'PARTY', 'ROBOT']

for scene in scenes:
    source_file = f"/home/shivraj/RT-simulations/{scene}/output_{scene}.log"
    dest = f"./{config_name}"

    try:
        shutil.copy(source_file, dest)
        print(f"output_{scene}.log copied to {config_name} folder...")
    except Exception as e:
        print(f"error occured during copying {e}")
        sys.exit()

print("all files copied...")
print()
