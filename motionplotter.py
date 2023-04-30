# Hack the Kano Motion Sensor

import json  # Import the JSON library for parsing the data from the Kano Motion Sensor
import time  # Import the time library for timestamps
import serial  # Import the PySerial library for reading data from the serial port
import argparse  # Import the argparse library for parsing command-line arguments

# Parse the command-line arguments to get the serial port the Kano Motion Sensor is connected to
parser = argparse.ArgumentParser(description='Kano Motion Sensor Plotter')
parser.add_argument('port', metavar='PORT', type=str, help='the serial port the Kano Motion Sensor is connected to')
args = parser.parse_args()

# Open the serial port for reading data from the Kano Motion Sensor
with serial.Serial(args.port, 115200) as monitor:

    # Print a message indicating that the plotter is starting
    print("Starting Kano Motion Sensor Plotter...")

    # Loop indefinitely to read data from the Kano Motion Sensor
    while True:
        try:
            # Read a line of data from the Kano Motion Sensor and strip any whitespace
            data = monitor.readline().decode().strip()

            # Parse the JSON data from the Kano Motion Sensor
            json_data = json.loads(data)

            # Extract the proximity value from the JSON data and convert it to a percentage value
            proximity = format(json_data['detail']['proximity'])
            intensity = round(float(proximity)/2.55)

            # If the intensity value is greater than zero, print a timestamp and the intensity percentage
            if intensity > 0:
                print(f"{time.time()} -> {intensity}%")

        # Handle keyboard interrupts, JSON decode errors, and key errors by breaking out of the loop
        except (KeyboardInterrupt, json.JSONDecodeError, KeyError):
            print("Exiting Kano Motion Sensor Plotter...")
            break
