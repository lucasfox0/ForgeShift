from data.models import ShiftInput

def get_input(): 
    shift_start = input("What time does your shift start? ")
    shift_end = input("What time does your shift end? ")
    context = input("Any context you would like to provide? ")
    tasks = []

    while (True):
        task = input("Enter a task (or press Enter to finish): ")
        if (task == ""):
            break
        else:
            tasks.append(task)
    
    return ShiftInput(shift_start=shift_start, shift_end=shift_end, context=context, tasks=tasks)