import numpy as np
import control

# parameters
M = 1.0
m = 0.12
l = 0.4
g = 9.81

A = np.array([
    [0, 1, 0, 0],
    [0, 0, -m*g/M, 0],
    [0, 0, 0, 1],
    [0, 0, (M+m)*g/(M*l), 0]
])

B = np.array([
    [0],
    [1/M],
    [0],
    [-1/(M*l)]
])

Q = np.diag([1, 1, 500, 50])
R = np.array([[10]])

K, S, E = control.lqr(A, B, Q, R)

print("K =", K)
print("Eigenvalues =", E)


import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Closed-loop system: x_dot = (A - B*K)x
A_cl = A - B @ K

def system(t, x):
    return A_cl @ x

# Initial condition (small angle disturbance)
x0 = [0, 0, 0.1, 0]  # 0.1 rad ≈ 5.7 degrees

# Time span
t_span = (0, 10)
t_eval = np.linspace(0, 10, 500)

# Solve ODE
sol = solve_ivp(system, t_span, x0, t_eval=t_eval)

# Plot results
plt.figure()

plt.plot(sol.t, sol.y[0], label='Cart Position (x)')
plt.plot(sol.t, sol.y[2], label='Pendulum Angle (theta)')

plt.xlabel('Time (s)')
plt.ylabel('States')
plt.title('LQR Controlled Inverted Pendulum')
plt.legend()
plt.grid()

plt.show()