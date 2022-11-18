import ubluetooth
import ubinascii
import urequests
import ujson
from micropython import const


_IRQ_SCAN_RESULT = const(5)
_IRQ_SCAN_DONE   = const(6)



def bt_irq(event, data):
    if event == _IRQ_SCAN_RESULT:
        addr_type, addr, connectable, rssi, adv_data = data
        addr_hex = ubinascii.hexlify(addr)
        if '{}'.format(addr_hex) == 'b\'10521c688846\'':
            name = "H1"
            #print('name:{} addr:{} rssi:{} '.format(name, addr_hex, rssi ))
            f=open("H1_270_200cm.csv","a")
            data=[name,str(addr_hex),str(rssi)]
            f.write(data[0]+","+data[1]+","+data[2]+"\n")
            f.close()
            
            #send_db(name, str(addr_hex), rssi)
        if '{}'.format(addr_hex) == 'b\'10521c67618a\'':
            name = "H2"
            #print('name:{} addr:{} rssi:{} '.format(name, addr_hex, rssi ))
            f=open("H2_150_200cm.csv","a")
            data=[name,str(addr_hex),str(rssi)]
            f.write(data[0]+","+data[1]+","+data[2]+"\n")
            f.close()
            #send_db(name, str(addr_hex), rssi)
        if '{}'.format(addr_hex) == 'b\'083af26e899a\'':
            name = "H3"
            #print('name:{} addr:{} rssi:{} '.format(name, addr_hex, rssi ))
            f=open("H3_180_200cm.csv","a")
            data=[name,str(addr_hex),str(rssi)]
            f.write(data[0]+","+data[1]+","+data[2]+"\n")
            f.close()
            #send_db(name, str(addr_hex), rssi)
 
        

    elif event == _IRQ_SCAN_DONE:
        print('Scan compelete')
        pass

def main():
    ble = ubluetooth.BLE()
    
    if ble.active() == False:
        ble.active(True)

    ble.irq(bt_irq)
    ble.gap_scan(10000000, 50000, 25000)

if __name__ == "__main__":
    main()












