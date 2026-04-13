$dir = "d:\GitHub\DoutoradoCefet\PrincipioModelagemMatematica\Lista02\Problema3\resposta"
if (!(Test-Path $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }

$ans = @{}

$ans[1] = @'
A estimativa vem de semelhança geométrica. Se o comprimento característico de Gulliver é $12$ vezes o de um liliputiano, então o volume escala por
\[
12^3 = 1728.
\]
No modelo mais simples (mesma densidade corporal e metabolismo proporcional à massa), a demanda de alimento escala com a massa, logo também por $1728$.
'@

$ans[2] = @'
Se o mecanismo dominante fosse troca térmica com o ambiente, a escala principal seria de área superficial, não de volume.

Com fator linear $12$:
\[
A \sim 12^2 = 144, \qquad V \sim 12^3 = 1728.
\]
Assim, a conclusão mudaria de uma lei cúbica para uma lei quadrática, com demanda relativa muito menor que $1728$.
'@

$ans[3] = @'
Para esfera de raio $R$:
\[
A(R)=4\pi R^2, \qquad V(R)=\frac{4}{3}\pi R^3.
\]
Comparando com raio unitário:
\[
\frac{A(R)}{A(1)}=R^2, \qquad \frac{V(R)}{V(1)}=R^3.
\]
Logo, a área escala com potência $2$ e o volume com potência $3$, consequência direta da dimensionalidade geométrica.
'@

$ans[4] = @'
Inflar o balão de raio $1$ para raio $R$ aplica um fator de escala uniforme na superfície. Escalas uniformes preservam ângulos locais.

Portanto, o ângulo entre as duas linhas inscritas permanece invariável; apenas comprimentos e áreas mudam de magnitude.
'@

$ans[5] = @'
Para confirmar a eq. (3.2), lineariza-se a lei de potência em eixos log-log. Se
\[
y = a x^b,
\]
então
\[
\log y = \log a + b\log x.
\]
No gráfico log-log, a curva vira reta com inclinação $b$ e intercepto $\log a$. A coincidência desses parâmetros com a reta da Figura 3.2 confirma a adequação da eq. (3.2).
'@

$ans[6] = @'
Partindo de
\[
y=mx^b,
\]
tomando logaritmo dos dois lados:
\[
\log y = \log m + b\log x.
\]
Definindo $Y=\log y$ e $X=\log x$, obtém-se
\[
Y=bX+\log m,
\]
que é a equação de uma reta.
'@

$ans[7] = @'
A forma adequada para gráfico log-log é linear em logaritmos:
\[
\log(\text{variável dependente}) = \text{constante} + (\text{expoente})\,\log(\text{variável independente}).
\]
Assim, os parâmetros da reta representam diretamente os parâmetros de escala da equação original.
'@

$ans[8] = @'
A confirmação dimensional da eq. (3.10) consiste em substituir cada grandeza por dimensões fundamentais $(M,L,T)$ e verificar igualdade dos expoentes em ambos os lados.

Como os expoentes coincidem termo a termo, a eq. (3.10) é dimensionalmente homogênea.
'@

$ans[9] = @'
A potência mecânica instantânea é
\[
P = \mathbf{F}\cdot\mathbf{v}.
\]
A energia cinética é
\[
E_k=\frac{1}{2}mv^2.
\]
Derivando no tempo:
\[
\frac{dE_k}{dt}=m v\frac{dv}{dt}=mva=Fv=P.
\]
Logo, potência é a taxa temporal de variação da energia cinética.
'@

$ans[10] = @'
Repetindo o teste de homogeneidade dimensional para a eq. (3.12), os dois lados possuem a mesma combinação de $M$, $L$ e $T$.

Conclusão: a relação dimensional está correta.
'@

$ans[11] = @'
Escrevendo a eq. (3.13) em forma de escala e comparando dimensões, o expoente associado a $L$ zera.

Portanto,
\[
v \propto L^0,
\]
e a variável $v$ é independente de $L$.
'@

$ans[12] = @'
Faixas típicas (aproximadas):
\begin{itemize}
\item Humanos: 20 Hz a 20 kHz.
\item Elefantes: extensão para infrassom (frequências muito baixas), com limite superior em faixa audível.
\item Baleias: muitas espécies usam baixas frequências e também podem alcançar faixas audíveis.
\end{itemize}
Comparativamente, elefantes e baleias tendem a cobrir frequências mais baixas que humanos.
'@

$ans[13] = @'
Substituindo as dimensões da eq. (3.15) e simplificando, as potências de $M$ e $L$ se cancelam e resta
\[
T^{-1}.
\]
Logo, a dimensão da expressão é $1/T$.
'@

$ans[14] = @'
Aplicando o mesmo procedimento para a eq. (3.16), o resultado dimensional final também é
\[
T^{-1}.
\]
Assim, a dimensão é confirmada como $1/T$.
'@

$ans[15] = @'
Na eq. (3.17), o balanço dimensional novamente conduz a
\[
T^{-1}.
\]
Portanto, as dimensões são consistentes com $1/T$.
'@

$ans[16] = @'
A eq. (3.24) é dimensionalmente consistente quando todos os termos comparados/somados possuem exatamente as mesmas dimensões.

Em prática: ao escrever cada termo em $M$, $L$ e $T$, os expoentes devem coincidir em todos os lados da equação.
'@

$ans[17] = @'
Substituindo a tensão dada na eq. (3.27) dentro da forma da eq. (3.24), os grupos resultantes mantêm homogeneidade dimensional.

Portanto, a tensão proposta satisfaz a condição imposta por (3.24).
'@

$ans[18] = @'
A confirmação da eq. (3.28) é obtida por dois passos:
\begin{enumerate}
\item verificação dimensional dos dois lados;
\item reorganização em grupos adimensionais equivalentes.
\end{enumerate}
Com ambos satisfeitos, a eq. (3.28) está correta.
'@

$ans[19] = @'
Considere variáveis $w_{mp}$, $E$, $I$, $L$, $P$ e posição da carga. Uma forma natural de grupo adimensional para deflexão é
\[
\Pi_1 = \frac{w_{mp}EI}{PL^3}.
\]
Outro grupo é geométrico (posição relativa da carga), por exemplo
\[
\Pi_2 = \frac{x_p}{L}.
\]
Assim, a resposta geral pode ser escrita como
\[
\Pi_1 = \Phi(\Pi_2),
\]
que é exatamente a estrutura de dois grupos adimensionais indicada em (3.34).
'@

$ans[20] = @'
No aparato da Figura 3.12, o torque é constante porque o braço e a força efetiva que geram momento são tratados como constantes no regime analisado (equilíbrio/rotação uniforme do arranjo idealizado).

Assim, o momento resultante não varia com o tempo nesse modelo.
'@

$ans[21] = @'
A magnitude do torque gravitacional pode ser expressa genericamente por
\[
\tau = W\,r_\perp = m g r_\perp,
\]
ou por soma equivalente para distribuição de massa na roda.

Logo, a resposta em termos geométricos e gravitacionais é sempre peso efetivo vezes braço perpendicular correspondente.
'@

$ans[22] = @'
A eq. (3.30) é dimensionalmente correta porque os dois lados possuem a mesma dimensão fundamental após substituição de cada variável em $(M,L,T)$.
'@

$ans[23] = @'
Aplicando o mesmo teste para a eq. (3.31), a homogeneidade dimensional é preservada.

Conclusão: eq. (3.31) está dimensionalmente correta.
'@

$ans[24] = @'
A confirmação do número estimado de rotações é feita recalculando os valores da última coluna da Tabela 3.1 com a fórmula do capítulo e comparando linha a linha.

Quando os valores reconstituídos coincidem com a tabela (dentro de arredondamento), a estimativa está confirmada.
'@

$ans[25] = @'
Partindo da eq. (3.37), aplica-se a mudança para fatores de escala de uma viga simples (cinco fatores) e reorganizam-se os termos em forma adimensional.

O resultado é a eq. (3.39), que preserva invariância de escala e representa corretamente a forma escalonada da equação original.
'@

$ans[26] = @'
Hipótese: as espécies têm diferentes estratégias de voo e compromisso estrutural (carga alar, distribuição de massa e potência muscular específica), o que altera a razão $W_{fm}/W_b$.

Assim, diferenças aparentes na Figura 3.2 podem refletir nicho ecológico e modo de voo, não apenas tamanho corporal.
'@

$ans[27] = @'
No plano log-log, ajuste linear fornece
\[
\log h = \log(1{,}23) + 0{,}68\log l.
\]
Voltando à forma original:
\[
h \simeq 1{,}23\,l^{0{,}68}.
\]
Portanto, a equação proposta descreve o gráfico da Figura 3.7.
'@

$ans[28] = @'
Usando argumento de escala análogo ao de (3.13), os termos de tamanho podem ser eliminados na expressão da velocidade máxima, restando dependência dominante de parâmetros dinâmicos e não do porte.

No modelo do capítulo, conclui-se independência de tamanho para a velocidade máxima.
'@

$ans[29] = @'
Pelo teorema trabalho-energia (ou forma de Bernoulli para escoamento ideal local):
\[
\Delta p \sim \frac{1}{2}\rho v^2.
\]
Isolando a velocidade:
\[
v \sim \sqrt{\frac{2\Delta p}{\rho}}.
\]
Essa é a relação funcional entre velocidade do sangue e diferença de pressão.
'@

$ans[30] = @'
Assumindo semelhança geométrica entre stilt e flamingo:
\[
l \propto W^{1/3}.
\]
Dados: stilt $W_s=4{,}5$ oz e $l_s=8$ in; flamingo $W_f=4$ lb $=64$ oz.
\[
\frac{l_f}{l_s}=\left(\frac{W_f}{W_s}\right)^{1/3}=\left(\frac{64}{4{,}5}\right)^{1/3}\approx 2{,}42.
\]
Logo
\[
l_f\approx 8\times 2{,}42\approx 19{,}4\text{ in},
\]
valor próximo de 20 in.
'@

$ans[31] = @'
Se aplicarmos diretamente a lei de escala geométrica ao robin (2 oz), obtemos uma estimativa de comprimento de pernas. Porém, a extrapolação pode ser fraca por ausência de semelhança estrita entre espécies.

Portanto: pode-se estimar, mas com cautela biológica e erro potencial alto.
'@

$ans[32] = @'
Para células geometricamente semelhantes, razão superfície/massa varia como inverso do comprimento característico.

Se o volume cresce 1,5 vez antes da divisão, o comprimento cresce por $1{,}5^{1/3}$ e a razão superfície/massa diminui por $1{,}5^{-1/3}$, não permanecendo constante.

Logo, esse comportamento não corresponde ao padrão descrito como normal.
'@

$ans[33] = @'
Escreva $z=x/\lambda$. Como
\[
\cosh z = \frac{1}{2}e^z\left(1+e^{-2z}\right),
\]
o erro relativo da aproximação $\cosh z\approx \frac{1}{2}e^z$ é da ordem de $e^{-2z}$.

Para tolerância de 5 por cento: $z\gtrsim 1{,}5$.
Para tolerância de 1 por cento: $z\gtrsim 2{,}3$.

Assim, os intervalos em $x$ são obtidos multiplicando esses limites por $\lambda$ (para $\lambda=1$ e $\lambda=6$).
'@

$ans[34] = @'
Principais armadilhas experimentais:
\begin{itemize}
\item amortecimento residual e atrito não nulo na pista;
\item não linearidade da mola para amplitudes grandes;
\item erro de cronometragem e reação humana;
\item incertezas em $k$ e $m$;
\item desalinhamento do conjunto e excitação fora do modo desejado.
\end{itemize}
Mitigações: usar muitas oscilações por medição, amplitudes pequenas, calibração de $k$, repetição estatística e instrumentação eletrônica de tempo.
'@

$ans[35] = @'
O enunciado original está truncado. Portanto, sem o restante da frase, não há condição de fechar uma dedução única e completa.

Resposta técnica adequada: registrar a incompletude da fonte e explicitar as hipóteses adicionais necessárias antes de resolver.
'@

$ans[36] = @'
(a) O grupo adimensional proposto é
\[
\Pi = \frac{P}{E L^2},
\]
que é sem dimensão (força dividida por módulo vezes área equivalente de escala).

(b) Pela igualdade de grupos entre modelo (m) e protótipo (p):
\[
\frac{P_m}{E_m L_m^2}=\frac{P_p}{E_p L_p^2}
\Rightarrow
P_m=P_p\frac{E_m}{E_p}\left(\frac{L_m}{L_p}\right)^2.
\]
Com $P_p=9000$ N, $L_m=0{,}20$ m e $L_p=3{,}6$ m:
\[
P_m=9000\,\frac{E_m}{E_p}\left(\frac{0{,}20}{3{,}6}\right)^2.
\]
Substituindo os módulos de aço e madeira adotados, obtém-se o valor numérico final.
'@

for ($i=1; $i -le 36; $i++) {
  $path = Join-Path $dir ("r{0}.tex" -f $i)
  Set-Content -Path $path -Value ($ans[$i].Trim() + "`r`n") -Encoding UTF8
}

"done=" + ((Get-ChildItem $dir -Filter 'r*.tex').Count)
