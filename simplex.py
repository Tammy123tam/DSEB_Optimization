import pandas as pd
import streamlit as st
import re
from sympy.parsing.sympy_parser import parse_expr
import sympy as sp

class Tableau(object):
    """docstring for Tableau"""
    def __init__(self, cost_function, constraints):
        super(Tableau, self).__init__()
        self.cost_function = cost_function
        self.constraints = constraints

        self.initTableau()

        # Initialize the tableau model
    def initTableau(self):
        self.constraints_count = len(self.constraints)
        self.var_count = len(self.cost_function)

        self.artificial_variable_count = 0

        self.cost_index = self.constraints_count

        self.basis = list()

        self.artificial_variable = list()

        self.columns = self.var_count + self.constraints_count + 1
        self.b_index = self.columns - 1

        self.lines = self.constraints_count + 1

        self.tableau = []

        # Adding the constraints into the tableau
        for j in range(0,self.constraints_count):
            self.tableau.append([]) # insert line
            for i in range(0,self.var_count):
                self.tableau[j].append(float(self.constraints[j][i]))

            for i in range(self.var_count,self.columns-1):
                eq = self.constraints[j][self.var_count]
                if i - self.var_count == j:
                    if eq == '<=' or eq == '<' or eq == 0:
                        self.tableau[j].append(1.0)
                    else:
                        self.tableau[j].append(-1.0)
                else:
                    self.tableau[j].append(0.0)

            # add b column
            self.tableau[j].append(float(self.constraints[j][self.var_count+1]))

        # Adding the costs
        self.tableau.append([])
        for i in range(0,self.var_count):
            self.tableau[self.constraints_count].append(float(self.cost_function[i]))
        for i in range(self.var_count,self.columns):
            self.tableau[self.constraints_count].append(0.0)

        # Add basis
        for i in range(self.var_count,self.columns-1):
            self.basis.append(i)
    

    def __str__(self):
        s = ""
        i = 0
        var = []
        value = []

        temp_basis = [i+1 for i in self.basis]

        for l in self.tableau:
            if i < len(self.basis):
                s += f'[x{temp_basis[i]}] ' + str(l)+"\n"
                var.append('x'+str(temp_basis[i]))
                value.append(f'x{temp_basis[i]} ')
            else:
                if i == len(temp_basis):
                    s += '[z] ' + str(l)+"\n"
                    var.append('z')
                else:
                    s += '[w] ' + str(l)+"\n"
                    var.append('w')
            i += 1
        temp_str_basis = "Basis: "
        for i in range(len(temp_basis)):
            temp_str_basis += f'x{temp_basis[i]}'
            if i != len(temp_basis)-1:
                temp_str_basis +=', '
        s+= temp_str_basis
        return s

    def __getitem__(self, key):
        return self.tableau[key]

    def __setitem__(self, key, value):
        self.tableau.insert(key, value)

    def changeBasis(self, enter, leave):
        out = self.basis.pop(leave)
        self.basis.insert(leave,enter)

        st.latex(r'\text{Changing basis: enter }'+'x_'+str(enter+1)+r'\text{ leave }'+ 'x_'+str(out+1))

    def addColumn(self, key, default_value):
        for r in self.tableau:
            r.insert(key,default_value)
        self.columns += 1

    def removeColumn(self,key):
        for r in self.tableau:
            r.pop(key)
        self.columns -= 1

    def addRow(self,key,default_value):
        self.tableau.insert(key,[])
        for i in range(0,self.columns):
            self.tableau[key].append(default_value)
        self.lines += 1

    def removeRow(self,key):
        self.tableau.pop(key)
        self.lines -= 1


# Class to represent Simplex Two Phases method
def to_dataframe(a):
    index = []
    for i in range(len(a)):
            if a[i]=="[" and a[i+1].isalpha():
                    temp = ""
                    for j in range(i+1,len(a)):
                            if a[j]==']':
                                    break
                            temp+=a[j]
                    index.append(temp)

    for i in range(len(index)):
            index[i] = index[i].replace("[","")
            index[i] = index[i].replace("]", "")
    columns = []
    for i in range(len(a)):
            if a[i]=='[' and (a[i+1].isnumeric() or a[i+1]=="-"):
                    x = i+1
                    for j in range(x,len(a)):
                            if a[j]=="]":
                                    y = j
                                    break
                    columns.append(a[x:y])
    data = []
    for i in range(len(columns)):

         columns[i]=columns[i].replace(",","")
         lst = columns[i].split()
         lst1 = [float(j) for j in lst]
         print(lst1)
         data.append(lst1)

    columns1 = [f'x{i+1}' for i in range(len(data[0])-1)]
    columns1.append('Solution')
    df = pd.DataFrame(data, index = index,columns=columns1)

    return df



