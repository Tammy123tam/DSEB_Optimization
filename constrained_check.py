import streamlit as st
import sympy as sp

def SOC(Lxx_at_point, solution, find_min):
    # Min
        if find_min == True:
            if Lxx_at_point.is_positive_semidefinite == True or (Lxx_at_point.is_positive_semidefinite == False and Lxx_at_point.is_negative_semidefinite == False):
                st.latex(r"\mathfrak{L}_{XX'} = " + sp.latex(Lxx_at_point) + r'\text{is positive semidefine}')
                st.latex(r'\text{Therefore, }' + sp.latex(solution) + r'\text{ satisfies the SONC}')

                if Lxx_at_point.is_positive_definite == True or (Lxx_at_point.is_positive_definite == False and Lxx_at_point.is_negative_definite == False):
                    st.latex(r'\textbf{Second-order sufficient condition: }')
                    st.latex(r"\mathfrak{L}_{XX'} = " + sp.latex(Lxx_at_point) + r'\text{is positive define}')
                    st.latex(r'\text{Therefore, }' + sp.latex(solution) + r'\text{ satisfies the SOSC}')
                    return solution
                else:
                    st.latex(r"\mathfrak{L}_{XX'} = " + sp.latex(Lxx_at_point) + r'\text{is not positive define}')
                    st.latex(r'\text{Therefore, }' + sp.latex(solution) + r'\text{ does not satisfy the SOSC}')
            else:
                st.latex(r"\mathfrak{L}_{XX'} = " + sp.latex(Lxx_at_point) + r'\text{is not positive semidefine}')
                st.latex(r'\text{Therefore, }' + sp.latex(solution) + r'\text{ does not satisfy the SONC}')
        
        # Max
        if find_min == False:
            if Lxx_at_point.is_negative_semidefinite == True or (Lxx_at_point.is_positive_semidefinite == False and Lxx_at_point.is_negative_semidefinite == False):
                st.latex(r"\mathfrak{L}_{XX'} = " + sp.latex(Lxx_at_point) + r'\text{is negative semidefine}')
                st.latex(r'\text{Therefore, }' + sp.latex(solution) + r'\text{ satisfies the SONC}')

                if Lxx_at_point.is_negative_definite == True or (Lxx_at_point.is_positive_definite == False and Lxx_at_point.is_negative_definite == False):
                    st.latex(r'\textbf{Second-order sufficient condition: }')
                    st.latex(r"\mathfrak{L}_{XX'} = " + sp.latex(Lxx_at_point) + r'\text{is negative define}')
                    st.latex(r'\text{Therefore, }' + sp.latex(solution) + r'\text{ satisfies the SOSC}')
                    return solution
                else:
                    st.latex(r"\mathfrak{L}_{XX'} = " + sp.latex(Lxx_at_point) + r'\text{is not negative define}')
                    st.latex(r'\text{Therefore, }' + sp.latex(solution) + r'\text{ does not satisfy the SOSC}')
            else:
                st.latex(r"\mathfrak{L}_{XX'} = " + sp.latex(Lxx_at_point) + r'\text{is not negative semidefine}')
                st.latex(r'\text{Therefore, }' + sp.latex(solution) + r'\text{ does not satisfy the SONC}')
