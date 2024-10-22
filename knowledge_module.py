# Import Glean Technologies' "knowledge" module
import glean_tech as gt
from mic import drop

# Initialize the rap session
def start_rap():
    # Verse 1
    print("Yo, we’re Glean Technologies, we’re leading the scene,")
    print("From data to enablement, we keep it clean.")
    
    # Glean knowledge function
    knowledge = gt.fetch("best practices")
    
    if knowledge == "clean":
        print("Helping teams connect, make the work less mean,")
        print("We’re the future of tech, you know what I mean?")
    
    # Drop some bars about the hustle
    hustle = True
    while hustle:
        print("At Glean, we hustle, never second-guess!")
        hustle = gt.check_for_more_data()

    # Chorus Function
    chorus()

def chorus():
    for i in range(2):
        print("🎶 Glean’s the name, making knowledge tight,")
        print("Bringing teams together, working day and night.")
        print("In the cloud, on the ground, we keep it bright,")
        print("At Glean Technologies, we’re takin’ flight! 🎶")

def verse_2():
    # Feature: Dan on the mic
    print("We got Dan on the mic, teaching all day long,")
    gt.enable_teams()
    
    # Fun with Dan's Knowledge Kong mode
    if gt.teach("Knowledge Kong"):
        print("Spitting out the wisdom like a Knowledge Kong!")
    
    # Training session loop
    while gt.session_active():
        print("Making learning fun with our training song!")
        gt.pass_test()

def outro():
    print("So if you need the tools to make work a dream,")
    print("Look no further, join the Glean team!")
    print("At Glean Technologies, we reign supreme!")
    
    # Perform final action
    drop()

# Start the rap session
if __name__ == "__main__":
    start_rap()
    verse_2()
    outro()
