$base = "d:\GitHub\DoutoradoCefet\PrincipioModelagemMatematica\Lista03\Problema4"
$edir = Join-Path $base "enunciado"

$pt = @'
\begin{enumerate}
    \item[\textbf{Problema 4.1.}] Mostre que a eq. (4.7) pode ser obtida substituindo $ix$ por $x$ na eq. (4.6).
    \item[\textbf{Problema 4.2.}] Determine os primeiros quatro termos das expansões de Taylor de $\tan x$ e $\cot x$ sobre $x = 0$.
    \item[\textbf{Problema 4.3.}] Determine os quatro primeiros termos das expansões de Taylor de $\tanh x$ e $\coth x$ sobre $x = 0$.
    \item[\textbf{Problema 4.4.}] Use a análise dimensional para determinar como o parâmetro catenário, $c$, está relacionado ao componente horizontal constante da tensão do cabo, $T_0$, e seu peso por unidade de comprimento (ou peso unitário), $\gamma$.
    \item[\textbf{Problema 4.5.}] Quanta curvatura de fita (sag) é permitida para medir uma distância de 50 m com precisão de 5%? Dentro de 2%?.
    \item[\textbf{Problema 4.6.}] O que pesa um corpo que pesa 10 N na superfície da Terra a uma altura de 10 m? No pico do Monte Everest? (Dica: você pode ter que procurar alguns fatos sobre o nosso planeta!).
    \item[\textbf{Problema 4.7.}] De acordo com a eq. (4.30), em que altitude o peso de 10 N na superfície da Terra cairia para 9 N? Para 5 N?.
    \item[\textbf{Problema 4.8.}] Compare os resultados obtidos no Problema 4.7 com os resultados mais exatos obtidos usando a eq. (4.29).
    \item[\textbf{Problema 4.9.}] O que pesa um corpo que pesa 10 N na superfície da Terra na superfície da lua? Na superfície do planeta Plutão? Na superfície do planeta Marte? (Dica: você pode ter que procurar alguns fatos sobre o ambiente de nossos planetas!).
    \item[\textbf{Problema 4.10.}] Se o potencial gravitacional correspondente à lei da gravitação de Newton (eq. (4.25)) é dado por $V_g = -GM_Em/R$, encontre a expressão exata que define esse potencial em função da altitude, $z$, a partir da superfície da Terra.
    \item[\textbf{Problema 4.11.}] Escreva uma expansão binomial dos resultados do Problema 4.10 para determinar a energia potencial acima da superfície da Terra para a primeira ordem em $z$.
    \item[\textbf{Problema 4.12.}] Preencha os elementos ausentes da tabela a seguir para a ordem de dois termos: $\sin x$, $\cos x$, $1 - \sin x$, $1 - \cos x$.
    \item[\textbf{Problema 4.13.}] Preencha os elementos ausentes da tabela a seguir para a ordem de dois termos: $\sinh x$, $\cosh x$, $1 - \sinh x$, $1 - \cosh x$.
    \item[\textbf{Problema 4.14.}] Desenvolva um coeficiente de expansão de volume, $\beta$, para um sólido de comprimento $L_0$, largura $W_0$ e altura $H_0$, que seja paralelo ao coeficiente de superfície, $\gamma$, da eq. (4.37).
    \item[\textbf{Problema 4.15.}] A que diferença de temperatura um sólido de alumínio teria de ser submetido para o coeficiente de superfície de expansão produzir erros de 1% na mudança de área em comparação com a mudança exata de área?.
    \item[\textbf{Problema 4.16.}] A que diferença de temperatura um sólido de alumínio teria que ser submetido ao coeficiente de expansão de volume para produzir erros de 1% na mudança de área em comparação com a mudança exata de área?.
    \item[\textbf{Problema 4.17.}] Arredonde cada um dos seguintes números para dois (2) algarismos significativos: (a) 5,237 (b) 0,82549 (c) 81,356 (d) $\pi$ (e) 6,2305 (f) 0,0428 (g) 10,45 (h) 4,035.
    \item[\textbf{Problema 4.18.}] Arredonde cada um dos seguintes números para três (3) algarismos significativos: (a) 5,237 (b) 0,82549 (c) 81,356 (d) $\pi$ (e) 6,2305 (f) 0,0428 (g) 10,45 (h) 4,035.
    \item[\textbf{Problema 4.19.}] Complete as seguintes multiplicações e expresse os resultados para o número correto de algarismos significativos: (a) $(6,28 \times 10^3) \times 2,712$ (b) $43,32 \times 0,3$ (c) $928 \times 4,23$.
    \item[\textbf{Problema 4.20.}] 99,9 e 100,1 têm o mesmo número de algarismos significativos? Explique sua resposta.
    \item[\textbf{Problema 4.21.}] Estime os intervalos dentro dos quais cada um dos seguintes números se encontra: (a) 7,7 (b) 7,70 (c) 1200 (d) $1,200 \times 10^{-3}$.
    \item[\textbf{Problema 4.22.}] Em que porcentagem o período de um pêndulo mudaria se seu comprimento fosse reduzido pela metade? Se fosse reduzido em um terço? Se o comprimento fosse reduzido para um terço de seu comprimento original?.
    \item[\textbf{Problema 4.23.}] Explique por que o período do pêndulo aumenta em 145% na lua.
    \item[\textbf{Problema 4.24.}] Como o período de um pêndulo mudaria, em comparação com seu valor na Terra, se o pêndulo estivesse em Marte? Em Plutão?.
    \item[\textbf{Problema 4.25.}] Como o período de um pêndulo mudaria em função de sua altura, $h$, acima da superfície da Terra? (Dica: A variação da aceleração gravitacional $g$ pode ser representada como uma função de $h$ a partir da lei da atração gravitacional de Newton).
    \item[\textbf{Problema 4.26.}] Desenhe dois alvos circulares de arco e flecha e use-os para representar os padrões de acerto de (a) um arqueiro que é exato (accurate), mas não preciso (precise); e (b) um arqueiro que é preciso, mas não exato.
    \item[\textbf{Problema 4.27.}] Verifique as formas finais das eqs. (4.51) e (4.52).
    \item[\textbf{Problema 4.28.}] Verifique as equações para $m$ e $b$ dadas nas eqs. (4.53) e (4.54).
    \item[\textbf{Problema 4.29.}] Discuta e explique as diferenças dimensionais entre as eqs. (4.53) e (4.54).
    \item[\textbf{Problema 4.30.}] Verifique os termos na terceira e quarta colunas da Tabela 4.3, bem como as somas de todas as quatro colunas.
    \item[\textbf{Problema 4.31.}] Verifique os cálculos de $m$ e $b$ encontrados nos resultados da Tabela 4.3.
    \item[\textbf{Problema 4.32.}] Determinar o desvio-padrão dos dados apresentados no quadro 4.4.
    \item[\textbf{Problema 4.33.}] Desenhe um histograma para os dados na Tabela 4.4 com 10 intervalos de largura de 4 dB.
    \item[\textbf{Problema 4.34.}] Mostre que o quadrado da variância amostral da eq. (4.57) pode ser lançado na forma alternativa $s^2 = \frac{1}{(n-1)} \left[ \sum_{i=1}^n x_i^2 - \frac{1}{n} \left(\sum_{i=1}^n x_i\right)^2 \right]$.
    \item[\textbf{Problema 4.35.}] Estime o erro cometido na aproximação de $y(x) = \sin x$ com uma fórmula de Taylor para $n = 4$ calculando o restante $R_5$.
    \item[\textbf{Problema 4.36.}] As afirmações de que $\sin x \simeq x$ e $\tan x \simeq x$ produzem aproximações semelhantes? Confirme e explique sua resposta.
    \item[\textbf{Problema 4.37.}] As leituras de um voltímetro analógico antiquado (ele tem mostradores, não leituras digitais!) estão sujeitas a algum erro sistemático quando todas as suas leituras são muito grandes. Descobriu-se que a magnitude do erro varia linearmente de 1 V com uma leitura de discagem de 5 V a 4 V com uma leitura de discagem de 80 V. (a) Quais são as tensões corretas para leituras de discagem de 80, 100, 50, 1, 35 e 10 V? (b) Qual é o erro percentual para cada uma das seis (6) leituras da parte (a)?.
    \item[\textbf{Problema 4.38.}] (a) É possível dispor de um conjunto de medições precisas, mas não exatas? Explicar. (b) É possível ter um conjunto de medições exatas, mas não precisas? Explicar.
    \item[\textbf{Problema 4.39.}] (a) Escreva a expansão da série de Taylor para $e^x$ sobre $x = 0$. (b) Calcule $e^{0,5}$ para cinco algarismos significativos usando os quatro primeiros termos da série encontrada na parte (a).
    \item[\textbf{Problema 4.40.}] (a) Que erro percentual foi incorrido no cálculo da parte (b) do Problema 4.39 se o valor real de $e^{0,5}$ for 1,6487? (b) Use o resto de Taylor (eq. (4.5)) para calcular o erro em $e^{0,5}$ após apenas quatro termos. O erro calculado na parte (a) deste problema é aceitável? Explicar.
    \item[\textbf{Problema 4.41.}] Avalie a seguinte função manualmente (sem calculadoras ou computadores, por favor) para $x = 4$: $(1 + 2/x)^{1/4}$.
    \item[\textbf{Problema 4.42.}] Como é que um observador sabe quando é suficiente, que foram feitas medições suficientes?.
    \item[\textbf{Problema 4.43.}] Faça uma lista de cinco novos exemplos (ou seja, não encontrados no texto) de erros sistemáticos.
    \item[\textbf{Problema 4.44.}] Faça uma lista de cinco novos exemplos (ou seja, não encontrados no texto) de erros aleatórios.
    \item[\textbf{Problema 4.45.}] A resistência de um resistor, $R$, é feita passando várias correntes, $I$, através dele e medindo as quedas de tensão correspondentes, $V$, e correntes com medidores analógicos imprecisos. Os dados resultantes são: $x_i = V$ (V): 10, 20, 30, 40, 50, 60, 70, 80; $y_i = I$ (A): 0.8, 1.1, 2.5, 4.2, 4.3, 4.7, 5.8, 6.4. (a) Que tipos de erro serão encontrados nos dados? (b) Supondo que $V = IR$, plote os dados (manualmente!) e estime visualmente (globo ocular) a linha de melhor ajuste para esses dados.
    \item[\textbf{Problema 4.46.}] Use o método dos mínimos quadrados para traçar uma curva $V$ versus $I$ para os dados do Problema 4.45. Como ele se compara com o resultado visual (globo ocular) do Problema 4.45?.
    \item[\textbf{Problema 4.47.}] Os dados apresentados a seguir compreendem 100 leituras dos níveis de ruído efetuados a 6 milhas de distância de um aeroporto, efetuadas tarde da noite a intervalos de 15 segundos. Encontre a média, a mediana e o desvio padrão desses dados.
    \item[\textbf{Problema 4.48.}] Os números estrelados nos dados do Problema 4.47 são leituras feitas enquanto uma aeronave estava voando diretamente acima. Se esses dados forem excluídos, quais são a média, a mediana e o desvio padrão dos 88 pontos de dados restantes?.
    \item[\textbf{Problema 4.49.}] Traçar (a) um histograma de todos os dados do problema 4.47 e (b) uma curva contínua do número de leituras em função do nível de ruído medido.
    \item[\textbf{Problema 4.50.}] Determinar a aproximação de campo distante da função $f(r)$ dada abaixo como uma expansão binomial para valores de $r \gg a$: $f(r) = \sqrt{a^2 + r^2}$.
    \item[\textbf{Problema 4.51.}] O potencial elétrico, $V_e$, à distância, $r$, ao longo do eixo de revolução de um disco de raio $a$ é dado por $V_e = \frac{q}{2\pi a^2 \varepsilon_0}(\sqrt{a^2 + r^2} - r)$, onde $q$ é a carga total que é distribuída uniformemente sobre a superfície do disco e $\varepsilon_0$ é a constante de permissividade. Usando os resultados do Problema 4.50, encontre uma aproximação de campo distante para o potencial elétrico para valores de $r \gg a$.
    \item[\textbf{Problema 4.52.}] Compare o número mínimo de termos mantidos nas expansões binomiais das soluções para os problemas 4.50 e 4.51. Esses números são iguais ou não? Por que esses números são iguais ou não?.
    \item[\textbf{Problema 4.53.}] Suponha que precisamos calcular a extensão radial ou deflexão $w$ de um balão esférico muito fino, o que significa que o raio da esfera se estende de $R$ a $R + w$ à medida que o balão é pressurizado. É feito de material elástico. Um colega encontra um livro didático que mostra uma fórmula para a pressão, $p$, que parece razoável: $w/R = pR/Eh$, onde $h$ é a espessura da parede do balão e $E$ é o módulo do material do qual a esfera é feita. Esta equação é dimensionalmente consistente?.
    \item[\textbf{Problema 4.54.}] Analise o comportamento limite da equação apresentada no Problema 4.53 à medida que a pressão, o módulo, o raio e a espessura vão para zero e se tornam infinitamente grandes. Esse comportamento limite está de acordo com sua estimativa intuitiva do que deve acontecer?.
    \item[\textbf{Problema 4.55.}] Use a equação do Problema 4.53 para derivar uma estimativa da magnitude da pressão, $p$, como uma fração do módulo, $E$. Estimar a fração de pressão para uma esfera de paredes finas, para a qual $h/R \ll 1$.
