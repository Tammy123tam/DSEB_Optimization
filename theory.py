import streamlit as st

def Theory_Gradient():
    st.subheader("The steepest descent algorithm")
    col1, col2 = st.columns([1,7])
    with col1:
        st.latex(r'''\text{This is a gradient algorithm where step size } \alpha_{k}\text{ is chosen to minimize }\phi_{k}(\alpha)=f\left(\mathbf{x}^{k}-\alpha \nabla f\left(\mathbf{x}^{k}\right)\right).''')
        st.latex(r'''\bullet\textbf{ Step 1:}\text{ Let }\mathbf{x}^{0}\text{ be a starting point.}''')
        st.latex(r'''\bullet\textbf{ Step 2:}\text{Assign k := 0}''')
        st.latex(r'''\bullet\textbf{ Step 3:}\text{ Find }\nabla f\left(\mathbf{x}^{k}\right).\text{ If }\nabla f\left(\mathbf{x}^{k}\right)=0,\text{ then go to }7^{\text {th }}\text{ Step, otherwise go to next step.}''')
        st.latex(r'''\bullet\textbf{ Step 4:}\text{ Find step size }\alpha_{k} : \alpha_{k}=\arg \min _{\alpha \geq 0} f\left(\mathbf{x}^{k}-\alpha \nabla f\left(\mathbf{x}^{k}\right)\right.''')
        st.latex(r'''\bullet\textbf{ Step 5:}\text{ Set }\mathbf{x}^{k+1}=\mathbf{x}^{k}-\alpha_{k} \nabla f\left(\mathbf{x}^{k}\right)''')
        st.latex(r'''\bullet\textbf{ Step 6:}\text{ Assign }k:=k+1\text{ and go back }3^{\text {rd }}\text{ Step}''')
        st.latex(r'''\bullet\textbf{ Step 7:}\text{ Stop the algorithm and conclude that }\mathbf{x}^{k}\text{ is an optimal solution.}''')

def Theory_Traveling_salesman_problem ():
    col1, col2 = st.columns([1,50])
    with col1:
        st.latex(r'''\textbf{Step 1:}''')
        st.latex(r'''\text{Let }d[i, j]\text{ indicates the distance between cities i and j. Function }C[x, V-\{x\}]\text{] is the length of the path starting from city }x .''')
        st.latex(r''' \text {V is the set of cities/vertices in given graph.}''')
        st.latex(r'''\text{The aim of TSP is to minimize the length function.}''')
        st.latex(r'''\textbf{Step 2:}''')
        st.latex(r'''\text{Assume that graph contains n vertices V1, V2, ..., Vn.}''')
        st.latex(r'''\text{TSP finds a path covering all vertices exactly once, and the same time it tries to minimize the overall traveling distance.}''')
        st.latex(r'''\textbf{Step 3:}''')
        st.latex(r'''\text{Mathematical formula to find minimum distance is stated below:}''')
        st.latex(r'''C(i, V)=\min \{d[i, j]+C(j, V-\{j\})\}, j \in V\text{ and }i \notin V.''')
        st.latex(r'''\text{TSP problem possesses the principle of optimality, i.e. for d[V1, Vn] to be minimum, any intermediate path (Vi, Vj) must be minimum.}''')

