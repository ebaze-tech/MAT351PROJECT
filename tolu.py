
"""
Midsemester Project – Beam Deflection Using Numerical Methods in Python
Author: Toluwanimi Faramade
Date: June 2025

Overview:
This project focuses on using numerical methods to solve deflection problems
in structural beams. We apply Picard's Iteration, Root Bisection Method
and Linear Iteration Method to four types of beam loading conditions.

GENERAL BEAM DEFLECTION EQUATION:
    d²y/dx² = M(x)/EI

Where:
    y(x) -> vertical deflection of the beam
    M(x) -> bending moment as a function of x
    E    -> Young's modulus (material stiffness)
    I    -> Moment of inertia (beam cross-section property)

We reduce the second-order ODE to two first-order ODEs:
    Let v = dy/dx (slope)
    Then:
        dv/dx = M(x)/EI
        dy/dx = v

This system of ODEs can be solved using Picard’s Iteration,
while Bisection and Linear Iteration are used to find critical values
such as max deflection locations.

BEAM CASES:

1. Simply Supported Beam with a Point Load at the Center:
    M(x) = (P/2)x for 0 ≤ x ≤ L/2
         = (P/2)(L - x) for L/2 < x ≤ L

2. Simply Supported Beam under Uniformly Distributed Load (UDL):
    M(x) = (w/2)(Lx - x²)

3. Cantilever Beam with a Point Load at Free End:
    M(x) = -P(L - x)

4. Cantilever Beam with UDL:
    M(x) = -(w/2)(L - x)²

IMPLEMENTATION IN PYTHON
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
E = 200e9           # Young's modulus in Pascals
I = 5e-6            # Moment of inertia in m^4
P = 1000            # Point load in Newtons
w = 500             # UDL in N/m
L = 2               # Beam length in meters

def EI():
    return E * I

# Define bending moment functions
def M_point_load_center(x):
    if x <= L / 2:
        return (P * x) / 2
    else:
        return (P * (L - x)) / 2

def M_udl_simply_supported(x):
    return (w / 2) * (L * x - x**2)

def M_point_load_cantilever(x):
    return -P * (L - x)

def M_udl_cantilever(x):
    return -(w / 2) * (L - x)**2

# Picard Iteration Method
def picard_iteration(x_vals, M_func, y0=0, v0=0, iterations=3):
    EI_val = EI()
    y = [y0 for _ in x_vals]
    v = [v0 for _ in x_vals]
    h = x_vals[1] - x_vals[0]

    for _ in range(iterations):
        for i in range(1, len(x_vals)):
            v[i] = v0 + sum(M_func(x_vals[j]) / EI_val * h for j in range(i))
            y[i] = y0 + sum(v[j] * h for j in range(i))
    return y

# Root Bisection Method
def bisection(f, a, b, tol=1e-6):
    if f(a) * f(b) > 0:
        raise ValueError("Function does not change sign in the interval.")
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0 or (b - a) / 2 < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Linear Iteration Method
def linear_iteration(g, x0, tol=1e-6, max_iter=100):
    for _ in range(max_iter):
        x1 = g(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    raise Exception("Linear iteration did not converge.")

# Plotting function
def plot_deflection(x_vals, y_vals, title="Beam Deflection"):
    plt.plot(x_vals, y_vals, label="Deflection")
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.show()

# Main runner for each beam case
def solve_and_plot():
    
    x_vals = np.linspace(0, L, 100)

    cases = [
        ("Simply Supported Beam - Point Load", M_point_load_center),
        ("Simply Supported Beam - UDL", M_udl_simply_supported),
        ("Cantilever Beam - Point Load", M_point_load_cantilever),
        ("Cantilever Beam - UDL", M_udl_cantilever),
    ]

    for name, M_func in cases:
        y_vals = picard_iteration(x_vals, M_func)
        print(f"Plotting: {name}")
        plot_deflection(x_vals, y_vals, name)

        # Root bisection example to find max deflection point (where slope ≈ 0)
        def slope_approx(x):
            h = 1e-5
            return (M_func(x + h) - M_func(x)) / h

        try:
            root = bisection(slope_approx, 0.1, L - 0.1)
            print(f"{name}: Approximate point of max deflection (Bisection): {root:.4f} m")
        except Exception as e:
            print(f"{name}: Bisection Error -", e)

        # Linear iteration (example: fixed point at L/2)
        try:
            g = lambda x: L / 2  # Known symmetry for center point
            fixed = linear_iteration(g, 0.1)
            print(f"{name}: Linear Iteration Result: {fixed:.4f} m\n")
        except Exception as e:
            print(f"{name}: Linear Iteration Error -", e)

if __name__ == "__main__":
    solve_and_plot()
