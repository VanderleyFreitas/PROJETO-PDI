<p align="center">
  <img src="https://github.com/VanderleyFreitas/PROJETO-PDI/blob/main/md_images/ufc_brasao.jpg" width="120">
  <h2 align="center">Identificador de bolos</h2>
  <p align="center">
    FUNDAMENTOS DE PROCESSAMENTO DIGITAL DE IMAGENS
    <br>
    <p align="center">Universidade Federal do Ceará</p>
    <p align="center">Departamento de Engenharia de Teleinformática</p>
    <p align="center">16 de abril de 2021</p>
  </p>
</p>

## Sumário
1. [Introdução](#introducao)
    1. [Estudo do problema](#estudo-problema)
2. [Aquisição de imagens](#aquisicao)
    1. [Algoritmo](#algoritmo)
4. [Pré-processamento](#preprocessamento)
    1. [Sub paragraph](#subparagraph1)
5. [Processamento](#processamento)

5. [conclusao](#conclusao)


## Introdução <a name="introducao"></a>
<p>Este documento tem o propósito de detalhar por completo o projeto "Identificador de bolos" a ser desenvolvido com a participação de toda a turma da disciplina de “Fundamentos de Processamento Digital de Imagens” gerenciada pelo aluno Vanderley Freitas.
É de fundamental importância definir todos os requisitos de uma aplicação para que se possa garantir um resultado mínimo desejado, pois é com base neles que o projeto será guiado.</p>

### Estudo do problema <a name="estudo-problema"></a>
É aqui de forma sucinta brevemente explicado um apanhado do problema.

Visando aferir qualitativamente a aplicação desenvolvida, fora produzido um vídeo que simulasse o deslocamento dos bolos em uma esteira de produção típica da indústria. Obtido o video, iniciou-se um devido tratamento dos seus frames para que os mesmos obtivessem melhores resultados durante a fase de processamento. Por fim, os frames pré-processados nos permitiu que pudessemos então:
* Delinear os bolos, isto é, conseguir localizá-los em seus respectivos frames.
* Identificar possíveis relevos, como também o centro do bolo para assim conseguir classificá-los.

Objetivando simplificar o problema, os membros pertencentes a este projeto formaram 4 equipes as quais atuariam independentemente visando assim concluir os requisitos de forma mais eficiente. As equipes formadas foram:
* Aquisição das imagens
* Pré-processamento do vídeo
* Processamento do vídeo
* Teste e qualidade

## Interface<a name="interface"></a>
### Objetivo
Nesta etapa, foi realizado o desenvolvimento de um sistema que permita obter as imagens necessárias por meio da geração de vídeos que simulem o deslocamento dos objetos na esteira. Para este fim, utilizamos a biblioteca React do JavaScript para gerar o vídeo e também a inserção de ruídos no vídeo para melhor simular um caso real. permitindo assim que o sistema possa devidamente tratá-los. Uma exemplo de imagem produzida pode ser vista abaixo:

<p align="center">
<img src="https://github.com/VanderleyFreitas/PROJETO-PDI/blob/main/md_images/frames312.jpg" width="480">
</p>
<p align="center">Figura 1 - Exemplo de imagem adquirida na aquisição de imagens</p>

### Tecnologias Utilizadas
- Na criação do vídeo:
O vídeo foi criado com React que é uma biblioteca JavaScript de código aberto com foco em criar interfaces de usuário em páginas web. Também
foram utilizados HTML e CSS, que são, respectivamente, uma linguagem baseada em marcação, que marca os elementos para definir quais
informações serão exibidas pela página e uma linguagem de folha de estilo que é composta por camadas tendo como função definir o visual (aparência)
e torná-las mais bonitas e agradáveis, através da alteração de características como cor, posicionamento dos elementos e layout.
- Na adição de ruídos:
O Python foi a ferramenta utilizada na geração de ruídos no vídeo, com as bibliotecas Matplotlib, que é uma biblioteca para a criação de visualizações
estáticas, animadas e interativas, a Numpy, que é usada para manipulação de matrizes e possui uma larga coleção de funções matemáticas para
trabalhar com essas estruturas e, por último, a biblioteca OpenCV (cv2) que foi utilizada para manipulação de imagens.

### Metodologia
O vídeo é criado no arquivo Index.tsx, pelo método componentDidMoint() onde as imagens são desenhadas no canvas. No arquivo tem um método chamado render()
que é responsável por renderizar o vídeo que é produzido pela biblioteca chamada PIXI.js.
As imagens usadas no projeto para a criação do vídeo ficam alocadas na pasta “sprites” em src/pages/Index/sprites.

Na parte de adição de ruídos, foi escolhido dois grupos de forma aleatória de pares ordenados, cada um com um tamanho de 0.5% do total da imagem. Assim,
tornamos todos os pixels 0,0,0 e o outro para 255,255,255.

## Pré-processamento <a name="preprocessamento"></a>
### Objetivo
Na seção de pré-processamento temos como atividade a manipulação das imagens obtidas com o intuito de realizar correções suficientes para que as mesmas estejam aptas ou adequadas para serem processadas. No contexto deste trabalho, estaremos minimizando possíveis ruídos inerentes da obtenção das imagens pelas câmeras e também gerando informações que permitam a equipe de processamento inferir as diferentes classes dos bolos.
Nesta seção, portanto, fora operado os seguintes métodos:
- Detecção de bordas de Canny
- Transformações morfológicas

### Tecnologias Utilizadas
- Biblioteca Skimage para implementação do algorítimo de Canny.
- Biblioteca CV2 para o ajuste dos contornos de cada bolo.

### Metodologia <a name="metodologia"></a>
O algoritmo de Canny é um famoso método para realizar a detecção de bordas em uma imagem. Este algoritmo basicamente segue os seguintes passos:
- **Redução de ruído**. Como as bordas são suscetíveis a ruídos, é um aplicado um filtro Gaussiano para removê-lo.
- **Busca do gradiente de intensidade**. A imagem suavizada é então filtrada com o operador de Sorbel nas direções horizontais e verticais, assim obtendo as primeiras derivadas dessas direções. Com isso, podemos encontrar a direção do gradiente e consequentemente as bordas.
- **Supressão não-máxima**. Para cada pixel é verificado se existe um máximo local no gradiente de direção. Se o ponto localizado na borda não for o máximo local, este é suprimido.
- **Limiarização por histerese**. Geramos duas imagens, onde cada uma tem seus pixels não nulos maiores que um limiar pré-estabelecido (conhecidos como limiar inferior e limiar superior). Assim, as bordas que tiverem intensidade localizada entre os dois tresholds serão consideradas como bordas ou possíveis candidatas a bordas. se estas bordas mantém uma conectividade com as bordas que estão acima do limiar superior, é mantido a borda. Caso contrário, estas são excluídas.

<p align="center">
<img src="https://github.com/VanderleyFreitas/PROJETO-PDI/blob/main/md_images/preprocessing_morphologic_operators.jpg" width="600">
</p>
<p align="center">Figura 2 - Implementação das operações morfológicas</p>

Para o caso do algoritmo aplicado, foi-se usado um desvio padrão de 5 e limiares com 10% e 15% do valor da intensidade máxima da imagem. Fornecemos esses parâmetros em conjunto com a imagem na função acima resultará na imagem abaixo:

<p align="center">
<img src="https://github.com/VanderleyFreitas/PROJETO-PDI/blob/main/md_images/preprocessing_canny.jpg" width="600">
</p>
<p align="center">Figura 2 - Implementação do algoritmo de detecção de bordas de Canny</p>

Transformações morfológicas são operações simples com a imagem utilizando-se principalmente de suas formas. No contexto desse projeto nós utilizamos operador de **fechamento**, que ajuda a remover o ruído interno (como pequenos buracos) dos objetos de estudo da imagem. Além deste, também utilizamos o operador gradiente morfológico para encontrar contornos no objeto. Abaixo, podemos ver como estes operadores foram utilizados:
<p align="center">
<img src="https://github.com/VanderleyFreitas/PROJETO-PDI/blob/main/md_images/preprocessing_image_result.jpg" width="600">
</p>

<p align="center">Figura 2 - Resultado da imagem com as técnicas de pré-processamento aplicado</p>

## Processamento <a name="processamento"></a>
### Objetivo
Os frames pré-processados são recebidos da etapa anterior para o processamento. Esta etapa tem como objetivo identificar os contornos dos bolos nas imagens e classificá-los quanto aos diferentes padrões de cobertura (coberto, semi-coberto ou não-coberto). Ao final do processo, devemos ter imagens com a classificação visível (em retângulos de cores diferentes contendo os bolos) e um vídeo gerado a partir dos frames processados.

### Tecnologias Utilizadas
Para realizar o processamento descrito acima, foram usados métodos implementados na
linguagem Python, usando alguns módulos da linguagem. São eles:
- Numpy: usado para lidar com arrays multidimensionais;
- CV2: biblioteca com métodos do OpenCV, usada para processamento de imagens.

### Metodologia
O processamento foi dividido em 4 grandes etapas, que englobam certas funções das
bibliotecas importadas: achar_bolos(), processamento(), frame_processado() e a compilação
dos frames em um vídeo final, no qual os bolos estão classificados visualmente.

1.1. A primeira, achar_bolos(), parte da imagem binária pré-processada para encontrar os
retângulos que contêm cada bolo. Ela aproveita a função cv2.findCountours() para encontrar
as coordenadas dos pixels mais externos (flag RETR_EXTERNAL) dos contornos dos bolos. A
flag CHAIN_APPROX_SIMPLE faz com que o contorno seja representado pela quantidade
mínima de coordenadas necessária (as arestas de polígono, por exemplo).

Com base nessas coordenadas, a função cv2.boundingRect() determina os retângulos
não-rotacionados que contêm os bolos. Ela retorna uma lista de retângulos, de modo que cada
retângulo é representado por uma array de 4 variáveis: x,y para as coordenadas do vértice
superior esquerdo, w para a largura e h para a altura.

1.2. A segunda, processamento(), recebe a lista de retângulos e classifica os bolos neles
contidos. Primeiramente, fazemos um filtro de mediana a fim de reduzir o impacto do ruído sal e
pimenta. Esse filtro é implementado usando a função cv2.medianBlur. Depois, fazemos uma
limiarização, usando como parâmetro 70 de intensidade, ou seja, pixels acima de 70 de
intensidade têm sua intensidade alterada para 255 (valor máximo). Caso contrário, eles terão
intensidade 0, ou seja, completamente pretos. Isso serve para salientar a diferença entre as
médias dos bolos cobertos e descobertos. Para isso usamos a função cv2.threshold.

Por fim, separamos uma janela 20x20 central da subimagem do bolo, a qual chamamos de
miolo. Usamos esse miolo para classificar se o bolo está coberto ou não através de sua média
de intensidade, calculada usando a função mean().

As menores intensidades correspondem aos bolos mais cobertos, dada a maior prevalência de
pixels brancos na imagem binária. As intensidades abaixo de 100 indicam bolos cobertos,
acima de 199 indicam bolos descobertos e valores intermediários indicam os semi-cobertos.

1.3. A terceira, frame_processado(), recebe os retângulos e as classificações. Os retângulos
coloridos são desenhados sobre o frame original com a função cv2.rectangle(), representando
visualmente as classificações dos bolos presentes naquele frame. As imagens são, então,
armazenadas em formato .jpg com a função cv2.imwrite().

1.4. A quarta e última etapa reúne os frames classificados (armazenados na mesma pasta pela
etapa anterior) em um array para produzir um vídeo no formato .avi em 30 fps com a função
cv2.videoWriter(). A função glob.glob() é aproveitada em conjunto com a re.findall() para
encontrar recursivamente os arquivos na pasta que seguem um padrão de nomeação (definido
na etapa anterior com a função cv2.imwrite).

Por fim, temos um vídeo no qual os bolos estão destacados em retângulos, de contorno
colorido de acordo com a classificação encontrada: verde para coberto, azul para semi-coberto
e vermelho para não-coberto.

## Teste e Qualidade <a name="teste e qualidade"></a>
### Objetivo
Esta etapa tem o propósito de detalhar por completo o projeto Identificador de Bolos a ser desenvolvido com a participação de toda a turma da disciplina de “Fundamentos de Processamento Digital de Imagens” gerenciada pelo aluno Vanderley Freitas. É de fundamental importância definir todos os requisitos de uma aplicação para que se possa garantir um resultado mínimo desejado, pois é com base neles que o projeto será guiado. Nesse documento será apresentado todos os requisitos funcionais necessários para o projeto, bem como os resultados dos testes realizados.

### Metodologia
Para garantia do teste e qualidade os seguintes tópícos foram implementados.

#### Requisitos Funcionais: 
Os requisitos abaixo representam, de forma geral, todos os problemas e necessidades que devem então ser atendidas e solucionadas pela aplicação.
- RF001 Geração de vídeo de esteira de bolos. Os bolos devem aparecer de maneira aleatória, com velocidade variante e a velocidade deve estar presente no vídeo.
 

## Conclusão <a name="conclusao"></a>
Com o término da execução do projeto e a devida implementação e teste do mesmo, podemos concluir que o ele atendeu os requisitos do funcionamento anteriormente planejado pelas equipes. Com os resultados obtidos, pode-se entender que a aplicação prática deste projeto poderiam ser novos passos para estudos futuros deste problema. Com a aplicação existente em uma indústria poderia fazer uma nova avaliação da eficácia do sistema e aperfeiçoar possíveis parâmetros adjuntos de novas variáveis inseridas no problema.
