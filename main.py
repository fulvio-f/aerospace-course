#Início do programa
print("Hello, Sábado Aeroespacial!")

#Adicionando bibliotecas importantes para o projeto
import network
import time
import ujson as json
import urequests as requests
import machine
'''
#Conectando o simulador wokwi a internet
print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
#Altere esses valores para a sua rede de acesso a internet
SSID  = 'Wokwi-GUEST'
senha = ''
sta_if.connect(SSID, senha)
while not sta_if.isconnected():
  print(".", end="")
  time.sleep(0.1)
print("Connected!")
'''

#Salvando em uma variável o número dos pinos do LED
R = machine.Pin(14)
G = machine.Pin(13)
B = machine.Pin(12)

#Inicializa a modulação PWM nos pinos
pwmR = machine.PWM(R)
pwmG = machine.PWM(G)
pwmB = machine.PWM(B)

#Determina a frequência do PWM
freq = 500
pwmR.freq(freq)
pwmB.freq(freq)
pwmG.freq(freq)

#Determina o ciclo de trabalho com todas as cores acesas para teste
brilho_max = 1023
brilho_min = 0
pwmR.duty(brilho_max)
pwmG.duty(brilho_max)
pwmB.duty(brilho_max)

#Inicia os canais PWM para teste dos leds
pwmR
pwmG
pwmB

#------------------ADICIONAR VIA JSON-------------------------------------------#
#Recebe os dados de temperatura de marte

#Salva a temperatura máxima e mínima do dia em variáveis
temp_max_C = 20
temp_min_C = 5
temp_atual = 15
#-------------------------------------------------------------------------------#

#Converte a temperatura para kelvin, para eliminar temperaturas negativas
def temp_escala_Kelvin(temp):
  temp_K = temp + 273.15
  return temp_K

temp_max_K = temp_escala_Kelvin(temp_max_C)
temp_min_K = temp_escala_Kelvin(temp_min_C)

#Cria uma nova escala, entre 0 e 1023 para a temperatura do dia
#Nesta escala, a temperatura máxima do dia vai ser 1023 e a mínima vai ser 0
def temp_escala_pwm(temp_lida):
  temp_pwm = int((temp_lida - temp_min_K) * (1023/(temp_max_K-temp_min_K)))
  return temp_pwm


#Le a temperatura atual fornecida e converte para a escala do pwm
temp_lida = temp_atual
temp_lida_K = temp_escala_Kelvin(temp_lida)
temp_pwm = temp_escala_pwm(temp_lida_K)

if temp_pwm > 1023:
  temp_pwm = 1023

if temp_pwm < 0:
  temp_pwm = 0


#Altera a cor dos LEDs a depender de quão quente ou frio está marte no momento
brilho_B = brilho_min + temp_pwm
brilho_R = brilho_max - temp_pwm
pwmB.duty(brilho_B)
pwmR.duty(brilho_R)

#Atualiza os LEDs
pwmR
pwmG
pwmB