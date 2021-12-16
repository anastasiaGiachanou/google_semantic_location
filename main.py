"Main program to test google_semantic_location history script"
# This code is based on the port-poc project located here: https://github.com/UtrechtUniversity/port-poc

from __init__ import *


if __name__ == '__main__':
    ##### result = process("../tests/data/Location History.zip")
    result = process("../tests/data/Person6.zip")
    
    print("Summary:\n", result["summary"])
    print("Dataframe\n\n", result["data_frames"])
    print("Errors\n\n", result["errors"])
    
    ## code to output the plot
    ## plots the top N activities per quarter (overall top N)
    ## We set N to 5
    print()

    ## if the dataframe is empty print a message
    if result["data_frames"][0].empty:
        print("No data were processed from 2016 to 2021!")
    else:
        print("Visualisation\n")
        activities_quarter_plot(result["data_frames"][0], 5)
