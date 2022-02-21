"Main program to test google_semantic_location history script"
# This code is based on the port-poc project located here: https://github.com/UtrechtUniversity/port-poc

from __init__ import *


if __name__ == '__main__':
    ##### result = process("../tests/data/Location History.zip")
    
    result = process("tests/data/Person6.zip")
    
    print("Summary:\n", result[0]['summary'])
    print("Total duration and distance for all the activities\n", result[0]['data_frame'])
    print("Duration per activity::\n")
    
    for k, v in result[0]['data_frames_activity'].items():
        print(k)
        print(v.to_string(index=False))
        print()

    print("Errors:\n", result[0]['errors'])
    


