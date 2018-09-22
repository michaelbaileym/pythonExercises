#Previously, you wrote a class called ExerciseSession that
#had three attributes: an exercise name, an intensity, and a
#duration.
#
#Add a new method to that class called calories_burned.
#calories_burned should have no parameters (besides self, as
#every method in a class has). It should return an integer
#representing the number of calories burned according to the
#following formula:
#
# - If the intensity is "Low", 4 calories are burned per
#   minute.
# - If the intensity is "Moderate", 8 calories are burned
#   per minute.
# - If the intensity is "High", 12 calories are burned per
#   minute.
#
#You may copy your class from the previous exercise and just
#add to it.


#Add your code here!
class ExerciseSession:
    def __init__(self, exerciseName, exerciseIntensity, exerciseDuration):
        self.log("Exercise created.")
        self.exerciseName = exerciseName
        self.exerciseIntensity = exerciseIntensity
        self.exerciseDuration = exerciseDuration
        self.caloriesBurned = 0
    
    def get_exercise(self):
        return self.exerciseName
    def get_intensity(self):
        return self.exerciseIntensity
    def get_duration(self):
        return self.exerciseDuration
    
    def set_exercise(self, newName):
        self.exerciseName = newName
    def set_intensity(self, newIntensity):
        self.exerciseIntensity = newIntensity
    def set_duration(self, newDuration):
        self.exerciseDuration = newDuration
    
    def calories_burned(self):
        if self.exerciseIntensity == "Low":
            self.caloriesBurned = 4 * self.exerciseDuration
        elif self.exerciseIntensity == "Moderate":
            self.caloriesBurned = 8 * self.exerciseDuration
        elif self.exerciseIntensity == "High":
            self.caloriesBurned = 12 * self.exerciseDuration
        return self.caloriesBurned
    
    def log(self, message):
        exerciseLog = open("log.txt", "a")
        print(message, file = exerciseLog)
        exerciseLog.close()


#If your code is implemented correctly, the lines below
#will run error-free. They will result in the following
#output to the console:
#240
#360
new_exercise = ExerciseSession("Running", "Low", 60)
print(new_exercise.calories_burned())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print(new_exercise.calories_burned())