class Simplex(object):
    """docstring for Simplex2D"""
    def __init__(self, tableau ):
        super(Simplex, self).__init__()
        self.tableau = tableau
        # hàm tạo bảng
        
    # First Phase
    def phase1(self):
        st.latex( r'\text{Simplex Phase 1 }')

        res = True
        if self.checkFeasibility() == False:

            self.addArtificialVariables()
            self.addNewCostFunction()

            simplex = Simplex(self.tableau)
            count = 1
            while simplex.canContinue():
                st.latex('')
                st.latex(r'\text{Iteration }'+ str(count))
                st.latex('')
                simplex.iteration()
                count += 1
                temp = str(simplex.tableau)
                st.dataframe(to_dataframe(temp))
               
            # In this case, the Phase 1 has finished with artificial variables
            if len(set(self.tableau.basis) & set(self.tableau.artificial_variable)) > 0:
                st.latex(r'\text{There still exist artifical variables}')
                res =  False
            else:
                # The sum of the infeasibilities is greater than 0, what characterizes an unfeasible solution
                if self.tableau[self.tableau.cost_index][self.tableau.b_index] > 0:
                    st.latex(r'\text{Sum of artificial variables is greater than 0, then the problem is not feasible}')
                    self.solution = 'infeasible'
                    res = False

                # Everything has happened fine. A feasible tableau has been found to proceed to Phase 2
                else:
                    st.latex(r'\text{Phase 1 has found feasible tableau}')
                    # Remove the artificial cost function
                    self.tableau.removeRow(self.tableau.cost_index)
                    self.tableau.cost_index = self.tableau.lines -1

                    # Remove the artifical variables
                    for i in self.tableau.artificial_variable:
                        self.tableau.removeColumn(self.tableau.columns-2)

                    self.tableau.b_index = self.tableau.columns-1

        st.latex(r'\text{Simplex Phase 1 End}')
        return res

    # Second Phase
    # This phase occurs only if the method has found a feasible solution in Phase 1
    def phase2(self):
        st.markdown('')
        st.latex(r'\text{Simplex Phase 2}')
        i = 1
        st.latex(r'\text{ Initial Tableau Phase 2}')
        temp = str(self.tableau)
        st.dataframe(to_dataframe(temp))
        b = True
        while self.canContinue():
            st.latex('')
            st.latex(r'\text{- Iteration }'+ str(i))
            st.latex('')
            b = self.iteration()
    
            temp = str(self.tableau)
            st.dataframe(to_dataframe(temp))
            if b == False:
                break
            i += 1
        if b == True:
            self.solution = self.tableau[self.tableau.cost_index][self.tableau.b_index]
        st.markdown('')
        st.latex(r'\text{Simplex Phase 2 Ends } ')

    # Exceute the method
    def execute(self):
        self.solution = None
        r = self.phase1()
        if r == True:
            self.phase2()

    # Add artificial variables into Tableau
    def requeredArtificalVariables(self):
        n = self.tableau.constraints_count
        n_of_variables = 0
        c = list()
        for i in range(0,n):
            for j in range(self.tableau.var_count,self.tableau.columns):
                if j - self.tableau.var_count == i:
                    if self.tableau[i][j] != 1:
                        n_of_variables += 1
                        c.append(i)

        return n_of_variables,c

    # Add artificial variable during the Phase 1	
    def addArtificialVariables(self):
        n_of_variables,c = self.requeredArtificalVariables()

        if n_of_variables  > 0:
            self.tableau.artificial_variable_count = n_of_variables
            for i in range(0,n_of_variables):
                idx = self.tableau.columns - 1
                self.tableau.addColumn(idx,0.0)
            
            idx = self.tableau.var_count+self.tableau.constraints_count
            for r in c:
                self.tableau.artificial_variable.append(idx)
                self.tableau[r][idx] = 1.0

                self.tableau.basis.remove(r+self.tableau.var_count)
                self.tableau.basis.append(idx)

                idx += 1

        self.tableau.b_index = self.tableau.columns - 1

    # Add an artificial cost function W during the Phase 1
    def addNewCostFunction(self):		
        n_of_variables,c = self.requeredArtificalVariables()
        if n_of_variables > 0:
            self.tableau.addRow(self.tableau.lines,0.0)
            idx = self.tableau.lines - 1
            for a in self.tableau.artificial_variable:
                self.tableau[idx][a] = 1.0

            for r in c:
                for i in range(0,self.tableau.columns):
                    self.tableau[idx][i] = self.tableau[idx][i] -  self.tableau[r][i]
            self.tableau.cost_index = self.tableau.lines - 1

    # Check if there still exist a direction of decreasing
    def canContinue(self):
        cost_index = self.tableau.cost_index
        for i in range (0,self.tableau.columns):
            if self.tableau[cost_index][i] < 0:
                return True
        return False

    def checkFeasibility(self):
        n,c = self.requeredArtificalVariables()
        st.latex(n)
        if n == 0:
            return True
        return False

    # Get the pivot, which is the column with the lowest value in cost line
    def getPivot(self):
        cost_index = self.tableau.cost_index
        pivot = 0
        for i in range (0,self.tableau.columns-1):
            if self.tableau[cost_index][i] < pivot:
                pivot = self.tableau[cost_index][i]
        return self.tableau[cost_index].index(pivot)

    # Check if the solution is unbounded
    def isBoundedSolution(self,pivot):
        # Given a pivot, check if there is at least one element in the pivot column that is positive
        for i in range(0,self.tableau.constraints_count):
            if self.tableau[i][pivot] > 0 :
                return True
        return False

    def isDegenerative(self,pivot):
        b_index = self.tableau.b_index
        limit_set  = set()
        limit = float("inf")
        for i in range(0,self.tableau.constraints_count):
            if self.tableau[i][pivot] > 0 :
                limit = self.tableau[i][b_index]/self.tableau[i][pivot]
                if limit in limit_set:
                    return True
        return False

    # Look for the minimum limit for the variable
    # pivot: pivot index
    def getConstraintLimit(self,pivot):
        b_index = self.tableau.b_index
        limit = float("inf")
        line_index = -1
        for i in range(0,self.tableau.constraints_count):
            if self.tableau[i][pivot] > 0:
                # print('l : '+str(self.tableau[i][b_index]/self.tableau[i][pivot]))
                if self.tableau[i][b_index]/self.tableau[i][pivot] < limit:
                    limit = self.tableau[i][b_index]/self.tableau[i][pivot]
                    line_index = i
        return line_index

    # Scaling matrix in order to obtain 0 in position 'pivot'
    # i: constraint index
    # pivot: pivot index
    def scalingMatrix(self,i,pivot):
        for j in range(0,self.tableau.lines):
            if i != j:
                pivot_value = self.tableau[j][pivot]
                for k in range(0,self.tableau.columns):
                    self.tableau[j][k] = self.tableau[j][k] - (self.tableau[i][k]*pivot_value)

    def gaussianOperation(self,constraint_index,pivot_index):
        pivot_value = self.tableau[constraint_index][pivot_index]
        for i in range(0,self.tableau.columns):
            self.tableau[constraint_index][i] = self.tableau[constraint_index][i] / pivot_value
        self.scalingMatrix(constraint_index,pivot_index)

    # Perform iteration for Simplex Method
    def iteration(self):
        pivot_index  = self.getPivot()
        if(self.isDegenerative(pivot_index)):
            st.latex(r'\text{Problem is degenerative and it needs to use another method}')
            self.solution = 'degenerative'
            return False

        # Check if the solution if bounded
        if(self.isBoundedSolution(pivot_index)):
            constraint_index = self.getConstraintLimit(pivot_index)
            if constraint_index == -1:
                return
            # change basis
            self.tableau.changeBasis(pivot_index,constraint_index)
            self.gaussianOperation(constraint_index, pivot_index)
            return True
        else:
            st.latex(r'\text{Solution is unbounded}' )
            self.solution = 'unbounded'
            return False

