# Componentes utilizados

  O código foi testado e desenvolvido utilizando o sensor ultrasssônico **HC-SR04** e os microcontroladores **ESP8266** e **ESP32**.
  ![ultrassonic](https://user-images.githubusercontent.com/35488608/160488663-30f5e664-6f71-4751-8e5e-fc77a4893b25.jpeg)
  > Ultrassônico HC-SR04

# Conexões
  
  As conexões do sensor devem ser feitas em portas digitais com a função de saída de dados. Esse sensor possui os pinos **Trigger**, será ligado e desligado por 10 microsegundos para habilitar a medição do sensor, e o **Echo**, responsável por receber os sinais ultrassôniocs enviado de volta. A conexão desses dois pinos são de livre escolha do usuário, desde que siga o requisito citado no início do parágrado.
  Os arquivo **ESP8266-hcsr04.qet** e **ESP32-hcsr04.qet** são exemplificações de possíveis conexões que podem ser feitas. Caso utilize de outro microcontrolador é possível utilizar esses arquivos como guias. 
  
# Como utilizar os códigos

  O sensor funciona ao acionar o pino trigger por 10us e, em seguida, medir o tempo em que o pino echo muda de estado lógico. Esses passos de medição e o cálculo da distância em si serão feitos pela classe **HCSR04** do arquivo **hc_sr04.py**. Nessa classe, também, está presente métodos para facilitar a obtenção da distância medida e a conversão do valor para as unidades de medida metro, centímetro ou milímetro.
  
```Python
from hc_sr04 import HCSR04

ultrassonic = HCSR04(5, 4) # HCSR04(trigger, echo, unit="m")

print(ultrassonic.distance())

print(ultrassonic.unit)

ultrassonic.unit = "cm"
print(ultrassonic.distance())

```
