from random import choice


def eat(food, is_healthy):
    if not isinstance(is_healthy, bool):
        raise ValueError
    end = "because YOLO"
    if is_healthy:
        end = "because my body is a temple"
    return f"I'm eating {food}, {end}"


def nap(num_hours):
    if num_hours < 2:
        return f"I'm feeling refreshed after 1 hour nap!"
    return f"Urgh, I overslept, I din't mean to sleep for {num_hours} hours"


def is_funny(person):
    if person == "tim":
        return False
    return True


def laugh():
    return choice(('lol', 'hahaha', 'tehehe'))
