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


## Visão Computacional com Câmera para Reconhecimento Facial

Para esta etapa, primeiramente, será implementado um sistema de reconhecimento facial simples, o qual será incrementado posteriormente para atingir o código final desta etapa.

Para permitir o uso da visão computacional, foi utilizada a biblioteca ```cv2``` (OpenCV) que fornece algumas funções úteis para visão computacional, dentre elas, o reconhecimento facial. Nos códigos desenvolvidos na prática, foram utilizadas as seguintes funções desta biblioteca, contidas nos trechos de código abaixo:
  - face_detector = cv2.CascadeClassifier('/home/sel/6219/Prática VI/Camera/haarcascade_frontalface_default.xml') - Carrega o classificador para detecção facial, que pode ser encontrado no diretório ```/home/sel/6219/Prática VI/Camera/haarcascade_frontalface_default.xml```, gerando o objeto ```face_detector```;
  - cv2.startWindowThread() - Inicia uma Thread para gerenciar janelas de visualização;
  - grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) - Utiliza a função ```cvtColor``` para converter a imagem ```img``` para escala de cinza, gerando a imagem ```grey```;
  - faces = face_detector.detectMultiScale(grey, 1.1, 5) - Utiliza o classificador em cascata ```face_detector``` para realizar a detecção dos rostos presentes na imagem em escala de cinza ```grey```, armazenado a posição dos mesmos na variável ```faces```;
  - cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0)) - Função utilizada para desenhar um retângulo verde ao redor do rosto presente na imagem original ```img```, baseado na posição dos rostos armazenadas em ```faces```;
  - cv2.imwrite(filename, img[y:y+h, x:x+w]) - Função para salvar apenas a parte da imagem que contém o rosto detectado (```img[y:y+h, x:x+w]```) como um arquivo JPEG cujo nome e diretório será ```filename```;
  - cv2.imshow("Camera", img) - Realiza a exibição da imagem com os retângulos desenhados (```img```) numa janela com título ```Camera```;
  - cv2.waitKey(1) - Aguarda 1ms antes de continuar com o loop e proceder para a próxima captura de imagem.

  Para permitir o salvamento das fotos no dispositivo, é necessário utilizar as bibliotecas ```os``` (Sistema Operacional) e ```time```, a primeira fornece algumas funções para interagir com o sistema operaciona da Raspberry Pi, e a segunda fornece algumas funções relacionadas ao controle de tempo. Nos códigos desenvolvidos na prática, foram utilizadas as seguintes funções destas bibliotecas, contidas nos trechos de código abaixo:
  - output_directory = '/home/sel/6219/Prática VI/Camera/detected_faces' - Define o diretório onde as imagens com rostos detectados serão armazenadas, no caso, numa pasta ```detected_faces```;
  - os.makedirs(output_directory, exist_ok = True) - Função utilizada para criar um diretório, caso ele não exista (```exit_ok = True```), cujo nome será ```output_directory```;
  - timestamp = int(time.time()) - Registra, na variável ```timestamp```, o valor do carimbo de data/hora Unix para o horário e data exatos no qual a foto foi tirada;
  - filename = os.path.join(output_directory, f"face_{timestamp}.jpg") - Gera um caminho e nome de arquivo (```filename```) único para a foto atual, concatenando:
    - O diretório de saída (```output_directory```);
    - A string ```"face_"```;
    - O carimbo de data/hora encontrado pela função descrita acima (```timestamp```);
    - A extensão do arquivo ```".jpg"```.

Para permitir o uso da câmera da Raspberry Pi, é necessário utilizar a biblioteca ```picamera2``` , que fornece o objeto referente a câmera para ser utilizado pelo código. Na prática, foram utilizadas as seguintes funções destas bibliotecas, contidas nos trechos de código abaixo:
  - picam2 = Picamera2() - Guarda o objeto ```Picamera2()``` sob nome de ```picam2```;
  - picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)})) - Função que configura a câmera (```picam2```) para criar uma visualização com formato de representação de cores 32 bits (```"format": 'XRGB8888'```) e resolução de 640x480 px (```"size": (640, 480)```);
  - picam2.start() - Função para iniciar a câmera (```picam2```);
  - img = picam2.capture_array() - Captura um quadro da câmera (```picam2```) e armazena-o na varável ```img```.

Para que haja o funcionamento do código, primeiramente deve-se conectar a câmera, atentando-se para que o placa esteja desligada. Após conectada, é possível testar o funcionamento da mesma com o simples comando ```libcamera-hello```. Além disso, é necessário baixar o arquivo do algoritmo Haar Cascade ([```haarcascade_frontalface_default.xml```](https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_frontalface_default.xml)), se atentando para o diretório onde o mesmo será salvo. Além disso é necessário instalar as bibliotecas Python OpenCV e PiCamera2 com o comando ```pip install opencv-python``` e ```pip install picamera2```. Com isso, ao utilizar o código referenciado abaixo, já pode-se verificar que ocorre a detecção do rosto, conforme as funções explicadas anteriormente, e as imagens são salvas no diretório especificado no código.
  - Código para detecção facial: [```facedetector.py```](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20VI/Camera/facedetector.py).

A partir deste código desenvolvido, foi proposto realizar uma alteração, na qual fosse adicionado algum outro recurso ao código. Optou-se por adicionar uma função para envio de e-mail após o reconhecimento de algum rosto pelo código anterior. Essa funcionalidade abre um leque de aplicações, com grande possibilidade de uso em segurança, por exemplo, permitindo informar alguém pelo e-mail quando um rosto fosse detectado numa câmera de vigilância instalada em sua residencia ou local de trabalho, permitindo assim o uso da Raspberry Pi com a câmera para garantir maior segurança para o indivíduo.

