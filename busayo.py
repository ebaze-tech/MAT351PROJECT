
# Midsemester Project – Newton-Raphson Method for Open Channel Flow
# Department of Mathematics
# Course Code: MAT 351
# Student Name: Oluwabusayo Akinkuehin
# Project Topic: Determination of Flow Depth in Open Channel Using Newton-Raphson Method

def manning_discharge(y, b=3.0, n=0.015, S=0.001):
    """Compute flow discharge Q given flow depth y using Manning’s equation."""
    A = b * y
    P = b + 2 * y
    R = A / P
    Q = (1/n) * A * (R ** (2/3)) * (S ** 0.5)
    return Q

def f(y, Q_target, b, n, S):
    """Nonlinear function: difference between computed Q and target Q."""
    return manning_discharge(y, b, n, S) - Q_target

def newton_raphson(Q_target, b=3.0, n=0.015, S=0.001, y0=1.0, tol=1e-6, max_iter=100):
    """Newton-Raphson iteration to find flow depth y."""
    delta = 1e-6  # Small delta for numerical derivative
    y = y0
    for i in range(max_iter):
        fy = f(y, Q_target, b, n, S)
        if abs(fy) < tol:
            print(f"Converged after {i+1} iterations.")
            return y
        dfy = (f(y + delta, Q_target, b, n, S) - fy) / delta
        if dfy == 0:
            raise ValueError("Zero derivative encountered.")
        y -= fy / dfy
    raise RuntimeError("Newton-Raphson did not converge.")

# Parameters
Q_target = 10.0  # Discharge (m³/s)
b = 3.0          # Channel width (m)
n = 0.015        # Manning's coefficient
S = 0.001        # Slope

# Solve for depth
depth = newton_raphson(Q_target, b, n, S, y0=1.0)
print(f"Flow depth y ≈ {depth:.4f} meters")
