#Fillipe Pinheiro Lima da Silva - NUSP: 11260443 - Turma 1
#Luigi Hideki Tanaka - NUSP: 11375246 - Turma 7

import numpy as np
"""import sympy as sp"""

np.set_printoptions(threshold=np.inf)                                                   #para imprimir a matriz dos autovetores para n=32 completa 

#interface com o usuário
5
item = str(input("Qual item deseja ser utilizado? (a,b ou c) "))
desl = str(input("Com deslocamento? (com ou sem) "))

#configurações para o item a
if item == 'a':                                                                         
    n = int(input("Tamanho da matriz A: "))                             
    massa = 0                                                                           #a massa não é utilizada no item a

#configurações para os itens b e c
else:                                                                                   
    exist = str(input("Deseja executar algum dos casos já existentes? (sim ou nao) "))  #possibilidade np.set_printoptions(threshold=np.inf)de criar caso personalizado  
    
    #casos do enunciado
    if exist == 'sim':
        caso = int(input("Qual caso? (1,2 ou 3) "))
        
        #casos 1 e 2 do item b
        if item == 'b':
            n = 5
            massa = 2
            if caso == 1:
                X0 = [-2, -3, -1, -3, -1]                                       #posições iniciais das massas do caso 1 - item b
            elif caso == 2:
                X0 = [1, 10, -4, 3, -2]                                         #posições iniciais das massas do caso 2 - item b
        
        #casos 1 e 2 do item c
        if item == 'c':
            n = 10
            massa = 2
            if caso == 1:
                X0 = [-2, -3, -1, -3, -1, -2, -3, -1, -3, -1]                   #posições iniciais das massas do caso 1 - item c
            elif caso == 2:
                X0 = [1, 10, -4, 3, -2, 1, 10, -4, 3, -2]                       #posições iniciais das massas do caso 2 - item c
        
        #caso 3 dos itens b e c precisa ser definido depois do cálculo dos autovetores, portanto foi definido no depois da decomposição QR
    
    #casos personalizados
    else:                                                                        
        caso = "personalizado"
        n = int(input("Insira a quantidade de massas: "))                       #quantidade de massas personalizada
        massa = float(input("Insira o valor de cada uma das massas em Kg: "))   #massa personalizada
        X0 = []                                                                 #vetor da posições iniciais
        for i in range(n): 
            pos = float(input("Posição inicial da massa %s: " % (i+1) ))        #posição inicial da massa i
            X0.append(pos)                                                      #armazena a posição inicial da massa i em X


#-------------------------------------------------------------------------------------------------------------------------------

#Definindo as funções que serão utilizadas

#função que gera a matriz tridiagonal A
def A_gen(n, item, massa):
    #gera a matriz A do item a
    if item == 'a':                                          
        A = 2*np.eye(n)                                      #incia A com todos os elementos da diag. principal iguais a 2
        for i in range(n-1):
            A[i,i+1], A[i+1,i] = -1, -1                      #transforma os elementos das subdiagonais em -1
        return A
    
    #gera a matriz A dos itens b e c
    else:
        if item == 'b': 
            A = np.eye(n)                                    #incia A como a matriz identidade de ordem n
            K = np.zeros(n+1)                                #vetor que armazena as constantes elásticas das molas
            for i in range(n+1):
                K[i] = 40 + 2*(i+1)                          #define a constante elástica da mola i do item b
                
        if item == 'c':
            A = np.eye(n)                                    #incia A como a matriz identidade de ordem n
            K = np.zeros(n+1)                                #vetor que armazena as constantes elásticas das molas
            for i in range(n+1):
                K[i] = 40 + 2*(-1)**(i+1)                    #define a constante elástica da mola i do item c
                
        for i in range(n):
            if i != n-1:
                A[i,i] = K[i] + K[i+1]
                A[i,i+1] = -K[i+1]
                A[i+1,i] = -K[i+1]
            A[n-1,n-1] = K[n-1] + K[n]
        A = (1/massa) * A                                    #divide a matriz A pelo valor da massa
        return A

