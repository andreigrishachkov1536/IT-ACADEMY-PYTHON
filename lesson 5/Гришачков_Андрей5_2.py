packets = [1, 1, 1, 0, 1, 0, 0, 1, 0, 1]
donepackets=0
total_donepackets=0
previous_packet = 1
for packet in packets:
    if packet==1:
        donepackets+=1
        total_donepackets+=1

    elif previous_packet == 0:
        print("Обнаружен критический сбой сети! Соединение разорвано.")
        print(f"Число успешных пакетов до сбоя {donepackets}")
        break
    previous_packet = packet

else:

    print(f"Число успешных пакетов  {total_donepackets}")








