"""
Midsemester Project – Numerical Differentiation Using Finite Differences  
Department of Mathematics  
Course Code: MAT 351  
Student: Ejiogu Esther
Matric No:
Project Topic: Newton’s Forward, Backward, and Central Differences in Soil Settlement Analysis  


1. INTRODUCTION

In highway pavement design, the vertical settlement of a soil layer under applied loads is critical for evaluating structural integrity and safety. Accurately estimating the rate of change of settlement (i.e., the gradient) helps civil engineers understand subsurface compaction behavior. This project applies numerical differentiation techniques — Forward, Backward, and Central Differences — to analyze settlement data.



2. PROBLEM STATEMENT

Given the measured settlement at regular depths, compute the rate of change (gradient) of settlement at depth = 0.4 m.

Data:
- Depths (in meters): [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
- Settlements (in mm): [0.0, 2.1, 3.8, 5.2, 6.0, 6.3]

Objective:
Estimate the gradient of the settlement at 0.4 m using:
- Forward Difference
- Backward Difference
- Central Difference



3. THEORETICAL BACKGROUND

Let h be the uniform interval between data points and f(x) the settlement function:

- h = 0.2 m
- f(x) is the settlement at depth x
- x = 0.4 m (point of interest), which corresponds to index i = 2

The finite difference methods are defined as follows:

- Forward Difference:
  f'(x) ≈ [ f(x + h) - f(x) ] / h

- Backward Difference:
  f'(x) ≈ [ f(x) - f(x - h) ] / h

- Central Difference:
  f'(x) ≈ [ f(x + h) - f(x - h) ] / 2h

These methods allow estimation of derivatives from discrete data points.



4. PYTHON IMPLEMENTATION
"""

# Data
depths = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]       # in meters
settlements = [0.0, 2.1, 3.8, 5.2, 6.0, 6.3]  # in mm
h = 0.2
i = 2  # Index corresponding to depth = 0.4 m

# Forward Difference
forward_diff = (settlements[i + 1] - settlements[i]) / h

# Backward Difference
backward_diff = (settlements[i] - settlements[i - 1]) / h

# Central Difference
central_diff = (settlements[i + 1] - settlements[i - 1]) / (2 * h)

# Output
print(f"Forward Difference at 0.4 m: {forward_diff:.2f} mm/m")
print(f"Backward Difference at 0.4 m: {backward_diff:.2f} mm/m")
print(f"Central Difference at 0.4 m: {central_diff:.2f} mm/m")
