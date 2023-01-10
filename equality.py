from sympy.parsing.sympy_parser import parse_expr
import sympy as sp
import streamlit as st
from latex2sympy2 import latex2sympy
import constrained_check

def gradient(f, x):
    return sp.Matrix([f]).jacobian(x)

class Equality:
    def __init__(self, objFunction, constraints, find_min):            
        self.objFunction = latex2sympy(objFunction)
        variables = list(self.objFunction.free_symbols)

        lagrange = latex2sympy(objFunction)
        lambda_var = []
        m = len(constraints)
        for i in range(m):
            constraints[i] = latex2sympy(constraints[i])
            lambda_var.append(sp.symbols(f'λ_{i+1}'))
            lagrange += sp.symbols(f'λ_{i+1}') * constraints[i]
        
        self.variables = variables
        self.numbVariables = len(self.variables)
        self.find_min = find_min
        self.numbConstraints = m
        self.lagrange = lagrange
        self.constraints = constraints
        self.lagrange_var = variables + lambda_var
        
        self.gradLagrange = (gradient(self.lagrange, self.lagrange_var)).T
        self.gradConstraints = gradient(constraints, variables)

        self.la_solution = []
        self.opt_solution = []

        self.showEq()       
        
    def showEq(self):
        st.latex(r'\text{Object funtion: f = }' + sp.latex(self.objFunction))
        st.latex(r'\text{Lagrange funtion: } \mathfrak{L} = ' + sp.latex(self.lagrange))
        self.FONC()
    
    def FONC(self):
        st.latex(r'\textbf{First-order necessary conditions:}')
        print_gradL = r'\left\{\begin{matrix}'
        for j in range(len(self.lagrange_var)):
            print_gradL += r'\frac{\partial \mathfrak{L}}{\partial ' + sp.latex(self.lagrange_var[j]) + r'} =' + sp.latex(self.gradLagrange[j]) + r' = 0\\ \\'
            if j == len(self.lagrange_var) - 1:
                print_gradL += r'\end{matrix}\right.'
        st.latex(print_gradL)
            
        gradLagrange_sol = sp.solve(self.gradLagrange, self.lagrange_var, dict=True)
        la_solution = []
        for i in range(len(gradLagrange_sol)):
            count = 0
            for j in range(len(self.lagrange_var)):
                if self.lagrange_var[j] not in gradLagrange_sol[i].keys():
                    gradLagrange_sol[i][self.lagrange_var[j]] = self.lagrange_var[j]
                if 'I' not in str(gradLagrange_sol[i][self.lagrange_var[j]]):
                    count += 1          
            if count == len(self.lagrange_var) and gradLagrange_sol[i] not in la_solution:
                la_solution.append(gradLagrange_sol[i])
        self.la_solution = la_solution

        if len(self.la_solution) < 1:
            st.latex(r'\Rightarrow \textbf{This Lagrange function does not have any solution}')
        else:
            if len(self.la_solution) == 1:
                st.latex(r'\textbf{The solution of Lagrange function is:}')
                print_optsol = r'\begin{matrix} '
                for key in self.la_solution[0].keys():
                    print_optsol += sp.latex(key) + '=' + sp.latex(self.la_solution[0][key]) + r' & '
                print_optsol += r'\end{matrix}'
                st.latex(print_optsol)

            else:
                st.latex(r'\textbf{The solutions of Lagrange function are:}')
                print_optsol = r'\left\{\begin{matrix} '
                for i in range(len(self.la_solution)):
                    for key in self.la_solution[i].keys():
                        print_optsol += sp.latex(key) + '=' + sp.latex(self.la_solution[i][key]) + r'& '
                    print_optsol += r' \\ '
                    if i == len(self.la_solution) - 1:
                        print_optsol += r'\end{matrix}\right.'
                st.latex(print_optsol)

            for i in range(len(self.la_solution)):
                if len(self.la_solution) > 1:
                    st.subheader(str(i+1) + '.')
                st.latex(r'\text{For: }' + sp.latex(la_solution[i]))
                self.regular(i)
                
    def regular(self, i):
        st.latex(r'\textbf{Check the regular condition: }')
        a = []
        for j in range(1, self.numbConstraints+1):
            a.append(parse_expr(f'a{j}'))
        a = sp.Matrix(a)
        gradConstraint_at_point = self.gradConstraints.subs([(self.variables[k], self.la_solution[i][self.variables[k]])\
                 for k in range(len(self.variables))])
        st.latex(r'\text{Dg(x) = }' + sp.latex(self.gradConstraints) + '=' + sp.latex(gradConstraint_at_point)) 

        if len(sp.solve(gradConstraint_at_point.T*a, a, dict=True)) == 1:
            st.latex(r'\Rightarrow' + r'\text{Rank Dg(x) = }' + str(len(self.constraints)))
            st.latex(r'\Rightarrow' + sp.latex(self.la_solution[i]) + r'\text{ is a regular solution.}')
            self.SOC(i)
        else:
            st.latex(r'\Rightarrow' + sp.latex(self.la_solution[i]) + r'\text{ is not a regular solution.}')
            st.latex(r"\textbf{Thus, this problem can not be solved by using Lagrange function}")

    def SOC(self, i):
        st.latex(r'\textbf{Second-order necessary condition: }')
        Lxx = gradient((gradient(self.lagrange, self.variables)), self.variables)
        Lxx_at_point = Lxx.subs([(self.lagrange_var[k], self.la_solution[i][self.lagrange_var[k]])\
                 for k in range(len(self.lagrange_var))])
        st.latex(r"\mathfrak{L}_{XX'} = f_{XX'} + \sum_{i=1}^m \lambda_i g^i_{XX'} = " \
            + sp.latex(Lxx) + " = " + sp.latex(Lxx_at_point))

        sol = constrained_check.SOC(Lxx_at_point, self.la_solution[i], self.find_min)
        if sol != None:
            self.opt_solution.append(sol)
        
        if i == len(self.la_solution) - 1:
            self.conclusion()
    
    def conclusion(self):
        if len(self.opt_solution) == 0:
            if self.find_min == True:
                st.latex(r'\textbf{Thus, there is no local minimum for problem.}')
            else:
                st.latex(r'\textbf{Thus, there is no local maximum for problem.}')
        else:
            if self.find_min == True:
                st.latex(r'\textbf{Thus, local minimum of problem:}')
            else:
                st.latex(r'\textbf{Thus, local maximum of problem:}')
            print_sol = r'\begin{matrix} '
            for i in range(len(self.opt_solution)):
                for key in self.variables:
                        print_sol += sp.latex(key) + '=' + sp.latex(self.opt_solution[i][key]) + r'& '
                print_sol += r' \\ '
                if i == len(self.opt_solution) - 1:
                    print_sol += r'\end{matrix}'
            st.latex(print_sol)