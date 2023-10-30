# Prática IV - Introdução ao Uso de Periféricos Embarcados e GPIO da Raspberry Pi

Para uso do GPIO da Raspberry Pi em aplicações embarcadas com programação em Python, é necessário o uso de bibliotecas como a ```RPi.GPIO``` ou ```GPIO Zero```, tais bibliotecas permitem que, por meio de funções pré-definidas, os pinos de GPIO sejam manipulados de forma a realizarem o que for desejado.

Para utilizar PWM (Pulse Width Modulation) com a biblioteca RPI.GPIO, foram utilizadas as funções:
  - pwm = GPIO.PWM(GPIO_PIN, PWM_FREQUENCY) - Define uma instância PWM chama ```pwm``` utilizando o pino ```GPIO_PIN``` com frequência ```PWM_FREQUENCY```;
  - pwm.start(DUTY_CYCLE) - Inicia a instância PWM chamada ```pwm``` com valor de duty cycle definido em ```DUTY_CYCLE```;
  - pwm.ChangeDutyCycle(DUTY_CYCLE) - Altera o valor do duty cycle da instância PWM chamada ```pwm``` para o valor de duty cycle definido em ```DUTY_CYCLE```.

Para utilização de sensores com as bibliotecas acima basta observar a implementação dos mesmos com as bibliotecas citadas, buscando realizar corretamente a conexão entre os pinos do sensor e os pinos GPIO da Raspberry. Além disso, uma grande gama de [exemplos](https://gpiozero.readthedocs.io/en/stable/recipes.html) está presente na documentação da biblioteca GPIO Zero como pode ser visto no site da mesma.

A prática em questão foi dividida em duas partes:

- Na primeira delas foi implementado um circuito utilizando modulação de pulso (PWM), de forma que, em um período tempo definido no código, o LED presente circuito aumenta o seu brilho gradativamente até chegar em seu brilho máximo (por meio do ciclo de trabalho do PWM), e, depois disso o LED apaga e o processo recomeça novamente. O código referente a esta parte é o ```pwm_led.py```.

- Na segunda parte da prática foi implementado um projeto da documentação do GPIO Zero. O projeto escolhido foi o do [GPIO Music Box](https://gpiozero.readthedocs.io/en/stable/recipes.html#gpio-music-box) que consiste em um botão que, quando ativado, faz com que a Raspberry Pi emita um som. No código elaborado, foram implentados cinco botões, sendo que cada um deles estava associado a um arquivo de áudio com sons de um instrumento musical, no caso uma bateria. Portanto, quando algum dos botões fosse pressionado, o som vinculado ao mesmo seria emitido. O código referente a esta parte é o ```sound.py```.