Para ser possível implementar a funcionalidade descrita acima, foi necessário adicionar as bibliotecas ```smtplib``` e ```email.message```, a primeira, responsável por estabelecer um servidor ```SMTP``` para realizar o envio do email, e a segunda, responsável por estabelecer uma estrutura pré-definida para uma mensagem de e-mail. Detalhando algumas funcionalidades de cada uma destas, temos o trecho de código onde é definida a função ```send_email(i)```, criada por nós:
  - msg = EmailMessage() - Define o objeto ```msg``` da classe ```EmailMessage()```;
  - msg.set_content(email_body) - Define o conteúdo do corpo do e-mail (```msg```) como sendo o contido na variável ```email_body```;
  - msg['From'] = from_email_addr - Define o remetente do e-mail (```msg```) como sendo o contido na variável ```from_email_addr```;
  - msg['To'] = to_email_addr - Define o destinatário do e-mail (```msg```) como sendo o contido na variável ```to_email_addr```;
  - msg['Subject'] = email_subject - Define o assunto do e-mail (```msg```) como sendo o contido na variável ```email_subject```;
  - msg.add_attachment(i, maintype='image', subtype='png') - Adiciona um anexo ao e-mail (```msg```), sendo aquele a imagem ```i``` registrada pela detecção facial;
    
  - server = smtplib.SMTP_SSL('smtp.gmail.com', 465) - Cria um servidor SMTP SSL chamado ```server```, cujo host é ```'smtp.gmail.com'``` e cuja porta é ```465```;
  - server.ehlo() - Identifica-se para o servidor EMSTP utilizando um ```EHLO```, não fornecendo argumentos, utiliza o nome de domínio completo do host local;
  - server.login(from_email_addr, from_email_password) - Realiza o login no servidor SMTP (```server```) com usuário ```from_email_addr``` e senha ```from_email_password```;
  - server.send_message(msg) - Envia o e-mail ```msg``` com parâmetros definidos anteriormente;
  - server.quit() - Encerra a sessão SMTP com o servidor ```server``` e encerra a conexão.

Como o código desenvolvido é open source e necessita de credenciais para fazer login no servidor SMTP, adicionou-se a biblioteca ```dotenv``` para evitar que senhas e informações sensíveis fiquem no código, já que esta biblioteca permite gerenciar valores salvos em variáveis de ambiente, por exemplo, um arquivo ```.env```. Sendo assim, as funções utilizadas de tal biblioteca são:
  - secrets = dotenv_values("Camera/.env") - Salva no dicionário ```secrets``` os valores contidos e indexados no arquivo ```.env``` presente na pasta ```Camera```;
  - from_email_addr = secrets["SENDEREMAIL"] - Define o endereço de e-mail do remetente ```from_email_addr``` como o valor contido no dicionário ```secrets``` sob chave ```"SENDEREMAIL"```;
  - from_email_password = secrets["SENDERPASSWORD"] - Define a senha do e-mail do remetente ```from_email_password``` como o valor contido no dicionário ```secrets``` sob chave ```"SENDERPASSWORD"```;
  - to_email_addr = secrets["RECEIVEREMAIL"] - Define o endereço de e-mail do destinatário ```to_email_addr``` como o valor contido no dicionário ```secrets``` sob chave ```"RECEIVEREMAIL"```.

Para utilizar a biblioteca acima foi criado um arquivo ```.env```, que segue a seguinte estrutura:

```
SENDERDOMAIN =
SENDEREMAIL = @${SENDERDOMAIN}
SENDERPASSWORD = 
RECEIVERDOMAIN = 
RECEIVEREMAIL = @${RECEIVERDOMAIN}
```

Acima, SENDERDOMAIN é o domínio do e-mail do remetente, SENDEREMAIL é o e-mail do remente (bastando inserir o usuário, por exemplo, python@${SENDERDOMAIN}), SENDERPASSWORD é a senha do e-mail do remetente, RECEIVERDOMAIN e RECEIVEREMAIL seguem uma lógica identica a SENDERDOMAIN e SENDEREMAIL.

Para garantir que o arquivo ```.env``` não seja rastreado pelo Git, é necessário adicionar um ```.gitignore```. Este arquvio pode se limitar a ter somente o ```.env```, no entanto, optou-se por utilizar o template para Python fornecido pela [coleção de arquivos ```.gitignore``` do Github](https://github.com/github/gitignore/tree/main), que contém uma grande gama destes arquivos e tem grande utilizade no desenvolvimento de códigos e aplicações nas mais diferentes linguagens de programação e frameworks.

Para demonstrar o funcionamento deste código, seguem algumas imagens exibindo alguns rostos detectados pelo mesmo e também um print de um dos e-mails enviado.

![ROSTO1](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20VI/Images/face_1701699000.png?raw=true)

![ROSTO2](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20VI/Images/face_1701699001.png?raw=true)

<!--- INSERIR FOTO DE UM EMAIL ENVIADO AQUI PARA MOSTRAR QUE FUNCIONA --->

![EMAIL](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20VI/Images/EMAIL.png?raw=true)

## Git e GitHub

Os códigos desenvolvidos nesta prática e nas práticas anteriores estão sendo versionados por meio do Git e estão também disponíveis no GitHub, como esta prática também tem enfoque no uso destas ferramentas, um arquivo .txt está presente junto aos arquivos desta prática, onde consta o resultado do comando ```git log``` após serem realizados todos os outros comandos necessários para versionar o código e subi-lo para o GitHub, como, por exemplo, ```git add```, ```git commit -m```, ```git push```, ```git status```, entre outros. O arquvio pode ser visto em [```Git.txt```](https://github.com/FernandoCZanchetta/SEL0337/blob/main/Pr%C3%A1tica%20VI/Git.txt).