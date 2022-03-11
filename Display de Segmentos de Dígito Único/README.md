
# Componentes utilizados

  O display de 7 segmentos com 1 dígito possui 10 pinos de conexões. A placa para o uso desse display deve possuir 8 pinos de saída de dados livres. Assim, neste projeto, foi utilizado o ESP32 e em cada conexão entre os pinos do display e da placa utilizou-se de um resistor de 330 ohms. 
  
  ![display_segmento](https://user-images.githubusercontent.com/35488608/157677868-f3c17a61-fa68-4d84-acec-6d262e0dd556.jpeg)
  > Display de 7 segmentos de dígito único.

# Conexões

  O display possui 2 pinos que são ligados ao GND da placa, enquanto, que os outros 8 funcionam como a ligação de LEDs. Essa ligação dos pinos devem ir nas portas digitais das placa, com a função de saída, e entre a ligação dos pinos deve haver 1 resistor de 330 ohms. Além disso, pela ligação do display ser correspondente a ligação de 8 LEDs existe a facilidade de substituição da placa utilizada, pois, o uso do display está voltado em torno do controle de energia desses LEDs.
  O arquivo **segment-esp32.qet** possui o esquema de conexões realizados no projeto. Esse arquivo possui as informações sobre qual LED cada pino controla, e, na imagem abaixo é possível vizualizar a divisão do display. Caso ocorra o uso de outra placa, o arquivo pode auxiliar na interpretação do circuito para os componentes disponíveis no momento.
  
  ![segment-display-division](https://user-images.githubusercontent.com/35488608/157680003-c5bfc556-f23b-4e21-8b07-405f4ed62e62.png)
  > Divisão dos segmentos do display.

# Como utilizar os códigos 

  A classe do arquivo **segment_display.py** possibilita o uso do ponto e da representação dos números de 0 a 9. Para representação de letras, o display é limitado, pois, possibilita o uso das letras de A a F. Assim, para utilizar o módulo é preciso criar uma instância da classe e passar os números dos pinos utilizados como parâmetros, e, de preferência organizados de A a G. 
  
```Python
from segment_display import SegmentDisplay
from time import sleep_ms

A, B, C, D, E, F, G, DP = (13, 12, 14, 27, 26, 25, 15, 2)

display = SegmentDisplay(A, B, C, D, E, F, G, DP)

# Representa os número de 0 a 9 com 100 milisegundos de intervalo
for i in range(10):
  display.value(i)
  sleep_ms(100)
  
# Desliga o display
display.off()

# Liga o display com o último valor passado
display.on()

# Liga o ponto
display.dot(1)

# Desliga o ponto
display.dot(0)
```
