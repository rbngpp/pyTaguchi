from numpy import size, zeros, random
import pandas as pd
import matplotlib.pyplot as plt

class Variable():
    def __init__(self, name, values):
        self.name = str(name)
        self.values = values
        self.dof = size(values)

# Ref. https://www.itl.nist.gov/div898/handbook/pri/section5/pri56.htm
class Taguchi():
    def __init__(self):
        self.variables = [] 
    
    def add(self, v):
        name = v["name"]
        value = v["values"]
        var = Variable(name,value)
        self.variables.append(var)
    
    def run(self, randomize=False):   
        assert size(self.variables) > 0, "Empty vector"
        self.FACTORS = size(self.variables)
        self.LEVELS = self.variables[0].dof
        self.check_dof()
        self.generate_design()
        if randomize == True:
            self.randomize_runs()
        self.generate_df()
        self.generate_plot()

    def check_dof(self):
        for variable in self.variables:
            if variable.dof != self.LEVELS:
                raise ValueError("Degrees of freedom should be the same!")
    
    def generate_design(self):
        if self.FACTORS == 3 and self.LEVELS == 2:
            self.design = 'L4'
            self.OBSERVATIONS = 4
            self.design_L4()
        elif self.FACTORS == 4 and self.LEVELS == 3:
            self.design = 'L9'
            self.OBSERVATIONS = 9
            self.design_L9()
        elif self.FACTORS == 5 and self.LEVELS == 4:
            self.design ='L16b'
            self.OBSERVATIONS = 16
            self.design_L16b()
        elif self.FACTORS == 7 and self.LEVELS == 2:
            self.design = 'L8'
            self.OBSERVATIONS = 8
            self.design_L8()
        elif self.FACTORS == 11 and self.LEVELS == 2:
            self.design = "L12"
            self.OBSERVATIONS = 12 
            self.design_L12()
        else:
            raise Exception("Taguchi design not available.")
        
    def randomize_runs(self):  
        self.matrix = self.matrix[random.choice(self.matrix.shape[0], self.matrix.shape[0], replace=False)]
    
    def generate_df(self):
        self.columns = []
        self.rows = []
        index = 0
        for variable in self.variables:
            self.columns.append(variable.name)
        while index < self.OBSERVATIONS:
            row = "RUN " + str(index+1)
            self.rows.append(row)
            index += 1
        self.df = pd.DataFrame(self.matrix, columns = self.columns, index = self.rows)
    
    def generate_plot(self):
        self.fig = plt.figure()
        ax = self.fig.add_subplot(111)
        ax.table(cellText = self.df.values,
          rowLabels = self.df.index,
          colLabels = self.df.columns,
          loc = "center",
          cellLoc="center"
         )
        plot_title = "Taguchi table " + self.design
        ax.set_title(plot_title)
        ax.axis("off")
        plt.show()
    
    def design_L4(self):
        # L4: https://www.itl.nist.gov/div898/software/dataplot/dex/L4.DAT
        self.matrix = zeros((4,3))
        # Row 1
        self.matrix[[0],[0]] = self.variables[0].values[0]
        self.matrix[[0],[1]] = self.variables[1].values[0]    
        self.matrix[[0],[2]] = self.variables[2].values[0]
        # Row 2
        self.matrix[[1],[0]] = self.variables[0].values[0]
        self.matrix[[1],[1]] = self.variables[1].values[1]    
        self.matrix[[1],[2]] = self.variables[2].values[1]
        # Row 3
        self.matrix[[2],[0]] = self.variables[0].values[1]
        self.matrix[[2],[1]] = self.variables[1].values[0]    
        self.matrix[[2],[2]] = self.variables[2].values[1]
        # Row 4
        self.matrix[[3],[0]] = self.variables[0].values[1]
        self.matrix[[3],[1]] = self.variables[1].values[1]    
        self.matrix[[3],[2]] = self.variables[2].values[0]
    
    def design_L9(self):
        # L9: https://www.itl.nist.gov/div898/software/dataplot/dex/L9.DAT
        self.matrix = zeros((9,4))
        # Row 1 : 1,1,1,1
        self.matrix[[0],[0]] = self.variables[0].values[0]
        self.matrix[[0],[1]] = self.variables[1].values[0]    
        self.matrix[[0],[2]] = self.variables[2].values[0]
        self.matrix[[0],[3]] = self.variables[3].values[0]
        # Row 2 : 1,2,2,2
        self.matrix[[1],[0]] = self.variables[0].values[0]
        self.matrix[[1],[1]] = self.variables[1].values[1]    
        self.matrix[[1],[2]] = self.variables[2].values[1]
        self.matrix[[1],[3]] = self.variables[3].values[1]
        # Row 3 : 1,3,3,3
        self.matrix[[2],[0]] = self.variables[0].values[0]
        self.matrix[[2],[1]] = self.variables[1].values[2]    
        self.matrix[[2],[2]] = self.variables[2].values[2]
        self.matrix[[2],[3]] = self.variables[3].values[2]
        # Row 4 : 2,1,2,3
        self.matrix[[3],[0]] = self.variables[0].values[1]
        self.matrix[[3],[1]] = self.variables[1].values[0]    
        self.matrix[[3],[2]] = self.variables[2].values[1]
        self.matrix[[3],[3]] = self.variables[3].values[2]
        # Row 5 : 2,2,3,1
        self.matrix[[4],[0]] = self.variables[0].values[1]
        self.matrix[[4],[1]] = self.variables[1].values[1]    
        self.matrix[[4],[2]] = self.variables[2].values[2]
        self.matrix[[4],[3]] = self.variables[3].values[0]
        # Row 6 : 2,3,1,2
        self.matrix[[5],[0]] = self.variables[0].values[1]
        self.matrix[[5],[1]] = self.variables[1].values[2]    
        self.matrix[[5],[2]] = self.variables[2].values[0]
        self.matrix[[5],[3]] = self.variables[3].values[1]
        # Row 7 : 3,1,3,2
        self.matrix[[6],[0]] = self.variables[0].values[2]
        self.matrix[[6],[1]] = self.variables[1].values[0]    
        self.matrix[[6],[2]] = self.variables[2].values[2]
        self.matrix[[6],[3]] = self.variables[3].values[1]
        # Row 8 : 3,2,1,3
        self.matrix[[7],[0]] = self.variables[0].values[2]
        self.matrix[[7],[1]] = self.variables[1].values[1]    
        self.matrix[[7],[2]] = self.variables[2].values[0]
        self.matrix[[7],[3]] = self.variables[3].values[2]
        # Row 9 : 3,3,2,1
        self.matrix[[8],[0]] = self.variables[0].values[2]
        self.matrix[[8],[1]] = self.variables[1].values[2]    
        self.matrix[[8],[2]] = self.variables[2].values[1]
        self.matrix[[8],[3]] = self.variables[3].values[0]
        
    def design_L16b(self):
        # L16b (1): https://www.york.ac.uk/depts/maths/tables/l16b.htm
        # L16b (2): https://www.itl.nist.gov/div898/software/dataplot/dex/L16B.DAT 
        self.matrix = zeros((16,5))
        # Row 1 : 1,1,1,1,1
        self.matrix[[0],[0]] = self.variables[0].values[0]
        self.matrix[[0],[1]] = self.variables[1].values[0]    
        self.matrix[[0],[2]] = self.variables[2].values[0]
        self.matrix[[0],[3]] = self.variables[3].values[0]
        self.matrix[[0],[4]] = self.variables[4].values[0]
        # Row 2 : 1,2,2,2,2
        self.matrix[[1],[0]] = self.variables[0].values[0]
        self.matrix[[1],[1]] = self.variables[1].values[1]    
        self.matrix[[1],[2]] = self.variables[2].values[1]
        self.matrix[[1],[3]] = self.variables[3].values[1]
        self.matrix[[1],[4]] = self.variables[4].values[1]
        # Row 3 : 1,3,3,3,3
        self.matrix[[2],[0]] = self.variables[0].values[0]
        self.matrix[[2],[1]] = self.variables[1].values[2]    
        self.matrix[[2],[2]] = self.variables[2].values[2]
        self.matrix[[2],[3]] = self.variables[3].values[2]
        self.matrix[[2],[4]] = self.variables[4].values[2]
        # Row 4 : 1,4,4,4,4
        self.matrix[[3],[0]] = self.variables[0].values[0]
        self.matrix[[3],[1]] = self.variables[1].values[3]    
        self.matrix[[3],[2]] = self.variables[2].values[3]
        self.matrix[[3],[3]] = self.variables[3].values[3]
        self.matrix[[3],[4]] = self.variables[4].values[3]
        # Row 5 : 2,1,2,3,4
        self.matrix[[4],[0]] = self.variables[0].values[1]
        self.matrix[[4],[1]] = self.variables[1].values[0]    
        self.matrix[[4],[2]] = self.variables[2].values[1]
        self.matrix[[4],[3]] = self.variables[3].values[2]
        self.matrix[[4],[4]] = self.variables[4].values[3]
        # Row 6 : 2,2,1,4,3
        self.matrix[[5],[0]] = self.variables[0].values[1]
        self.matrix[[5],[1]] = self.variables[1].values[1]    
        self.matrix[[5],[2]] = self.variables[2].values[0]
        self.matrix[[5],[3]] = self.variables[3].values[3]
        self.matrix[[5],[4]] = self.variables[4].values[2]
        # Row 7 : 2,3,4,1,2
        self.matrix[[6],[0]] = self.variables[0].values[1]
        self.matrix[[6],[1]] = self.variables[1].values[2]    
        self.matrix[[6],[2]] = self.variables[2].values[3]
        self.matrix[[6],[3]] = self.variables[3].values[0]
        self.matrix[[6],[4]] = self.variables[4].values[1]
        # Row 8 : 2,4,3,2,1
        self.matrix[[7],[0]] = self.variables[0].values[1]
        self.matrix[[7],[1]] = self.variables[1].values[3]    
        self.matrix[[7],[2]] = self.variables[2].values[2]
        self.matrix[[7],[3]] = self.variables[3].values[1]
        self.matrix[[7],[4]] = self.variables[4].values[0]
        # Row 9 : 3,1,3,4,2
        self.matrix[[8],[0]] = self.variables[0].values[2]
        self.matrix[[8],[1]] = self.variables[1].values[0]    
        self.matrix[[8],[2]] = self.variables[2].values[2]
        self.matrix[[8],[3]] = self.variables[3].values[3]
        self.matrix[[8],[4]] = self.variables[4].values[1]
        # Row 10 : 3,2,4,3,1
        self.matrix[[9],[0]] = self.variables[0].values[2]
        self.matrix[[9],[1]] = self.variables[1].values[1]    
        self.matrix[[9],[2]] = self.variables[2].values[3]
        self.matrix[[9],[3]] = self.variables[3].values[2]
        self.matrix[[9],[4]] = self.variables[4].values[0]
        # Row 11 : 3,3,1,2,4
        self.matrix[[10],[0]] = self.variables[0].values[2]
        self.matrix[[10],[1]] = self.variables[1].values[2]    
        self.matrix[[10],[2]] = self.variables[2].values[0]
        self.matrix[[10],[3]] = self.variables[3].values[1]
        self.matrix[[10],[4]] = self.variables[4].values[3]
        # Row 12 : 3,4,2,1,3
        self.matrix[[11],[0]] = self.variables[0].values[2]
        self.matrix[[11],[1]] = self.variables[1].values[3]    
        self.matrix[[11],[2]] = self.variables[2].values[1]
        self.matrix[[11],[3]] = self.variables[3].values[0]
        self.matrix[[11],[4]] = self.variables[4].values[2]
        # Row 13 : 4,1,4,2,3
        self.matrix[[12],[0]] = self.variables[0].values[3]
        self.matrix[[12],[1]] = self.variables[1].values[0]    
        self.matrix[[12],[2]] = self.variables[2].values[3]
        self.matrix[[12],[3]] = self.variables[3].values[1]
        self.matrix[[12],[4]] = self.variables[4].values[2]
        # Row 14 : 4,2,3,1,4
        self.matrix[[13],[0]] = self.variables[0].values[3]
        self.matrix[[13],[1]] = self.variables[1].values[1]    
        self.matrix[[13],[2]] = self.variables[2].values[2]
        self.matrix[[13],[3]] = self.variables[3].values[0]
        self.matrix[[13],[4]] = self.variables[4].values[3]
        # Row 15 : 4,3,2,4,1
        self.matrix[[14],[0]] = self.variables[0].values[3]
        self.matrix[[14],[1]] = self.variables[1].values[2]    
        self.matrix[[14],[2]] = self.variables[2].values[1]
        self.matrix[[14],[3]] = self.variables[3].values[3]
        self.matrix[[14],[4]] = self.variables[4].values[0]
        # Row 16 : 4,4,1,3,2
        self.matrix[[15],[0]] = self.variables[0].values[3]
        self.matrix[[15],[1]] = self.variables[1].values[3]    
        self.matrix[[15],[2]] = self.variables[2].values[0]
        self.matrix[[15],[3]] = self.variables[3].values[2]
        self.matrix[[15],[4]] = self.variables[4].values[1]
        
    def design_L8(self):
        # L8: https://www.itl.nist.gov/div898/software/dataplot/dex/L8.DAT
        self.matrix = zeros((8,7))
        # Row 1 : 1,1,1,1,1,1,1
        self.matrix[[0],[0]] = self.variables[0].values[0]
        self.matrix[[0],[1]] = self.variables[1].values[0]    
        self.matrix[[0],[2]] = self.variables[2].values[0]
        self.matrix[[0],[3]] = self.variables[3].values[0]
        self.matrix[[0],[4]] = self.variables[4].values[0]
        self.matrix[[0],[5]] = self.variables[5].values[0]
        self.matrix[[0],[6]] = self.variables[6].values[0]
        # Row 2 : 1,1,1,2,2,2,2
        self.matrix[[1],[0]] = self.variables[0].values[0]
        self.matrix[[1],[1]] = self.variables[1].values[0]    
        self.matrix[[1],[2]] = self.variables[2].values[0]
        self.matrix[[1],[3]] = self.variables[3].values[1]
        self.matrix[[1],[4]] = self.variables[4].values[1]
        self.matrix[[1],[5]] = self.variables[5].values[1]
        self.matrix[[1],[6]] = self.variables[6].values[1]
        # Row 3 : 1,2,2,1,1,2,2
        self.matrix[[2],[0]] = self.variables[0].values[0]
        self.matrix[[2],[1]] = self.variables[1].values[1]    
        self.matrix[[2],[2]] = self.variables[2].values[1]
        self.matrix[[2],[3]] = self.variables[3].values[0]
        self.matrix[[2],[4]] = self.variables[4].values[0]
        self.matrix[[2],[5]] = self.variables[5].values[1]
        self.matrix[[2],[6]] = self.variables[6].values[1]
        # Row 4 : 1,2,2,2,2,1,1
        self.matrix[[3],[0]] = self.variables[0].values[0]
        self.matrix[[3],[1]] = self.variables[1].values[1]    
        self.matrix[[3],[2]] = self.variables[2].values[1]
        self.matrix[[3],[3]] = self.variables[3].values[1]
        self.matrix[[3],[4]] = self.variables[4].values[1]
        self.matrix[[3],[5]] = self.variables[5].values[0]
        self.matrix[[3],[6]] = self.variables[6].values[0]
        # Row 5 : 2,1,2,1,2,1,2
        self.matrix[[4],[0]] = self.variables[0].values[1]
        self.matrix[[4],[1]] = self.variables[1].values[0]    
        self.matrix[[4],[2]] = self.variables[2].values[1]
        self.matrix[[4],[3]] = self.variables[3].values[0]
        self.matrix[[4],[4]] = self.variables[4].values[1]
        self.matrix[[4],[5]] = self.variables[5].values[0]
        self.matrix[[4],[6]] = self.variables[6].values[1]
        # Row 6 : 2,1,2,2,1,2,1
        self.matrix[[5],[0]] = self.variables[0].values[1]
        self.matrix[[5],[1]] = self.variables[1].values[0]    
        self.matrix[[5],[2]] = self.variables[2].values[1]
        self.matrix[[5],[3]] = self.variables[3].values[1]
        self.matrix[[5],[4]] = self.variables[4].values[0]
        self.matrix[[5],[5]] = self.variables[5].values[1]
        self.matrix[[5],[6]] = self.variables[6].values[0]
        # Row 7 : 2,2,1,1,2,2,1
        self.matrix[[6],[0]] = self.variables[0].values[1]
        self.matrix[[6],[1]] = self.variables[1].values[1]    
        self.matrix[[6],[2]] = self.variables[2].values[0]
        self.matrix[[6],[3]] = self.variables[3].values[0]
        self.matrix[[6],[4]] = self.variables[4].values[1]
        self.matrix[[6],[5]] = self.variables[5].values[1]
        self.matrix[[6],[6]] = self.variables[6].values[0]
        # Row 8 : 2,2,1,2,1,1,2
        self.matrix[[7],[0]] = self.variables[0].values[1]
        self.matrix[[7],[1]] = self.variables[1].values[1]    
        self.matrix[[7],[2]] = self.variables[2].values[0]
        self.matrix[[7],[3]] = self.variables[3].values[1]
        self.matrix[[7],[4]] = self.variables[4].values[0]
        self.matrix[[7],[5]] = self.variables[5].values[0]
        self.matrix[[7],[6]] = self.variables[6].values[1]
        
    def design_L12(self):
        # L12: https://www.york.ac.uk/depts/maths/tables/l12.gif
        self.matrix = zeros((12,11))
        # Row 1 :   1,1,1     1,1,1   1,1,1   1,1
        self.matrix[[0],[0]] = self.variables[0].values[0]
        self.matrix[[0],[1]] = self.variables[1].values[0]    
        self.matrix[[0],[2]] = self.variables[2].values[0]
        self.matrix[[0],[3]] = self.variables[3].values[0]
        self.matrix[[0],[4]] = self.variables[4].values[0]
        self.matrix[[0],[5]] = self.variables[5].values[0]
        self.matrix[[0],[6]] = self.variables[6].values[0]
        self.matrix[[0],[7]] = self.variables[7].values[0]
        self.matrix[[0],[8]] = self.variables[8].values[0]
        self.matrix[[0],[9]] = self.variables[9].values[0]
        self.matrix[[0],[10]] = self.variables[10].values[0]
        # Row 2 :   1,1,1     1,1,2   2,2,2   2,2
        self.matrix[[1],[0]] = self.variables[0].values[0]
        self.matrix[[1],[1]] = self.variables[1].values[0]    
        self.matrix[[1],[2]] = self.variables[2].values[0]
        self.matrix[[1],[3]] = self.variables[3].values[0]
        self.matrix[[1],[4]] = self.variables[4].values[0]
        self.matrix[[1],[5]] = self.variables[5].values[1]
        self.matrix[[1],[6]] = self.variables[6].values[1]
        self.matrix[[1],[7]] = self.variables[7].values[1]
        self.matrix[[1],[8]] = self.variables[8].values[1]
        self.matrix[[1],[9]] = self.variables[9].values[1]
        self.matrix[[1],[10]] = self.variables[10].values[1]
        # Row 3 :   1,1,2     2,2,1   1,1,2   2,2
        self.matrix[[2],[0]] = self.variables[0].values[0]
        self.matrix[[2],[1]] = self.variables[1].values[0]    
        self.matrix[[2],[2]] = self.variables[2].values[1]
        self.matrix[[2],[3]] = self.variables[3].values[1]
        self.matrix[[2],[4]] = self.variables[4].values[1]
        self.matrix[[2],[5]] = self.variables[5].values[0]
        self.matrix[[2],[6]] = self.variables[6].values[0]
        self.matrix[[2],[7]] = self.variables[7].values[0]
        self.matrix[[2],[8]] = self.variables[8].values[1]
        self.matrix[[2],[9]] = self.variables[9].values[1]
        self.matrix[[2],[10]] = self.variables[10].values[1]
        # Row 4 :   1,2,1     2,2,1   2,2,1   1,2
        self.matrix[[3],[0]] = self.variables[0].values[0]
        self.matrix[[3],[1]] = self.variables[1].values[1]    
        self.matrix[[3],[2]] = self.variables[2].values[0]
        self.matrix[[3],[3]] = self.variables[3].values[1]
        self.matrix[[3],[4]] = self.variables[4].values[1]
        self.matrix[[3],[5]] = self.variables[5].values[0]
        self.matrix[[3],[6]] = self.variables[6].values[1]
        self.matrix[[3],[7]] = self.variables[7].values[1]
        self.matrix[[3],[8]] = self.variables[8].values[0]
        self.matrix[[3],[9]] = self.variables[9].values[0]
        self.matrix[[3],[10]] = self.variables[10].values[1]
        # Row 5 :   1,2,2     1,2,2   1,2,1   2,1
        self.matrix[[4],[0]] = self.variables[0].values[0]
        self.matrix[[4],[1]] = self.variables[1].values[1]    
        self.matrix[[4],[2]] = self.variables[2].values[1]
        self.matrix[[4],[3]] = self.variables[3].values[0]
        self.matrix[[4],[4]] = self.variables[4].values[1]
        self.matrix[[4],[5]] = self.variables[5].values[1]
        self.matrix[[4],[6]] = self.variables[6].values[0]
        self.matrix[[4],[7]] = self.variables[7].values[1]
        self.matrix[[4],[8]] = self.variables[8].values[0]
        self.matrix[[4],[9]] = self.variables[9].values[1]
        self.matrix[[4],[10]] = self.variables[10].values[0]
        # Row 6 :   1,2,2     2,1,2   2,1,2   1,1
        self.matrix[[5],[0]] = self.variables[0].values[0]
        self.matrix[[5],[1]] = self.variables[1].values[1]    
        self.matrix[[5],[2]] = self.variables[2].values[1]
        self.matrix[[5],[3]] = self.variables[3].values[1]
        self.matrix[[5],[4]] = self.variables[4].values[0]
        self.matrix[[5],[5]] = self.variables[5].values[1]
        self.matrix[[5],[6]] = self.variables[6].values[1]
        self.matrix[[5],[7]] = self.variables[7].values[0]
        self.matrix[[5],[8]] = self.variables[8].values[1]
        self.matrix[[5],[9]] = self.variables[9].values[0]
        self.matrix[[5],[10]] = self.variables[10].values[0]
        # Row 7 :   2,1,2     2,1,1   2,2,1   2,1
        self.matrix[[6],[0]] = self.variables[0].values[1]
        self.matrix[[6],[1]] = self.variables[1].values[0]    
        self.matrix[[6],[2]] = self.variables[2].values[1]
        self.matrix[[6],[3]] = self.variables[3].values[1]
        self.matrix[[6],[4]] = self.variables[4].values[0]
        self.matrix[[6],[5]] = self.variables[5].values[0]
        self.matrix[[6],[6]] = self.variables[6].values[1]
        self.matrix[[6],[7]] = self.variables[7].values[1]
        self.matrix[[6],[8]] = self.variables[8].values[0]
        self.matrix[[6],[9]] = self.variables[9].values[1]
        self.matrix[[6],[10]] = self.variables[10].values[0]
        # Row 8 :   2,1,2     1,2,2   2,1,1   1,2
        self.matrix[[7],[0]] = self.variables[0].values[1]
        self.matrix[[7],[1]] = self.variables[1].values[0]    
        self.matrix[[7],[2]] = self.variables[2].values[1]
        self.matrix[[7],[3]] = self.variables[3].values[0]
        self.matrix[[7],[4]] = self.variables[4].values[1]
        self.matrix[[7],[5]] = self.variables[5].values[1]
        self.matrix[[7],[6]] = self.variables[6].values[1]
        self.matrix[[7],[7]] = self.variables[7].values[0]
        self.matrix[[7],[8]] = self.variables[8].values[0]
        self.matrix[[7],[9]] = self.variables[9].values[0]
        self.matrix[[7],[10]] = self.variables[10].values[1]
        # Row 9 :   2,1,1     2,2,2   1,2,2   1,1
        self.matrix[[8],[0]] = self.variables[0].values[1]
        self.matrix[[8],[1]] = self.variables[1].values[0]    
        self.matrix[[8],[2]] = self.variables[2].values[0]
        self.matrix[[8],[3]] = self.variables[3].values[1]
        self.matrix[[8],[4]] = self.variables[4].values[1]
        self.matrix[[8],[5]] = self.variables[5].values[1]
        self.matrix[[8],[6]] = self.variables[6].values[0]
        self.matrix[[8],[7]] = self.variables[7].values[1]
        self.matrix[[8],[8]] = self.variables[8].values[1]
        self.matrix[[8],[9]] = self.variables[9].values[0]
        self.matrix[[8],[10]] = self.variables[10].values[0]
        # Row 10 :   2,2,2     1,1,1   1,2,2   1,2
        self.matrix[[9],[0]] = self.variables[0].values[1]
        self.matrix[[9],[1]] = self.variables[1].values[1]    
        self.matrix[[9],[2]] = self.variables[2].values[1]
        self.matrix[[9],[3]] = self.variables[3].values[0]
        self.matrix[[9],[4]] = self.variables[4].values[0]
        self.matrix[[9],[5]] = self.variables[5].values[0]
        self.matrix[[9],[6]] = self.variables[6].values[0]
        self.matrix[[9],[7]] = self.variables[7].values[1]
        self.matrix[[9],[8]] = self.variables[8].values[1]
        self.matrix[[9],[9]] = self.variables[9].values[0]
        self.matrix[[9],[10]] = self.variables[10].values[1]
        # Row 11 :   2,2,1     2,1,2   1,1,1   2,2
        self.matrix[[10],[0]] = self.variables[0].values[1]
        self.matrix[[10],[1]] = self.variables[1].values[1]    
        self.matrix[[10],[2]] = self.variables[2].values[0]
        self.matrix[[10],[3]] = self.variables[3].values[1]
        self.matrix[[10],[4]] = self.variables[4].values[0]
        self.matrix[[10],[5]] = self.variables[5].values[1]
        self.matrix[[10],[6]] = self.variables[6].values[0]
        self.matrix[[10],[7]] = self.variables[7].values[0]
        self.matrix[[10],[8]] = self.variables[8].values[0]
        self.matrix[[10],[9]] = self.variables[9].values[1]
        self.matrix[[10],[10]] = self.variables[10].values[1]
        # Row 12 :   2,2,1     1,2,1   2,1,2   2,1
        self.matrix[[11],[0]] = self.variables[0].values[1]
        self.matrix[[11],[1]] = self.variables[1].values[1]    
        self.matrix[[11],[2]] = self.variables[2].values[0]
        self.matrix[[11],[3]] = self.variables[3].values[0]
        self.matrix[[11],[4]] = self.variables[4].values[1]
        self.matrix[[11],[5]] = self.variables[5].values[0]
        self.matrix[[11],[6]] = self.variables[6].values[1]
        self.matrix[[11],[7]] = self.variables[7].values[0]
        self.matrix[[11],[8]] = self.variables[8].values[1]
        self.matrix[[11],[9]] = self.variables[9].values[1]
        self.matrix[[11],[10]] = self.variables[10].values[0]