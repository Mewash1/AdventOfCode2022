def jungle(file):
    with open(file, 'r') as rfile:
        calories = rfile.readlines()
    calories = [entry[:-1] for entry in calories]
    maxCalories = 0
    currentCalories = 0

    for entry in calories:
        if entry != '':
            currentCalories += int(entry)
        else:
            if currentCalories > maxCalories:
                maxCalories = currentCalories
            currentCalories = 0
    
    return maxCalories

def jungle2(file):
    with open(file, 'r') as rfile:
        calories = rfile.readlines()
    calories = [entry[:-1] for entry in calories]
    calories.append('')
    totalCalories = []
    currentCalories = 0
    for entry in calories:
        if entry != '':
            currentCalories += int(entry)
        else:
            totalCalories.append(currentCalories)
            currentCalories = 0
    
    totalCalories.sort(reverse=True)
    
    return sum(totalCalories[:3])

if __name__ == "__main__":
    print(jungle2("input.txt"))