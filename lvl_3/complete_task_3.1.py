class Matrix:
    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.data = [[None for _ in range(columns)] for _ in range(rows)]

    def set_value(self,row,column,value):
#        print(value)
        self.data[row][column]=value

    def get_value(self,row,column):
        return self.data[row][column]



matrix = Matrix(9,9)

for i in range(9):
    for j in range(9):
        matrix.set_value(i,j,(i+1)*(j+1))
        #print(i,j)
for i in range(9):
    for j in range(9):
        print('%3d' % matrix.get_value(i,j), end=' ')
    print('\n')
# можно так
#for i in range(9):
#    for j in range(9):
#        print('%3d' % matrix.data[i][j], end=' ')
#    print('\n')