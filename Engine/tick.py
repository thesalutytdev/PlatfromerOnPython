class Tick:
    current_tick = 0
    def tick(self):
        self.current_tick += 1
    def setTick(self, tick: int):
        self.current_tick = tick
    def getTick(self):
        return self.current_tick