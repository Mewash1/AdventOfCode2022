def rucksack(file):
    with open(file, 'r') as rfile:
        backpacks = [(list(item[:-1][:int(len(item)/2)]), list(item[:-1][int(len(item)/2):])) for item in rfile.readlines()]
    totalPriority = 0
    for backpack in backpacks:
        firstCompartment = set()
        bothCompartments = set()
        for item in backpack[0]:
            firstCompartment.add(item)
        for item in backpack[1]:
            if item in firstCompartment and item not in bothCompartments:
                bothCompartments.add(item)
                shift = -38 if item.isupper() else -96
                # print(ord(item) + shift)
                totalPriority += ord(item) + shift
    return totalPriority

def badges(file):
    with open(file, 'r') as rfile:
        rucksacks = [list(item[:-1]) for item in rfile.readlines()]
    groups = []
    i = 0
    for i in range(int(len(rucksacks)/3)):
        groups.append(rucksacks[i*3:(i+1)*3])
    totalPriority = 0
    for group in groups:
        sharedItems = dict()
        for elf in group:
            elfItems = set()
            for item in elf:
                if item not in elfItems:
                    elfItems.add(item)
                    if item not in sharedItems:
                        sharedItems[item] = 1
                    else:
                        sharedItems[item] += 1
                        if sharedItems[item] == 3:
                            shift = -38 if item.isupper() else -96
                            totalPriority += ord(item) + shift
    return totalPriority

if __name__ == '__main__':
    #print(rucksack("input.txt"))
    groups = badges("input.txt")
    print(groups)