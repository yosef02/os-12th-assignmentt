import numpy as np
import tkinter as tk

class BankerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Banker's Algorithm")

        
        self.num_processes = 0
        self.num_resources = 0
        self.available = None
        self.max_need = None
        self.allocation = None
        self.processes = []
        self.request_process_num = None
        self.request = None

        
        self.num_processes_label = tk.Label(master, text="Number of processes:")
        self.num_processes_entry = tk.Entry(master)
        self.num_resources_label = tk.Label(master, text="Number of resource types:")
        self.num_resources_entry = tk.Entry(master)
        self.available_label = tk.Label(master, text="Number of available resources of each type:")
        self.available_entry = tk.Entry(master)
        self.max_need_label = tk.Label(master, text="Maximum need for each process:")
        self.max_need_text = tk.Text(master, height=10, width=40)
        self.allocation_label = tk.Label(master, text="Current allocation for each process:")
        self.allocation_text = tk.Text(master, height=10, width=40)
        self.request_process_label = tk.Label(master, text="Process number:")
        self.request_process_entry = tk.Entry(master)
        self.request_label = tk.Label(master, text="Resource request:")
        self.request_entry = tk.Entry(master)
        self.result_label = tk.Label(master, text="")
        self.check_button = tk.Button(master, text="Check", command=self.check)
        self.request_button = tk.Button(master, text="Request", command=self.handle_request)

        
        self.num_processes_label.grid(row=0, column=0, padx=5, pady=5)
        self.num_processes_entry.grid(row=0, column=1, padx=5, pady=5)
        self.num_resources_label.grid(row=1, column=0, padx=5, pady=5)
        self.num_resources_entry.grid(row=1, column=1, padx=5, pady=5)
        self.available_label.grid(row=2, column=0, padx=5, pady=5)
        self.available_entry.grid(row=2, column=1, padx=5, pady=5)
        self.max_need_label.grid(row=3, column=0, padx=5, pady=5)
        self.max_need_text.grid(row=3, column=1, padx=5, pady=5)
        self.allocation_label.grid(row=4, column=0, padx=5, pady=5)
        self.allocation_text.grid(row=4, column=1, padx=5, pady=5)
        self.request_process_label.grid(row=5, column=0, padx=5, pady=5)
        self.request_process_entry.grid(row=5, column=1, padx=5, pady=5)
        self.request_label.grid(row=6, column=0, padx=5, pady=5)
        self.request_entry.grid(row=6, column=1, padx=5, pady=5)
        self.result_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)
        self.check_button.grid(row=8, column=0, padx=5, pady=5)
        self.request_button.grid(row=8, column=1, padx=5, pady=5)

    def get_input(self):
        self.num_processes = int(self.num_processes_entry.get())
        self.num_resources = int(self.num_resources_entry.get())
        self.available = np.array([int(x) for x in self.available_entry.get().split()])
        self.max_need = np.zeros((self.num_processes, self.num_resources), dtype=int)
        self.allocation = np.zeros((self.num_processes, self.num_resources), dtype=int)

        max_need_text = self.max_need_text.get("1.0", tk.END).splitlines()
        allocation_text = self.allocation_text.get("1.0", tk.END).splitlines()

        for i in range(self.num_processes):
            self.max_need[i] = np.array([int(x) for x in max_need_text[i].split()])
            self.allocation[i] = np.array([int(x) for x in allocation_text[i].split()])

        self.processes = list(range(self.num_processes))

    def check(self):
        self.get_input()

        if isSafe(self.processes, self.available, self.max_need, self.allocation):
            self.result_label.config(text="The system is in a safe state.")
        else:
            self.result_label.config(text="The system is not in a safe state.")

    def handle_request(self):
        self.request_process_num = int(self.request_process_entry.get())
        self.request = np.array([int(x) for x in self.request_entry.get().split()])

        self.get_input()

        if np.all(self.request <= self.max_need[self.request_process_num] - self.allocation[self.request_process_num]) and np.all(self.request <= self.available):
            new_available = self.available - self.request
            new_allocation = self.allocation.copy()
            new_allocation[self.request_process_num] += self.request

            if isSafe(self.processes, new_available, self.max_need, new_allocation):
                self.result_label.config(text="Request granted.")
                self.available = new_available
                self.allocation = new_allocation
            else:
                self.result_label.config(text="Request denied. Granting the request would result in a deadlock.")
        else:
            self.result_label.config(text="Request denied. The request exceeds the maximum need or available resources.")

def isSafe(processes, available, max_need, allocation):
    num_processes = len(processes)
    num_resources = len(available)
    need = max_need - allocation

  
    finish = [False] * num_processes

   
    work = available.copy()

    
    safe_sequence = []

   
    while len(safe_sequence) < num_processes:
        
        found = False

        
        for i in range(num_processes):
            if not finish[i] and np.all(need[i] <= work):                
                work += allocation[i]
                finish[i] = True
                safe_sequence.append(processes[i])
                found = True


        if not found:
            break

    if len(safe_sequence) == num_processes:
        return True
    else:
        return False

root = tk.Tk()
gui = BankerGUI(root)
root.mainloop()