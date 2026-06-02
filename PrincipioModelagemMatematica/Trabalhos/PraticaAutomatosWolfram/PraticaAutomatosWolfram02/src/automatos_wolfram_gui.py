import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import unicodedata

# Funções do autômato

def regra_para_binario(regra):
    return np.array([int(bit) for bit in f"{regra:08b}"])

def estado_inicial(n, tipo='Central', densidade=0.5, agrupado=False):
    estado = np.zeros(n, dtype=int)
    if tipo == 'Central':
        estado[n//2] = 1
    elif tipo == 'Aleatório':
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

def simular(regra, tamanho=101, passos=100, tipo_ini='Central', densidade=0.5, agrupado=False):
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


def normalizar_texto(texto):
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
    texto = texto.lower().replace(' ', '_')
    return ''.join(ch for ch in texto if ch.isalnum() or ch in ('_', '-'))


CLASSES_REFERENCIA = {
    'Homogêneo': [0, 8, 32, 160, 250, 255],
    'Periódico': [4, 12, 36, 44, 73, 77, 78, 94, 104, 108, 128, 132, 136, 140, 156, 204],
    'Caótico': [18, 22, 30, 45, 60, 90, 105, 106, 122, 126, 146, 150, 170, 182],
    'Complexo': [54, 110]
}

_CLASSIFICACAO_CACHE = {}


def _entropia_binaria(fracao_um):
    p = float(np.clip(fracao_um, 1e-12, 1 - 1e-12))
    return -(p * np.log2(p) + (1 - p) * np.log2(1 - p))


def _metricas_regra(regra, tamanho=121, passos=120):
    evolucao = simular(regra, tamanho=tamanho, passos=passos, tipo_ini='Aleatório', densidade=0.5, agrupado=False)

    atividade = evolucao.mean(axis=1)
    inicio = max(1, passos // 3)
    atividade_estavel = atividade[inicio:]
    entropias = np.array([_entropia_binaria(v) for v in atividade_estavel])

    transicao = np.abs(np.diff(evolucao, axis=0)).mean()

    regra_binaria = regra_para_binario(regra)
    a = estado_inicial(tamanho, 'Central')
    b = a.copy()
    idx = (tamanho // 2) + 1
    b[idx] = 1 - b[idx]

    distancias = []
    for _ in range(passos):
        a = aplicar_regra(a, regra_binaria)
        b = aplicar_regra(b, regra_binaria)
        distancias.append(np.mean(a != b))

    sensibilidade = float(np.mean(distancias[inicio:]))

    return {
        'entropia_media': float(np.mean(entropias)),
        'variacao_atividade': float(np.std(atividade_estavel)),
        'taxa_transicao': float(transicao),
        'sensibilidade': sensibilidade,
    }


def classificar_regra_detalhada(regra):
    if regra in _CLASSIFICACAO_CACHE:
        return _CLASSIFICACAO_CACHE[regra]

    for classe, regras in CLASSES_REFERENCIA.items():
        if regra in regras:
            resultado = (classe, 'referência', 'Classificação canônica da literatura para ECA.')
            _CLASSIFICACAO_CACHE[regra] = resultado
            return resultado

    metricas = _metricas_regra(regra)
    entropia = metricas['entropia_media']
    transicao = metricas['taxa_transicao']
    sensibilidade = metricas['sensibilidade']

    if entropia < 0.12 and transicao < 0.05:
        classe = 'Homogêneo'
    elif entropia < 0.45 and transicao < 0.20:
        classe = 'Periódico'
    elif entropia > 0.78 and transicao > 0.32 and sensibilidade < 0.35:
        classe = 'Caótico'
    else:
        classe = 'Complexo'

    resumo = (
        f"Heurística: H={entropia:.2f}, T={transicao:.2f}, S={sensibilidade:.2f}."
    )
    resultado = (classe, 'heurística', resumo)
    _CLASSIFICACAO_CACHE[regra] = resultado
    return resultado


def classificar_regra(regra):
    """Classifica a regra em uma das 4 classes de Wolfram."""
    classe, _, _ = classificar_regra_detalhada(regra)
    return classe


def converter_valor(texto, minimo, maximo, inteiro=True):
    try:
        valor = int(float(texto)) if inteiro else float(str(texto).replace(',', '.'))
    except (ValueError, TypeError):
        return None
    if valor < minimo or valor > maximo:
        return None
    return valor

def main():
    sg.theme('DarkBlue3')
    label_size = (12, 1)
    slider_size = (22, 20)
    input_size = (6, 1)
    input_pad = ((0, 0), (22, 0))

    layout_controles = [
        [
            sg.Text('Regra:', size=label_size),
            sg.Column([[sg.Slider(range=(0,255), orientation='h', size=slider_size, default_value=30, key='regra', enable_events=True), sg.Input('30', size=input_size, key='regra_txt', enable_events=True, pad=input_pad)]], pad=(0, 0))
        ],
        [
            sg.Text('Tamanho:', size=label_size),
            sg.Column([[sg.Slider(range=(21,201), orientation='h', size=slider_size, default_value=101, key='tamanho', enable_events=True), sg.Input('101', size=input_size, key='tamanho_txt', enable_events=True, pad=input_pad)]], pad=(0, 0))
        ],
        [
            sg.Text('Passos:', size=label_size),
            sg.Column([[sg.Slider(range=(10,200), orientation='h', size=slider_size, default_value=100, key='passos', enable_events=True), sg.Input('100', size=input_size, key='passos_txt', enable_events=True, pad=input_pad)]], pad=(0, 0))
        ],
        [
            sg.Text('Estado inicial:', size=label_size),
            sg.Column([[sg.Combo(['Central', 'Aleatório'], default_value='Central', key='tipo_ini', size=(22,1), enable_events=True)]], pad=(0, 0))
        ],
        [
            sg.Text('Densidade:', size=label_size),
            sg.Column([[sg.Slider(range=(0.05,1.0), resolution=0.05, orientation='h', size=slider_size, default_value=0.5, key='densidade', enable_events=True), sg.Input('0.5', size=input_size, key='densidade_txt', enable_events=True, pad=input_pad)]], pad=(0, 0))
        ],
        [
            sg.Text('Agrupado:', size=label_size),
            sg.Column([[sg.Combo(['Não', 'Sim'], default_value='Não', key='agrupado', size=(22,1))]], pad=(0, 0))
        ],
        [
            sg.Text('', size=label_size),
            sg.Column([[
                sg.Button('Simular', size=(12,1), button_color=('white', '#007ACC')),
                sg.Button('Salvar', size=(12,1)),
                sg.Button('Sair', size=(8,1))
            ]], pad=(0, 0))
        ],
    ]
    layout = [
        [
            sg.Frame('Parâmetros', layout_controles, element_justification='left'),
            sg.VSeperator(),
            sg.Column([
                [sg.Canvas(key='-CANVAS-')],  # canvas ainda maior
                [sg.Text('Classes de Wolfram: I Homogêneo | II Periódico | III Caótico | IV Complexo', size=(72,1))],
                [sg.Text('Convenção: t=0 no topo e tempo cresce para baixo.', size=(50,1))],
                [sg.Text('Clique no gráfico para obter informações da célula.', key='info', size=(50,1))],
            ], element_justification='center')
        ]
    ]
    window = sg.Window('Autômatos Celulares de Wolfram', layout, finalize=True, resizable=True)

    def atualizar_controles_densidade(tipo_inicial):
        habilitar = tipo_inicial == 'Aleatório'
        window['densidade'].update(disabled=not habilitar)
        window['densidade_txt'].update(disabled=not habilitar)

    fig_agg = None
    fig = None
    evolucao = None
    ultima_config = None
    atualizar_controles_densidade(window['tipo_ini'].get())
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
            window['regra_txt'].update(str(regra))
            classe = classificar_regra(regra)
            agrupado = values['agrupado'] == 'Sim'
            agrupado_str = 'Sim' if agrupado else 'Não'
        if event == 'tamanho':
            window['tamanho_txt'].update(str(int(values['tamanho'])))
        if event == 'passos':
            window['passos_txt'].update(str(int(values['passos'])))
        if event == 'densidade':
            window['densidade_txt'].update(f"{float(values['densidade']):.2f}")

        if event == 'regra_txt':
            regra_txt = converter_valor(values['regra_txt'], 0, 255, inteiro=True)
            if regra_txt is not None:
                window['regra'].update(regra_txt)
                classe = classificar_regra(regra_txt)
                agrupado = values['agrupado'] == 'Sim'
                agrupado_str = 'Sim' if agrupado else 'Não'
        if event == 'tamanho_txt':
            tamanho_txt = converter_valor(values['tamanho_txt'], 21, 201, inteiro=True)
            if tamanho_txt is not None:
                window['tamanho'].update(tamanho_txt)
        if event == 'passos_txt':
            passos_txt = converter_valor(values['passos_txt'], 10, 200, inteiro=True)
            if passos_txt is not None:
                window['passos'].update(passos_txt)
        if event == 'densidade_txt':
            densidade_txt = converter_valor(values['densidade_txt'], 0.05, 1.0, inteiro=False)
            if densidade_txt is not None:
                window['densidade'].update(densidade_txt)
                window['densidade_txt'].update(f"{densidade_txt:.2f}")
        if event == 'tipo_ini':
            atualizar_controles_densidade(values['tipo_ini'])
        # Atualiza classificação ao mudar o combo de agrupado
        if event == 'agrupado':
            regra = int(values['regra'])
            classe = classificar_regra(regra)
            agrupado = values['agrupado'] == 'Sim'
            agrupado_str = 'Sim' if agrupado else 'Não'
        if event == 'Salvar':
            if fig is None:
                sg.popup('Nenhum gráfico foi gerado ainda.', title='Salvar gráfico')
                continue
            if ultima_config is None:
                sg.popup('Execute uma simulação antes de salvar.', title='Salvar gráfico')
                continue

            pasta_saida = os.path.join(os.getcwd(), 'resultados')
            os.makedirs(pasta_saida, exist_ok=True)

            nome_arquivo = (
                f"regra_{ultima_config['regra']}"
                f"_tamanho_{ultima_config['tamanho']}"
                f"_passos_{ultima_config['passos']}"
                f"_estado_{normalizar_texto(ultima_config['tipo_ini'])}"
                f"_densidade_{str(ultima_config['densidade']).replace('.', '_')}"
                f"_agrupado_{'sim' if ultima_config['agrupado'] else 'nao'}"
                f"_classe_{normalizar_texto(ultima_config['classe'])}"
                f".png"
            )
            caminho_arquivo = os.path.join(pasta_saida, nome_arquivo)

            if os.path.exists(caminho_arquivo):
                resposta = sg.popup_yes_no(
                    f'O arquivo ja existe:\n{caminho_arquivo}\n\nDeseja sobrescrever?',
                    title='Arquivo existente'
                )
                if resposta != 'Yes':
                    window['info'].update('Salvamento cancelado: arquivo ja existente.')
                    continue

            fig.savefig(caminho_arquivo, dpi=300, bbox_inches='tight')
            window['info'].update(f'Gráfico salvo em: {caminho_arquivo}')
        if event == 'Simular':
            fig_anterior = fig
            regra = converter_valor(values['regra_txt'], 0, 255, inteiro=True)
            tamanho = converter_valor(values['tamanho_txt'], 21, 201, inteiro=True)
            passos = converter_valor(values['passos_txt'], 10, 200, inteiro=True)
            densidade = converter_valor(values['densidade_txt'], 0.05, 1.0, inteiro=False)
            if None in (regra, tamanho, passos, densidade):
                sg.popup('Confira os campos: regra (0-255), tamanho (21-201), passos (10-200), densidade (0.05-1.0).', title='Parâmetros inválidos')
                continue
            window['regra'].update(regra)
            window['tamanho'].update(tamanho)
            window['passos'].update(passos)
            window['densidade'].update(densidade)
            window['regra_txt'].update(str(regra))
            window['tamanho_txt'].update(str(tamanho))
            window['passos_txt'].update(str(passos))
            window['densidade_txt'].update(f"{densidade:.2f}")
            tipo_ini = values['tipo_ini']
            agrupado = values['agrupado'] == 'Sim'
            evolucao = simular(regra, tamanho, passos, tipo_ini, densidade, agrupado)
            # Tamanho menor e responsivo
            largura = max(5, min(8, tamanho/25))  # entre 5 e 8
            altura = max(3, min(5, passos/40))    # entre 3 e 5
            fig, ax = plt.subplots(figsize=(largura, altura))
            fig.subplots_adjust(top=0.80, bottom=0.18)  # aumenta a margem superior e inferior
            # Convenção de referência dos autômatos de Wolfram: t=0 na linha superior e tempo aumentando para baixo.
            # Também evita branco puro para estados 0 para melhorar visibilidade de padrões homogêneos.
            cmap_wolfram = ListedColormap(['#374151', '#f8fafc'])
            ax.imshow(
                evolucao,
                cmap=cmap_wolfram,
                vmin=0,
                vmax=1,
                interpolation='nearest',
                aspect='auto',
                origin='upper'
            )
            classe, metodo_classificacao, resumo_classificacao = classificar_regra_detalhada(regra)
            agrupado_str = 'Sim' if agrupado else 'Não'
            titulo = f"Regra {regra} | Classe: {classe}\nAgrupado: {agrupado_str} | Tamanho: {tamanho} | Passos: {passos}"
            ax.set_title(titulo)
            ax.set_xlabel('Células')
            ax.set_ylabel('Tempo (t=0 no topo)')
            window['info'].update(
                f"Classe: {classe} ({metodo_classificacao}). {resumo_classificacao}"
            )
            ultima_config = {
                'regra': regra,
                'tamanho': tamanho,
                'passos': passos,
                'tipo_ini': tipo_ini,
                'densidade': densidade,
                'agrupado': agrupado,
                'classe': classe,
            }
            if fig_agg:
                fig_agg.get_tk_widget().forget()
            fig_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
            if fig_anterior is not None:
                plt.close(fig_anterior)
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
