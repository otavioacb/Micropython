# Componentes utilizados 

  Os códigos foram desenvolvidos e testados utilizando o **ESP8266** com **Micropython**. A ponte H para controle dos motores DC foi a proveniente do circuito integrado **L293D**, mais especificamente do motor shield L293D para ESP8266. Por último, utilizei uma bateria 9V para alimentação dos motores, e, não aconselho o uso da porta USB do seu computador para alimentação dos motores. <br>
  
  ![Motor Shield L293D para ESP8266](https://user-images.githubusercontent.com/35488608/157535500-b82f9661-2ed1-4d05-b7eb-2cca8ba5f527.jpeg)
  > Motor shield L293D utilizado com ESP8266<br>
  
  
  ![Circuito integrado L293D](https://user-images.githubusercontent.com/35488608/157535492-5689187a-3b79-4611-b32a-83a6ade0cddf.jpeg) 
  > Circuito integrado L293D, componente substituto do shield.

# Conexões 
  
  Ao utilizar o shield, é preciso, apenas, encaixar o ESP no espaço reservado, conectar os fios de cada motor nos encaixes pro motor A e B e por último alimentar o shield com a bateria pelos pinos **VM** e **GND**. Além disso, o shield precisa de um mini jumper para conexões entre linhas, pois ele é utilizado para conectar o pino VIN com o VM, localizados imediatamente atrás das conexões da bateria e dos motores. <br><br>
  O projeto, também, pode ser feito com outra placa programada por Micropython. Para fazer as conexões, com outras placas, recomendo que dê uma olhada no arquivo **circuito-L293D.qet**. Nesse arquivo, tem de forma detalhada como realizar as conexões do L293D com os motores. Vale destacar, que no diagrama de conexões os pinos **IN 1**, **IN 2**, **IN 3** e **IN 4** são os pinos de entrada dos sinais para os motores. Por último, lembre-se de conectar o GND da placa com o da bateria pra fechar o circuito corretamente.
  
# Como utilizar os códigos 

  Para controlar os motores, é necessário salvar os arquivos **motor.py**, **createMotor.py** e **controlMotor.py**. O motor.py é responsável por criar as conexões dos pinos, a velocidade e a direção do motor. Já, createMotor.py é responsável por criar um objeto da classe Motor e, por meio de uma única função controlar de uma forma mais fácil a direção e a velocidade do motor. Enquanto, que em controlMotor.py é criado dois objetos da classe ControlMotor, um para o motor A e outro para o B, e nesse arquivo conseguimos controlar 1 motor por vez ou os dois ao mesmo tempo.

```python
from controlMotor import ControlMotor

motores = ControlMotor()

# Controla a velocidade do Motor A
motores.controlA(600) # Frente
motores.controlA(-600) # Trás

# Controla a velocidade do Motor B
motores.controlB(600) # Frente
motores.controlB(-600) # Trás

# Controla a velocidade dos 2 motores
motores.controlAll(600, 600) # Frente
motores.controlAll(-600, -600) # Trás
motores.controlAll(-600, 600) # Direita
motores.controlAll(600, -600) # Esquerda
```
