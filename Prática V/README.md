# Prática V - Protocolos de Comunicação em Sistemas Embarcados

Para uso do I2C da Raspberry Pi, é necessário o uso de bibliotecas como a ```SMBus```, já que a mesma permite que, por meio de funções pré-definidas, os pinos de GPIO sejam manipulados de forma a estabelecerem a interface física necessária para uso deste protocolo de comunicação. No Arduino UNO, o uso da biblioteca ```<Wire.h>``` é imprescindível para tal tarefa, realizando função semalhante a da biblioteca descrita acima.

Para utilizar o I2C (Inter-Integrated Circuit) na Raspberry Pi com a biblioteca ```SMBus```, foram utilizadas as funções:
  - Bus = SMBus(I2C_PORT) - Define uma instância I2C chamada ```Bus``` utilizando a porta ```I2C_PORT```;
  - Bus.write_byte(I2CBUS_ADDRESS, I2C_DATA_BYTE) - Utiliza a instância I2C chamada ```Bus``` para enviar o byte contido em ```I2C_DATA_BYTE``` no enderço I2C ```I2CBUS_ADDRESS```;
  - Bus.read_i2c_block_data(I2CBUS_ADDRESS, I2CDATA_REGISTER, RECEIVED_DATA_BYTE_NUMBER) - Utiliza a instância I2C chamada ```Bus``` para ler um bloco de dados de 32 bytes presente no endereço ```I2CBUS_ADDRESS```, cujo endereço de registrador é ```I2CDATA_REGISTER``` e ```RECEIVED_DATA_BYTE_NUMBER``` especifica o número de bytes presente no endereço solicitado.

Para utilizar o I2C (Inter-Integrated Circuit) no Arduino UNO com a biblioteca ```<Wire.h>```, foram utilizadas as funções:
  - Wire.begin(I2CBUS_ADDRESS) - Inicia a instância I2C chamada ```Wire``` estabelecida pela biblioteca, indicando que o dispositivo terá endereço I2C sendo ```I2CBUS_ADDRESS```;
  - Wire.onReceive(I2CHandler) - Estabelece que, quando a instância ```Wire``` receber um conjunto de dados, a função ```I2CHandler``` será chamada;
  - Wire.available() - Verifica se há dados no buffer de entrada do barramento I2C (representado pela instância ```Wire```), retornando um valor não nulo, caso haja, e nulo, caso não haja;
  - Wire.read() - Realiza a leitura dos dados presentes no buffer de entrada do barramento I2C (representado pela instância ```Wire```) permitindo que a mesma seja usada como desejado (no caso desta prática, a leitura foi salva numa variável);
  - Wire.write(highByte(BYTE)) e Wire.write(lowByte(BYTE)) - Reliza a escrita de um byte no barramento I2C por highByte e lowByte, ou seja, o mesmo byte é divido e enviado separadamente;
  - Wire.onRequest(I2CRequestHandler) - Chama a função ```I2CRequestHandler``` ao receber uma requisição advinda da Raspberry Pi.

Para verificar se ocorreu o estabelecimento de um barramento I2C no endereço desejado, o comando ```sudo i2cdetect -y 1``` foi utilizado, produzindo o seguinte resultado, caso tenha ocorrido:

![I2C](https://raw.githubusercontent.com/FernandoCZanchetta/SEL0337/main/Pr%C3%A1tica%20V/Images/I2C_DETECT.png)

A prática em questão foi dividida em duas partes:

- Para ambas as partes o mesmo circuito foi implementado, no entanto, na primeira parte, o objetivo era enviar uma instrução a partir da Raspebrry Pi para acender ou apagar o LED interno da placa Arduino UNO, via I2C. Algumas imagens do circuito montado estão presentes abaixo.

	![Circuito I](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20V/Images/POTENTIOMETER_1.png?raw=true)

    ![Circuito II](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20V/Images/POTENTIOMETER_2.png?raw=true)

	 - O código referente a esta parte, para a Raspberry Pi, é o [```LED_I2C.py```](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20V/LED_I2C.py).
     - Já para o Arduino UNO, o projeto da ArduinoIDE está contido na pasta [```/I2C_LED```](https://github.com/FernandoCZanchetta/SEL0337/tree/main/Pr%C3%A1tica%20V/I2C_LED).

- Na segunda parte da prática utilizou-se o protocolo I2C para apresentar, na Raspberry Pi, o resultado da medição de um potenciômetro, sendo assim, ao utilizar ```read_i2c_block_data``` retira-se o último bloco de dados presente no barramento I2C, que é enviado pelo Arduino UNO com a leitura do potenciômetro. Além disso, algumas conversões são realizadas, devido à diferença da resolução do I2C existente entre a Raspberry Pi e o Arduino UNO. A leitura é exibida tanto no monitor serial da ArduinoIDE, quanto printado no terminal da Raspeberry, o que permitiu constatar que a leitura estava coincidindo em ambos os dispositivos.
	
	- O código referente a esta parte é o [```POTENTIOMETER_I2C.py```](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20V/POTENTIOMETER_I2C.py).
    - Já para o Arduino UNO, o projeto da ArduinoIDE está contido na pasta [```/I2C_POTENTIOMETER```](https://github.com/FernandoCZanchetta/SEL0337/tree/main/Pr%C3%A1tica%20V/I2C_POTENTIOMETER).

    - As imagens do terminal da Raspberry Pi e do Monitor Serial da ArduindoIDE exibindo o mesmo valor de leitura do potenciômetro estão presentes abaixo:

    ![Terminal](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20V/Images/Terminal.png?raw=true)

    ![Monitor Serial](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20V/Images/Serial_Monitor.png?raw=true)