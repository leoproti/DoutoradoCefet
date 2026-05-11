from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

p = Path('figuras_prova')
p.mkdir(exist_ok=True)

# Q2: escala omega ~ sqrt(g/h)
g = 9.81
h = np.linspace(5, 80, 250)
omega = np.sqrt(g / h)
fig, ax = plt.subplots(figsize=(7.2, 4.5))
ax.plot(h, omega, lw=2, color='#1f77b4')
ax.set_xlabel('h [m]')
ax.set_ylabel('omega [rad/s]')
ax.set_title('Questao 2: escala omega ~ sqrt(g/h)')
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig(p / 'q2_escala_omega_h.png', dpi=180)
plt.close(fig)

# Q3: depreciacao do carro
V0 = 51500
t = np.linspace(0, 10, 300)
V = V0 * (0.88**t)
fig, ax = plt.subplots(figsize=(7.2, 4.5))
ax.plot(t, V, lw=2.2, color='#d62728')
ax.scatter(np.arange(0, 11), V0 * (0.88**np.arange(0, 11)), s=20, color='#d62728')
ax.set_xlabel('t [anos]')
ax.set_ylabel('V(t) [R$]')
ax.set_title('Questao 3: V(t)=51500*(0.88)^t')
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig(p / 'q3_depreciacao.png', dpi=180)
plt.close(fig)

# Q4: sequencia LCG para semente 0
m, a, c = 10, 11, 9
x = [0]
for _ in range(10):
    x.append((a * x[-1] + c) % m)
fig, ax = plt.subplots(figsize=(7.2, 4.5))
ax.step(range(len(x)), x, where='post', lw=2, color='#2ca02c')
ax.plot(range(len(x)), x, 'o', color='#2ca02c')
ax.set_xlabel('n')
ax.set_ylabel('X_n')
ax.set_title('Questao 4: LCG X_(n+1)=(11X_n+9) mod 10, semente 0')
ax.set_yticks(range(0, 10))
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig(p / 'q4_lcg_semente0.png', dpi=180)
plt.close(fig)

print('graficos_prova_ok')
