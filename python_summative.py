import random

import datetime  # imports date and time module for datetime stamps

fhand = open("output_file.txt",
             "a+")  # Creates file and solves the problem of data overwrite using the append function

stamp = datetime.datetime.now()

fhand.write('Date and Time Stamp: ' + str(stamp))  # Writes the date and time to each output of the file

fhand.write('\n \n')  # adds some space after the time stamp in output file


for i in range(1, 33):  # counts 1 to 32

    readings = [random.random() for reading in range(1, 17)]  # create a list of random floats 16 times

    fhand.write('DSI {0}: {1}\n '.format(i, readings))  # Writes each sensor (DSI) into the file

fhand.write('\n \n \n')  # Adds space after the output

fhand.close()  # Closes the output file


def corrupted_data():   # define a function that reads the error into a new file

    error_file = open("error_log.txt", "a+")   # the error file that stores the location of the error

    newoutput_file = open("output_file.txt", "r")   # the new output file

    stamp = ''

    for line in newoutput_file:

        line = line.rstrip()

        if line.startswith('2019'):
            stamp = line

        if not 'err' in line:
            continue

        error_file.write(stamp)

        error_file.write('\n')

        error_file.write(line)

        error_file.write('\n \n')

    error_file.close()

    newoutput_file.close()


corrupted_data()
