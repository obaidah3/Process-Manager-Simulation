import random
import time

# Define the Process class to simulate each process in the system
class Process:
    def __init__(self, name, student_id, grade, cpu_burst, priority=1):
        self.name = name
        self.id = student_id
        self.grade = grade
        self.state = "New"  # New, Ready, Running, Terminated
        self.cpu_burst = cpu_burst
        self.execution_time = 0
        self.priority = priority
        self.memory_pages = random.randint(1, 3)
        self.page_faults = 0
        self.allocated_pages = []  # Track actual page numbers allocated

    def __str__(self):
        return (f"Process ID: {self.id}, Name: {self.name}, Grade: {self.grade}, "
                f"State: {self.state}, CPU Burst: {self.cpu_burst}, Priority: {self.priority}, "
                f"Memory Pages: {self.memory_pages}, Page Faults: {self.page_faults}")


# Define the ProcessManager class to handle scheduling and memory management
class ProcessManager:
    def __init__(self, filename="processes.txt", delay=0.1):
        self.processes = []
        self.completed_processes = []
        self.cpu_time = 0
        self.memory = {}  # page_number: process_id
        self.filename = filename
        self.delay = delay  # Base delay for simulation
        self.load_processes_from_file()

    def add_sample_processes(self):
        # Add predefined processes instead of interactive input
        samples = [
            ("Alice", "001", 85.0, 3, 2),
            ("Bob", "002", 90.5, 2, 4),
            ("Charlie", "003", 78.2, 4, 3)
        ]
        for name, sid, grade, burst, priority in samples:
            self.add_process(name, sid, grade, burst, priority)

    def add_process(self, name, student_id, grade, cpu_burst, priority=1):
        proc = Process(name, student_id, grade, cpu_burst, priority)
        self.processes.append(proc)
        self.save_process_to_file(proc)
        print(f"Added: {proc}\n")

    def save_process_to_file(self, process):
        with open(self.filename, "a") as f:
            f.write(f"{process.name} | {process.id} | {process.grade} | {process.cpu_burst} | {process.priority}\n")

    def load_processes_from_file(self):
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    name, sid, grade, burst, pri = [x.strip() for x in line.split("|")]
                    proc = Process(name, sid, float(grade), int(burst), int(pri))
                    self.processes.append(proc)
        except FileNotFoundError:
            print(f"No existing data ({self.filename}). Starting fresh.\n")

    def allocate_memory(self, process):
        print(f"Allocating {process.memory_pages} pages for {process.name}...")
        tries = 0
        while len(process.allocated_pages) < process.memory_pages and tries < 10 * process.memory_pages:
            page = random.randint(1, 100)
            tries += 1
            if page not in self.memory:
                self.memory[page] = process.id
                process.allocated_pages.append(page)
            else:
                process.page_faults += 1
                print(f"Page fault: {process.name} could not allocate page {page}.")
        if len(process.allocated_pages) < process.memory_pages:
            print(f"Warning: Only allocated {len(process.allocated_pages)} / {process.memory_pages} pages.")

    def free_memory(self, process):
        print(f"Freeing memory for {process.name}...")
        for page in process.allocated_pages:
            self.memory.pop(page, None)
        process.allocated_pages.clear()

    def execute_process(self, process, time_slice=None):
        process.state = "Running"
        run_time = time_slice or process.cpu_burst
        print(f"-- Executing {process.name} ({process.id}) for {run_time} units.")
        for step in range(run_time):
            time.sleep(self.delay)
            process.execution_time += 1
            self.cpu_time += 1
            print(f"[Time {self.cpu_time}] {process.name}: {process.execution_time}/{process.cpu_burst} units, Faults: {process.page_faults}")
        if process.execution_time >= process.cpu_burst:
            process.state = "Terminated"
            self.completed_processes.append(process)
            print(f"*** {process.name} completed.\n")

    def fcfs(self):
        print("\n== FCFS Scheduling ==")
        for proc in list(self.processes):
            proc.state = "Ready"
            self.allocate_memory(proc)
            self.execute_process(proc)
            self.free_memory(proc)

    def sjf(self):
        print("\n== SJF Scheduling ==")
        for proc in sorted(self.processes, key=lambda p: p.cpu_burst):
            proc.state = "Ready"
            self.allocate_memory(proc)
            self.execute_process(proc)
            self.free_memory(proc)

    def priority_scheduling(self):
        print("\n== Priority Scheduling ==")
        for proc in sorted(self.processes, key=lambda p: p.priority, reverse=True):
            proc.state = "Ready"
            self.allocate_memory(proc)
            self.execute_process(proc)
            self.free_memory(proc)

    def round_robin(self, time_quantum):
        print("\n== Round Robin Scheduling ==")
        queue = self.processes.copy()
        while queue:
            proc = queue.pop(0)
            if proc.state == "Terminated":
                continue
            proc.state = "Ready"
            if not proc.allocated_pages:
                self.allocate_memory(proc)
            share = min(time_quantum, proc.cpu_burst - proc.execution_time)
            self.execute_process(proc, share)
            if proc.state != "Terminated":
                queue.append(proc)
            else:
                self.free_memory(proc)

    def display_processes(self):
        print("\n-- Active Processes --")
        for p in self.processes:
            print(p)

    def display_completed(self):
        print("\n-- Completed Processes --")
        for p in self.completed_processes:
            print(p)

    def display_stats(self):
        total_faults = sum(p.page_faults for p in self.completed_processes)
        print(f"\nTotal CPU Time: {self.cpu_time} units.")
        print(f"Completed: {len(self.completed_processes)} processes. Page Faults: {total_faults}\n")

    def run_all(self):
        self.add_sample_processes()
        self.display_processes()
        self.fcfs()
        self.sjf()
        self.priority_scheduling()
        self.round_robin(time_quantum=2)
        self.display_completed()
        self.display_stats()

if __name__ == "__main__":
    pm = ProcessManager(delay=0.05)
    pm.run_all()
