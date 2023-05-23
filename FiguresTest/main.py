from Figure import Figure
size = 3
sizemap = 15
orangeFigure = Figure(1, 2, 3, 4, 5, 'S')
blackFigure = Figure(3, 4, 3, 4, 5, 'C')
Figures = [orangeFigure, blackFigure]


Map = [[0 for x in range(sizemap)] for y in range(sizemap)]
def insertFiguresIntoMap():
    for i in range(len(Figures)):
        Map[Figures[i].y][Figures[i].x] = Figures[i].look

def printMapOfFigures():
    for i in range(sizemap):
        for j in range(sizemap):
            print(Map[i][j], end='')
        print("\n")

def main():
    insertFiguresIntoMap()
    printMapOfFigures()

if __name__ == "__main__":
    main()