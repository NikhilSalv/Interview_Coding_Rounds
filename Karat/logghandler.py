import unittest
import collections.abc
from os.path import exists
import subprocess
import collections 

"""
We are writing software to analyze logs for toll booths on a highway. This highway is a divided highway with limited access; the only way on to or off of the highway is through a toll booth.

There are three types of toll booths:
* ENTRY (E in the diagram) toll booths, where a car goes through a booth as it enters the highway.
* EXIT (X in the diagram) toll booths, where a car goes through a booth as it exits the highway.
* MAINROAD (M in the diagram), which have sensors that record a license plate as a car drives through at full speed.


         Exit Booth                   Entry Booth
             ^                             |
             |                             v
---<---------X---------M---------<---------E---------<---------
                                         (West-bound side)

===============================================================

                                         (East-bound side)
------>---------E---------M--------->---------X--------->------
                ^                             |
                |                             v
           Entry Booth                    Exit Booth

For our first task:
1-1) Read through and understand the code and comments below. Feel free to run the code and tests.
1-2) The tests are not passing due to a bug in the code. Make the necessary changes to LogEntry to fix the bug.
"""

"""
We are interested in how many people are using the highway, and so we would like to count how many complete journeys are taken in the log file.

A complete journey consists of:
* A driver entering the highway through an ENTRY toll booth.
* The driver passing through some number of MAINROAD toll booths (possibly 0).
* The driver exiting the highway through an EXIT toll booth.

For example, the following excerpt of log lines contains complete journeys for the cars with JOX304 and THX138:

.
.
.
90750.191 JOX304 250E ENTRY
91081.684 JOX304 260E MAINROAD
91082.101 THX138 110E ENTRY
91483.251 JOX304 270E MAINROAD
91873.920 THX138 120E MAINROAD
91874.493 JOX304 280E EXIT
.
.
91982.102 THX138 290E EXIT
.

The log contains only complete journeys, there are no missing entries.

2-1) Write a function in LogFile named count_journeys() that returns how many
     complete journeys there are in the given LogFile.
"""

class LogEntry:
    """
    Represents an entry from a single log line.

    Log lines look like this in the file:

    34400.409 SXY288 210E ENTRY

    Where:
    * 34400.409 is the timestamp in seconds since the software was started.
    * SXY288 is the license plate of the vehicle passing through the toll booth.
    * 210E is the location and traffic direction of the toll booth. Here, the
        toll booth is at 210 kilometers from the start of the tollway, and the E
        indicates that the toll booth was on the east-bound traffic side.
        Tollbooths are placed every ten kilometers.
    * ENTRY indicates which type of toll booth the vehicle went through. This is
        one of "ENTRY", "EXIT", or "MAINROAD".
    """

    def __init__(self, log_line):
        tokens = log_line.split(" ")
        print(tokens[0],"________")
        self.timestamp = float(tokens[0])
        self.license_plate = tokens[1]
        self.booth_type = tokens[3] # check this
        self.location = int(tokens[2][:-1])  # 012
        direction_letter = tokens[2][-1] # E
        if direction_letter == "E":
            self.direction = "EAST"
        elif direction_letter == "W":
            self.direction = "WEST"
        else:
            raise ValueError

    def __str__(self):
        return "<LogEntry timestamp: %f  license: %s  location: %d  direction: %s  booth type: %s>" % (
                self.timestamp, self.license_plate, self.location, self.direction, self.booth_type)

class LogFile(collections.abc.Sequence):
    """
    Represents a file containing a number of log lines, converted to LogEntry objects.
    """
    def __init__(self, file_handle):
        self.log_entries = []
        for line in file_handle:
            log_entry = LogEntry(line.strip())
            self.log_entries.append(log_entry)

    def __getitem__(self, index):
        return self.log_entries[index]

    def __len__(self):
        return len(self.log_entries)
        
    def count_journeys(self):
        counted_journey = 0
        default_dictionary = collections.defaultdict(list) #{license_plate:[booth_type, bool]}
        for log_line in self.log_entries:
            print(log_line.license_plate,"____", log_line.booth_type)
            print(default_dictionary)
    
            license_plate = log_line.license_plate
            booth_type = log_line.booth_type
            
            if license_plate in default_dictionary:
                print("Inside for loop")
                if booth_type == "EXIT":
                    counted_journey += 1
                    default_dictionary[license_plate] = [booth_type, True]
                    print(default_dictionary)
            else:
                default_dictionary[license_plate] = [booth_type, False]
        return counted_journey
        

class TestSuite(unittest.TestCase):
    # These tests are not meant to be exhaustive, and primarily show usage.
    def test_log_file(self):
        with open("tollbooth_small.log") as fh:
            log_file = LogFile(fh)
        self.assertEqual(len(log_file), 7)
        for entry in log_file:
            self.assertTrue(type(entry) == LogEntry)

    def test_log_entry(self):
        log_line = "44776.619 KTB918 310E MAINROAD"
        log_entry = LogEntry(log_line)
        self.assertEqual(log_entry.timestamp, 44776.619) # failed
        self.assertEqual(log_entry.license_plate, "KTB918")
        self.assertEqual(log_entry.location, 310)
        self.assertEqual(log_entry.direction, "EAST")
        self.assertEqual(log_entry.booth_type, "MAINROAD")
        log_line = "52160.132 ABC123 400W ENTRY"
        log_entry = LogEntry(log_line)
        self.assertEqual(log_entry.timestamp, 52160.132)
        self.assertEqual(log_entry.license_plate, "ABC123")
        self.assertEqual(log_entry.location, 400)
        self.assertEqual(log_entry.direction, "WEST")
        self.assertEqual(log_entry.booth_type, "ENTRY")
        
    def test_count_journeys(self):
        with open("tollbooth_small.log") as fh:
            log_file = LogFile(fh)
        self.assertEqual(2, log_file.count_journeys())
        with open("tollbooth_small.log") as fh:
            log_file = LogFile(fh)
        self.assertEqual(2, log_file.count_journeys())

if __name__ == "__main__":
    unittest.main()