def Theory_Optimization_under_equality_constraints():
    st.subheader("Optimization under equality constraints")
    col1, col2 = st.columns([1,50])
    with col1:
        st.latex(r'''Find: \mathbf{x}^*=\left(x_1^*, \ldots, x_n^*\right)\text{ that minimize } f\left(x_1, \ldots, x_n\right)\text{ subject to}''')
        st.latex(r'''\begin{aligned} &g^1\left(x_1, \ldots, x_n\right)=0\quad (1)\\ &\vdots \\ &g^m\left(x_1, \ldots, x_n\right)=0,\quad m<n\end{aligned} ''')
        st.latex(r'''Denote: ''')
        st.latex(r'''\text{ f : objective function.}''')
        st.latex(r'''g^i(i=1, \ldots, m):\text{Constrained functions, m < n.}''')
        st.latex(r'''\text{A feasible point }\mathbf{x}^*\text{ is said to be a regular point of the constraints if the gradient vectors }\nabla g^1\left(\mathbf{x}^*\right), \ldots, \nabla g^m\left(\mathbf{x}^*\right)\text{ are linearly independent:}''')
    st.subheader("1. FIRST - ORDER NECESSARY CONDITIONS")
    col1, col2 = st.columns([1,50])
    with col1:
        st.latex(r'''\textbf{Lagrangean :}''')
        st.latex(r'''\mathfrak{L}\left(\lambda_1, \ldots, \lambda_m, x_1, \ldots, x_n\right)=f\left(x_1, \ldots, x_n\right)+\sum_{i=1}^m \lambda_i \cdot g^i\left(x_1, \ldots, x_n\right) \lambda_1, \ldots, \lambda_m : \text{ Lagrange multiplier (2).}''')
        st.latex(r'''\textbf{Vector form:}''')
        st.latex(r'''\begin{aligned}&\mathfrak{L}(\boldsymbol{\lambda},\mathbf{x})=f(\mathbf{x})+\boldsymbol{\lambda}^T \mathbf{g}(\mathbf{x})\quad(3)\\ \\ &\mathbf{x}=\left(x_1, x_2, \ldots, x_n\right)^T \\ &\boldsymbol{\lambda}=\left(\lambda_1, \ldots, \lambda_m\right)^T \\ &\mathbf{g}(\mathbf{x})=\left(g^1\left(x_1, x_2, \ldots, x_n\right), \ldots, g^m\left(x_1, x_2, \ldots, x_n\right)\right)^T \end{aligned}''')
        st.latex(r'''****\textbf{THEOREM 1}****''')
        st.latex(r'''\text{Let }\mathbf{x}^*\text{ be an optimal solution of problem (1). Assume that }\mathbf{x}^*\text{ is a regular point. Then there must exist an unique vector }\boldsymbol{\lambda}^* \in \mathbb{R}^m\text{ such that:}''')
        st.latex(r'''\begin{aligned} &\frac{\partial \mathfrak{L}}{\partial \lambda_1}\left(\mathbf{x}^*,\boldsymbol{\lambda}^*\right)=g^1\left(\mathbf{x}^*\right)=0, \\ &\cdots \\ &\frac{\partial \mathfrak{L}}{\partial \lambda_m}\left(\mathbf{x}^*, \boldsymbol{\lambda}^*\right)=g^m\left(\mathbf{x}^*\right)=0, \\ &\frac{\partial \mathfrak{L}}{\partial x_1}\left(\mathbf{x}^*,\boldsymbol{\lambda}^*\right)=\frac{\partial f}{\partial x_1}\left(\mathbf{x}^*\right)+\sum_{i=1}^m \lambda_i^* \frac{\partial g^i}{\partial x_1}\left(\mathbf{x}^*\right)=0\quad (4), \\ &\cdots \\ &\frac{\partial \mathfrak{L}}{\partial x_n}\left(\mathbf{x}^*,\boldsymbol{\lambda}^*\right)=\frac{\partial f}{\partial x_n}\left(\mathbf{x}^*\right)+\sum_{i=1}^m \lambda_i^* \frac{\partial g^i}{\partial x_n}\left(\mathbf{x}^*\right)=0, \end{aligned}''')
        st.latex(r'''\text{Write condition (4) in Theorem 1 more compactly:}''')
        st.latex(r'''\\\mathfrak{L}_{\boldsymbol{\lambda}}\left(\mathbf{x}^*, \boldsymbol{\lambda}^*\right)=\mathbf{g}\left(\mathbf{x}^*\right)=\mathbf{0} \text \quad and \quad \mathfrak{L}_{\mathbf{x}}=\nabla f\left(\mathbf{x}^*\right)+\boldsymbol{\lambda}^{* T} D \mathbf{g}\left(\mathbf{x}^*\right)=\mathbf{0}''')
        st.latex(r'''\text{ where }\mathbf{g}\left(\mathbf{x}^*\right)\text{ is a vector in }\mathbb{R}^m \mathbf{g}\left(\mathbf{x}^*\right)=\left[\begin{array}{c} g^1\left(\mathrm{x}^*\right) \\ \cdots \\ g^m\left(\mathrm{x}^*\right) \end{array}\right]''')
        st.latex(r'''\text{ and }D\mathbf{g}\left(\mathbf{x}^*\right)\text{ is a } m\times n\text{ matrix }D\mathbf{g}\left(\mathrm{x}^*\right)=\left[\begin{array}{c} \nabla g^1\left(\mathrm{x}^*\right)^T \\ \cdots \\ \nabla g^m\left(\mathrm{x}^*\right)^T \end{array}\right]''')
    st.subheader("2. SECOND - ORDER CONDITIONS")
    col1, col2 = st.columns([1,50])
    with col1:
        st.latex(r'''\text {Given problem (1) and the corresponding Lagrangean (2), consider the Hessian of }\mathfrak{L}:''')
        st.latex(r'''\begin{aligned} &\mathbf{B}=\left[\begin{array}{cc} \mathfrak{L}_{\lambda \lambda^{\prime}} & \mathfrak{L}_{\lambda \mathbf{x}^{\prime}} \\ \mathfrak{L}_{\mathrm{x} \lambda^{\prime}} & \mathfrak{L}_{\mathrm{xx}^{\prime}} \end{array}\right] \end{aligned}''')
        st.latex(r'''\begin{aligned} =\left[\begin{array}{cc} \mathbf{0} & D \mathbf{g}(\mathbf{x}) \\ D \mathbf{g}(\mathbf{x})^T & f_{\mathbf{x x}^{\prime}}+\sum_{i=1}^m \lambda_i \mathbf{g}_{\mathbf{x x ^ { \prime }}}^i \end{array}\right] \text {, } \end{aligned} ''')
        st.latex(r'''\text{Where }\mathbf{B}\text{ is the }(m+n) \times (m+n)\text{ Hessian matrix of }\mathfrak{L}(\boldsymbol{\lambda}, \mathbf{x})\text{ and the four submetrics }\mathfrak{L}_{\lambda \lambda^{\prime}}, \mathfrak{L}_{\lambda \mathbf{x}^{\prime}}, \mathfrak{L}_{\mathbf{x} \lambda^{\prime}}, \mathfrak{L}_{\mathbf{x} \mathbf{x}^{\prime}}\text{ are of order }m \times m, m \times n, n \times m, n \times n\text{ respectively.}''')
        st.latex(r'''****\textbf{THEOREM 2}****''')
        st.latex(r'''\textbf{(Second - order necessary conditions)}''')
        st.latex(r'''\text{Let }\mathbf{x}^*\text{ be a local minimum for problem (1). Suppose that }\mathbf{x}^*\text{ is regular point. Then, there exists }\lambda^*\text{ such that:}''')
        st.latex(r'''\text{(i) }\left(\mathbf{x}^*, \boldsymbol{\lambda}^*\right)\text{satisfy (4)}''')
        st.latex(r'''\text{(ii) For all vectors }\mathbf{y} \in \mathbb{R}^n\text{ satisfying }D\mathbf{g}\left(\mathbf{x}^*\right) \mathbf{y}=0\text{,we have }\mathbf{y}^T \mathbf{L}^* \mathbf{y} \geq 0,\text{ where }\mathbf{L}^*=\mathfrak{L}_{\mathrm{xx}^{\prime}}\left(\mathbf{x}^*, \lambda^*\right)=\left[f_{\mathrm{xx}^{\prime}}\left(\mathbf{x}^*, \lambda^*\right)+\sum_{i=1}^m \lambda_i \mathbf{g}_{\mathbf{x x ^ { \prime }}}^i\left(\mathbf{x}^*, \lambda^*\right)\right]''')
        st.latex(r'''\text{ Note: If }\mathbf{x}^*\text{ is a local maximum for problem (1), modify (ii) to }\mathbf{y}^T \mathbf{L}^* \mathbf{y} \leq 0\text{, for all vectors }\mathbf{y} \in \mathbb{R}^n\text{ satisfying }D \mathbf{g}\left(\mathbf{x}^*\right) \mathbf{y}=0''')
        st.latex(r'''****\textbf{THEOREM 3}****''')
        st.latex(r'''\textbf{(Second-order sufficient conditions)}''')
        st.latex(r'''\text{ (i) Let }\left(\mathbf{x}^*,\boldsymbol{\lambda}^*\right)\text{ satisfy the first order condition (4).In addition,let }\mathbf{L}^*\text{ be positive-definite for all vectors }\mathbf{y} \in \mathbb{R}^n \backslash\{\mathbf{0}\}\text{ satisfying }D(\mathbf{x}^*)\mathbf{y}=0\text{ then }\mathbf{x}^*\text{ is a local minimum for problem (1).}''')
        st.latex(r'''\text{(ii) If we modify (i) to negative-definite we have the sufficient condition for a local maximum for problem(1)}''')
        st.latex(r'''****\textbf{THEOREM 4}****''')
        st.latex(r'''\textbf{Assume that rank Dg(x*) = m.}''')
        st.latex(r'''\text{(i) Let }\left(\mathbf{x}^*, \boldsymbol{\lambda}^*\right)\text{ satisfy the first order condition (4). }\mathbf{B}^*\text{ be valued at }\left(\mathbf{x}^*, \boldsymbol{\lambda}^*\right).\text{ In addition,let the 2m+1, 2m+2,....,m+n leading principal minors of }\mathbf{B}^*\text{ be the same sign as }(-1)^m\text{ then }\mathbf{x}^*\text{ is a local minimum for problem}''')
        st.latex(r'''\text{ (i) Let }\left(\mathbf{x}^*, \boldsymbol{\lambda}^*\right)\text{ satisfy the first order condition (4). In addition, let the leading principal minors order of 2m+1, 2m+2,....,m+n of }\mathbf{B}^*\text{ alternate in sign beginning with that of }(-1)^{m+1}\text{ then }\mathbf{x}^*\text{ is a local maximum for problem}''')
    