def extract_coefficient(eq):
    f = re.findall(r"([+-])?\s*(?:(\d+)\s*\*\s*)?([a-z]\w*)", eq)
    return [int(symbol + (coeff or '1')) for (symbol, coeff, var) in f]

def extract_coefficientfrom_ineq(ineq):
    f = extract_coefficient(ineq)
    for i, char in enumerate(ineq):
        if char == '<' or char == '>' or char == '=':
            if ineq[i+1] == '=':
                f.append(char + ineq[i+1])
                f.append(int(ineq[i+2:len(ineq)]))
            else:
                f.append(char)
                f.append(int(ineq[i + 1:len(ineq)]))
            break
    return f

def test():
    f = st.sidebar.text_input("Input cost function with format: 3*x_1 + 5*x_2 ...")
    f = f.replace(" ","")
    f = f.replace("_","")
    f = f.replace("^","**")
    try:
      for i in range(len(f)):
          if f[i].isnumeric() and f[i+1].isalpha():
            f = f[:i+1] + "*" + f[i+1:]
    except:
      pass
    
    variables = []
    for i in range(len(extract_coefficient(f))):
      variables.append(sp.symbols(f'x{i+1}')) 
    st.latex(r"\text{ Minimizing f(x) = }" + sp.latex(parse_expr(f)))

    f = extract_coefficient(f)
    num_var = len(f)
    st.latex(r"\text{s.t: }")
    
    num_cons = int(st.sidebar.number_input("Number of constrains u want to add:"))
    
    r= list()
    needInput = 1
    while(needInput <= num_cons):
        r_i = st.sidebar.text_input('Adding contrain #' + str(needInput))
        r_i = r_i.replace(" ","")
        r_i = r_i.replace("_","")
        r_i = r_i.replace("^","**")
        try:
            for i in range(len(r_i)):
                if r_i[i].isnumeric() and r_i[i+1].isalpha():
                    r_i = r_i[:i+1] + "*" + r_i[i+1:]
        except:
            pass
        if ">=" in r_i or "<=" in r_i:
            st.latex(sp.latex(parse_expr(r_i)))
        else:
            temp = r_i
            for i in range(len(temp)):
                if temp[i] =='=':
                    x = i
                    break
            st.latex(sp.latex(parse_expr(temp[:i]))+ str(temp[i:]))
        r_i = extract_coefficientfrom_ineq(r_i)
        if len(r_i) != num_var + 2:
            st.sidebar.error("Invalid input, enter the input again. ")
            continue
        r.append(r_i)
        needInput += 1
    st.latex(f"x_i>=0 (i = 1,...{num_var})")
    st.markdown('<div style="text-align: center;">---------------------------------------------------------------------------</div>', unsafe_allow_html=True )
    tableau = Tableau(f,r)
    simplex = Simplex(tableau)
    
    simplex.execute()
  
    st.latex(r'\text{Solution: }'+f'{simplex.solution}')
