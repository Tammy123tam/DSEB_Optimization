import streamlit as st
from latex2sympy2 import latex2sympy
def input_uc1( command):
    obj_function = st.sidebar.text_input("Enter f(x) = ")
    if command ==1:
        return obj_function
    elif command ==2:
        temp_obj_function = latex2sympy(obj_function)
        variables = list(temp_obj_function.free_symbols)
        
        n = len(variables)
        initial_val = list(float(num) for num in st.sidebar.text_input("Enter the list of initial values separated by space ").strip().split())[:n]
        max_iter = st.sidebar.number_input("Enter the number of max iteration: ")
        return obj_function, initial_val, max_iter
        
def input_uc2():
    obj_function = st.sidebar.text_input("Enter f(x) = ")
    temp_obj_function = latex2sympy(obj_function)
    variables = list(temp_obj_function.free_symbols)
    n = len(variables)    
    initial_val = list(float(num) for num in st.sidebar.text_input("Enter the list of initial values separated by space ").strip().split())[:n]
    max_iter = st.sidebar.number_input("Enter the number of max iteration: ")
    return obj_function, initial_val, max_iter