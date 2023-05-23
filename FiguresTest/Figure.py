class Figure:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.Vx = 0.0
        self.Vy = 0.0
        self.size = 0.0
        self.look = '~'
    def __init__(self, x, y, Vx, Vy,size, look):
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.size = size
        self.look = look
    def MoveTheFigure(self, maxwidth, maxheight):
        if(self.x >= 0 or self.x <= maxwidth):
            self.Vx = -self.Vx
        if(self.y >= 0 or self.y <= maxheight):
            self.Vy = -self.Vy





