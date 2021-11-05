# EP1Numerico
 ## Exercício Programa 1 da disciplina Métodos Numéricos e Aplicações ministrada na Escola politécnica da Universidade de São Paulo

#### O projeto tem como o objetivo o desenvolvimento de métodos numéricos capazes de encontrar autovalores e autovetores. Fazê-lo de maneira rápida e precisa é fundamental e, portanto, nesse programa, será detalhada a implementação do algoritmo QR com deslocamento espectral para a determinação de autovalores e autovetores de matrizes tridiagonais simétricas.

# Instruções para a execução do programa: 

> Necessário executar o programa em uma IDE do Python 3.8

> Para definir qual item deseja-se testar, é necessário informar ao programa logo na primeira resposta. As possíveis respostas que o fazem funcionar são ‘a’, ‘b’ e ‘c’. Caso não seja uma escolhida uma dessas 3 opções, o programa não será executado corretamente.

> Em seguida, informe se deseja com ou sem deslocamento espectral. As únicas respostas válidas são ‘com’ ou ‘sem’. Caso não seja uma escolhida uma dessas 2 opções, o programa não será executado corretamente.

> Para o item a:
>> Defina o tamanho da dimensão da matriz tri diagonal. Qualquer valor pode ser
inserido desde que o tipo de entrada seja integer. Caso contrário, o programa não será executado corretamente.

> Para o item b:
>> Defina se deseja executar um dos casos pré-definidos. Essa entrada aceita como resposta válida ‘sim’ ou ‘nao’. Caso não seja uma escolhida uma dessas 2 opções, o programa não será executado corretamente.
>> Se a resposta da entrada anterior for ‘sim’, será feita mais uma pergunta acerca de qual dos casos você deseja executar. São numerados de 1 a 3 e eles estão associados às seguintes condições iniciais:
>>> Caso 1: X(0) = -2, -3, -1, -3, -1 
>>> Caso 2: X(0) = 1, 10, -4, 3, -2 
>>> Caso 3: X(0) correspondente ao modo de maior frequência
>> Se a reposta da entrada anterior for ‘nao’. Será pedido em diferentes linhas: o número de massas do sistema, o valor de cada uma das massas apenas uma vez e a posição inicial de cada uma delas. Nesses campos, apenas serão aceitas entradas dos tipos integer ou float. Caso uma entrada de outro tipo seja inserida, o programa não será executado corretamente.

> Para o item c:
>> Defina se deseja executar um dos casos pré-definidos. Essa entrada aceita como resposta válida ‘sim’ ou ‘nao’. Caso não seja uma escolhida uma dessas 2 opções, o programa não será executado corretamente.
>> Se a resposta da entrada anterior for ‘sim’, será feita mais uma pergunta acerca de qual dos casos você deseja executar. São numerados de 1 a 3 e eles estão associados às seguintes condições iniciais:
>>> Caso 1: X(0) = -2, -3, -1, -3, -1, -2, -3, -1, -3, -1
>>> Caso 2: X(0) = 1, 10, -4, 3, -2,  1, 10, -4, 3, -2
>>> Caso 3: X(0) correspondente ao modo de maior frequência
>> Se a reposta da entrada anterior for ‘nao’. Será pedido em diferentes linhas: o número de massas do sistema, o valor de cada uma das massas apenas uma vez e a posição inicial de cada uma delas. Nesses campos, apenas serão aceitas entradas dos tipos integer ou float. Caso uma entrada de outro tipo seja inserida, o programa não será executado corretamente.

> Importante para a plotagem dos gráficos caso assim queira. Necessário desfazer as aspas triplas nas linhas 5, 95, 109, 239, 241 e 249. Além disso, é necessário executar o programa através de algum ambiente disponível no conda depois de ter instalado a biblioteca sympy.