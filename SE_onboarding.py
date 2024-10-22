# Import necessary modules for survival
import enablement_tasks as et
import coffee_machine as cm
import time_management as tm
from motivation import caffeine_boost, panic_mode
from deadline import looming_deadline
from brain import overload

# Initialize variables
new_SE = True
tasks = et.get_all("onboarding")
completed_tasks = 0
energy_level = 50  # Starting energy level (out of 100)

# Main onboarding function
def complete_onboarding():
    global completed_tasks, energy_level
    
    # Step 1: Prepare for the flood of tasks
    print("📝 Starting onboarding enablement... Buckle up!")
    
    # Step 2: Triage tasks and figure out where to start
    for task in tasks:
        print(f"🧐 Reviewing task: {task['name']}")
        
        # If task looks hard, procrastinate (classic move)
        if task["difficulty"] == "hard":
            print("🙄 Looks tough... I'll save this one for later.")
            tm.snooze(task, "until panic_mode activates")
        else:
            print(f"✔️ Let's knock out {task['name']}!")
            task_status = et.complete(task)
            if task_status == "completed":
                completed_tasks += 1
                energy_level -= 10  # Completing tasks is tiring!
            else:
                print(f"❌ Failed to complete: {task['name']}. Revisit during panic_mode.")

        # Boost energy levels with coffee after every few tasks
        if completed_tasks % 3 == 0:
            print("☕ Coffee break! Boosting energy...")
            energy_level += caffeine_boost(cm.brew_coffee())
        
        # Check for brain overload
        if overload.detect():
            print("💥 Brain overload detected. Time to panic.")
            panic_mode(energy_level)
    
    # Step 3: When deadline looms, switch to turbo mode
    if looming_deadline():
        print("⏳ Deadline is tomorrow! Activating panic_mode...")
        while not et.all_completed():
            print("⚡ Turbo mode activated! Completing tasks at lightning speed.")
            completed_tasks += et.complete_next(panic_mode=True)
            energy_level -= 5  # Panic mode burns energy fast!
            if energy_level < 20:
                print("🛑 Low energy. Emergency coffee run!")
                energy_level += caffeine_boost(cm.brew_coffee(strength="triple shot"))
    
    # Step 4: Celebrate your victory (or survival)
    if et.all_completed():
        print("🎉 Enablement complete! You’ve survived onboarding!")
    else:
        print("🤔 Hmm... still a few tasks left, but we'll deal with that later.")

# Run onboarding process
if new_SE:
    print("💡 Welcome to the SE world! Time to get onboarded...")
    complete_onboarding()

# Output the final status
if completed_tasks == len(tasks):
    print("🚀 All tasks completed. Ready to crush the SE game!")
else:
    print(f"✅ You completed {completed_tasks}/{len(tasks)} tasks. Good enough for now!")
