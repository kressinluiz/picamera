import serial

ser = serial.Serial("/dev/ttyS0", baudrate=2000000)
readings = []
done = False
while not done:
    print("Iniciando leitura!")
    ser.timeout = 5
    current_char = ser.read(20)
    print("Leitura encerrada!")
    print("Resultado: " + current_char)
    """ # check for equals sign
    if current_char == b'=':
        reading = ser.read(8)
        readings.append(reading)

    # this part will depend on your specific needs.
    # in this example, we stop after 10 readings
    # check for stopping condition and set done = True
    if len(readings) >= 10:
        done = True """
