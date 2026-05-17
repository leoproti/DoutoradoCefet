import pandas as pd
import numpy as np
import os

base_path = "Trabalhos/PraticaGeradorRandonWalk/src/dados"

def load_csv(path):
    return pd.read_csv(os.path.join(base_path, path))

# Load data
p_in = load_csv("input/entrada_parametros.csv")
tcl_in = load_csv("input/entrada_tcl_parametros.csv")
h_out = load_csv("output/saida_teste_hipotese.csv")
tcl_out = load_csv("output/saida_tcl_resumo.csv")
traj_out = load_csv("output/saida_trajetorias.csv")

# Parametros Entrada
n_walks = p_in.loc[p_in['parametro'] == 'N_WALKS', 'valor'].values[0]
n_steps = p_in.loc[p_in['parametro'] == 'N_STEPS', 'valor'].values[0]

# Deslocamentos Finais
cols = [c for c in traj_out.columns if 'caminhada' in c.lower()]
finais = traj_out.iloc[-1][cols].values
media_finais = np.mean(finais)

# MSD results
alpha = h_out['alpha_est'].iloc[0]
c_est = h_out['C_est'].iloc[0]
r2 = h_out['r2_ajuste'].iloc[0]
se = h_out['std_err_alpha'].iloc[0]
t_stat = h_out['t_stat'].iloc[0]
t_crit = h_out['t_critico'].iloc[0]
p_val = h_out['p_valor'].iloc[0]
gl = h_out['graus_liberdade'].iloc[0]
ic_alpha = [alpha - t_crit * se, alpha + t_crit * se]

# TCL results
m_z = tcl_out['media_Z'].iloc[0]
s_z = tcl_out['desvio_padrao_Z'].iloc[0]
ks_s = tcl_out['ks_stat'].iloc[0]
ks_p = tcl_out['ks_pvalor'].iloc[0]

print(f"--- RELATORIO DE VERIFICACAO ---")
print(f"N_WALKS: {n_walks}, N_STEPS: {n_steps}")
print(f"Deslocamentos Finais: {list(finais.astype(int))}")
print(f"Media Finais: {media_finais:.1f}")
print(f"MSD: alpha={alpha:.6f}, C={c_est:.4f}, R2={r2:.4f}, SE={se:.6f}, t={t_stat:.6f}, tcrit={t_crit:.6f}, p={p_val:.2e}, gl={gl}")
print(f"IC95 alpha: [{ic_alpha[0]:.4f}, {ic_alpha[1]:.4f}]")
print(f"TCL: MediaZ={m_z:.6f}, StdZ={s_z:.4f}, KS={ks_s:.4f}, p-KS={ks_p:.4f}")

# Comparacao com LaTeX
print("\n--- DIVERGÊNCIAS DETECTADAS ---")
ref_media_finais = -86.8
if abs(media_finais - ref_media_finais) > 0.01:
    print(f"Media Finais: CSV ({media_finais:.1f}) vs LaTeX ({ref_media_finais})")

ref_alpha = 1.016797
if abs(alpha - ref_alpha) > 1e-6:
    print(f"Alpha: CSV ({alpha:.6f}) vs LaTeX ({ref_alpha:.6f})")

ref_ks_p = 0.3895
if abs(ks_p - ref_ks_p) > 0.001:
    print(f"KS p-valor: CSV ({ks_p:.4f}) vs LaTeX ({ref_ks_p:.4f}) -> DIVERGÊNCIA")

ref_std_z = 0.9863
if abs(s_z - ref_std_z) > 0.001:
     print(f"Std Z: CSV ({s_z:.4f}) vs LaTeX ({ref_std_z:.4f}) -> DIVERGÊNCIA")
