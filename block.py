lass Block:
    def __init__(self, canvas, color):

        self.canvas = canvas
      
        self.id = self.canvas.create_rectangle(10, 10, 100, 50, fill=color)
        

    def delete(self):
        self.canvas.delete(self.id, 0)

        pos = self.canvas.coords(self.id)

