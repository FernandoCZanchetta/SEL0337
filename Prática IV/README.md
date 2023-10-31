# Prática IV - Introdução ao Uso de Periféricos Embarcados e GPIO da Raspberry Pi

Para uso do GPIO da Raspberry Pi em aplicações embarcadas com programação em Python, é necessário o uso de bibliotecas como a ```RPi.GPIO``` ou ```GPIO Zero```, tais bibliotecas permitem que, por meio de funções pré-definidas, os pinos de GPIO sejam manipulados de forma a realizarem o que for desejado.

Para utilizar PWM (Pulse Width Modulation) com a biblioteca RPI.GPIO, foram utilizadas as funções:
  - pwm = GPIO.PWM(GPIO_PIN, PWM_FREQUENCY) - Define uma instância PWM chama ```pwm``` utilizando o pino ```GPIO_PIN``` com frequência ```PWM_FREQUENCY```;
  - pwm.start(DUTY_CYCLE) - Inicia a instância PWM chamada ```pwm``` com valor de duty cycle definido em ```DUTY_CYCLE```;
  - pwm.ChangeDutyCycle(DUTY_CYCLE) - Altera o valor do duty cycle da instância PWM chamada ```pwm``` para o valor de duty cycle definido em ```DUTY_CYCLE```.

Para utilização de sensores com as bibliotecas acima basta observar a implementação dos mesmos com as bibliotecas citadas, buscando realizar corretamente a conexão entre os pinos do sensor e os pinos GPIO da Raspberry. Além disso, uma grande gama de [exemplos](https://gpiozero.readthedocs.io/en/stable/recipes.html) está presente na documentação da biblioteca GPIO Zero como pode ser visto no site da mesma.

A prática em questão foi dividida em duas partes:

- Na primeira delas foi implementado um circuito utilizando modulação de pulso (PWM), de forma que, em um período tempo definido no código, o LED presente circuito aumenta o seu brilho gradativamente até chegar em seu brilho máximo (por meio do ciclo de trabalho do PWM), e, depois disso o LED apaga e o processo recomeça novamente.
	- A onda PWM gerada foi analizada no osciloscópio, como pode ser visto na figura abaixo. A partir desta, constata-se que, no momento da obtenção da imagem o duty cycle era de 48,02% e a frequência condiz com o esperado, já que, como o período mostrado é de 5 ms, calcula-se que a frequência correspondente é 200 Hz, como definido no código.

		![Osciloscópio](https://github.com/FernandoCZanchetta/SEL0337/blob/pratica-4/Pr%C3%A1tica%20IV/Images/PWM%20Wave%20-%20Scope.png)
	
	 - O circuito montado para possíbilitar a execução desta parte está exibido nas duas figuras abaixo. A diferença existente entre ambas as fotos é o valor do duty cycle atual do código no momento em que foram tiradas, o que, consequentemente, permite observar uma diferença na intensidade do brilho do LED. A montagem do circuito é relativamente simples, consistindo em um LED ligado em série com um resistor, e estes conectados com um pino GND e o pino GPIO 21 da Raspberry.
	 
	 	![LED 1](https://github.com/FernandoCZanchetta/SEL0337/blob/pratica-4/Pr%C3%A1tica%20IV/Images/LED_1.png)

		![LED 2](https://github.com/FernandoCZanchetta/SEL0337/blob/pratica-4/Pr%C3%A1tica%20IV/Images/LED_2.png)

	 - O código referente a esta parte é o [```pwm_led.py```](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20IV/pwm_led.py).

- Na segunda parte da prática foi implementado um projeto da documentação do GPIO Zero. O projeto escolhido foi o do [GPIO Music Box](https://gpiozero.readthedocs.io/en/stable/recipes.html#gpio-music-box) que consiste em um botão que, quando ativado, faz com que a Raspberry Pi emita um som. No código elaborado, foram implentados cinco botões, sendo que cada um deles estava associado a um arquivo de áudio com sons de um instrumento musical, no caso uma bateria. Portanto, quando algum dos botões fosse pressionado, o som vinculado ao mesmo seria emitido. 
	- A montagem prática realizada para implementar o circuito está presente na figura abaixo, consistindo nos botões citados acima, conectados todos ao GND em um terminal e a pinos GPIO em outro, além de ter sido utilizada a caixa de som, conectada a Raspberry Pi para que fosse possível que a mesma emitisse os sons desejados.

		![MUSIC BOX](https://github.com/FernandoCZanchetta/SEL0337/blob/pratica-4/Pr%C3%A1tica%20IV/Images/MUSIC_BOX.png)
	
	- O código referente a esta parte é o [```sound.py```](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20IV/sound.py).