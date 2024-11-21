class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError(" queue is empty  ")

    def is_empty(self):
       
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)


def simulate_print_queue(jobs):
   
    queue = Queue()

    # Enqueue all print jobs
    for job in jobs:
        queue.enqueue(job)

    print("Processing print jobs:")

    # Process jobs in order
    while not queue.is_empty():
        current_job = queue.dequeue()
        print(f"Printing: {current_job}")


# Test cases 
print_jobs = [
    "Job 1: Print name",
    "Job 2: Print ID #",
    "Job 3: Print Email",
    "Job 4: Print Age",
    "Job 5: Print phone #",
]

simulate_print_queue(print_jobs)
