import matplotlib.pyplot as plt


def main() -> None:
    # Dados fornecidos
    t = [0, 1, 2, 3, 4, 6]
    v = [51500, 45320, 39882, 35096, 30885, 23917]
    log10_v = [4.712, 4.656, 4.601, 4.545, 4.490, 4.379]

    # Figura com dois paineis:
    # 1) V(t) com eixo y logaritmico
    # 2) log10(V) em escala linear
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), constrained_layout=True)

    ax1 = axes[0]
    ax1.plot(t, v, marker="o", linewidth=1.8)
    ax1.set_yscale("log")
    ax1.set_title("V(t) com eixo y em escala log")
    ax1.set_xlabel("t (anos)")
    ax1.set_ylabel("V(t) (R$)")
    ax1.grid(True, which="both", linestyle="--", alpha=0.45)

    ax2 = axes[1]
    ax2.plot(t, log10_v, marker="s", linewidth=1.8, color="tab:orange")
    ax2.set_title("log10(V) vs t")
    ax2.set_xlabel("t (anos)")
    ax2.set_ylabel("log10 V")
    ax2.grid(True, linestyle="--", alpha=0.45)

    output_path = "Lista02/Problemas/figuras/grafico_v_log.png"
    fig.savefig(output_path, dpi=200)
    print(f"Grafico salvo em: {output_path}")


if __name__ == "__main__":
    main()