#função para gerar o vetor Y
"""def Y_gen(X0):
    t = sp.symbols('t')                                      #criação da variável tempo
    Y = [t]*n               
    coef = np.zeros(n)                                       #vetor com os coeficientes do termos de Y(t)
    coef = V.T @ X0 
    for i in range(n):
        Y[i] = coef[i]*sp.cos(w[i]*t)
    return Y


#função que plota os gráficos plotagem dos gráficos
def plotagem(X):
    for i in range(n):
        t = sp.symbols('t') 
        sp.plot(X[i], (t, 0, 10), title="Massa %s" % (i+1), xlabel='tempo (s)', ylabel='posição (m)')"""
        


#função sgn()
def sgn(d):    
    if d >= 0:
        return 1                                             #d >= 0
    else:
        return -1                                            #d < 0

    
#função que gera um valor de d_k
def d_gen(A, m):      
    alpha_m1 = A[m-2,m-2]                                    #penultimo elemento do conjunto alpha
    alpha_m = A[m-1,m-1]                                     #ultimo elemento do conjunto alpha
    return (alpha_m1 - alpha_m)/2                            #calculo de d_k


#função que gera um valor de mi para cada iteração k
def mi_gen(A, m):     
    d = d_gen(A, m)                                          #geração de d_k                  
    alpha_m = A[m-1,m-1]                                     #ultimo elemento do conjunto alpha
    beta_m1 = A[m-1,m-2]                                     #penultimo elemento do conjunto beta
    return alpha_m + d - sgn(d)*np.sqrt(d**2 + beta_m1**2)   #calculo de mi_k


#função que gera c e s para cada Q de cada iteração k
def cs_gen(alpha, beta):     
    if abs(alpha) > abs(beta):                               #testa se |alpha| > |beta|
        tau = -beta/alpha                                    #calculo de tau
        c = 1/(np.sqrt(1+tau**2))                            #calculo de c
        s = c*tau                                            #calculo de s
    else:
        tau = -alpha/beta                                    #calculo de tau
        s = 1/(np.sqrt(1+tau**2))                            #calculo de s
        c = s*tau                                            #calculo de c
    return [c, s]


#função que gera Q para cada iteração k 
def Q_gen(i, c, s):      
    Q = np.eye(n)                                            #inicia Q como matriz identidade de ordem n
    Q[i,i] = c                                               #substitui o elemento da posição (i,i) por c
    Q[i+1,i] = s                                             #substitui o elemento da posição (i+1,i) por s
    Q[i,i+1] = -s                                            #substitui o elemento da posição (i,i+1) por -s
    Q[i+1,i+1] = c                                           #substitui o elemento da posição (i+1,i+1) por c
    return Q

#-------------------------------------------------------------------------------------------------------------------------------

#Valores de iniciais e de entrada
A = A_gen(n, item, massa)                                    #gera a matriz A
V = np.eye(n)                                                #inicializa a matriz de auto-vetores
ck = np.zeros(n-1)                                           #vetor que armazena os valores dos cossenos em cada iteração
sk = np.zeros(n-1)                                           #vetor que armazena os valores dos senos em cada iteração
erro = 10**(-6)                                              #erro para o critério de parada

#Algoritmo QR tridiagonal com deslocamento
k = 0                                                        #parâmetro que representa a quantidade de iterações realizadas
m = n                                                        #auxiliar que segmenta A sempre que atinge uma condição de parada
Ak = A                                                       #matriz auxiliar que muda a cada iteração

