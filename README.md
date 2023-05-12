
# Banker's Algorithm

This program is an implementation of Banker algorithm which is used to avoid deadlock.
The algorithm is used to determine whether a system is in a safe state or not, 
meaning that it can give the resources to each process without causing a deadlock.

at the beginning, i initialized variables for necessery data like the number of processes, 
number of resource types, available resources, maximum need, and current allocation for each process.

The get_input function is called when the user clicks the (check) or (request) buttons.
it retrieves the input data from the GUI entry fields and text boxes and stores them in the variables.

The check function is called when the user clicks the (check) button.
it calls the get_input method to retrieve the input data, and then calls the isSafe function to determine if the system in a safe state or not.

The handle_request functon is called when user click the (request) button. 
it retrieves the process number and resource request and calls the get_input function to retrieve the input data. 
it then checks if the requested resources can be granted without causing a deadlock. 
if the request can be granted, it updates the available resources and current alocation.
if not it displays a message saying that the request was denied.

The isSafe function is the backbone function in the program. 
it takes in the current state of the system, including the available resources, the maximum need of each process, and the current allocation of resources for each process 
then simulates the allocation of resources to each process and checks if the system is in a safe by checking if there exists a sequence of processes that could be completed without making deadlock.
