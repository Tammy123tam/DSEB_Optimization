# import imp
from operator import le
import streamlit as st
from sympy.abc import *
from sympy import hessian, Matrix,Symbol,diff,solve,simplify
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
import numpy as np
import re
from time import time
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import math
import networkx as nx
from latex2sympy2 import latex2sympy

class Unconstrained_Opti:
  def __init__(self,obj_function,option):
    self.obj_function = obj_function
    self.option = option 

  #Check convex or concave for uncontrained problem without initial value
  def is_not_convex(self,f,max_time=0.5,min_points=1000):
      """
      Input:
          f: a callable function, should take arguments of the form (n,x) where n is the number of samples
          and return a scalar
          num_variables: the number of variables in x
         
      Output:
          result: bool, true if the function is not convex
    
      """
      
      f = latex2sympy(f)
      variables = list(f.free_symbols)
      n = len(variables)

      
      t0 = time()
      while time()-t0 < max_time:
         
          pts = np.random.randn(2,min_points,n)
          mean_pt = np.mean(pts,axis=0)
          f1 = []
          f2 = []
          for i in range(len(pts[0])):
            f1.append((f.subs([(variables[values],pts[0][i][values]) for values in range(n)]) +f.subs([(variables[values],pts[1][i][values]) for values in range(n)] ))/2)
            f2.append(f.subs([(variables[values],mean_pt[i][values]) for values in range(n)] ))
          f1 = np.array(f1) 
          f2 = np.array(f2)
          if np.any(f1<f2):
            return True
          else:
            return False
  def is_not_concave(self,f,max_time=1,min_points=1000):
      f = "(-1)*("+ f +")"
      return self.is_not_convex(f)

  

  def Un_op_without(self):
    temp_obj = self.obj_function
    
    self.obj_function = latex2sympy(self.obj_function)
    variables = list(self.obj_function.free_symbols)
    
    try:
      temp_var1 = [str(i) for i in variables]
      temp_var = [int(i[2:]) for i in temp_var1] 
      for i in range(len(temp_var)):
        for j in range(i+1,len(temp_var)):
          if temp_var[i]>temp_var[j]:
            temp_var[i],temp_var[j]=temp_var[j],temp_var[i]
            variables[i],variables[j] = variables[j],variables[i]
    except:
      pass
    n = len(variables)
    st.latex(f"f({sp.latex(variables)}) = {sp.latex(self.obj_function)}")
    
    # Check the function is convex, concave or neither of them
    if self.is_not_concave(temp_obj) == True and not(self.is_not_concave(temp_obj) == True and self.is_not_convex(temp_obj)==True):
      convex =1 

      st.latex(r"\text{The function f(x) is convex}")
    elif self.is_not_convex(temp_obj) == True and not(self.is_not_concave(temp_obj) == True and self.is_not_convex(temp_obj)==True):
      convex = 0
      st.latex(r"\text{The function f(x) is concave}")
    elif self.is_not_concave(temp_obj) == True and self.is_not_convex(temp_obj)==True:
      convex = -1    
      st.latex(r"\text{The function f(x) is neither concave nor convex}")
    else : 
      convex = 2  
      st.latex(r"\text{The function f(x) is both concave and convex}")

    gradient = lambda f, variables: Matrix([f]).jacobian(variables)
    gradMat = (gradient(self.obj_function, variables)).T
    st.latex(r"\text{The Gradient Matrix of f(x) is } \nabla f(x) = " + sp.latex(gradMat))
    hessMat = hessian(self.obj_function, variables)
    st.latex(r"\text{The Hessian matrix of the function is H(x) =}" + sp.latex(hessMat))
    st.latex(r"\text{The value of x when }  \nabla f(x) =0: ")
    local = solve(gradMat,variables,dict=True)
    local1 = []
    for i in local:
      a= []
      for j in i.values():
        a.append(j)
      local1.append(a)
    if local1:
      count =1
      for i in local1:
        st.latex(f"x^{count} = " + sp.latex(i))
        count +=1
    else:
      st.latex(r"\text{There is no value of x satisfied} \nabla f(x) =0. \text{There is no local minimum or maximum.}")
      return

    
    localMax =[]
    localMin = []
    count =1
    for i in local1:
      st.markdown('<div style="text-align: center;">---------------------------------------------------------------------------</div>', unsafe_allow_html=True )
      hessMat_at_point = hessMat.subs([(variables[values],i[values]) for values in range(n)])
      hessMat_at_point_T = np.array(hessMat_at_point).T
      symmetric = np.all(np.array(hessMat_at_point,dtype = float) ==np.array(hessMat_at_point_T,dtype = float))
      st.latex(r"\text{The Hessian matrix at }" + f'x^{count}'+ "=" + sp.latex(i) + r"\text{is }" + sp.latex(hessMat_at_point))
      eig_value, eig_vector = np.linalg.eig(np.array(hessMat_at_point,dtype = float))
      temp_eig_value = sp.Matrix(eig_value)
      st.latex(r"\text{The eigenvalues of the Hessian matrix at }"+f'x^{count}'+ "="+ sp.latex(i) + r"\text{is }" +sp.latex(temp_eig_value))


      #Check whether Hessian matrix is posive (negative) semidefinite or not
      # Posive (negative) semidefinite is a symmetric maxtrix which has all eigenvalues are non- negative (non-positive)
      if self.option ==1:
        if np.all(np.linalg.eigvals(np.array(hessMat_at_point,dtype=float)) >=0) and symmetric == True:
          localMin.append(i)
          st.latex(r"\text{The Hessian matrix at }" + f'x^{count} ='+ sp.latex(i) + r"\text{ is positive semidefinite (a symmetric maxtrix which has all eigenvalues are non-negative)}")
          st.latex(f"x^{count} ="+sp.latex(i) +r"\text{ is local minimum}")

        else:
          st.latex(r"\text{The Hessian matrix at }" + f'x^{count} ='+ sp.latex(i) + r"\text{ is not positive semidefinite (positive semidefinite matrix is a symmetric maxtrix which has all eigenvalues are non-negative)}")
        

      if self.option ==2: 
        if np.all(np.linalg.eigvals(np.array(hessMat_at_point,dtype=float)) <=0) and symmetric == True :
            localMax.append(i)
            st.latex(r"\text{The Hessian matrix at }" + f'x^{count} ='+ sp.latex(i) + r"\text{ is negative semidefinite (a symmetric maxtrix which has all eigenvalues are non-positive)}")
            st.latex(f"x^{count} ="+sp.latex(i) +r"\text{ is local maximum}")
        else:
          st.latex(r"\text{The Hessian matrix at }" + f'x^{count} ='+ sp.latex(i) + r"\text{ is not negative semidefinite (negative semidefinite matrix is a symmetric maxtrix which has all eigenvalues are non-positive)}")

      if self.option ==1:
        if localMin:
          if convex == -1:
            count1 = 0 
            for i in localMin:
              obj_fun_at_point = self.obj_function.subs([(variables[values],i[values]) for values in range(n)])
              st.latex(r"\text{Local minimum is }" + sp.latex(obj_fun_at_point) + r"\text{ at }"+f'x^{count} ='+sp.latex(localMin[count1]))
              count1 +=1
          elif convex ==2 or convex ==1:
            obj_fun_at_point = self.obj_function.subs([(variables[values],localMin[0][values]) for values in range(n)])
            st.latex(r"\text{The local minimum of a convex function is global minimum. The global minimum is }" +  sp.latex(obj_fun_at_point) +  r"\text{ at }"+f'x^{count} =' + sp.latex(localMin[0]))
        else:
          st.latex(r"\text{There is no local minumum}")

      elif self.option ==2: 
        if localMax:
          if convex == -1:
            count1 =0
            for i in localMax:
              obj_fun_at_point = self.obj_function.subs([(variables[values],i[values]) for values in range(n)])  
              st.latex(r"\text{Local maximum is }" + sp.latex(obj_fun_at_point) + r"\text{at x = }"+sp.latex(localMax[count1]))
              count1 +=1
          elif convex ==2 or convex ==0:
            obj_fun_at_point = self.obj_function.subs([(variables[values],localMax[0][values]) for values in range(n)])
            st.latex(r"\text{The local maximum of a concave function is global maximum. The global maximum is }" +  sp.latex(obj_fun_at_point) +   r"\text{ at }"+f'x^{count} =' + sp.latex(localMax[0]))
        else:
          st.latex(r"\text{There is no local maximum}")
      count +=1



