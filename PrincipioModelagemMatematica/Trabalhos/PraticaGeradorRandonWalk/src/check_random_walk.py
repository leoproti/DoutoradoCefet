import pandas as pd
import numpy as np
import os

base_path = "Trabalhos/PraticaGeradorRandonWalk/src/dados"

def load_csv(path):
    return pd.read_csv(os.path.join(base_path, path))

# Load data
p_in = load_csv("input/entrada_parametros.csv")
p_tcl_in = load_csv("input/entrada_tcl_parametros.csv")
h_out = load_csv("output/saida_teste_hipotese.csv")
tcl_out = load_csv("output/saida_tcl_resumo.csv")
traj_out = load_csv("output/saida_trajetorias.csv")
msd_out = load_csv("output/saida_msd.csv")

print("--- PARAMETROS DE ENTRADA ---")
print(p_in.to_string(index=False))
print("\n--- PARAMETROS TCL ---")
print(p_tcl_in.to_string(index=False))

print("\n--- DESLOCAMENTOS FINAIS ---")
# Check columns
cols = traj_out.columns.tolist()
walk_cols = [c for c in cols if "caminhada" in c.lower() or "walk" in c.lower()]
if not walk_cols:
    walk_cols = cols[1:] # Assume first is index/time

last_row = traj_out.iloc[-1]
final_displacements = last_row[walk_cols].values
print(f"Deslocamentos: {final_displacements}")
print(f"Media dos finais: {np.mean(final_displacements):.4f}")

print("\n--- TESTE DE HIPOTESE (MSD) ---")
print(h_out.to_string(index=False))

if 'alpha_est' in h_out.columns and 'std_err' in h_out.columns:
    alpha = h_out['alpha_est'].iloc[0]
    se = h_out['std_err'].iloc[0]
    t_crit = h_out['t_crit'].iloc[0]
    ic_low = alpha - t_crit * se
    ic_high = alpha + t_crit * se
    print(f"IC95 para alpha: [{ic_low:.6f}, {ic_high:.6f}]")

print("\n--- METRICAS TCL ---")
print(tcl_out.to_string(index=False))