def Theory_Optimization_under_inequality_constraints():
    st.subheader("Optimization under equality and inequality constraints")
    col1, col2 = st.columns([1,50])
    with col1:
        st.latex(r'''\textbf{1. APPROACHING PROCESS}''')
        st.latex(r'''\textbf{Example 1 - Problem with sign constraints:}''')
        st.latex(r'''\text{Given a problem:}''')
        st.latex(r'''\begin{cases}f\left(\mathbf{x_1}\right) & \rightarrow \min \\\mathbf{x_1}&\geq 0\end{cases}\quad(1)''')
        st.latex(r'''\text{where }f\left(\mathbf{x_1}\right)\text{ is a differentiable function on }[0,+\infty].\text{ At the point where }f\left(\mathbf{x_1}\right)\text{ obtains its local minimum, we have:}''')
        st.latex(r'''\begin{cases}f^{\prime}\left(\mathbf{x_1}\right) & \geq 0 \\\mathbf{x_1}& \geq 0\\f^{\prime}\left(\mathbf{x_1}\right) \cdot\mathbf{x_1}&=0\end{cases}''')
        st.latex(r'''\text{Consider a general optimization problem for n variables:}''')
        st.latex(r'''\begin{cases}f(\mathbf{x}) & \rightarrow \min\quad (3)\\ \mathbf{x} \geq 0, & \mathbf{x} \in R^n\end{cases}''')
        st.latex(r'''\text{where } f(\mathbf{x^*})\text{ is differentiable on the feasible set D. At the points }\mathbf{x^*}\text{ where }f(\mathbf{x^*})\text{ obtains its local minimum, we must have:}''')
        st.latex(r'''\begin{cases}\nabla f\left(\mathbf{x}^*\right) & \geq 0 \\\mathbf{x}^* & \geq 0\quad (4)\\ \left\langle\nabla f\left(\mathbf{x}^*\right), \mathbf{x}^*\right\rangle & =0\end{cases}''')
        st.latex(r'''\textbf{Example 2 - Problem with inequality constraints}''')
        st.latex(r'''\text{Consider the problem:}''')
        st.latex(r'''f\left(\mathbf{x_1},\mathbf{x_2}\right) \rightarrow \min\\\left\{\begin{array}{l} h\left(\mathbf{x_1},\mathbf{x_2}\right)=0\quad (5)\\ g\left(\mathbf{x_1},\mathbf{x_2}\right) \leq 0 \end{array}\right.''')
        st.latex(r'''\text{The corresponding equality constrained problem is:}''')
        st.latex(r'''\begin{gathered} f\left(\mathbf{x_1},\mathbf{x_2}\right) \rightarrow \min \\ \begin{cases}h\left(\mathbf{x_1},\mathbf{x_2}\right) & =0 \\ g\left(\mathbf{x_1},\mathbf{x_2}\right)+s & =0\quad (6)\\s & \geq 0\end{cases}\end{gathered}''')
        st.latex(r'''\text{Lagrangean: }L(\mathbf{x}, s, \lambda, \mu)=f(\mathbf{x})+\lambda h(\mathbf{x})+\mu[g(\mathbf{x})+s]''')
        st.latex(r'''\text{The solution of the following system of equations can be the solution of problem (6):}''')
        st.latex(r'''\left\{\begin{array}{l}\frac{\partial L}{\partial \mathbf{x_1}}=\frac{\partial f}{\partial \mathbf{x_1}}+\lambda \frac{\partial h}{\partial \mathbf{x_1}}+\mu \frac{\partial g}{\partial \mathbf{x_1}}=0 \\\frac{\partial L}{\partial \mathbf{x_2}}=\frac{\partial f}{\partial \mathbf{x_2}}+\lambda \frac{\partial h}{\partial \mathbf{x_2}}+\mu \frac{\partial g}{\partial \mathbf{x_2}}=0 \\\frac{\partial L}{\partial s}=\mu \geq 0 ; \quad s \geq 0 ; \quad \mu \cdot s=0 \\\frac{\partial L}{\partial \lambda}=h\left(\mathbf{x_1},\mathbf{x_2}\right)=0 \\\frac{\partial L}{\partial \mu}=g\left(\mathbf{x_1},\mathbf{x_2}\right)+s=0\end{array}\right.''')
        st.latex(r'''\Leftrightarrow\left\{\begin{array}{l}\nabla f(\mathbf{x})+\lambda \nabla h(\mathbf{x})+\mu \nabla g(\mathbf{x})=0 ; \quad h(\mathbf{x})=0 \\\mu \geq 0 ; \quad g(\mathbf{x}) \leq 0 ; \quad \mu g(\mathbf{x})=0\end{array}\right.''')
        st.latex(r'''\textbf{2. KARUSH - KUHN - TUCKER CONDITIONS}''')
        st.latex(r'''\text{Consider a general constrained problem:}''')
        st.latex(r'''\begin{gathered}f(\mathbf{x}) \longrightarrow \min \\\begin{cases}h^i(\mathbf{x})=0 & (i=\overline{1, m})\quad (9) \\g^j(\mathbf{x}) \leq 0 & (j=\overline{1, p})\end{cases}\end{gathered}''')
        st.latex(r'''\text { The Lagrangean: } L(\mathbf{x}, \boldsymbol{\lambda}, \boldsymbol{\mu})=f(\mathbf{x})+\sum_{i=1}^m \lambda_i h^i(\mathbf{x})+\sum_{j=1}^p \mu_j g^j(\mathbf{x}) \text {. }''')
        st.latex(r'''\text{The Karush-Kuhn-Tucker (KKT) conditions are:}''')
        st.latex(r'''\left\{\begin{array}{l}\nabla f(\mathbf{x})+\sum_{i=1}^m \lambda_i \nabla h^i(\mathbf{x})+\sum_{j=1}^p \mu_j \nabla g^j(\mathbf{x})=0 \\h^i(\mathbf{x})=0, \quad(i=\overline{1, m})\quad\quad (10)\\\mu_j \geq 0 ; \quad g^j(\mathbf{x}) \leq 0 ; \quad \mu_j g^j(\mathbf{x})=0 ; \quad(j=\overline{1, p})\end{array}\right.''')
        st.latex(r'''\textbf{3. REGULARITY CONDITIONS AND KKT CONDITIONS}''')
        st.latex(r'''\text{Consider problem (9), suppose that D is not an empty set; is the feasible set and } \mathbf{x^*}\text{ is a boundary point of D}''')
        st.latex(r'''\text { Denote: } J\left(\mathbf{x}^*\right)=\left\{j \mid g^j\left(\mathbf{x}^*\right)=0\right\}''')
        st.latex(r'''\text{Then we say that}\mathbf{x^*}\text{ is a regular point if the below vectors are linearly independent:}''')
        st.latex(r'''\nabla h^i\left(\mathbf{x}^*\right)(i=\overline{1, m}), \quad \nabla g^j\left(\mathbf{x}^*\right)\left(j \in J\left(\mathbf{x}^*\right)\right)''')
        st.latex(r'''\textbf{4. OPTIMAL CONDITIONS}''')
        st.latex(r'''****\textbf{ Theorem 1 }****''')
        st.latex(r'''\textbf{(KKT theorem)}''')
        st.latex(r'''\text {Let } f, h^i(i=\overline{1, m}), g^j(j=\overline{1, p})\text{ are continuously differentiable functions. Let }\mathbf{x}^*\text{ be a regular point and a local minimizer for the problem (9). Then exist}''')
        st.latex(r'''\boldsymbol{\lambda}^* \in \mathbb{R}^m, \boldsymbol{\mu}^* \in \mathbb{R}^p:\left\{\begin{array}{l}\nabla f\left(\mathbf{x}^*\right)+\sum_{i=1}^m \lambda_i^* \nabla h^i\left(\mathbf{x}^*\right)+\sum_{j=1}^p \mu_j^* \nabla g^j\left(\mathbf{x}^*\right)=0 \\\mu_j^* \geq 0 ; \quad \mu_j^* g^j\left(\mathbf{x}^*\right)=0 ; \quad(j=\overline{1, p})\quad (14)\end{array}\right.''')
        st.latex(r'''\text{Points that can be optimal points: All interior points of D satisfying K - T conditions. Boundary points satisfying both regularity conditions and K - T conditions. Boundary points not satisfying regularity conditions nor K - T conditions.}''')
        st.latex(r'''\text{Denote: }T\left(\boldsymbol{x}^*\right)=\left\{\boldsymbol{y} \in \mathbb{R}^n:\left\langle\nabla h^i\left(\boldsymbol{x}^*\right), \boldsymbol{y}\right\rangle=0,\left\langle\nabla g^j\left(\boldsymbol{x}^*\right), \boldsymbol{y}\right\rangle=0, i=\overline{1, m}, j \in J\left(\boldsymbol{x}^*\right)\right\}''')
        st.latex(r'''\text {Let } f, h^i(i=\overline{1, m}), g^j(j=\overline{1, p})\text{  be twice continuously differentiable functions. Let }\mathbf{x}^*\text{ be a regular point and a local minimizer for the problem (9). Then exist}''')
        st.latex(r'''****\textbf{Theorem 2}****''')
        st.latex(r'''\textbf{(Second-order necessary conditions)}''')
        st.latex(r'''\text {Let } f, h^i(i=\overline{1, m}), g^j(j=\overline{1, p})\text{  be twice continuously differentiable functions. Let }\mathbf{x}^*\text{ be a regular point and a local minimizer for the problem (9). Then exist}''')
        st.latex(r'''\boldsymbol{\lambda}^* \in \mathbb{R}^m, \boldsymbol{\mu}^* \in \mathbb{R}^p:\nabla f\left(\mathbf{x}^*\right)+\sum_{i=1}^m \lambda_i^* \nabla h^i\left(\mathbf{x}^*\right)+\sum_{j=1}^p \mu_j^* \nabla g^j\left(\mathbf{x}^*\right)=0, \quad \mu_j^* \geq 0, \quad \mu_j^* g^j\left(\mathbf{x}^*\right)=0 ; \quad(j=\overline{1, p})\\For\quad\mathbf{y} \in T\left(\mathbf{x}^*\right): \mathbf{y}^T L^*\mathbf{y}\geq0. Where, L^*=\left[\frac{\partial^2 L}{\partial\mathbf{x_j}\partial\mathbf{x_k}}\left(\mathbf{x}^*, \boldsymbol{\lambda}^*, \boldsymbol{\mu}^*\right)\right]''')
        st.latex(r'''\text {Denote : }J\left(\mathbf{x}^*, \boldsymbol{\mu}^*\right)=\left\{j: \nabla g^j\left(\mathbf{x}^*\right)=0, \mu_j^*>0\right\} T\left(\mathbf{x}^*, \boldsymbol{\mu}^*\right)=
        \left\{\mathbf{y} \in \mathbb{R}^n:\left\langle\nabla h^i\left(\mathbf{x}^*\right), \mathbf{y}\right\rangle=0,\left\langle\nabla g^j\left(\mathbf{x}^*\right), \mathbf{y}\right\rangle=0, i=\overline{1, m}, j \in J\left(\mathbf{x}^*, \boldsymbol{\mu}^*\right)\right\}''')
        st.latex(r'''****\textbf{Theorem 3}****''')
        st.latex(r'''\textbf{(Second-order sufficient conditions)}''')
        st.latex(r'''\text {Suppose that } f, h^i(i=\overline{1, m}), g^j(j=\overline{1, p}) \text{ be twice continuously differentiable functions and there exist a regular point }\mathbf{x}^*\text{ ∈ D and vector }\boldsymbol{\lambda}^* \in \mathbb{R}^m,\text{vector }\boldsymbol{\mu}^*\in\mathbb{R}^p\text{ that:}''')
        st.latex(r'''\nabla f\left(\mathbf{x}^*\right)+\sum_{i=1}^m \lambda_i^* \nabla h^i\left(\mathbf{x}^*\right)+\sum_{j=1}^p \mu_j^* \nabla g^j\left(\mathbf{x}^*\right)=0, \quad \mu_j^* \geq 0, \quad \mu_j^* g^j\left(\mathbf{x}^*\right)=0 ; \quad(j=\overline{1, p})\text{.For all }\mathbf{y} \in T\left(\mathbf{x}^*, \boldsymbol{\mu}^*\right), \mathbf{y} \neq \mathbf{0} : \mathbf{y}^T L^* \mathbf{y}>0.\text{Then, } \mathbf{x}^*\text{ is a strict local minimizer of problem (9).}''')


