import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------
# Parameters and Constants
# -----------------------------------
L = 10.0                        # Beam length (meters)
EI = 2e11 * 8.333e-6            # Flexural rigidity (E × I)
P = 1000                        # Point load (Newtons)
a = 5.0                         # Load position (meters)
spread = 0.05                   # Spread of Gaussian approximation of point load
dx = 0.1                        # Step size for RK4
N = 101                         # Number of points for Central Difference

# -----------------------------------
# Load Function: Gaussian approximation of Dirac Delta
# -----------------------------------
def gaussian_load(x, a, spread):
    return P * np.exp(-((x - a)**2) / (2 * spread**2)) / (spread * np.sqrt(2 * np.pi))

# -----------------------------------
# Runge-Kutta 4th Order Method for Beam Deflection
# -----------------------------------
def beam_deflection_rk4():
    def system_of_odes(x, Y):
        """
        Solves: y'''' = w(x)/EI as a system of 1st-order ODEs
        Y = [y, y', y'', y''']
        """
        y1, y2, y3, y4 = Y
        w = gaussian_load(x, a, spread)
        return np.array([y2, y3, y4, w / EI])

    def rk4_step(f, x, Y, h):
        """Runge-Kutta 4th order step"""
        k1 = f(x, Y)
        k2 = f(x + h/2, Y + h * k1 / 2)
        k3 = f(x + h/2, Y + h * k2 / 2)
        k4 = f(x + h, Y + h * k3)
        return Y + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)

    x_vals = np.arange(0, L + dx, dx)
    Y = np.array([0.0, 0.0, 0.0, 0.0])  # Initial conditions: [y, y', y'', y''']
    y_deflections = []

    for x in x_vals:
        y_deflections.append(Y[0])  # Store vertical deflection y
        Y = rk4_step(system_of_odes, x, Y, dx)

    return x_vals, y_deflections

# -----------------------------------
# Central Difference Method for Beam Deflection
# -----------------------------------
def beam_deflection_central_difference():
    x_vals = np.linspace(0, L, N)
    dx = L / (N - 1)
    w_vals = gaussian_load(x_vals, a, spread=0.1)  # Use slightly wider spread
    rhs = w_vals / EI * dx**4  # RHS after multiplying both sides by dx⁴

    A = np.zeros((N, N))
    b = rhs.copy()

    # Fill matrix A using 4th order central difference:
    for i in range(2, N - 2):
        A[i, i-2] = 1
        A[i, i-1] = -4
        A[i, i]   = 6
        A[i, i+1] = -4
        A[i, i+2] = 1

    # Apply boundary conditions: Simply Supported Beam (y = 0 at both ends)
    A[0, 0] = A[1, 1] = A[-2, -2] = A[-1, -1] = 1
    b[0] = b[1] = b[-2] = b[-1] = 0

    # Solve system of equations for deflection
    y_deflections = np.linalg.solve(A, b)
    return x_vals, y_deflections

# -----------------------------------
# Plotting Utility
# -----------------------------------
def plot_deflection(x, y, method_name):
    plt.plot(x, y, label=method_name)

# -----------------------------------
# Main Execution
# -----------------------------------
def main():
    # Runge-Kutta Method
    x_rk4, y_rk4 = beam_deflection_rk4()
    plot_deflection(x_rk4, y_rk4, 'Runge-Kutta Method')

    # Central Difference Method
    x_cdf, y_cdf = beam_deflection_central_difference()
    plot_deflection(x_cdf, y_cdf, 'Central Difference Method')

    # Final Plot
    plt.figure(figsize=(10, 4))
    plot_deflection(x_rk4, y_rk4, 'Runge-Kutta Method')
    plot_deflection(x_cdf, y_cdf, 'Central Difference Method')
    plt.xlabel('Beam Length (m)')
    plt.ylabel('Deflection (m)')
    plt.title('Beam Deflection Under Point Load')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Run the code
if __name__ == "__main__":
    main()
