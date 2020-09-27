#!/usr/bin/env python3
# hamming.py

def hamming_distance(string1, string2):
    # Start with distance of 0
    distance = 0
    # Loop over string index 
    L = len(string1)
    for i in range(L):
        #Add 1 to distance if two characters are not identical
        if string1[i] != string2[i]:
            distance += 1
    return distance

if __name__ == "__main__":

     #Check to make sure there are at least two arguments
     arg_count = len(sys.argv) - 1
     if arg_count < 2: 
         raise Exception("This script requires 2 arguments: string 1 and string 2")

     string1 = sys.argv[1]
     string2 = sys.argv[2]

     distance = hamming_distance(string1, string2)
     for i in range(len(distance)):
         print("{}\t{}".format(i,distance[i]))

