# Componentes utilizados

  O shift register utilizado foi o 74HC595N que possibilitou o controle de 8 LEDs. A placa para o desenvolvimento foi o ESP8266, mas outras placas que funcionem com Micropython podem ser utilizadas. 
  
  ![74hc595](https://user-images.githubusercontent.com/35488608/157538142-9f126905-e72d-452e-a9e0-6996a40739ca.jpeg)
  > Circuito integrado 74HC595
# Conexões 

  Neste projeto, é importante prestar atenção nas conexões, pois muitas portas não irão funcionar com shift register. Primeiramente, se você estiver utilizando o ESP8266 ou ESP32 confira os arquivos que começam com **circuito-ESP** de extensão **qet**. Esses arquivos irão mostrar as conexões realizadas que derão certo pra cada placa. No entanto, caso esteja utilizando outras placas consulte o arquivo **circuito-geral.qet**. <br><br>
  No arquivo circuito-geral, as conexões **SER**, **RCLK**, **SRCLK**, **VCC** e **SRCLR** não estarão sendo utilizadas, pois mudam a conexão dependendo da placa utilizada. Os pinos SER, RCLK e SRCLK devem ir nos pinos digitais da placa, pois, o SER é por onde os dados entram, o RCLK habilita a entrada de dados e o SCRLK é o clock do shift register. Enquanto que o VCC e o SRCLR devem ir nos pinos de alimentação e de 3.3V, respectivamente. Por último, vale destacar que se a alimentação do VCC não for suficiente parte dos LEDs não irão acender, então, pode ser utilizado uma alimentação externa de até 6V para o shift register.
  
# Como utilizar os códigos

  Após as conectar tudo corretamente, salve os arquivos **led.py** e **controlLed.py** na placa. O arquivo led.py é onde fica a comunicação com o módulo mudando o estado do pino do RCLK e SRCLK para enviar os estados de cada pino do shift register. Os estados de cada pino devem ser enviados em uma string com 8 caracteres, por exemplo '10101010', '11111111' ou '10000001', onde 1 indica o LED ligado e 0 desligado. Por último, é preciso importar a classe ControlLed do arquivo controlLed.py, pois lá ficam todas as funções com padrões predefinidos, mas caso queira criar seus próprios padrões basta importar a classe Led de led.py e utilizar o método shift() para enviar os estados dos LEDs.
  
 ```python
 from controlLed import ControlLed
 from led import Led
 
 
 control_led = ControlLed()
 led = Led()
 
 # Padrões predefinidos
 control_led.on() # Liga todos os LEDs
 control_led.off() # Desliga todos os LEDs
 control_led.blink('10101010', 10) # Pisca um padrão dos leds por um tempo específico
 
 # Comunicação direta
 led.shift('11111111') # Liga todos os LEDs
 led.shift('00000000') # Desliga todos os LEDs
 
 led.shift('10101010') # Liga apenas os ímpares
 led.shift('01010101') # Liga apenas os pares
 ```