class Unconstrained_Opti1:
# Class for unconstrained optimization with initial value, maximum iteration
  def __init__(self,obj_function, initial_val, max_iter,option):
        self.obj_function = obj_function
        self.initial_val = initial_val
        self.max_iter  = max_iter
        self.option = option
        

        #Option 1 for minimize and 2 for maximize
  
  def Newton_Optimizer_UN(self):

        self.obj_function = latex2sympy(self.obj_function)
        variables = list(self.obj_function.free_symbols)
        try:
          temp_var1 = [str(i) for i in variables]
          temp_var = [int(i[2:]) for i in temp_var1] 
          for i in range(len(temp_var)):
            for j in range(i+1,len(temp_var)):
              if temp_var[i]>temp_var[j]:
                temp_var[i],temp_var[j]=temp_var[j],temp_var[i]
                variables[i],variables[j] = variables[j],variables[i]
        except:
          pass
       
        if self.option ==1:
          st.latex(r"\text{Find the minimum of the function }"+"f("+ sp.latex(variables)+ ") = "+sp.latex(self.obj_function)+r"\text{ with initial point }x^0= "+sp.latex(self.initial_val)+ r"\text{ and the maximum number of iterations is }"+f"{int(self.max_iter)}")
        else: 
          st.latex(r"\text{Find the maximum of the function }"+"f("+ sp.latex(variables)+ ") = "+sp.latex(self.obj_function)+r"\text{ with initial point }x^0= "+sp.latex(self.initial_val)+ r"\text{ and the maximum number of iterations is }"+f"{int(self.max_iter)}")
        gradient = lambda obj_function, variables: Matrix([obj_function]).jacobian(variables)
        
        #Compute Gradient and Hessian
        gradMat = (gradient(self.obj_function, variables)).T   #Transposes the Matrix computed by Jacobian
        hessMat = hessian(self.obj_function, variables)
        st.latex(r"\text{The Gradient Matrix of f(x) is } \nabla f(x) = " + sp.latex(gradMat))
        st.latex(r"\text{The Hessian matrix of the function is H(x) =}" + sp.latex(hessMat))
        
        #Compute Gradient at given points
        gradMat_at_point = gradMat.subs([(variables[values],self.initial_val[values]) for values in range(len(self.initial_val))])
        st.latex(r"\text{The gradient of function at initial point }x^0 = "+ sp.latex(self.initial_val) + r'\text{ is }'+ r"\nabla f(x) =" + sp.latex(gradMat_at_point))

        
        optimized_parameters = Matrix(len(variables),1, [values for values in self.initial_val])
        iter = 1
        check = 0
        while (np.all(np.array(gradMat_at_point)==0) == False):
            check =1
            st.subheader(f"Iteration {iter}: ")
            #Compute Hessian at initial points:
            hessMat_at_point = hessMat.subs([(variables[values],optimized_parameters[values]) for values in range(len(optimized_parameters))])
            hessMat_at_point = np.float64(hessMat_at_point)
            temp = optimized_parameters
            if np.linalg.det(hessMat_at_point) == 0:
              st.latex(f"The determinant of Hessian matrix at x{iter-1} equals to 0")
              return
            optimized_parameters = optimized_parameters -((np. linalg. inv(hessMat_at_point))*(gradMat_at_point))
          

            st.latex(f"x^{iter} = x^{iter-1} - (H_{iter-1})^-1 *"+ r" \nabla f(x_"+f"{iter-1}) = {sp.latex(temp)} - {sp.latex(sp.Matrix(np. linalg. inv(hessMat_at_point)))} * {sp.latex(gradMat_at_point)} = {sp.latex(optimized_parameters)}")

            #Recomputing using new guesses
            gradMat_at_point = gradMat.subs([(variables[values],optimized_parameters[values]) for values in range(len(optimized_parameters))])
            st.latex(r"\text{The Gradient Matrix at }"+f"x^{iter} = "+sp.latex(optimized_parameters)+r"\text{ is }"+r"\nabla f(x^"+f"{iter})"+ f" = {sp.latex(gradMat_at_point)}" )
            hessMat_at_point = hessMat.subs([(variables[values],optimized_parameters[values]) for values in range(len(optimized_parameters))])
            st.latex(r"\text{The Hessian Matrix at }"+ f"x^{iter} = "+sp.latex(optimized_parameters)+r"\text{ is }"+f"H(x^{iter}) = "+sp.latex(hessMat_at_point))
            iter+=1  

            if iter == self.max_iter:
              st.latex(r"\text{You've reached the maximum number of iterations. The approximated solution of the given problem is }"+f"{self.obj_function.subs([(variables[values],optimized_parameters[values]) for values in range(len(optimized_parameters))])}"+r"\text{ at x = }"+ sp.latex(optimized_parameters))
              return 

        if check ==0:
          hessMat_at_point = hessMat.subs([(variables[values],optimized_parameters[values]) for values in range(len(optimized_parameters))])
          st.latex(r"\text{The Hessian Matrix at }"+ f"x^{iter-1} = "+sp.latex(optimized_parameters)+r"\text{ is }"+f"H(x^{iter}) = "+sp.latex(hessMat_at_point))


        if self.option ==1: 
          if  np.all(np.linalg.eigvals(np.array(hessMat_at_point,dtype=float)) >= 0):
            eig_value, eig_vector = np.linalg.eig(np.array(hessMat_at_point,dtype = float))
            temp_eig_value = sp.Matrix(eig_value)
            st.latex(r"\text{The eigenvalues of the Hessian matrix at }"+f'x^{iter-1}'+ "="+ sp.latex(optimized_parameters) + r"\text{is }" +sp.latex(temp_eig_value))
            st.latex(r"\text{The Hessian Matrix at }" +f'x^{iter-1}'+ "="+ sp.latex(optimized_parameters) +r"\text{is Positive Semidefinite (it is symmetric and has all eigenvalues are non-negative). }")
            st.latex(r"\text{The minimum value is }"+f"{self.obj_function.subs([(variables[values],optimized_parameters[values]) for values in range(len(optimized_parameters))])}"+r"\text{ at }"+f'x^{iter-1}'+ "="+ sp.latex(optimized_parameters) )
          else:
            st.latex(r"\text{The Hessian Matrix at}"+f'x^{iter-1}'+ "="+ sp.latex(optimized_parameters)+r"\text{is not Positive Semidefinite }")
            st.latex(r"\text{There is no minimum value}")
        elif self.option ==2:
          if np.all(np.linalg.eigvals(np.array(hessMat_at_point,dtype=float)) <= 0):
            eig_value, eig_vector = np.linalg.eig(np.array(hessMat_at_point,dtype = float))
            temp_eig_value = sp.Matrix(eig_value)
            st.latex(r"\text{The eigenvalues of the Hessian matrix at }"+f'x^{iter-1}'+ "="+ sp.latex(optimized_parameters) + r"\text{is }" +sp.latex(temp_eig_value))
            st.latex(r"\text{The Hessian Matrix at }" +f'x^{iter-1}'+ "="+ sp.latex(optimized_parameters) +r"\text{is Negative Semidefinite (it is symmetric and has all eigenvalues are non-positive). }")
            st.latex(r"\text{The maximum value is }"+f"{self.obj_function.subs([(variables[values],optimized_parameters[values]) for values in range(len(optimized_parameters))])}"+r"\text{ at }"+f'x^{iter-1}'+ "="+ sp.latex(optimized_parameters) )
          else:
            st.latex(r"\text{The Hessian Matrix at}"+f'x^{iter-1}'+ "="+ sp.latex(optimized_parameters)+r"\text{is not Negative Semidefinite }")
            st.latex(r"\text{There is no maximum value}")


  def minimize(self,f):
   
    alpha = Symbol('α')
    f = parse_expr(f)
    derivative = diff(f)
    derivative= str(derivative)
    results = solve(simplify(derivative),alpha)
    mini_val = f.subs(alpha,0)
    minima = 0 
    for i in range(len(results)):
        if  type(results[i]) == sp.core.add.Add:
          continue
        a = f.subs(alpha,results[i])
        if mini_val >= a:
            minima = results[i]
    return minima


  def GradientDescent(self):
    self.obj_function = self.obj_function.replace(" ","")
    self.obj_function = self.obj_function.replace("_","")
    self.obj_function = self.obj_function.replace("^","**")
    self.obj_function = self.obj_function.replace("[","(")
    self.obj_function = self.obj_function.replace("{","(")
    self.obj_function = self.obj_function.replace("}",")")
    self.obj_function = self.obj_function.replace("]",")")
    try:
      for i in range(len(self.obj_function)):
          if (self.obj_function[i].isnumeric() and self.obj_function[i+1].isalpha()) or (self.obj_function[i].isnumeric() and self.obj_function[i+1] =="(") or (self.obj_function[i] ==")" and (self.obj_function[i+1].isnumeric() or self.obj_function[i+1].isalpha()) ):
            self.obj_function = self.obj_function[:i+1] + "*" + self.obj_function[i+1:]
    except:
      pass
    
    variables = re.findall(r'([a-z]\d*)', self.obj_function)
    variables = list(set(variables))
    try:
      temp_var = [int(i[1:]) for i in variables]  
      for i in range(len(temp_var)):
        for j in range(i+1,len(temp_var)):
          if temp_var[i]>temp_var[j]:
            temp_var[i],temp_var[j]=temp_var[j],temp_var[i]
            variables[i],variables[j] = variables[j],variables[i]
    except:
      pass
    
    n = len(variables)
    for i in range(n):
        variables[i] = sp.symbols(variables[i])
   
    if self.option ==2:
      self.obj_function = "(-1)* (" + self.obj_function + ")"
    temp_f = self.obj_function
    self.obj_function = parse_expr(self.obj_function)
    if self.option ==1:
      st.latex(r"\text{Find the minimum of the function }"+"f("+ sp.latex(variables)+ ") = "+sp.latex(self.obj_function)+r"\text{ with initial point }x^0= "+sp.latex(self.initial_val)+ r"\text{ and the maximum number of iterations is }"+f"{int(self.max_iter)}")
    elif self.option ==2: 
      st.latex(r"\text{Find the maximum of the function }"+"f("+ sp.latex(variables)+ ") = "+sp.latex(self.obj_function)+r"\text{ with initial point }x^0= "+sp.latex(self.initial_val)+ r"\text{ and the maximum number of iterations is }"+f"{int(self.max_iter)}")
    gradient = lambda obj_function, variables: Matrix([obj_function]).jacobian(variables)
    

    gradMat = (gradient(self.obj_function, variables)).T
    st.latex(r"\text{The Gradient Matrix of f(x) is } \nabla f(x) = " + sp.latex(gradMat))
 

    gradMat_at_point = gradMat.subs([(variables[values],self.initial_val[values]) for values in range(len(self.initial_val))])
    st.latex(r"\text{The gradient of function at initial point }x^0 = "+ sp.latex(self.initial_val) + r'\text{ is }'+ r"\nabla f(x) =" + sp.latex(gradMat_at_point))
    alpha = Symbol('α')
    x = self.initial_val
    step =1
    while (np.all(np.array(gradMat_at_point)==0) == False):
        st.latex(r"\text{Iteration }"+f"{step}: ")
        # If gradient of x is different from 0, move to next step 
        xk = [(f'{x[i]} - α*{gradMat_at_point[i]}') for i in range(n)]
        xk  = sp.Matrix(xk)
        st.latex(f"x^{step} = x^{step-1} - α * "+r'\nabla f('+f'x^{step-1}) ='+sp.latex(sp.Matrix(x))+"-α*"+sp.latex(gradMat_at_point)+"="+sp.latex(xk) )
        temp_f1 = temp_f
        for i in range(n): 
            temp_f1 = temp_f1.replace(f'x{i+1}',f'(x{i+1})')
            temp_f1 = temp_f1.replace(f'x{i+1}',str(xk[i]))   
        #Find alpha_k such that alpha_k = argminf(xk - alpha * gradient)
        st.latex(f"f(x^{step}) =  {sp.latex(parse_expr(temp_f1))}")
        alpha_k = self.minimize(temp_f1)
        st.latex(r"\text{The minimizer of f(}"+f"x^{step})"+r"\text{ at } \alpha =" +f"{alpha_k}"+r"\text{ with α >=0}" )
        x = [(x[i] - alpha_k*gradMat_at_point[i]) for i in range(n)]
        step+=1
        gradMat_at_point = gradMat.subs([(variables[values],x[values]) for values in range(n)])
      
        if step ==self.max_iter:
          fx  = self.obj_function.subs([(variables[values],x[values]) for values in range(n)])
          if self.option ==1:
            st.latex(r"\text{You've reached the maximum number of iteration. The approximate minimum value is }" + f"{fx}" + r"\text{ at x = }"+ sp.latex(x))
          else: 
            st.latex(r"\text{You've reached the maximum number of iteration. The approximate maximum value is }" + f"{fx}" + r"\text{ at x = }"+ sp.latex(x))
          return

    fx  = self.obj_function.subs([(variables[values],x[values]) for values in range(n)])      
    st.latex(r"\text{The optimal value is }" + f"{fx}" + r"\text{ at x = }"+ sp.latex(x))

