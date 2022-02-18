"Main program to test google_semantic_location history script"
# This code is based on the port-poc project located here: https://github.com/UtrechtUniversity/port-poc

from __init__ import *


if __name__ == '__main__':
    ##### result = process("../tests/data/Location History.zip")
    
    result = process("tests/data/Person5.zip")
    
    print("Summary:\n", result["summary"])
    print("\n")
    print("Total duration and distance for all the activities\n\n")
    print(result["data_frame"])
        
    for k, v in result["data_frames_activity"].items():
        print(k)
        print(v.to_string(index=False))
        print()
    
    print("\nDuration per activity:\n")
    print("Errors\n\n", result["errors"])
    print()


