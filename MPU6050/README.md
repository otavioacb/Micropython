# Componentes utilizados

  O projeto foi desenvolvido utilizando o **ESP32**, como a placa de desenvolvimento, e o **MPU6050**, como acelerômetro e giroscópio. Vale ressaltar que o MPU possui um sensor de temperatura, mas este projeto não faz uso dos valores dessa parte do módulo. 
  
  ![mpu6050](https://user-images.githubusercontent.com/35488608/158063247-26ac5ed1-19be-4ff0-ab4b-e2bf2373cd34.jpeg)
  > Acelerômetro e giroscópio MPU6050.

# Conexões 
  
  O MPU funciona via protocolo **I2C**, por isso seus pinos principais são o **SCL** e o **SDA**. Os pinos **XDA** e **XCL** são utilizados pra conexão de outros sensores complementares, mas não é o caso deste projeto. Os outros pinos são o **AD0**, responsável por definir o endereço do módulo, e o **INT**, capaz de interromper a saída de dados. Assim, para utilizar o módulo é preciso conectar o SCL, SDA, VCC e GND, sendo opcional conectar o AD0 para definição de endereço, pois sem conexão ou com nível lógico LOW o endereço é 0x68, caso queira utilizar o outro endereço basta definir o pino no nível lógico HIGH pra usar o endereço 0x69.<br><br>
  O arquivo **mpu6050.qet** representa as conexões com o ESP32. Caso utilize outro microcontrolador é importante testar as portas que irão funcionar corretamente com o módulo, pois existe algumas que não se comunicam corretamente ao utilizar a biblioteca SoftI2C ou I2C do micropython. Porém, este projeto é flexível a mudança das portas utilizadas como SCL e SDA. 
  
# Como utilizar os códigos

  A classe MPU6050 do arquivo **mpu.py** é a responsável por facilitar o acesso dos registros de memória do módulo. Ao definir a instância dessa classe, será possível calibrar o módulo e acessar os valores do acelerômetro e giroscópio. Além disso, a classa fornece um metódo que adiciona um complimentary filter nos valores antes de serem enviados para uso.
  
```Python
from machine import Pin
from time import sleep_ms, ticks_ms, ticks_diff
from mpu import MPU6050

# MPU6050(scl, sda)
mpu = MPU6050(Pin(5), Pin(2))

msOld = ticks_ms()
mpu.calibrate()

while True:
  # Carrega os valores dos sensores para uso pela class
  # Também retorna esses valores em um dicionário
  mpu.get_values()

  # Calcula o tempo passado para utilizar na hora de buscar 
  # o ângulo do giroscópio
  dt = ticks_diff(ticks_ms(), msOld)/1000.0
  msOld = ticks_ms()

  # Retorna os ângulos de rotação nos eixos x, y e z 
  # Esse método utiliza um filtro contra ruídos
  theta, phi, rho = mpu.get_complimentary_values(dt)
  
  # Espera um giro de 90° no eixo z
  if(abs(rho) >= 90):
      print("OK")
      break
  else:
      sleep_ms(100)
```
