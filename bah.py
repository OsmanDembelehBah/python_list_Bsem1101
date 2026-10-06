class Task:
  
    def __init__(self, task_id, title, category):
        self.task_id = task_id
        self.title = title
        self.category = category
        self.is_completed = False

    def mark_completed(self):
       
        self.is_completed = True

    def display_info(self):
        
        status = "Done" if self.is_completed else "Pending"
        return f"[{self.task_id}] {self.title} ({self.category}) - Status: {status}"


class TaskManager:
   
    def __init__(self):
        
        self.tasks = []

    def add_task(self, task):
       
        self.tasks.append(task)
        print(f"Added task: '{task.title}'")

    def show_all_tasks(self):
        
        if not self.tasks:
            print("No tasks available.")
            return
        
        print("\n--- CURRENT TASKS ---")
        for task in self.tasks:
            print(task.display_info())
        print("---------------------\n")



if __name__ == "__main__":
    
    manager = TaskManager()

    
    t1 = Task(1, "Review OOP Principles", "Study")
    t2 = Task(2, "Practice Git Commands", "DevOps")
    t3 = Task(3, "Arrive to Class on Time", "Personal")

    
    manager.add_task(t1)
    manager.add_task(t2)
    manager.add_task(t3)

    
    manager.show_all_tasks()

    
    print("Marking Task 1 as completed...")
    t1.mark_completed()

    
    manager.show_all_tasks()