def Theory_Unconstrained_optimization_problems():
    col1, col2 = st.columns([1,50])
    with col1:
        st.latex(r'''\text{Consider the problem finding }\mathbf{x} \in D\text{ such that }f(\mathbf{x})\text{ attains its maximum (minimum) where }f(\mathbf{x})\text{ is continuously}''')
        st.latex(r'''\text{differentiable to the second-order. This problem is a unconstrained optimization problem if an optimal solution }\mathrm{x}^*''')
        st.latex(r'''\text{ is an interior point of }D \text{or }\mathrm{x}^* \in \operatorname{int} D.''')
        st.latex(r'''\textbf{First-order necessary condition: }''')
        st.latex(r'''\mathbf{x}^*\text{ is local maximal (minimal) of }f(\mathbf{x}),\text{ then }\nabla f\left(\mathbf{x}^*\right)=0.''')
        st.latex(r'''\textbf{Second-order necessary condition: }''')
        st.latex(r'''\mathbf{x}^*\text{ is local maximal (minimal) of }f(\mathbf{x}),\text{ then the Hessian matrix }H\left(\mathbf{x}^*\right)\text{ of }f(\mathbf{x})\text{ at }\mathbf{x}^*\text{ is negative (positive) semidefinite.}''')
        st.latex(r'''\textbf{Sufficient condition (for $\mathbf{x}^*$ to be local maximal):}''')
        st.latex(r'''\text{ If }\nabla f\left(\mathbf{x}^*\right)=0\text{ and the Hessian matrix }H\left(\mathbf{x}^*\right)\text{ is negative (positive) semidefinite, then }f(\mathbf{x})\text{ attains its local maximum}''')
        st.latex(r'''\text{(minimum) }\mathbf{x}^*.''')


