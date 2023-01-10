import streamlit as st
from sympy.abc import *
from unconstrained_application import *
from simplex import *
from theory import *
from input import input_uc1, input_uc2
import equality
import inequality

st.set_page_config(page_title = 'DSEB Optimization', layout = 'wide')

intro = st.container()
unconstrained = st.container()
constrained = st.container()
app = st.container()
option1= st.container()
option2 = st.container()
option3 = st.container()
option4 = st.container()
members = st.container()
tam,ly,thao,dung,linh,thien = st.columns(6)

add_selectbox = st.sidebar.selectbox("Which part do you want to practice? ", ("Home Page",\
    "Unconstrained Optimization", "Constrained Optimization", "Application of Optimization" ))

if add_selectbox == "Home Page":
    with intro:   
        st.image("image//des.png")
        st.title("WELCOME TO DSEB OPTIMIZATION ♡")
        st.write("DSEB Optimization is a step-by-step intructions for solving unconstrained, \
            constrained problems due to the happy, undepressing experience studying this course.")
    with unconstrained:
        st.header("1. Unconstrained Optimization")
        st.caption("Click on 'Unconstrained Optimization' in the left column.")
        st.write(r''' - Global Optimization ''')
        st.write(r''' - Gradient method (The steepest descent algorithm)''')
        st.write(r''' - Newton - Raphson method ''')
    with constrained:
        st.header("2. Constrained Optimization")
        st.caption("Click on 'Constrained Optimization' in the left column.")
        st.write(r''' - Linear Programming Problem: Using Simplex Method ''')
        st.write(r''' - Non-Linear Programming Problem''')
        st.caption(r'''1. Under equality constraints''')
        st.caption(r'''2. Under equality and inequality constraints''')
    with app:
        st.header("3. Application of Optimization")
        st.caption("Click on 'Application of Optimization' in the left column")
        st.write(r''' - Traveling Salesman Problem: Dynamic approach ''')
        
    with members:
        st.header("About us ") 
        st.markdown("**We are building an interesting application. We are depressed because of Optimization,\
             but you won't!**")
    with tam:
        st.image("image/tam.jpg")
        st.markdown("**Trịnh Tâm**")
    with ly:
        st.image("image/ly.jpg")
        st.markdown("**Cẩm Ly**")
    with thao:
        st.image("image/thao.jpg")
        st.markdown("**Nguyễn Thảo**")
    with linh:
        st.image("image/linh.jpg")
        st.markdown("**Thùy Linh**")
    with dung:
        st.image("image/dung.jpg")
        st.markdown("**Mai Dung**")
    with thien:
        st.image("image/thien.jpg")
        st.markdown("**Ngọc Thiện**")

    # Tạo ra hộp chứa thông tin: 
    st.info("♥ Do you like this app? ")
    if st.button('Yes'):
        st.balloons()
        st.write("Thank you for your feedback!")
    elif st.button('No'):
        st.write("Thank you so much for your feedback. Your feedbacks will help us to improve and develop\
             DSEB Optimization further.")

