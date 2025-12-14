class Robot:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.version = "1.0"
    def introduce(self):
        print(f"Hello, my name is {self.name}.")
        print(f"I am a {self.model} model, running version {self.version}.")
        print("I am here to assist you!")
robot_one = Robot(name="Tom", model="AssistantBot")
robot_two = Robot(name="Jerry", model="Flexo")
print("--- Robot One Introduction ---")
robot_one.introduce() 
print("\n--- Robot Two Introduction ---")
robot_two.introduce()