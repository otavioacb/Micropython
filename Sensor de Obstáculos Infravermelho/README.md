# Componentes utilizados
  A biblioteca foi criada com auxílio do módulo **Sensor de Obstáculos Infravermelho Reflexivo**, e, pode ser utilizada com outros módulos de pinagem e funcionamento similar.
  
  ![ir_sensor](https://user-images.githubusercontent.com/35488608/167315082-04fe59a5-383e-48ee-a62f-ebc23c3e0847.jpeg)
  > Sensor de obstáculos 

# Conexões
  O módulo possui, apenas, 3 pinos para conexão. O **GND** e o **Vcc** são para alimentação. O pino **OUT** será o pino digital que passará a informação da presença, ou não, do obstáculo. Esse pino deve ir em uma porta digital que possua a função de entrada. Por último, caso reste dúvidas da conexão o arquivo **obstacle-esp32.qet** possui um exemplo de esquema de conexões utilizado e que pode ser replicado em outros microcontroladores.
  
# Como utilizar os códigos 
  O uso do sensor é baseado na leitura do nível lógico do pino OUT. Quando, o sensor estiver próximo do obstáculo o pino irá possuir o valor 0. Logo, a classe **ObstacleSensor** ao receber o pino do sensor irá fazer a leitura desses valores e devolver um valor booleano por meio dos métodos **detected()** e **not_detected()**.
  
```Python
from obstacle import ObstacleSensor
from machine import Pin

ob_sensor = Pin(2, Pin.IN)

print(ob_sensor.detected()) # Retorna True se tiver detectado algo, caso contrário retorna False

print(ob_sensor.not_detected()) # Retorna True se não tiver detectado, e, False se tiver detectado
```
