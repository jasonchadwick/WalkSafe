# WalkSafe
 Map app that gives safer walking routes. TartanHacks 2020 project.

In the file loadNodedata, you will find the code used to retrieve all
nodes that refer to streets in manhatten from Open Street Map, a mapping API

In the crimeParsing File, we have functions that are used to take NYPD complaint data,
and turn it into a dictionary that holds all crimes, our value for how dangerous those
crimes are, and where those crimes occured. 

In the calcRisk file, we have our function that takes in a dictionary of crimes and their locations, 
and computes the danger score for one node at all times given all the crimes that happened around it
and when those crimes happend, with a higher value placed on closer crimes and crimes that happened around
the same time of day as the node given.

In the search and searchProblem files we have uor A* implementation

In the crimeTesting file, we input our nodes from data.txt, our crimes from the nodetimerisk folder, a dictionary
that maps approximate locations to all nodes within some range. We then getRoute, using two Nodes, and plot our data
onto a heatmap of crimes within the range of our path. Note that the findClosestNode function finds the closest node in
our database to an x,y coordinate entered, so that given a user input we can compute our A* only using nodes we have.
Since manhatten is so dense, we will be able to find a node very close(<500 feet) to any inputted coordinate.
