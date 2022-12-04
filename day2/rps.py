# x, y, z; a,b,c = rock, paper, scisscors

def rps(file):
    games = {
    ('A', 'X') : 3,
    ('A', 'Y') : 6,
    ('A', 'Z') : 0,
    ('B', 'X') : 0,
    ('B', 'Y') : 3,
    ('B', 'Z') : 6,
    ('C', 'X') : 6,
    ('C', 'Y') : 0,
    ('C', 'Z') : 3, }

    values = {'X':1, 'Y':2, 'Z':3}

    with open(file, 'r') as rfile:
        moves = [tuple(entry[:-1].split(" ")) for entry in rfile.readlines()]
    totalValue = 0
    for move in moves:
        totalValue += games.get(move) + values.get(move[1])
    return totalValue

def rps2(file):
    signValue = {
    ('A', 'X') : 3,
    ('A', 'Y') : 1,
    ('A', 'Z') : 2,
    ('B', 'X') : 1,
    ('B', 'Y') : 2,
    ('B', 'Z') : 3,
    ('C', 'X') : 2,
    ('C', 'Y') : 3,
    ('C', 'Z') : 1, }

    games = {
    ('A', 'X') : 0,
    ('A', 'Y') : 3,
    ('A', 'Z') : 6,
    ('B', 'X') : 0,
    ('B', 'Y') : 3,
    ('B', 'Z') : 6,
    ('C', 'X') : 0,
    ('C', 'Y') : 3,
    ('C', 'Z') : 6, }

    with open(file, 'r') as rfile:
        moves = [tuple(entry[:-1].split(" ")) for entry in rfile.readlines()]
    totalValue = 0
    for move in moves:
        # print(games.get(move) + +signValue.get(move))
        totalValue += games.get(move) + +signValue.get(move)
    return totalValue

if __name__ == "__main__":
    print(rps2("input.txt"))