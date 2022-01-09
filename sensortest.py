#Bibliotheken
import lgpio
import time

#GPIO definieren (Modus, Pins, Output)
h = lgpio.gpiochip_open(0)
GPIO_TRIGGER = 23
GPIO_ECHO = 24
lgpio.gpio_claim_output(h, GPIO_TRIGGER)
lgpio.gpio_claim_input(h, GPIO_ECHO)

def entfernung():
    # Trig High setzen
    lgpio.gpio_write(h, GPIO_TRIGGER, 1)

    # Trig Low setzen (nach 0.01ms)
    time.sleep(0.00001)
    lgpio.gpio_write(h, GPIO_TRIGGER, 0)

    Startzeit = time.time()
    Endzeit = time.time()

    # Start/Stop Zeit ermitteln
    while lgpio.gpio_read(h,GPIO_ECHO) == 0:
        Startzeit = time.time()

    while lgpio.gpio_read(h,GPIO_ECHO) == 1:
        Endzeit = time.time()

    # Vergangene Zeit
    Zeitdifferenz = Endzeit - Startzeit

    # Schallgeschwindigkeit (34300 cm/s) einbeziehen
    entfernung = (Zeitdifferenz * 34300) / 2

    return entfernung

if __name__ == '__main__':
    try:
        while True:
            distanz = entfernung()
            print ("Distanz = %.1f cm" % distanz)
            time.sleep(1)

        # Programm beenden
    except KeyboardInterrupt:
        print("Programm abgebrochen")
        lgpio.gpiochip_close(h)