def TravellingSalesmanProblem(command):
  if command ==1:
    n = st.sidebar.number_input("Enter the number of nodes: ")
    n = int(n)
    S = []
    for i in range(1,n+1):
        S.append(i)
    coordinates = []
    for i in range(n):
        coordinates.append(list(float(num) for num in st.sidebar.text_input(f"Enter the coordinate of node {i+1} separated by space ").strip().split())[:n]) 
  else:
    n = 5
    st.sidebar.number_input("Enter the number of nodes: ",n)
    n = int(n)
    S = []
    for i in range(1,n+1):
        S.append(i)
    coordinates = [[1,4],[3,6],[2,5],[7,9],[5,7]]
    for i in range(n):
        st.sidebar.text_input(f"Enter the coordinate of node {i+1} separated by space ", f'{coordinates[i][0]} {coordinates[i][1]}')

  matrix = [[math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2) for j in range(n)] for i in range(n)]

  col_names = []
  row_names = []
  for i in range(n):
      col_names.append('N' + str(i+1))
      row_names.append('N' + str(i+1))  
  st.write("-------------------------------------------------------------------------")
  st.dataframe(pd.DataFrame(matrix,columns = col_names, index = row_names))

  # ُSelect the start node
  if command ==1:
    m = int(st.sidebar.number_input("Select a node to start with:  "))
  else: 
    m = 3
    st.sidebar.number_input("Select a node to start with:  ",m)
  S.remove(m)
  st.write("-------------------------------------------------------------------------")
  st.write("")
  st.latex(r"\text{Meaning of symbols: }")
  st.latex(r"\text{[a,b] means distance from node a to ending ( which is also starting) node b. }")
  st.latex(r"\text{[a][b] means distance from node a to node b.}")
  st.latex(r"\text{[a]\{[b,c]\} means distance from node a to node b to node c to the ending ( which is also starting) node.}")
  st.latex(r"\text{[a]\{(b,c)\} means the minimum distance from node a to ending ( which is also starting) node through the nodes b,c.}")

  st.write("-------------------------------------------------------------------------")
  # First Stage
  st.latex(r"\text{Stage 1 :}")
  x = list([row[m-1] for row in matrix])
  for i in range(n):
      if i != m-1:
          st.latex("["+str(i+1)+","+str(m)+"]"+" = "+str(x[i]))
          
  st.write("-------------------------------------------------------------------------")

  # (n-1)! Stage

  v =  sum([list(itertools.combinations(S, i)) for i in range(1,len(S)+1)], [])
  w = [[0 for row in range(n+1)] for col in range(n+1)]    
  D = [[0 for row in range(len(v)+1)] for col in range(n+1)]
  P = [[0 for row in range(len(v)+1)] for col in range(n+1)]
  D[0].clear()
  P[0].clear()
  for i in v:
      D[0].append(list(i))
      P[0].append(list(i))

  for i in range(n):
      for j in range(n):
          w[i+1][j+1] = matrix[i][j]

  def findsubsets(S,k):
      return set(itertools.combinations(S,k))

  # AminusJ generates A-{Vj}
  def AminusJ(A,jj,j):
      if len(list(A[jj]))>= 2:
          y = list(A[jj])
          y.remove(j)
          list(A[jj]).insert(0,j)
          return D[j][D[0].index(y)]
      else:
          return w[j][m]

      
  # AMJ is AminusJ just for st.write's stuffs
  def AMJ(A,jj,j):
      x = list(A[jj])
      x.remove(j)
      return x 


  for k in range(1,n-1):
      st.latex(r"\text{Stage } "+str(k+1)+" :")
      A = list(findsubsets(S,k))
      for jj in range(0,len(findsubsets(S,k))):
          g = []
          for i in range(1,n+1):
              g = list(A[jj])
              if i!= m and i not in g:
                  temp = []
                  minimum = math.inf
                  for j in list(A[jj]):
                      D[i][D[0].index(list(A[jj]))] = w[i][j] + AminusJ(A,jj,j)
                      if k == 1:
                          st.latex("["+str(i)+"]\{ "+str(j)+"\} = "+str(D[i][D[0].index(list(A[jj]))]))
                        
                      else:
                          st.latex("["+str(i)+"]["+str(j)+"] + "+str(j)+"\{"+str(AMJ(A,jj,j))+"\} = "+str(D[i][D[0].index(list(A[jj]))]))
                      temp.append(D[i][D[0].index(list(A[jj]))])
                      for p in temp:
                          if minimum > p:
                              minimum = p
                              P[i][D[0].index(list(A[jj]))] = j
                  D[i][D[0].index(list(A[jj]))] = minimum
                  if k != 1:
                      st.latex("=>["+str(i)+"]\{"+str(A[jj])+"\} = "+str(minimum))
                      st.write("------------------------------")

  # Last Stage    

  st.latex(r"\text{Last Stage :}")
  temp2 = []
  minimum2 = math.inf

  # Final Subset minus j
  def FMJ(v,j):
      x = list(v[len(v)-1])
      x.remove(j)
      return x
  for j in range(1,n+1):
      if j != m:
          D[m][D[0].index(list(v[len(v)-1]))] = w[m][j]+ D[j][D[0].index(FMJ(v,j))]
          st.latex("["+str(m)+"]["+str(j)+"] + "+str(j)+"\{"+str(FMJ(v,j))+"\} = "+str(D[m][D[0].index(list(v[len(v)-1]))]))
          temp2.append(D[m][D[0].index(list(v[len(v)-1]))])
          for p in temp2:
              if minimum2 > p:
                  minimum2 = p
                  P[m][D[0].index(list(v[len(v)-1]))] =  j          
  D[m][D[0].index(list(v[len(v)-1]))] = minimum2    
  minlength = D[m][D[0].index(list(v[len(v)-1]))]

  
  st.write("-------------------------------------------------------------------------")
  st.latex(r"\text{The minimum length is }"+str(minlength))
  st.latex(r"\text{The optimal path is }:")
  d = []
  r = m
  g = list(v[len(v)-1])
  for i in range(0,n-1):
      t = P[r][D[0].index(g)]
      d.append(t)
      r = t
      g.remove(t)
  d.insert(0,m)
  d.append(m)
  text = ""
  for i in range(len(d)-1):
      text += str(d[i])+"----->"
  st.latex(text+str(d[len(d)-1])) 
  a = [i[0] for i in coordinates]
  b = [i[1] for i in coordinates]
  st.set_option('deprecation.showPyplotGlobalUse', False)
  plot = plt.figure()
  plt.axis()
  G = nx.Graph()
  plt.axis()
  fig, ax = plt.subplots()
  for i in range(len(d)-1):
      G.add_edge(d[i],d[i+1])
  
  pos = dict()
  for i in range(len(d)):
      pos[d[i]] = coordinates[d[i]-1]
  nx.draw_networkx(G, pos=pos,ax = ax)
  ax.set_xlim(-1, max(a)+1)
  ax.set_ylim(0,max(b)+1)
  ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
  plt.show()
  plot = plt.show()
  st.pyplot(plot)




