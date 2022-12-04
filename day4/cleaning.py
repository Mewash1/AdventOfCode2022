def convertToSet(shortString):
    newSet = set()
    start, finish = shortString.split('-')
    for i in range(int(start), int(finish) + 1):
        newSet.add(i)
    return newSet

def cleaning(file, strict=False):
    with open(file, 'r') as rfile:
        pairs = [tuple(entry[:-1].split(',')) for entry in rfile.readlines()]
    total = 0
    for pair in pairs:
        section1, section2 = convertToSet(pair[0]), convertToSet(pair[1])
        if not strict:
            if section1.issubset(section2) or section2.issubset(section1):
                total += 1
        else:
            if any(i in section1 for i in section2):
                total += 1 
    return total

if __name__ == "__main__":
    print(cleaning("input.txt", strict=True))