if add_selectbox == "Unconstrained Optimization":
    st.image("image//thanks.png")
    with option1: 
        st.title("Welcome to Unconstrained Optimization Problems ♡")
        option_un_opti = st.sidebar.radio("Choose method: ", ["Without Initial Value", "With Initial Value"])
        
        if option_un_opti == "Without Initial Value":

            option_un_opti_1 = st.sidebar.radio("Without Initial Value, which part do you want to learn? ",\
                ("Theory", "Exercise"))
            if option_un_opti_1 == "Theory" :
                st.subheader(r'''Without initial value - Part 1: Theory''')
                Theory_Unconstrained_optimization_problems()
                Theory_convex()
            if  option_un_opti_1 == "Exercise":
                st.subheader(r'''Without initial value - Part 2: Exercise''')
                st.latex(r'''\text{- Without Initial Value, solving unconstrained optimization problems}''')
                max_min = st.sidebar.radio("Choose option: ", ["Minimize","Maximize"])
                if max_min == "Minimize":
                    option = 1
                else:
                    option = 2
                try:
                    obj_function = "2*x_1^2 + (x_2-x_1)^2"
                    st.sidebar.text_input("Enter f(x) = ", obj_function)
                    c = Unconstrained_Opti(obj_function, option)
                    c.Un_op_without()
                except:
                    pass
            
        if option_un_opti == "With Initial Value":
            with option2:
                option_un_opti1 = st.sidebar.radio("Choose algorithm: ",\
                    ["Gradient Descent Method", "Newton Raphson Method"])
                if option_un_opti1 == 'Gradient Descent Method':
                    option_un_opti_1 = st.sidebar.radio("Without Initial Value, which part do you want to learn? ", ("Theory","Exercise"))
                    if option_un_opti_1 == "Theory" :
                        st.subheader(r'''With initial value - Gradient Descent Method - Part 1: Theory''')
                        st.write("Using Gradient Descent Method to solve unconstrained optimization problems")
                        Theory_Gradient()
                    if  option_un_opti_1 == "Exercise":
                        st.subheader(r'''With initial value - Gradient Descent Method - Part 2: Exercise''')
                        st.write("Using Gradient Descent Method to solve unconstrained optimization problems")
                        max_min1 = st.sidebar.radio("Choose option: ", ["Minimize","Maximize"])

                        if max_min1 == "Minimize":
                            option = 1
                        else:
                            option = 2
                        try: 
                            obj_function = "x_1^2 + 2(x_2- x_1)^2"
                            st.sidebar.text_input("Enter f(x) = ", obj_function)
                            st.sidebar.text_input("Enter the list of initial values separated by space", "6 6")
                            st.sidebar.text_input("Enter the number of max iteration:", "5")
                            temp_obj_function = latex2sympy(obj_function)
                            variables = list(temp_obj_function.free_symbols)
                            n = len(variables)    
                            initial_val = list(float(num) for num in "6 6".strip().split())[:n]
                            max_iter = 5
                            a = Unconstrained_Opti1(obj_function, initial_val, max_iter,option)
                            a.GradientDescent()
                        except:
                            pass

                if option_un_opti1 == 'Newton Raphson Method':
                    option_un_opti_new = st.sidebar.radio("For Newton-Raphson method, please choose: ",["Theory","Exercise"])
                    if option_un_opti_new == "Theory":
                        st.subheader(r'''With initial value - Newton Raphson Method - Part 1: Theory''')
                        st.write("Newton's method is a general approach for solving systems of non-linear equations.\
                            Newton's method can conceptually be seen as a steepest descent method, and we will show how it can be applied for convex optimization.")
                        Theory_Newton ()
                    if option_un_opti_new == "Exercise":
                        st.subheader(r'''With initial value - Newton Raphson Method - Part 2: Exercise''')
                        st.write("Newton's method is a general approach for solving systems of non-linear equations.\
                            Newton's method can conceptually be seen as a steepest descent method, and we will show how it can be applied for convex optimization.")
                        max_min2 = st.sidebar.radio("Choose option: ", ["Minimize","Maximize"])
                        if max_min2 == "Minimize":
                            option = 1
                        else:
                            option = 2
                        try:
                            obj_function = "x_1^2 + 2(x_2- x_1)^2"
                            st.sidebar.text_input("Enter f(x) = ", obj_function)
                            st.sidebar.text_input("Enter the list of initial values separated by space", "6 6")
                            st.sidebar.text_input("Enter the number of max iteration:", "5")
                            temp_obj_function = latex2sympy(obj_function)
                            variables = list(temp_obj_function.free_symbols)
                            n = len(variables)    
                            initial_val = list(float(num) for num in "6 6".strip().split())[:n]
                            max_iter = 5
                            b = Unconstrained_Opti1(obj_function, initial_val, max_iter,option)
                            b.Newton_Optimizer_UN()
                        except:
                            pass


