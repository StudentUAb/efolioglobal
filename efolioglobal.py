
# UC: 21048 - Física Geral 
# Ano 2022/23 - EFOLIO Global 
# - Calcule a velocidade e rapidez do barco 
#   quando sai da zona com corrente horizontal
# - UAb
#  Aluno: 2100927 - Ivo Baptista 
# segund a lei de newton 
# F = m * a
# então deduzimos que a=f/m obtendo a aceleraçao do barco

m = 80.0  # massa do barco (kg)
v0 = 7.0  # velocidade constante (nós)
vx0 = v0 * 1.852 / 3.600  # velocidade inicial segundo x
Fx = lambda t: 200 * (4*t - t**2)  # força x

# Constantes e intervalo de tempo
h = 1.0  # passo de integração (segundos)
t0 = 0.0  # tempo inicial (segundos)
tf = 4.0  # tempo final (segundos)
n = int((tf - t0) / h) + 1  # número de iterações

# Listas para guardar t, vx, k1 e k2
t = [0.0] * n
vx = [0.0] * n
k1 = [0.0] * n
k2 = [0.0] * n

# Iniciais
t[0] = t0
vx[0] = vx0

# Método de Huen
for i in range(n-1):
    k1[i] = Fx(t[i]) / m  #aplicando a=f/m
    k2[i] = Fx(t[i] + h) / m #a=f/m mas acrescentamos o passo h
    vx[i+1] = vx[i] + h * k1[i] # o incremento da velocidade
    t[i+1] = t[i] + h
    # Impressão dos resultados comparando valor de v com o vx no array é o mesmo
    print(f"t = {t[i+1]:.2f}s, vx = {vx[i+1]:.2f}m/s, k1 = {k1[i]:.2f}, k2 = {k2[i]:.2f}")
