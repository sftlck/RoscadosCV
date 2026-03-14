# Software de Medição de Calibradores Roscados

Este software foi desenvolvido para o uso de medição do ângulo de flancos de calibradores roscados externos cilíndricos ou cônicos. Além de exibir o resultado, o software armazena a imagem capturada com os resultados em uma pasta de arquivos determinada pelo usuário.

<img class="center" src="IP 04 Lado Posterior.PNG" alt="Projeção de Perfil de Calibrador Roscado Cilíndrico" style="width: 600px; height: auto">

> Imagem do perfil de rosca um Calibrador roscado cilíndrico externo, fixado entre dois pontos em um microscópio de medição

O algoritmo de detecção espera uma Região de Interesse (ROI) determinada pelo usuário, realiza transformações de cores na imagem, depois aplica um Canny, busca por segmentos de pixels que formam linhas e finalmente calcula o ângulo entre segmentos distintos, donde os pontos para formar as linhas são ajustados por regressão linear. Erros de execução são interceptados pelo Exceptions.py.

<img class="center" src="TAMS menu.PNG" alt="Menu inicial do software" stye="width: 600px; height: auto">

> Imagem de apresentação do software, onde os campos de texto permitem identificar o instrumento de medição, ordem de serviço e conjunto de lentes utilizado

<img class="center" src="Select ROI.PNG" alt="Janela de seleção de Região de Interesse (ROI)" style="width: 600px; height: auto">

> Janela de captura de imagem da câmera, selecionando a ROI (Região de Interesse) para medição

<img class="center" src="Results.PNG" alt="Resultados de Medição do Calibrador Roscado Cilíndrico" style="width: 600px; height: auto">

> Imagem dos resultados de medição impressos na janela principal, onde há os valores calculados, a Ordem de Serviço e a Identificação (em vermelho, canto direito) e um link para a pasta de armazenamento da imagem visualizada (acima)

{INSERIR IMAGEM DA PASTA DE ARQUIVOS QUE CONTÉM O INSTRUMENTO EM MEDIÇÃO}

{INSERIR IMAGEM DO TERMINAL PARA CÓPIA DE RESULTADOS PARA O EXCEL}

{INSERIR IMAGEM DA ESTRUTURA DO EXPLORADOR DE ARQUIVOS}

Para usar o software, é necessário saber qual é a relação entre a resolução de sua câmera e o comprimento real, tilizando a equação comprimento/pixels. Utilize uma Lupa graduada com padrões rastreáveis ao SI para determinar o valor de {SÍMBOLO}. Os softwares auxiliares disponíveis e descritos abaixo fornecem resultados para o cálculo da constante {SÍMBOLO}

{INSERIR FIGURA DA EQUAÇÃO}

## Programa para Medição de Pixel - Comprimento

{TEXTO DE APRESENTAÇÃO}
{IMAGEM}

## Programa para Medição de Pixel - Ângulo

{TEXTO DE APRESENTAÇÃO}
{IMAGEM}

- [x] Medir semiângulo de calibradores roscados cônicos e cilídricos utilizando a câmera instalada no dispositivo
- [x] Armazenar resultados de medições
- [x] Configurar parâmetros de detecção de flancos
- [x] Indexar registros como Ordem de Serviço e Identificação de Intrumento
- [x] Abrir arquivo do computador para processar ângulos também
- [x] Medir o Ângulo de Cone de calibradores roscados cônicos
- [x] Medir o Passo de calibradores roscados cônicos e cilídricos
- [x] Criar um software auxiliar para calibração de comprimento de pixel do microscópio
- [x] Criar um software auxiliar para calibração de ângulo do microscópio
- [ ] Criar uma lista de seleção interativa de lentes para correção óptica de medições de comprimento e ângulo
- [ ] Criar uma lista de seleção interativa de lentes para correção óptica de medições de comprimento e ângulo
