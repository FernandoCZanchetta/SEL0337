# Prática VII - Configuração do SystemD para Gerenciar Serviços Personalizados em Sistemas Embarcados


Primeiramente, para a realização desta prática, montou-se um circuito simples de LED, conectando um pino da Raspberry Pi num resistor, conectado a um LED, conectado ao GND da Raspberry Pi. Com este circuito, foi possível desenvolver a atividade prática.

Utilizando bash script, foi feito um programa para realizar o blink de um LED. O código relativo a este programa é [```LEDblink.sh```](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20VII/LEDblink.sh). Neste código, temos:
  - #!/bin/bash - Indica que o script deve ser executado utilizando o interpretador Bash;
  - echo 21 > /sys/class/gpio/export - Exporta o pino GPIO 21, permitindo que o mesmo seja controlado;
  - echo out > /sys/class/gpio/gpio21/direction - Configura a direção do pino como sendo de saída;
  - do - Marca o início do bloco de comandos que serão executados no loop infitino
  - echo 'valor' > /sys/class/gpio/gpio21/value - Define o valor do pino GPIO 21 como sendo 'value' (substituir value pelo valor desejado (0 ou 1)), permitindo, assim, ligar e desligar o LED;
  - sleep 0.2s - Aguarda 0,2s;
  - done - Marca o fim do bloco de comandos que estão inseridos no loop.

Após isso, permitiu-se a execução do arquivo por meio do comando ```sudo chmod +x ./LEDblink.sh```, e isso pode ser testado rodando o mesmo, digitando ```./LEDblink.sh``` no terminal. Com este arquivo pronto, proceudeu-se à criação de uma unit file, arquivo responsável por inserir um serviço no SystemD. Assim foi criado o arquivo [```LEDblink.service```](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20VII/LEDblink.service), que consiste em:
  - [Unit] - Seção responsável pelas informações do serviço e descrição das dependências, portanto:
    - Description=BlinkLED - Descrição do serviço;
    - After=multi-user.target - Utilizado para informar que este serviço só pode ser iniciado após ```multi-user.target``` estar pronto, caso fosse necessário que a internet já estivesse habilitada para rodar o serviço, por exemplo, utilizaria-se: ```After=network.target```.
  - [Service] - Contém as configurações da execução do serviço que será inicializado, então:
    - ExecStart=/home/sel/6219/"Prática VII"/LEDblink.sh - Informa o(s) arquivo(s) que devem ser executados na inicialização do serviço;
    - ExecStop= - Informa o(s) arquivo(s) que devem ser executados na finalização do serviço;
    - user=SEL - Informa o nome de usuário.
  - [Install] - Descreve o comportamento de inicialização do serviço, sendo assim:
    - WantedBy=multi-user.target - Informa ao SystemD o grupo alvo do qual o serviço que será inicializado faz parte.

Para que o serviço seja devidamente reconhecido e esteja a disposição no estágio ```init system``` da inicialização da placa, é necessário colocar o arquivo ```.service``` gerado no diretório padrão de serviços do SystemD. Isso pode ser feito com o comando ```sudo cp LEDblink.service /lib/systemd/system/```. Com isso, já é possível testar o funcionamento do serviço por meio do comando ```sudo systemctl start LEDblink``` e, para parar a execução utiliza-se ```sudo systemctl stop LEDblink```. Ao utilizar o comando ```sudo systemctl enable LEDblink```, o serviço passa a estar habilitado para rodar durante o Boot da Rasberry Pi, então, ao reiciar a Raspberry, já é possível perceber que o serviço realmente é executado.

Para tornar a experiência mais visual, é possível desativar a splash screen, por meio do comando ```sudo raspi-config```, indo para os submenus ```System``` e, depois, ```Splash Screen```. Ao fazer isso, as mensagens de incialização são exibidas e, a descrição dada no unit file será usada para identificar o serviço, mostrando o status de execução na frente dela, por exemplo: ```[  OK  ] BlinkLED...```.

Se for necessário corrigir algum erro, pode-se utillizar o ```systemctl status LEDblink.service``` e analisar as mensagens de erro. Caso deseje-se desabilitar o serviço no Boot, utiliza-se ```sudo systemctl disable LEDblink```. Caso seja feita alguma alteração no serviço é preciso recarregá-lo por meio do ```sudo systemctl daemon-reload```.

Como resultado de todo este procedimento citado, tem-se o GIF abaixo, que demonstra o funcionamento do serviço construído acima.

![LEDBLINK](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20VI/Images/BLINK.gif?raw=true)

De forma análoga ao procedimento realizado acima, é possível criar um serviço que execute um programa em Python, portanto escolheu-se o programa [```pwm_led.py```](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20VII/pwm_led.py), já desenvolvido em práticas anteriores. O unit file para este caso deve também incluir ```/usr/bin/python3``` em ```ExecStart```, já que o python também deve ser inciado para que o arquivo ```.py``` possa rodar. Sendo assim, criou-se o arquivo [```pythoncode.service```](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20VII/pythoncode.service). Realizando novamente os procedimentos citados acima para inclusão do serviço na sequencia de Boot, foi possível adquirir exito na prática.

O histórico de comandos utilizados no terminal está presente no arquivo [```history.txt```](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20VII/history.txt) e mostra toda a sequência de execução desta prática.