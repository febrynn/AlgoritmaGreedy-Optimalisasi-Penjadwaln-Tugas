from datetime import datetime

def greedy_schedule(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: (x[1], -x[2]))
    schedule = []
    for task in sorted_tasks:
        schedule.append(task)
    return schedule

def get_tasks(num_tasks):
    tasks = []
    for i in range(num_tasks):
        name, deadline, difficulty = input(f"Masukkan tugas {i+1} (nama, deadline (format: DD/MM/YYYY), tingkat kesulitan): ").split(", ")
        deadline = datetime.strptime(deadline, "%d/%m/%Y")
        tasks.append((name.strip(), deadline, int(difficulty)))
    return tasks

def print_schedule(schedule):
    print("Jadwal Tugas:")
    for i, task in enumerate(schedule, 1):
        print(f"{i}. {task[0]} (Deadline: {task[1].strftime('%d/%m/%Y')}, Tingkat Kesulitan: {task[2]})")

num_tasks = int(input("Masukkan jumlah tugas: "))
tasks = get_tasks(num_tasks)
schedule = greedy_schedule(tasks)

print("\nJadwal Tugas sebelum diurutkan:")
print_schedule(tasks)
print("\nJadwal Tugas setelah diurutkan berdasarkan deadline dan tingkat kesulitan:")
print_schedule(schedule)
