# Componentes Utilizados

  Os componentes utilizados foram **1 Módulo KY-016 LED RGB** e **1 ESP8266**. A utilização do módulo foi opcional, mas o uso de um LED RGB comum funciona da mesma forma.
  
  ![led_rgb](https://user-images.githubusercontent.com/35488608/158032667-25a64260-eef4-41c7-8785-850be1072c91.jpeg)
  > Módulo KY-016 LED RGB.

# Conexões
  
  Antes de realizar as conexões é preciso entender o tipo de LED RGB que você possui. Existem dois tipos de LEDs que são o **cátodo comum** e o **ânodo comum**. O cátodo comum possui o polo negativo compartilhado com os 3 LEDs que compões o RGB, enquanto, que o ânodo comum possui o polo positivo compartilhado com os LEDs. Assim, durante o uso desse LED as conexões da parte RGB são as mesmas para os dois tipos, mas o pino de energia é diferente indo no **VCC** ou no **GND** da placa.

  ![led-rgb-tipos](https://user-images.githubusercontent.com/35488608/158033255-39581ff0-4105-4e3b-916f-3d03af55f055.jpeg)
  > Tipos de LEDs RGB.
  
  Seguindo adiante, para o uso do LED é preciso conectar os 3 pinos que controlaram as cores **vermelha**, **verde** e **azul** nos pinos PWM da placa. Neste projeto, foi utilizado o ESP8266 e seus pinos PWM são o 0, 2, 4, e 5. Caso utilize de outra placa de desenvolvimento, procure quais os pinos são PWM e que possuem a função de saída de dados. Assim, para facilitar as conexões o arquivo **led-rgb.qet** possui uma representação de como os pinos do LED foram conectados a placa.
  
# Como utilizar os códigos
  
  A classe **RGB** do arquivo **rgb.py** é responsável por criar e controlar 3 pinos PWM para cada cor do LED. Essa classe facilita a troca de cores e a mudança de frequência do LED. O uso da classe é simples, mas na hora de criar a instância dela é importante passar corretamente os pinos seguindo a ordem do vermelho, verde e azul. 

```Python
from rgb import RGB

led_rgb = RGB(0, 4, 5)

# Muda as cores do LED
led_rgb.colors(255, 0, 0) # Vermelho
led_rgb.colors(0, 255, 0) # Verde 
led_rgb.colors(0, 0, 255) # Azul

# Muda a frequência do LED
# Possibilita o efeito de piscar
led_rgb.freq(300)
```