def test1():
    f = "-12*x_1 - 3*x_2 - x_3 "
    st.sidebar.text_input("Input cost function with format: 3*x_1 + 5*x_2 ...",f)
    f = f.replace(" ","")
    f = f.replace("_","")
    f = f.replace("^","**")
    try:
      for i in range(len(f)):
          if f[i].isnumeric() and f[i+1].isalpha():
            f = f[:i+1] + "*" + f[i+1:]
    except:
      pass
    
    variables = []
    for i in range(len(extract_coefficient(f))):
      variables.append(sp.symbols(f'x{i+1}')) 
    st.latex(r"\text{ Minimizing f(x) = }" + sp.latex(parse_expr(f)))

    f = extract_coefficient(f)
    num_var = len(f)
    st.latex(r"\text{s.t: }")
    num_cons = 3
    st.sidebar.number_input("Number of constrains u want to add:",num_cons)
    r = list()
    r1= ['10*x_1 + 2*x_2 + x_3 <= 100','7*x_1 + 3*x_2 + 2*x_3 <= 77','2*x_1 + 4*x_2 + x_3 <= 80']
    needInput = 1
    while(needInput <= num_cons):
        r_i = r1[needInput-1]
        st.sidebar.text_input('Adding contrain #' + str(needInput),r_i)
        r_i = r_i.replace(" ","")
        r_i = r_i.replace("_","")
        r_i = r_i.replace("^","**")
        try:
            for i in range(len(r_i)):
                if r_i[i].isnumeric() and r_i[i+1].isalpha():
                    r_i = r_i[:i+1] + "*" + r_i[i+1:]
        except:
            pass
        if ">=" in r_i or "<=" in r_i:
            st.latex(sp.latex(parse_expr(r_i)))
        else:
            temp = r_i
            for i in range(len(temp)):
                if temp[i] =='=':
                    x = i
                    break
            st.latex(sp.latex(parse_expr(temp[:i]))+ str(temp[i:]))
        r_i = extract_coefficientfrom_ineq(r_i)
        if len(r_i) != num_var + 2:
            st.sidebar.error("Invalid input, enter the input again. ")
            continue
        # r.append(r_i)
        needInput += 1
        r.append(r_i)
    st.latex(f"x_i>=0 (i = 1,...{num_var})")
    st.markdown('<div style="text-align: center;">---------------------------------------------------------------------------</div>', unsafe_allow_html=True )
    tableau = Tableau(f,r)
    simplex = Simplex(tableau)
    
    simplex.execute()

