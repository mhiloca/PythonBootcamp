def speak(animal="dog"):
    noises = {'dog': 'woof', 'cat': 'meow', 'duck': 'quack', 'pig': 'oink'}
    noise = noises.get(animal)
    if animal:
        return noise
    return "?"


print(speak("cat"))

