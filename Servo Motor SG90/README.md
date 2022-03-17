# Componentes utilizados
  
  Esta versão do projeto foi testada com o **Servo Motor SG90 de 180°** com o **ESP8266**. 

  ![servo_motor](https://user-images.githubusercontent.com/35488608/158857300-492125cb-f0c3-44d1-aa2b-15b828846c84.jpeg)
  > Servo motor SG90.

# Conexões

  O SG90 possui o pino VCC alimentado de 3.3V até 6V, o GND e o PWM. Os pinos **VCC** e **GND** são conectados da forma usual de alimentação de qualquer componente ou módulo. No entanto, o pino **PWM**, como o nome sugere, é obrigatório o uso de um pino PWM do microcontrolador que emita um sinal de **50Hz**. Assim, ao conectar no ESP8266 o servo funcionará corretamente, mas no ESP32 o PWM não funciona bem a 50Hz e esse continuo buscando uma alternativa para o problema. <br> <br>
  O arquivo **servo-motor-esp8266** exemplifica a conexão entre o servo e o ESP8266. Vale destacara que o pino PWM não precisa ser o mesmo do arquivo. Além disso, se estiver utilizando outro microcontrolador e existir dúvidas na conexão o arquivo pode lhe dar uma ajuda nessa parte.
  
# Como utilizar os códigos

  O arquivo **servo.py** possui a classe **ServoMotor** que irá facilitar o controle do servo. Essa classe é responsável por receber um ângulo para o servo e converter o valor para o duty cycle correto do PWM.
  
```Python
from servo import ServoMotor
from machine import Pin
from time import sleep

servo = ServoMotor(Pin(4))

# Move o servo de 0° até 180° de 10 em 10 passos
for i in range(0, 181, 10):
  servo.angle = i
  sleep(0.5)
  print(servo.angle)
  
for i in range(180, -1, -10):
  servo.angle = i
  sleep(0.5)
  print(servo.angle)
```
