#helper functions:
def filled_row(size):
    row = []
    for i in range(size):
        row.append("X")
    return row






class TileMatrix:
    
    def __init__(self,cols,rows):
        self.cols = cols
        self.rows = rows
        self.matrix = []
        for i in range(rows):
            self.matrix.append(filled_row(cols))
    def change_cell(self, column, row, element):
        self.matrix[row][column] = element
    def save_to_file(self):
        f = open('savedmap.txt', 'w')
        for row in self.matrix:
            line = ""
            for char in row:
                line += char
            line += '\n'
            f.write(line)
        f.close()

        
        
        
