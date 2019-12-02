def running_average():
    prev = []

    def inner_function(num):
        prev.append(num)
        print(prev)
        return sum(prev) / len(prev)
    return inner_function


rAvg = running_average()
print(rAvg(1))
print(rAvg(3))
