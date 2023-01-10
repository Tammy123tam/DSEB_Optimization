from sympy.parsing.sympy_parser import parse_expr
import sympy as sp
import streamlit as st
from latex2sympy2 import latex2sympy
import constrained_check

def gradient(f, x):
    return sp.Matrix([f]).jacobian(x)

class Inequality:
    def __init__(self, objFunction, eqConstraints, ineqConstraints, find_min):
        self.objFunction = latex2sympy(objFunction)
    
        variables = list(self.objFunction.free_symbols) 
        n = len(variables) 
        lagrange = latex2sympy(objFunction)
        
        lambda_var = []
        m = len(eqConstraints)
        for i in range(m):
            eqConstraints[i] = latex2sympy(eqConstraints[i])
            lambda_var.append(sp.symbols(f'λ_{i+1}'))
            lagrange += sp.symbols(f'λ_{i+1}') * eqConstraints[i]
                    
        mu_var = []
        p = len(ineqConstraints)
        for i in range(p):
            ineqConstraints[i] = latex2sympy(ineqConstraints[i])
            
        for i in range(p):
            mu_var.append(sp.symbols(f'μ_{i+1}'))
            lagrange += sp.symbols(f'μ_{i+1}') * ineqConstraints[i]

        self.variables = variables
        self.numbVariables = n
        self.find_min = find_min
        self.eqConstraints = eqConstraints
        self.numbEqConstraints = m
        self.ineqConstraints = ineqConstraints
        self.numbIneqConstraints = p
        self.lagrange = lagrange
        self.lagrange_var = variables + lambda_var + mu_var
        self.numLagrange_var = n + m + p
        self.lambda_var = lambda_var
        self.mu_var = mu_var
        self.gradLagrange = (gradient(self.lagrange, self.variables)).T
        self.gradConstraints = (gradient(self.eqConstraints+self.ineqConstraints, self.variables)).T

        # KKT var
        self.KKT_sol = []
        self.equality_KKT = []
        self.inequality_KKT = []

        self.opt_solution = []
        self.index = int()
        self.KKT()
        
    def KKT(self):        
        self.equality_KKT += self.eqConstraints
        self.equality_KKT += list(self.gradLagrange.T)
        self.inequality_KKT += self.ineqConstraints
        
        st.latex(r'\text{The Lagrange function is: } \mathfrak{L} =' + sp.latex(self.lagrange))
        st.latex(r'\text{The KKT condition is:}')

        print_KKT = r'\left\{\begin{matrix}'
        for i in range(len(list(self.gradLagrange.T))):
            print_KKT += sp.latex(list(self.gradLagrange.T)[i]) + r'= 0 \\ '
        for i in range(self.numbEqConstraints):
            print_KKT += sp.latex(self.eqConstraints[i]) + r'= 0 \\ '
        for i in range(self.numbIneqConstraints):
            self.equality_KKT.append(parse_expr(f'u{i+1}') * self.ineqConstraints[i])
            self.inequality_KKT.append(parse_expr(f'-u{i+1}'))
            print_KKT += r'u_' + str(i+1) + r'\geq 0 ;& ' 
            print_KKT += r'g_' + str(i+1) + '=' + sp.latex(self.ineqConstraints[i]) + r'\leq 0 ;& '
            print_KKT += r'u_' + str(i+1) + '*(' + sp.latex(self.ineqConstraints[i]) + r')= 0 \\ '
        print_KKT += r'\end{matrix}\right.'
        st.latex(print_KKT)
    
        KKT_sol_temp = sp.solve(self.equality_KKT, self.lagrange_var, dict=True)
        KKT_sol = []
        for i in range(len(KKT_sol_temp)):
            for j in range(self.numbIneqConstraints):
                if KKT_sol_temp[i][self.mu_var[j]] >= 0 and \
                    self.ineqConstraints[j].subs([(self.variables[k], KKT_sol_temp[i][self.variables[k]])\
                         for k in range(len(self.variables))]) <= 0 and\
                            KKT_sol_temp[i] not in KKT_sol:
                    KKT_sol.append(KKT_sol_temp[i])
                else:
                    continue

        if len(KKT_sol) == 0:
            st.latex(r'\Rightarrow \text{KKT condition has no solution}')
        else:
            st.latex(r'\Rightarrow \text{The solutions of KKT condition is:}')
            print_KKTsol = r'\left\{\begin{matrix}'
            for i in range(len(KKT_sol)):
                for key in KKT_sol[i].keys():
                    print_KKTsol += sp.latex(key) + '=' + sp.latex(KKT_sol[i][key]) + r'&'
                print_KKTsol += r'\\'
            print_KKTsol += r'\end{matrix}\right.'
            st.latex(print_KKTsol)

            self.KKT_sol += KKT_sol

            for i in range(len(KKT_sol)):
                if len(KKT_sol) > 1:
                    st.subheader(str(i+1) + '.')
                st.latex(r"\textbf{For KKT's solution:}" + sp.latex(self.KKT_sol[i]))
                self.index = i
                self.interior(self.index)
            
    def interior(self, i):
        count = 0
        for j in range(len(self.ineqConstraints)):
            if self.ineqConstraints[j].subs([(self.variables[k], self.KKT_sol[i][self.variables[k]])\
                 for k in range(len(self.variables))]) < 0:
                continue
            else:
                count += 1                
        if count == len(self.ineqConstraints):
            for j in range(len(self.ineqConstraints)):
                st.latex(r"\text{Substitute the solution to inequality constraints:}")
                st.latex(sp.latex(self.ineqConstraints[j]) + "= 0")
            st.latex(r"\Rightarrow" + sp.latex(self.KKT_sol[i]) + r"\text{is an interior point satisfying KKT condition.}")
            st.latex(r"\text{Therefore, }" + sp.latex(self.KKT_sol[i]) + r"\text{ is a optimal solution}")
            self.SOC(self.index)
        else:
            self.regular(self.index)
     
    def regular(self, i):
        J = self.eqConstraints.copy()
        for j in range(len(self.ineqConstraints)):
            if int(self.ineqConstraints[j].subs([(self.lagrange_var[k], self.KKT_sol[i][self.lagrange_var[k]])\
                 for k in range(len(self.lagrange_var))])) == 0:
                J.append(self.ineqConstraints[j])
        gradJ = (gradient(J, self.variables)).T
        for k in range(self.numbVariables):
            if self.variables[k] in self.KKT_sol[i].keys():
                gradJ = gradJ.subs(self.variables[k], self.KKT_sol[i][self.variables[k]]) 
        
        st.latex(r'\textbf{Check the regularity conditions:}')
        a = []
        for i in range(len(J)):
            a.append(sp.symbols(f'a_{i+1}'))
        a = sp.Matrix(a)
        a_sol = sp.solve(gradJ*a, a, dict=True)
        for i in range(len(J)):
            st.latex(sp.latex(gradJ) + '*' + sp.latex(a) + '= 0')
        if len(a_sol) == 1:
            st.latex(r'\text{There is only one solution:}' + sp.latex(a) + r'= [0]')
            st.latex(r'\Rightarrow' + sp.latex(self.KKT_sol[i])  + r'\text{is a regular solution}')
            self.SOC(self.index)
        else:
            st.latex(r'\text{This function has nontrivial solutions: }' + sp.latex(a))
            st.latex(f'\Rightarrow' + sp.latex(self.KKT_sol[i]) + r'\text{ is not a regular solution nor optimal solution}')
    
    def SOC(self, i):
        st.latex(r'\textbf{Second-order necessary condition: }')
        Lxx = (gradient((gradient(self.lagrange, self.variables)), self.variables)).T
        Lxx_at_point = Lxx.subs([(self.lagrange_var[k], self.KKT_sol[i][self.lagrange_var[k]])\
                 for k in range(len(self.lagrange_var))])
        st.latex(r"\mathfrak{L}_{XX'} = f_{XX'} + \sum_{i=1}^m \lambda_i g^i_{XX'} = " \
            + sp.latex(Lxx) + " = " + sp.latex(Lxx_at_point))

        sol = constrained_check.SOC(Lxx_at_point, self.KKT_sol[i], self.find_min)
        if sol != None:
            self.opt_solution.append(sol)

        if i == len(self.KKT_sol) - 1:
            self.conclusion()
    
    def conclusion(self):
        st.latex(sp.latex(self.opt_solution))
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
                    print_sol += sp.latex(key) + ' = ' + sp.latex(self.opt_solution[i][key]) + ' & '
                print_sol += r' \\ '
                if i == len(self.opt_solution) - 1:
                    print_sol += r'\end{matrix}'
            st.latex(print_sol)