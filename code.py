import board
import analogio
import time
from lcd.lcd import LCD

from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

TMP36_PIN = board.A0  # Analog input connected to TMP36 output.

i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c,0x27), num_rows=2, num_cols=16)
# Function to simplify the math of reading the temperature.
lcd.set_cursor_pos(0,0)
lcd.print("temp:")
def tmp36_temperature_C(analogin):
    millivolts = analogin.value * (analogin.reference_voltage * 1000 / 65535)
    return (millivolts - 500) / 10


tmp36 = analogio.AnalogIn(TMP36_PIN)


while True:
   
    temp_C = tmp36_temperature_C(tmp36)
   
    temp_F = (temp_C * 9/5) + 32
   
    print("Temperature: {}C {}F".format(temp_C, temp_F))
    time.sleep(1.0)
    lcd.set_cursor_pos(0, 6)
    lcd.print( "{}C " .format(temp_C)) 
    lcd.set_cursor_pos(1,0)
    lcd.print( "{}F" .format(temp_F)) 