if add_selectbox == "Constrained Optimization":
    st.image("image//thanks.png")
    with option3:
        st.title("Welcome to Constrained Optimization Problems ♡")
        option_con_opti = st.sidebar.radio("Choose method: ",["Linear Programming Problem","Non Linear Programming Problem"])
        if option_con_opti =="Linear Programming Problem":
            option_con_opti_sim = st.sidebar.radio("Simplex method used to solve Linear Programming Problem",["Theory","Exercise"])
            if option_con_opti_sim == "Theory":
                st.subheader("Linear Programming Problem (using Simplex Method) - Part 1: Theory")
                st.write("Simplex method is an approach to solving linear programming models by hand using \
                    slack variables, tableaus, and pivot variables as a means to finding the optimal solution\
                         of an optimization problem. Simplex tableau is used to perform row operations on the\
                             linear programming model as well as for checking optimality.")
                Theory_Simplex_method()
            if option_con_opti_sim == "Exercise":
                st.subheader("Linear Programming Problem (using Simplex Method) - Part 2: Exercise")
                st.write("Simplex method is an approach to solving linear programming models by hand using \
                    slack variables, tableaus, and pivot variables as a means to finding the optimal solution\
                         of an optimization problem. Simplex tableau is used to perform row operations on the\
                             linear programming model as well as for checking optimality.")                
                st.latex(r'\text{Solve linear programming problem:}')
                st.latex(r'''\begin{aligned}& \boldsymbol{z} = f(x)=\langle\boldsymbol{c}, \boldsymbol{x}\rangle \rightarrow \min \\&\
                     \begin{cases}\sum_{j=1}^n A_j x_j=\boldsymbol{b} & \left(b \in \mathbb{R}^m\right) \\x \geq 0 & \left(x \in \mathbb{R}^n\right)\end{cases}\end{aligned}''')
                st.latex(r'\text{Notes on input: Enter the full function of the coefficients in the form:}')
                st.latex('a*x_1 + b*x_2 .... ')
                st.latex(r"\text{If you want to find the maximize of the objective function, you can multiply -1 to the objective function}")
                st.latex(r'\text{Guide for entering input:}')
                st.latex(r'''\text{Minimize }f(x) = 2*x_1 + 5*x_2 + 4*x_3 + x_4 - 5*x_5
                \\s.t\left\{\begin{matrix}
                x_1 + 2x_2 + 4x_3 + 0x_4 - 3x_5 = 152 \\ 
                20x_1 + 4x_2 + 2x_3 + x_4 + 3x_5 >= 60 \\ 
                30x_1 + 3x_2 + 0x_3 + 0x_4 + x_5 <= 36
                \end{matrix}\right.''')
                st.subheader('Your case')
                try:
                    test1()
                except:
                    pass

        if option_con_opti =="Non Linear Programming Problem":
            with option4:
                option_con_opti1 = st.sidebar.radio("Choose type of non linear programming problem: ", \
                    ["Under equality constraints", "Under equality and unequality constraints"])
                if option_con_opti1 == "Under equality constraints":
                    option_con_opti_non_lag = st.sidebar.radio("With equation: ",["Theory","Exercise"])
                    if option_con_opti_non_lag == "Theory":
                        st.subheader("Non-linear Programming Problem - Part 1: Theory")
                        st.write("Lagrange functions are the basis of many of the more successful methods \
                            for non-linear constraints in optimization calculations. Sometimes they are used \
                                in conjunction with linear approximations to the constraints and sometimes \
                                    penalty terms are included to allow the use of algorithms for unconstrained \
                                        optimization")

                        Theory_Optimization_under_equality_constraints()
                    if option_con_opti_non_lag == "Exercise":
                        st.subheader("Non-linear Programming Problem - Part 2: Exercise")
                        st.write("Lagrange functions are the basis of many of the more successful methods \
                            for non-linear constraints in optimization calculations. Sometimes they are used \
                                in conjunction with linear approximations to the constraints and sometimes \
                                    penalty terms are included to allow the use of algorithms for unconstrained \
                                        optimization")
                      
                        option = st.sidebar.radio("Choose option: ", ["Minimize","Maximize"])
                        if option == "Minimize":
                            find_min = True
                        elif option == "Maximize":
                            find_min = False

                        try:
                            objFunction = "x_1^2 + x_2^2 "
                            st.sidebar.text_input("Enter object function (f) ",objFunction)
                            constraints = ['x_1 + x_2 - 2']
                            m = 1
                            st.sidebar.text_input('Number of equality constrained: ',str(m))
                            for i in range(int(m)):
                                st.sidebar.text_input(f'Constraint g{i+1} = ',constraints[i])
                            equality.Equality(objFunction, constraints, find_min)
                        except:
                            pass

                if option_con_opti1 == "Under equality and unequality constraints":
                    option_con_opti_non_2 = st.sidebar.radio("With both equation and inequality", ["Theory","Exercise"])
                    if option_con_opti_non_2 == "Theory":
                        st.subheader("Non-linear Programming Problem (using KKT conditions) - Part 1: Theory")
                        st.write("In mathematical optimisation, the Karush - Kuhn - Tucker (KKT) conditions, \
                            also known as the Kuhn - Tucker conditions, are first derivative tests for a solution \
                                in nonlinear programming to be optimal, provided that some regularity conditions are \
                                    satisfied.")
                        Theory_Optimization_under_inequality_constraints()
                    if option_con_opti_non_2 == "Exercise":
                        st.subheader("Non-linear Programming Problem (using KKT conditions) - Part 2: Exercise")
                        st.write("In mathematical optimisation, the Karush - Kuhn - Tucker (KKT) conditions, \
                            also known as the Kuhn - Tucker conditions, are first derivative tests for a solution \
                                in nonlinear programming to be optimal, provided that some regularity conditions are \
                                    satisfied.")
                        option = st.sidebar.radio("Choose option: ", ["Minimize", "Maximize"])
                        if option == "Minimize":
                            find_min = True
                        else:
                            find_min = False

                        try:
                            objFunction = 'x_1^2 + 4*x_2^2'
                            st.sidebar.text_input("Enter object function (f) ",objFunction)
                            eqConstraints = ['x_1 + 2*x_2 -2 ']
                            ineqConstraints = ['-x_1^2-2*x_2^2+4 ']
                            with st.sidebar:
                                st.write("Form of inequality constraints: ")
                                st.latex("h_i = 0")
                            m = 1
                            st.sidebar.text_input('Number of equality constrained: ',str(m))
                            for i in range(int(m)):
                                st.sidebar.text_input(f'Equality constraint h{i+1} = ',eqConstraints[i])

                            with st.sidebar:
                                st.write("Form of inequality constraints: ")
                                st.latex("g_i <= 0")
                            p = 1
                            st.sidebar.text_input('Number of inequality constrained: ',str(p))
                            for i in range(int(p)):
                                st.sidebar.text_input(f'Inequality constraint g{i+1} = ',ineqConstraints[i])
                           

                            inequality.Inequality(objFunction, eqConstraints, ineqConstraints, find_min)
                        except:
                            pass                        

if add_selectbox =="Application of Optimization":
    st.image("image//thanks.png")
    with option4:
        st.title(r'''Welcome to Traveling Salesman Problem ♡''')
        st.write("The traveling salesman problem (TSP) is an algorithmic problem tasked with finding the shortest \
            route between a set of points and locations that must be visited.}\\\text{ In the problem statement, \
                the points are the cities a salesperson might visit.")
        option_app = st.sidebar.radio("Choose options:",["Theory","Exercise"])
        if option_app == "Theory":
            st.header("Algorithm for Traveling salesman problem - Part 1: Theory")
            Theory_Traveling_salesman_problem ()
        if option_app == "Exercise":
            st.header("Algorithm for Traveling salesman problem - Part 2: Exercise")
            try:
                TravellingSalesmanProblem(2)
            except:
                pass


if add_selectbox == "Home Page":
    pass
else:
    with st.sidebar:
        st.markdown("TIPS TO INPUT")
        st.write("For example, we have: ")
        st.latex("x_{1}^2 +2x_{2}+ 6")
        st.write("The format input: x_1^2 + 2*x_2 + 6")
        st.write("To enter the coordinate of node separated by space (In Application of Optimization): \
            We enter two numbers and separate them by a space. ")