while m > 1:                                                 #m vai de n até 2
    fim = False
    while fim == False:
        mi = 0
        
        if desl == "com":
            if k > 0:                                        #testa se k > 0
                mi = mi_gen(Ak, m)                           #gera mi_k
        Ak =  Ak - mi * np.eye(n)                            #subtrai deslocamento espectral

        for i in range(m-1):
            cs = cs_gen(Ak[i,i], Ak[i+1, i])                 #gera c e s
            ck[i] = cs[0]                                    #armazena os valores de c da iteração k
            sk[i] = cs[1]                                    #armazena os valores de s da iteração k
            Q = Q_gen(i, ck[i], sk[i])                       #gera a matriz Q(i,i+1,theta), onde c=cos(theta) e s=sen(theta)
            Ak = Q @ Ak                                      #realiza as rotações de Givens

        for i in range(m-1):
            Q = Q_gen(i, ck[i], sk[i])                       #gera a matriz Q(i,i+1,theta), onde c=cos(theta) e s=sen(theta)
            Ak = Ak @ Q.T                                    #atualiza a matriz Ak

        Ak = Ak + mi * np.eye(n)                             #soma deslocamento espectral

        for i in range(m-1):
            Q = Q_gen(i, ck[i], sk[i])                       #gera a matriz Q(i,i+1,theta), onde c=cos(theta) e s=sen(theta)
            V = V @ Q.T                                      #atualiza a matriz de auto-vetores

        k += 1                                               #atualiza a quantidade de iterações

        beta_m1 = Ak[m-2, m-1]                               #elemento que deve ser menor que o erro
        if abs(beta_m1) < erro:                              #condição de parada
            fim = True                                       
                 
    m -= 1                                                   #decrementa 1 de m
    
AUTVAL = Ak                                                  #armazena os auto-valores na matriz AUTVAL
AUTVET = V                                                   #armazena os auto-vetores na matriz AUTVET

#-------------------------------------------------------------------------------------------------------------------------------

#posições iniciaias para o caso 3
if item == 'b' or item == 'c':
    if caso == 3:
        X0 = V.T[0]                                          #posições iniciais iguais ao autovetor correspondente ao maior autovalor
        
#-------------------------------------------------------------------------------------------------------------------------------
#saídas do programa

autovalores = np.zeros(n)                                    #vetor que armazena os autovetores
for i in range(n):
    autovalores[i] = AUTVAL[i,i]                             #armazena em "autovetores" os elementos da diag. principal de AUTVAL

#saídas para o caso a
if item == 'a':
    print("\n ---Item a %s deslocamento---" % desl)          #informa o item e se houve deslocamento escolhido
    print("\n Ordem da matriz A: %s" % n)                    #informa a ordem da matriz A escolhida
    print("\n Número de iterações: %s" % k)                  #informa o número de iterações que foram necessárias
    print("\n Autovalores de A: \n")
    print(autovalores)                                       #imprime os auto-valores calculados
    print("\n Autovetores de A: \n")
    print(AUTVET)                                            #imprime os auto-vetores calculados

#saídas para os casos b e c
else:
    w = np.zeros(n)                                                            #vetor que guarda as frequências
    for i in range(n):
        w[i] = np.sqrt(AUTVAL[i,i])                                            #armazena em w a raiz quadrada dos auto-valores 
    """Y = Y_gen(X0)                                                             #criação do vetor Y
    X = V @ Y                                                                 #obtenção do vetor X com as equações da variação temporal da posição
    print("\n ---Item %s %s deslocamento, caso %s---" % (item, desl, caso))    #informa o item, se houve deslocamento e o caso escolhido"""
    print("\n Posições iniciais: \n")
    print('X0 = %s' % X0)                                                      #imprime as posições iniciais da opção escolhida
    print("\n Número de iterações: %s" % k)                                    #informa o número de iterações que foram necessárias
    print("\n Autovalores de A: \n")
    print(autovalores)                                                         #imprime os auto-valores calculados
    print("\n Autovetores de A: \n")
    print(AUTVET)                                                              #imprime os auto-vetores calculados
    """plotagem(X)                                                             #imprime os gráficos correspondentes a opção escolhida"""