def Theory_convex():
    col1, col2 = st.columns([1,50])
    with col1:
        st.latex(r"\textbf{* CONVEX AND CONVEX FUNCTION}")
        st.latex(r'''\textbf{Let }f(\mathbf{x})\textbf{ be convex on D:}''')
        st.latex(r'''\text{Then }f(\mathbf{x})\text{ attains its global minimum at }\mathbf{x}^*\text{ is and only if }\nabla f\left(\mathbf{x}^*\right)=0.''')
        st.latex(r'''\textbf{Let }f(\mathbf{x})\textbf{ be concave on D:}''')
        st.latex(r'''\text{Then }f(\mathbf{x})\text{ attains its global maximum at }\mathbf{x}^*\text{ if and only if }\nabla f\left(\mathbf{x}^*\right)=0''')

def Theory_Simplex_method():
    st.subheader("1. SIMPLEX ALGORITHM")
    col1, col2 = st.columns([1,50])
    with col1:
        st.latex(r'''\text{Consider a standard problem having extreme point }\boldsymbol{x}^0 \text{ with basis }J_0.''')
        st.latex(r'''\begin{aligned}& \boldsymbol{z} = f(x)=\langle\boldsymbol{c}, \boldsymbol{x}\rangle \rightarrow \max \\& \begin{cases}\sum_{j=1}^n A_j x_j=\boldsymbol{b} & \left(b \in \mathbb{R}^m\right) \\x \geq 0 & \left(x \in \mathbb{R}^n\right)\end{cases}\end{aligned}''')
        st.latex(r'''\text{Without loss of generality, we can assume that }''')
        st.latex(r'''\left\{J_0=1,2, \ldots, m\right\}.''')
        st.latex(r'''\text{Then this problem can be transformed into canonical form:}''')
        st.latex(r''' \boldsymbol{z}=f(\boldsymbol{x})=f\left(\boldsymbol{x}^0\right)-\sum_{k=m+1}^n \Delta_k x_k \rightarrow \max\left\{x_j+\sum_{k=m+1}^n x_{j k} x_k=x_j^0 \quad\left(j \in J_0\right)\right.''')
        st.latex(r'''\textbf{ Step 1. Construct a simplex table corresponding to extreme point } x^0''')
        st.latex(r'''\begin{array}{|c|c|ccccccccccccc|c|}
        \hline & c_j & c_1 & c_2 & \ldots & c_r & \ldots & c_m & c_{m+1} & \ldots & c_k & \ldots & c_s & \ldots & c_n & \\
        \text { Coef. } & \text { Basis } & x_1 & x_2 & \ldots & x_r & \ldots & x_m & x_{m+1} & \ldots & x_k & \ldots & x_s & \ldots & x_n & \text { Sol. } \\
        \hline c_1 & x_1 & 1 & 0 & \ldots & 0 & \ldots & 0 & x_{1, m+1} & \ldots & x_{1, k} & \ldots & x_{1, s} & \ldots & x_{1, n} & x_1^0 \\
        \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
        c_r & x_r & 0 & 0 & \ldots & 1 & \ldots & 0 & x_{r, m+1} & \ldots & x_{r, k} & \ldots & {\left[x_{r, s}\right]} & \ldots & x_{r, n} & x_r^0 \\
        \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
        c_m & x_m & 0 & 0 & \ldots & 0 & \ldots & 1 & x_{m, m+1} & \ldots & x_{m, k} & \ldots & x_{m, s} & \ldots & x_{m, n} & x_m^0 \\
        \hline & \mathbf{z_j} & &\\\hline & -(c_j - \mathbf{z_j})) & 0 & 0 & \ldots & 0 & \ldots & 0 & \Delta_{m+1} & \ldots & \Delta_k & \ldots & \Delta_s & \ldots & \Delta_n & f\left(\boldsymbol{x}^0\right) \\\hline\end{array}''')
        st.latex(r'''\textbf{Step 2. Check the optimality of extreme point }x^0''')
        st.latex(r'''\oplus\text{ If }\Delta_k \geq 0, \forall k \notin J_0\text{ then }\boldsymbol{x}^0\text{ is an extreme optimal solution }\longrightarrow\text{. Stop the algorithm}.''')
        st.latex(r'''\oplus\text{ If there exists }\Delta_k<0\text{ then move to Step 3 .}''')
        st.latex(r'''\textbf{Step 3. Check if the problem is solvable }x^0''')
        st.latex(r'''\oplus\text{ If there exists }\Delta_k<0\text{ and }x_{j k} \leq 0 \forall j \in J_0\text{ then conclude that this problem is unsolvable}''')
        st.latex(r'''\text{because the objective function is unbounded on the feasible domain.}''')
        st.latex(r'''\oplus\text{ If for all }\Delta_k<0\text{ there exists }x_{j k} \geq 0,\text{ move to Step 4  }''')
        st.latex(r'''\textbf{Step 4. Choose entering variable and leaving variable to the set of basic variables}''')
        st.latex(r'''\oplus\text{ Find }\min \left\{\Delta_k: \Delta_k<0, k \notin J_0\right\}=\Delta_s,\text{ then }x_s\text{ is an entering variable. }''')
        st.latex(r'''\oplus\text{ Find }\min \left\{\frac{x_j^0}{x_{j j}}, j \in J_0\right\}=\frac{x_r^0}{x_{r s}},\text{ then }x_r\text{ is a leaving variable}''')
        st.latex(r'''\textbf{Step 5. Pivoting Form a new simplex table, in which, in basic variable column replace }x_r \textbf{ by } x_s.''')
        st.latex(r'''\oplus\text{ Divide }r^{\text {th }}\text{ row by }x_{r s},\text{ the obtained row is called pivot and write this row }x_5 \text{ into the new table.}''')
        st.latex(r'''\oplus\text{ Transform the other rows in the old table into corresponding rows in the new ones.}''')
        st.latex(r'''\text{Obtained result is a simplex table corresponding to a new extreme point }\boldsymbol{x}^1,\text{ better than }\boldsymbol{x}^0.''')
        st.latex(r'''\text{Return to Step 2 and repeat the algorithm, after a finite number of step, conclude that either the problem}''')
        st.latex(r'''\text{is unsolvable because the objective function is unbounded or find the optimal solution which is an extreme.}''')
    st.subheader("2. TWO-PHASES METHOD TO SOLVE GENERAL LP")
    col1, col2 = st.columns([1,7])
    with col1:
        st.latex(r'''\textbf{For the standard form LP:}''')
        st.latex(r'''\begin{array}{r}\mathbf{z}=f(x)=c^T \boldsymbol{x} \rightarrow \max \\\begin{cases}A x=b & \left(b \in \mathbb{R}^m\right) \\\boldsymbol{x} \geq 0 & \left(\boldsymbol{x} \in \mathbb{R}^n\right)\end{cases}\end{array}''')
        st.latex(r'''\textbf{Recall that }\boldsymbol{A} \in \mathbb{R}^{m \times n}.\textbf{ We define the auxiliary LP:}''')
        st.latex(r'''\begin{gathered}P\left(\boldsymbol{x}^a\right)=x_1^a+x_2^a \ldots x_m^a \rightarrow \min \\\begin{cases}\boldsymbol{A x}+\boldsymbol{x}^a=\boldsymbol{b} & \left(\boldsymbol{b} \in \mathbb{R}^m\right) \\\boldsymbol{x} \geq \mathbf{0}, \boldsymbol{x}^a \geq 0 & \left(\boldsymbol{x} \in \mathbb{R}^n, \boldsymbol{x}^a \in \mathbb{R}^m\right)\end{cases}\end{gathered}''')
        st.latex(r'''\textbf{Phase I}''')
        st.latex(r'''\oplus\text{ Find and apply simplex method on auxiliary LP with cost: }''')
        st.latex(r'''\min \sum_{i=1}^m x_i^a''')
        st.latex(r'''\oplus\text{ If the optimal cost in auxiliary is}''')
        st.latex(r'''\text{ Zero: Extreme point of original LP found.}''')
        st.latex(r'''\text{ Positive: Original LP is infeasible}''')
        st.latex(r'''\textbf{ Phase II}''')
        st.latex(r'''\oplus\text{ Take the extreme point found in Phase I to start Phase II.}''')
        st.latex(r'''\oplus\text{ Use cost coefficients of original LP to compute reduced costs.}''')
        st.latex(r'''\oplus\text{ Apply simplex method to original LP.}''')

