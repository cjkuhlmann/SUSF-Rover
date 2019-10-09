##SUSF - Example differential and network encoder.

####Pros:
- Seamless addition of new variables
- Clear to modify and define values 
- Modular
- Requires no extra work when changing variable names or adding new objects

####Cons:
- Requires standardised variables
- Requires exceptions if any variables stored in a command state are not to be compared or sent.
- Data directly accessed rather than through interface (doesn’t use get() and set() commands for custom data structures. This doesn’t really matter if ppl are careful when editing and setting variables )
- Requires rover data to be integer of float in order to be compared

####Code Explanation
The code requires standardised variables which must be rover variables (defined in the roverVar class). 
The function loops through all attributes belonging to a controlState object. If it finds a non-roverVar variable then it recurses with this new object. Once a roverVar has been found the program will find the differential between that variable and the other programState's equivalent of it and saves the new value in the first programState. When this is done it will return to the previous level of the callstack and continue this process until all roverVars have been compared. 
Exceptions for standard variables can be created too such that the program will not try to recurse with a non-user defined data type.

The function for preparing data to be sent to the network module works similarly but instead of comparing when it finds a roverVar it gets its name and data and concatenates it. These values will be serrated by something like a comma such that the interface can parse the text and look for the variable names and assign the to its own variables correctly.



