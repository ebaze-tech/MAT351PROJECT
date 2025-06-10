"""

Midsemester Project – Beam Deflection Using Binomial Series  
Department of Mathematics  
Course Code: MAT 351  
Student: Abiodun David
Matric No:
Project Topic: Beam Deflection Analysis Under Axial Strain Using Binomial Series Approximation  

1. INTRODUCTION

In structural engineering, deflection analysis of beams under loading is a fundamental aspect of design and assessment. When axial strain is introduced, the stiffness of the beam is affected, resulting in modified deflection behavior. This project uses the binomial series approximation to incorporate axial strain effects into the classical beam deflection formula for a simply supported beam subjected to a uniformly distributed load.

2. PROBLEM STATEMENT

A simply supported steel beam of length L = 6m carries a uniformly distributed load of q = 15 kN/m
- Modulus of Elasticity: E = 200e9 GPa
- Moment of Inertia: I = 8e-5 m⁴
- Axial Strain: 0.005 

Objective:
- Calculate the standard maximum deflection at the beam's midpoint without strain.
- Adjust the deflection result by approximating the nonlinear stiffness term using a binomial series.

"""

# Input parameters
q = 15000        # Load intensity (N/m)
L = 6            # Beam length (m)
E = 200e9        # Modulus of elasticity (Pa)
I = 8e-5         # Moment of inertia (m⁴)
epsilon = 0.005  # Axial strain

# Step 1: Calculate standard deflection (without strain)
# Formula: delta = (5 * q * L⁴) / (384 * E * I)
L_fourth = L ** 4
EI = E * I
delta_standard = (5 * q * L_fourth) / (384 * EI)

# Step 2: Apply binomial series approximation to (1 + epsilon)⁻¹
# Binomial expansion: (1 + x)⁻¹ ≈ 1 - x + x² - x³ for small x
binomial_approx = 1 - epsilon + epsilon**2 - epsilon**3

# Step 3: Adjust deflection using strain approximation
delta_adjusted = delta_standard * binomial_approx

# Step 4: Convert deflections to millimeters
delta_standard_mm = delta_standard * 1000  # Convert m to mm
delta_adjusted_mm = delta_adjusted * 1000  # Convert m to mm

# Step 5: Output the results
print("MAT 351 – Beam Deflection Using Binomial Series")
print("--------------------------------------------------")
print(f"Standard Deflection (without strain): {delta_standard_mm:.1f} mm")
print(f"Adjusted Deflection (with strain): {delta_adjusted_mm:.1f} mm")

# Verification: Calculate exact adjusted deflection
exact_factor = 1 / (1 + epsilon)
delta_adjusted_exact = delta_standard * exact_factor
delta_adjusted_exact_mm = delta_adjusted_exact * 1000
print(f"Exact Adjusted Deflection: {delta_adjusted_exact_mm:.1f} mm")

'''
# Explanation
- Step 1: Computes the standard deflection using the Euler-Bernoulli formula delta = (5 * q * L^4) / (384 * E * I).
- Step 2: Applies the binomial series to approximate (1 + e)^-1 for e = 0.005, using the first three terms: 1 - e + e^2 - e^3.
- Step 3: Adjusts the deflection by multiplying the standard deflection by the binomial approximation.
- Step 4: Converts results to millimeters for practical interpretation.
- Step 5: Verifies the binomial approximation by computing the exact adjustment factor 1/(1 + e).

# Final Answer
The maximum deflection of the beam, accounting for the axial strain e = 0.005, is approximately 157.4 mm.

# Notes
- The binomial series is accurate for small e (< 0.1), ensuring convergence.
- The code is simple and suitable for educational or preliminary design purposes.
- For critical applications, validate results with finite element analysis or exact numerical methods.
'''