import numpy as np
import matplotlib.pyplot as plt
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Funções do autômato

def regra_para_binario(regra):
    return np.array([int(bit) for bit in f"{regra:08b}"])

def estado_inicial(n, tipo='central', densidade=0.5, agrupado=False):
    estado = np.zeros(n, dtype=int)
    if tipo == 'central':
        estado[n//2] = 1
    elif tipo == 'aleatorio':
        k = int(densidade * n)
        if agrupado:
            inicio = np.random.randint(0, n-k+1)
            estado[inicio:inicio+k] = 1
        else:
            ocupados = np.random.choice(n, k, replace=False)
            estado[ocupados] = 1
    return estado

def aplicar_regra(estado, regra_binaria):
    tamanho = len(estado)
    novo_estado = np.zeros(tamanho, dtype=int)
    for i in range(tamanho):
        esquerda = estado[(i - 1) % tamanho]
        centro   = estado[i]
        direita  = estado[(i + 1) % tamanho]
        padrao = (esquerda << 2) | (centro << 1) | direita
        novo_estado[i] = regra_binaria[7 - padrao]
    return novo_estado

def simular(regra, tamanho=101, passos=100, tipo_ini='central', densidade=0.5, agrupado=False):
    regra_binaria = regra_para_binario(regra)
    estado = estado_inicial(tamanho, tipo_ini, densidade, agrupado)
    evolucao = [estado.copy()]
    for _ in range(passos):
        estado = aplicar_regra(estado, regra_binaria)
        evolucao.append(estado.copy())
    return np.array(evolucao)

# Função para desenhar o gráfico no canvas do PySimpleGUI

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg
def classificar_regra(regra):
    """Classifica a regra segundo Wolfram."""
    classes = {
        'Homogêneo': [0, 8, 32, 160, 250, 255],
        'Periódico': [4, 12, 36, 44, 73, 77, 78, 94, 104, 108, 128, 132, 136, 140, 156, 204],
        'Caótico': [18, 22, 30, 45, 60, 90, 105, 106, 122, 126, 146, 150, 170, 182],
        'Complexo': [54, 110]
    }
    for classe, regras in classes.items():
        if regra in regras:
            return classe
    return 'Não classificada'

def main():
    sg.theme('DarkBlue3')
    layout_controles = [
        [sg.Text('Regra:', size=(12,1)), sg.Slider(range=(0,255), orientation='h', size=(20,20), default_value=30, key='regra', enable_events=True)],
        [sg.Text('Tamanho:', size=(12,1)), sg.Slider(range=(21,201), orientation='h', size=(20,20), default_value=101, key='tamanho', enable_events=True)],
        [sg.Text('Passos:', size=(12,1)), sg.Slider(range=(10,200), orientation='h', size=(20,20), default_value=100, key='passos', enable_events=True)],
        [sg.Text('Estado inicial:', size=(12,1)), sg.Combo(['central', 'aleatorio'], default_value='central', key='tipo_ini', size=(12,1))],
        [sg.Text('Densidade:', size=(12,1)), sg.Slider(range=(0.05,1.0), resolution=0.05, orientation='h', size=(20,20), default_value=0.5, key='densidade')],
        [sg.Text('Agrupado:', size=(12,1)), sg.Combo(['Não', 'Sim'], default_value='Não', key='agrupado', size=(12,1))],
        [sg.Button('Simular', size=(12,1), button_color=('white', '#007ACC')), sg.Button('Sair', size=(8,1))],
    ]
    layout = [
        [
            sg.Frame('Parâmetros', layout_controles, element_justification='left'),
            sg.VSeperator(),
            sg.Column([
                [sg.Canvas(key='-CANVAS-')],  # canvas ainda maior
                [sg.Text('Clique no gráfico para obter informações da célula.', key='info', size=(50,1))],
            ], element_justification='center')
        ]
    ]
    window = sg.Window('Autômatos Celulares de Wolfram', layout, finalize=True, resizable=True)
    fig_agg = None
    evolucao = None
    # Atualiza classificação inicial ao abrir a interface
    regra = int(window['regra'].Widget.get())
    agrupado = window['agrupado'].Widget.get() == 'Sim'
    classe = classificar_regra(regra)
    agrupado_str = 'Sim' if agrupado else 'Não'

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Sair'):
            break
        # Atualiza classificação ao mover o slider da regra
        if event == 'regra':
            regra = int(values['regra'])
            classe = classificar_regra(regra)
            agrupado = values['agrupado'] == 'Sim'
            agrupado_str = 'Sim' if agrupado else 'Não'
        # Atualiza classificação ao mudar o combo de agrupado
        if event == 'agrupado':
            regra = int(values['regra'])
            classe = classificar_regra(regra)
            agrupado = values['agrupado'] == 'Sim'
            agrupado_str = 'Sim' if agrupado else 'Não'
        if event == 'Simular':
            regra = int(values['regra'])
            tamanho = int(values['tamanho'])
            passos = int(values['passos'])
            tipo_ini = values['tipo_ini']
            densidade = float(values['densidade'])
            agrupado = values['agrupado'] == 'Sim'
            evolucao = simular(regra, tamanho, passos, tipo_ini, densidade, agrupado)
            plt.close('all')
            # Tamanho menor e responsivo
            largura = max(5, min(8, tamanho/25))  # entre 5 e 8
            altura = max(3, min(5, passos/40))    # entre 3 e 5
            fig, ax = plt.subplots(figsize=(largura, altura))
            fig.subplots_adjust(top=0.80, bottom=0.18)  # aumenta a margem superior e inferior
            ax.imshow(evolucao, cmap='binary')
            classe = classificar_regra(regra)
            agrupado_str = 'Sim' if agrupado else 'Não'
            titulo = f"Regra {regra} | Classe: {classe}\nAgrupado: {agrupado_str} | Tamanho: {tamanho} | Passos: {passos}"
            ax.set_title(titulo)
            ax.set_xlabel('Células')
            ax.set_ylabel('Tempo')
            if fig_agg:
                fig_agg.get_tk_widget().forget()
                plt.close('all')
            fig_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
            # campo removido
            def onclick(event):
                if event.inaxes:
                    x = int(round(event.xdata))
                    y = int(round(event.ydata))
                    val = evolucao[y, x] if 0 <= y < evolucao.shape[0] and 0 <= x < evolucao.shape[1] else None
                    window['info'].update(f'Célula: {x}, Tempo: {y}, Valor: {val}')
            fig.canvas.mpl_connect('button_press_event', onclick)
    window.close()

if __name__ == '__main__':
    main()