def Theory_Newton ():
    st.subheader("1. Newton's method for a nonlinear equation")
    col1, col2 = st.columns([1,50])
    with col1:
        st.latex(r'''\bullet\text{ Let }f: \mathbb{R} \longrightarrow \mathbb{R}\text{ be differentiable. We want to find }\bar{x}\text{ satisfying }f(\bar{x})=0. ''')
        st.latex(r'''\bullet\text{ For any }x^k,\text{ let}: ''')
        st.latex(r'''f_L\left(x^k\right)=f\left(x^k\right)+f^{\prime}\left(x^k\right)\left(x-x^k\right) ''')
        st.latex(r'''\text{be the linear approximation of }f\text{ at }x^k.''')
        st.latex(r'''\bullet\text{ We move from }x^k\text{ to }x^{k+1}\text{ by setting:} ''')
        st.latex(r'''f_L\left(x^{k+1}\right)=0 \Leftrightarrow f\left(x^k\right)+f^{\prime}\left(x^k\right)\left(x^{k+1}-x^k\right)=0 ''')
        st.latex(r'''\bullet\text{ We will keep iterating until }\left|f\left(x^k\right)\right|<\epsilon\text{ or }\left|x^{k+1}-x^k\right|<\epsilon\text{ for some predetermined }\epsilon>0.''')
    st.subheader("2. Newton's method for single-variate NLPs")
    col1, col2 = st.columns([1,50])
    with col1:
        st.latex(r'''\bullet\text{ Let }f\text{ be twice differentiable. We want to find }\bar{x}\text{ satisfying }f^{\prime}(\bar{x})=0 ''')
        st.latex(r'''\bullet\text{ For any }x^k,\text{ let} ''')
        st.latex(r'''f_L^{\prime}(x)=f^{\prime}\left(x^k\right)+f^{\prime \prime}\left(x^k\right)\left(x-x^k\right)''')
        st.latex(r'''\text{be the linear approximation of }f^{\prime}\text{ at }x^k. ''')
        st.latex(r'''\bullet\text{ To approach }\bar{x}\text{ we move from }x^k \text{ to } x^{k+1} \text{ by setting }''')
        st.latex(r'''f_L^{\prime}\left(x^{k+1}\right)=0 \Leftrightarrow f^{\prime}\left(x^k\right)+f^{\prime \prime}\left(x^k\right)\left(x^{k+1}-x^k\right)=0 ''')
        st.latex(r'''\bullet\text{ We will keep iterating until }\left|f^{\prime}\left(x^k\right)\right|<\epsilon\text{ or }\left|x^{k+1}-x^k\right|<\epsilon\text{ for some predetermined }\epsilon>0.''')
        st.latex(r'''\bullet\text{ Note that }f^{\prime}(\bar{x})=0\text{ does not guarantee a global minimum. That is why showing }f\text{ is convex is useful!} ''')
        st.latex(r'''\bullet\text{ Let $f$ be twice differentiable. We want to find $\bar{x}$ satisfying $f(\bar{x})=0$} ''')
        st.latex(r'''\bullet\text{ Let }f\text{ be twice differentiable. We want to find }\bar{x}\text{ satisfying }f^{\prime}(\bar{x})=0. ''')
        st.latex(r'''\bullet\text{ For any }x^k,\text{ let} ''')
        st.latex(r'''f_Q^{\prime}(x)=f\left(x^k\right)+f^{\prime}\left(x^k\right)\left(x-x^k\right)+\frac{1}{2} f^{\prime \prime}\left(x^k\right)\left(x-x^k\right)^2''')
        st.latex(r'''\text{be the quadratic approximation of }f\text{ at }x^k. ''')
        st.latex(r'''\bullet\text{ We move from $x^k$ to }x^{k+1}\text{ by moving to the global minimum of the quadratic approximation} ''')
        st.latex(r'''x^{k+1}=\arg \min _{x \in \mathbb{R}}\left[f\left(x^k\right)+f^{\prime}\left(x^k\right)\left(x-x^k\right)+\frac{1}{2} f^{\prime \prime}\left(x^k\right)\left(x-x^k\right)^2\right] ''')
        st.latex(r'''\bullet\text{ Differentiating the above objective function with respect to }x,\text{ we have} ''')
        st.latex(r'''f^{\prime}\left(x^k\right)+f^{\prime \prime}\left(x^k\right)\left(x^{k+1}-x^k\right)=0 \Leftrightarrow x^{k+1}=x^k-\frac{f^{\prime}\left(x^k\right)}{f^{\prime \prime}\left(x^k\right)} ''')
        st.latex(r'''\bullet\text{ Let }f\text{ be twice differentiable. We want to find }\bar{x}\text{ satisfying }f(\bar{x})=0 ''')
    st.subheader("3. Newton's Method for multi-variate NLPs")
    col1, col2 = st.columns([1,50])
    with col1:
        st.latex(r'''\text{The unconstrained Problem: Find }\boldsymbol{x}^* \in \mathbb{R}^n\text{ such that }f(\boldsymbol{x})\text{ attains its minimum where }f(\boldsymbol{x})\text{ is a third-order continuously differentiable function.} ''')
        st.latex(r'''\bullet\text{ The Taylor series expansion of }f\text{ about current point }\boldsymbol{x}^k.''')
        st.latex(r'''f(\boldsymbol{x}) \approx f\left(\boldsymbol{x}^k\right)+\left(\boldsymbol{x}-\boldsymbol{x}^k\right)^T \boldsymbol{d}^k+\frac{1}{2}\left(\boldsymbol{x}-\boldsymbol{x}^k\right)^T H\left(\boldsymbol{x}^k\right)\left(\boldsymbol{x}-\boldsymbol{x}^k\right) \triangleq q(\boldsymbol{x})''')
        st.latex(r'''\text{We have }q\left(\boldsymbol{x}^k\right)=f\left(\boldsymbol{x}^k\right), \nabla q\left(\boldsymbol{x}^k\right)=\nabla f\left(\boldsymbol{x}^k\right)=\boldsymbol{d}^k\text{ and }\nabla^2 q\left(\boldsymbol{x}^k\right)=\nabla^2 f\left(\boldsymbol{x}^k\right)=H\left(\boldsymbol{x}^k\right)\text{ Then, instead of minimize }f(\boldsymbol{x}),\text{ we minimize }q(\boldsymbol{x}) ''')
        st.latex(r'''\bullet\text{ If } H\left(\boldsymbol{x}^k\right)>0 \text { then }q\text{archive a minimum at } ''')
        st.latex(r'''x^{k+1}:=x^k-H\left(x^k\right)^{-1} \boldsymbol{d}^k''')