\end{enumerate}
'@

$en = @'
\begin{enumerate}
    \item[\textbf{Problem 4.1.}] Show that eq. (4.7) can be obtained by substituting $ix$ for $x$ in eq. (4.6).
    \item[\textbf{Problem 4.2.}] Determine the first four terms of the Taylor expansions of $\tan x$ and $\cot x$ about $x = 0$.
    \item[\textbf{Problem 4.3.}] Determine the first four terms of the Taylor expansions of $\tanh x$ and $\coth x$ about $x = 0$.
    \item[\textbf{Problem 4.4.}] Use dimensional analysis to determine how the catenary parameter, $c$, is related to the constant horizontal component of the cable tension, $T_0$, and its weight per unit length (or unit weight), $\gamma$.
    \item[\textbf{Problem 4.5.}] How much tape sag is permissible to measure a 50 m distance accurately to within 5%? Within 2%?.
    \item[\textbf{Problem 4.6.}] What does a body that weighs 10 N at the earth’s surface weigh at a height of 10 m? At the peak of Mt. Everest? (Hint: You might have to look up some facts about our planet!).
    \item[\textbf{Problem 4.7.}] According to eq. (4.30), at what altitude would the weight of 10 N at the earth’s surface drop to 9 N? To 5 N?.
    \item[\textbf{Problem 4.8.}] Compare the results obtained in Problem 4.7 with more exact results obtained by using eq. (4.29).
    \item[\textbf{Problem 4.9.}] What does a body that weighs 10 N at the earth’s surface weigh on the surface of the moon? On the surface of the planet Pluto? On the surface of the planet Mars? (Hint: You might have to look up some facts about our planet’s environment!).
    \item[\textbf{Problem 4.10.}] If the gravitational potential corresponding to Newton’s law of gravitation (eq. (4.25)) is given by $V_g = -Gm_em / R$, find the exact expression that defines this potential as a function of altitude, $z$, from the earth’s surface.
    \item[\textbf{Problem 4.11.}] Write a binomial expansion of the results of Problem 4.10 to determine the potential energy above the earth’s surface to the first order in $z$.
    \item[\textbf{Problem 4.12.}] Fill in the missing elements of the following table to two-term order: $\sin x$, $\cos x$, $1-\sin x$, $1-\cos x$.
    \item[\textbf{Problem 4.13.}] Fill in the missing elements of the following table to two-term order: $\sinh x$, $\cosh x$, $1-\sinh x$, $1-\cosh x$.
    \item[\textbf{Problem 4.14.}] Develop a volume coefficient of expansion, $\beta$, for a solid of length $L_0$, width $W_0$, and height $H_0$, that parallels the surface coefficient, $\gamma$, of eq. (4.37).
    \item[\textbf{Problem 4.15.}] To what temperature difference would an aluminum solid have to be subjected for the surface coefficient of expansion to produce errors of 1% in the area change compared to the exact area change?.
    \item[\textbf{Problem 4.16.}] To what temperature difference would an aluminum solid have to be subjected for the volume coefficient of expansion to produce errors of 1% in the area change compared to the exact area change?.
    \item[\textbf{Problem 4.17.}] Round off each of the following numbers to two (2) significant figures: (a) 5.237 (b) 0.82549 (c) 81.356 (d) $\pi$ (e) 6.2305 (f) 0.0428 (g) 10.45 (h) 4.035.
    \item[\textbf{Problem 4.18.}] Round off each of the following numbers to three (3) significant figures: (a) 5.237 (b) 0.82549 (c) 81.356 (d) $\pi$ (e) 6.2305 (f) 0.0428 (g) 10.45 (h) 4.035.
    \item[\textbf{Problem 4.19.}] Complete the following multiplications and express the results to the correct number of significant figures: (a) $(6.28 \times 10^3) \times 2.712$ (b) $43.32 \times 0.3$ (c) $928 \times 4.23$.
    \item[\textbf{Problem 4.20.}] Do 99.9 and 100.1 have the same number of significant figures? Explain your answer.
    \item[\textbf{Problem 4.21.}] Estimate the ranges within which each of the following numbers lie: (a) 7.7 (b) 7.70 (c) 1200 (d) $1.200 \times 10^{-3}$.
    \item[\textbf{Problem 4.22.}] By what percentage would the period of a pendulum change if its length was halved? If it was reduced by one-third? If the length was reduced to one-third of its original length?.
    \item[\textbf{Problem 4.23.}] Explain why the pendulum period increases by 145% on the moon.
    \item[\textbf{Problem 4.24.}] How would the period of a pendulum change, compared to its value on earth, if the pendulum was on Mars? On Pluto?.
    \item[\textbf{Problem 4.25.}] How would the period of a pendulum change as a function of its height, $h$, above the surface of the earth? (Hint: The variation of the gravitational acceleration $g$ can be represented as a function of $h$ from Newton’s law of gravitational attraction).
    \item[\textbf{Problem 4.26.}] Draw two circular archery targets and use them to depict the hit patterns of (a) an archer who is accurate, but not precise; and (b) an archer who is precise, but not accurate.
    \item[\textbf{Problem 4.27.}] Verify the final forms of eqs. (4.51) and (4.52).
    \item[\textbf{Problem 4.28.}] Verify the equations for $m$ and $b$ given in eqs. (4.53) and (4.54).
    \item[\textbf{Problem 4.29.}] Discuss and explain the dimensional differences between eqs. (4.53) and (4.54).
    \item[\textbf{Problem 4.30.}] Verify the terms in the third and fourth columns of Table 4.3, as well as the sums of all four columns.
    \item[\textbf{Problem 4.31.}] Verify the calculations of $m$ and $b$ found from the results in Table 4.3.
    \item[\textbf{Problem 4.32.}] Determine the standard deviation for the data presented in Table 4.4.
    \item[\textbf{Problem 4.33.}] Draw a histogram for the data in Table 4.4 with 10 intervals of 4 dB width.
    \item[\textbf{Problem 4.34.}] Show that the square of the sample variance of eq. (4.57) can be cast in the alternative form $s^2 = \frac{1}{(n-1)} \left[ \sum_{i=1}^n x_i^2 - \frac{1}{n} \left(\sum_{i=1}^n x_i\right)^2 \right]$.
    \item[\textbf{Problem 4.35.}] Estimate the error made in approximating $y(x) = \sin x$ with a Taylor’s formula to $n = 4$ by evaluating the remainder $R_5$.
    \item[\textbf{Problem 4.36.}] Do the statements that $\sin x \simeq x$ and $\tan x \simeq x$ produce similar approximations? Confirm and explain your answer.
    \item[\textbf{Problem 4.37.}] The readings of an old-fashioned analog voltmeter are subject to some systematic error where all of its readings are too large. The magnitude of the error has been found to vary linearly from 1 V at a dial reading of 5 V to 4 V at a dial reading of 80 V. (a) What are the correct voltages for dial readings of 80, 100, 50, 1, 35, and 10 V? (b) What is the percentage error for each of the six readings in part (a)?.
    \item[\textbf{Problem 4.38.}] (a) Is it possible to have a set of measurements that are precise but not accurate? Explain. (b) Is it possible to have a set of measurements that are accurate but not precise? Explain.
    \item[\textbf{Problem 4.39.}] (a) Write the Taylor series expansion for $e^x$ about $x = 0$. (b) Calculate $e^{0.5}$ to five significant figures using the first four terms of the series found in part (a).
    \item[\textbf{Problem 4.40.}] (a) What percentage error was incurred in the calculation of part (b) of Problem 4.39 if the true value of $e^{0.5}$ is 1.6487? (b) Use the Taylor remainder (eq. (4.5)) to calculate the error in $e^{0.5}$ after only four terms. Is the error calculated in part (a) acceptable? Explain.
    \item[\textbf{Problem 4.41.}] Evaluate the following function by hand for $x = 4$: $(1 + 2/x)^{1/4}$.
    \item[\textbf{Problem 4.42.}] How does an observer know when enough measurements have been taken?.
    \item[\textbf{Problem 4.43.}] Make a list of five new examples of systematic errors.
    \item[\textbf{Problem 4.44.}] Make a list of five new examples of random errors.
    \item[\textbf{Problem 4.45.}] The resistance of a resistor, $R$, is estimated by passing several currents, $I$, through it and measuring corresponding voltage drops, $V$, and currents with imprecise analog meters. Data: $x_i = V$ (V): 10, 20, 30, 40, 50, 60, 70, 80; $y_i = I$ (A): 0.8, 1.1, 2.5, 4.2, 4.3, 4.7, 5.8, 6.4. (a) What kinds of error will be found? (b) Assuming $V = IR$, plot and eyeball the best-fit line.
    \item[\textbf{Problem 4.46.}] Use the method of least squares to plot a $V$ versus $I$ curve for the data of Problem 4.45. How does it compare with the eyeball result?.
    \item[\textbf{Problem 4.47.}] The data comprise 100 readings of noise levels taken 6 mi away from an airport, at 15 s intervals. Find mean, median, and standard deviation.
    \item[\textbf{Problem 4.48.}] The starred numbers in Problem 4.47 were taken while an aircraft flew overhead. If those are deleted, what are the mean, median, and standard deviation of the remaining 88 points?.
    \item[\textbf{Problem 4.49.}] Draw (a) a histogram of all data of Problem 4.47 and (b) a continuous curve of number of readings versus measured noise level.
    \item[\textbf{Problem 4.50.}] Determine a far-field approximation of $f(r)=\sqrt{a^2+r^2}$ as a binomial expansion for $r \gg a$.
    \item[\textbf{Problem 4.51.}] The electric potential at distance $r$ along the axis of a disk of radius $a$ is $V_e = \frac{q}{2\pi a^2 \varepsilon_0}(\sqrt{a^2 + r^2} - r)$. Using Problem 4.50, find a far-field approximation for $r \gg a$.
    \item[\textbf{Problem 4.52.}] Compare the minimum number of terms kept in the binomial expansions of Problems 4.50 and 4.51. Are they the same? Why or why not?.
    \item[\textbf{Problem 4.53.}] Suppose we need radial extension or deflection $w$ of a very thin spherical balloon, with radius extending from $R$ to $R+w$ under pressure. Formula proposed: $w/R = pR/Eh$, where $h$ is wall thickness and $E$ is modulus. Is this dimensionally consistent?.
    \item[\textbf{Problem 4.54.}] Analyze limit behavior of Problem 4.53 as pressure, modulus, radius, and thickness go to zero and to infinity. Does this behavior match intuition?.
    \item[\textbf{Problem 4.55.}] Use the equation in Problem 4.53 to estimate pressure magnitude $p$ as a fraction of modulus $E$. Estimate this fraction for a thin-walled sphere with $h/R \ll 1$.
