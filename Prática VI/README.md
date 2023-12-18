# Prática VI - Introdução às Interfaces de Visão Computacional, Sistemas de Versionamento de Arquivos e Controle de Acesso Via Tags

Esta prática consistiu em três etapas distintas, portanto, serão tecidos alguns comentários e explicações dos códigos desenvolvidos a cada etapa.

## Controle de Acesso via TAGs RFID

Nesta etapa, buscou-se, primeiramente analisar o funcionamento das TAGs RFID, realizando a gravação e leitura de dados e ID das mesmas, além de, posteriormente, implementar um sistema de verificação, onde, a partir de um circuito básico e o código desenvolvido, era possível comparar se o ID de uma TAG estava cadastrado numa base de dados de ID armazenada no código.

Para permitir o uso das TAGs RFID, foi utilizada a biblioteca ```mfrc522``` que fornece uma interface com o módulo ```RFID-RC522```. A biblioteca fornece uma instância para o módulo, permitindo assim seu uso para escrita e leitura dos dados e ID de uma TAG. Portanto, nos códigos desenvolvidos na prática, foram utilizadas as seguintes funções desta biblioteca:
  - reader = SimpleMFRC522() - Define uma instância para o módulo RFID com nome ```reader``` a partir da classe SimpleMFRC522();
  - reader.write(data) - Utilliza a instância ```reader``` para escrever o dado contido em ```data``` na TAG que for aproximada do módulo RFID;
  - id, texto = reader.read() - Utiliza a instância ```reader``` para ler os dados contidos na TAG aproximada do módulo e armazena:
    - O ID da TAG na variável ```id```;
    - O dado contido na TAG na variável ```texto```.

Além desta biblioteca, foram utilizadas algumas outras funções da biblioteca ```time``` e ```RPi.GPIO```, que já foram detalhadas em práticas anteriores. Sendo assim, procedeu-se à montagem do circuito, conforme observado na imagem abaixo.

![Circuito RFID](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20VI/Images/RFID.png?raw=true)

Para que haja o funcionamento do módulo, a interface SPI deve estar habilitada, o que pode ser feito facilmente utilizando o comando ```sudo raspi-config``` e se dirigindo ao submenu ```Interfaces```. Além disso é necessário instalar a biblioteca com o comando ```pip3 install mfrc522```. Com isso, procedemos para os dois primeiros códigos trabalhados:
  - O primeiro código é o [```TAGWriter.py```](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20VI/RFID/TAGWriter.py), que realiza a gravação de um Número USP como dado numa TAG RFID que seja aproximada do sensor;
  - O segundo código é o [```TAGReader.py```](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20VI/RFID/TAGReader.py), que realiza a leitura tanto do dado presente na TAG, quanto do ID da mesma.

Estes códigos citados acima serviram como base para entender o funcionamento das TAGs e para o desenvolvimento do próximo código. Neste, há uma "base de dados" no código, onde estão armazenados as IDs que tem acesso permitido, ou seja, que estão cadastradas. Quando ocorre a leitura de uma TAG, seu ID é identificado e:
  - Caso esteja cadastrado, um LED verde é acesso e ```"Acesso liberado!"``` é printado na saída;
  - Caso o ID não esteja cadastrado, um LED vermelho acende e ```"Acesso negado!"``` é printado.
Um vídeo explicativo do funcionamento do código está presente abaixo, juntamente do código.
  - Código é o [```TAGVerifier.py```](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20VI/RFID/TAGVerifier.py).
  ![RFID](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20VI/Images/RFID.gif?raw=true)