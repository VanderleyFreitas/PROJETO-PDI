<p align="center">
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

Objetivando simplificar o problema, os membros pertencentes a este projeto formaram 5 equipes as quais atuariam independentemente visando assim concluir os requisitos de forma mais eficiente. As equipes formadas foram:
* Aquisição das imagens
* Pré-processamento do vídeo
* Processamento do vídeo
* Teste e qualidade

## Aquisição de imagens<a name="aquisicao"></a>
Nesta etapa, foi realizado o desenvolvimento de um sistema que permita obter as imagens necessárias por meio da geração de vídeos que simulem o deslocamento dos objetos na esteira. Para este fim, utilizamos a biblioteca React do JavaScript para gerar o vídeo e também a inserção de ruídos no vídeo para melhor simular um caso real. permitindo assim que o sistema possa devidamente tratá-los. Uma exemplo de imagem produzida pode ser vista abaixo:

<p align="center">
<img src="https://github.com/VanderleyFreitas/PROJETO-PDI/blob/main/md_images/frames312.jpg" width="480">
</p>
<p align="center">Figura 1 - Exemplo de imagem adquirida na aquisição de imagens</p>

A criação do vídeo é feita utilizando o método componentDidMoint(), que realiza os desenhos no canvas e posteriormente são renderizados. Por fim, as imagens já são adicionadas com ruidos inseridos.

## Pré-processamento <a name="preprocessamento"></a>
Na seção de pré-processamento temos como atividade a manipulação das imagens obtidas com o intuito de realizar correções suficientes para que as mesmas estejam aptas ou adequadas para serem processadas. No contexto deste trabalho, estaremos minimizando possíveis ruídos inerentes da obtenção das imagens pelas câmeras e também gerando informações que permitam a equipe de processamento inferir as diferentes classes dos bolos.
Nesta seção, portanto, fora operado os seguintes métodos:
- Detecção de bordas de Canny
- Transformações morfológicas

### Algoritmo <a name="algoritmo"></a>
[CONTEUDO SOBRE ALGORITMO DE CANNY]

Transformações morfológicas são operações simples com a imagem utilizando-se principalmente de suas formas. No contexto desse projeto nós utilizamos operador de **fechamento**, que ajuda a remover o ruído interno (como pequenos buracos) dos objetos de estudo da imagem. Além deste, também utilizamos o operador gradiente morfológico para encontrar contornos no objeto. Abaixo, podemos ver como estes operadores foram utilizados:
<p align="center">
<img src="https://github.com/VanderleyFreitas/PROJETO-PDI/blob/main/md_images/preprocessing_morphologic_operators.jpg" width="600">
</p>

<p align="center">Figura 2 - Implementação das operações morfológicas</p>

### Processamento <a name="processamento"></a>
This is a sub paragraph, formatted in heading 3 style

## Another paragraph <a name="subparagraph1"></a>
The second paragraph text

## Conclusão <a name="conclusao"></a>
This project is simple Lorem ipsum dolor generator.