\end{enumerate}
'@

Set-Content -Path (Join-Path $edir "enunciado_pt.tex") -Value $pt -Encoding UTF8
Set-Content -Path (Join-Path $edir "enunciado_en.tex") -Value $en -Encoding UTF8

$pattern = '\\item\[\\textbf\{Problema 4\.(\d+)\.\}\]\s*(.*?)(?=\r?\n\s*\\item\[\\textbf\{Problema 4\.|\r?\n\\end\{enumerate\})'
$matches = [regex]::Matches($pt, $pattern, [System.Text.RegularExpressions.RegexOptions]::Singleline)
foreach ($m in $matches) {
    $n = [int]$m.Groups[1].Value
    $body = $m.Groups[2].Value.Trim()
    Set-Content -Path (Join-Path $edir ("e{0}.tex" -f $n)) -Value ($body + "`r`n") -Encoding UTF8
}

$lista = Join-Path $base "lista.tex"
$c = Get-Content -Path $lista -Raw
$c = $c -replace 'Problemas 3\.1 a 3\.36','Problemas 4.1 a 4.55'
$c = $c -replace '\\foreach \\i in \{1,\.\.\.,36\}','\\foreach \\i in {1,...,55}'
$c = $c -replace 'Problema 3\\.\\i','Problema 4.\\i'
Set-Content -Path $lista -Value $c -Encoding UTF8

"updated_items=" + $matches.Count
"e_files=" + ((Get-ChildItem $edir -Filter 'e*.tex').Count)
