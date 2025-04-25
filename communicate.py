# đoạn code này dùng để gửi dữ liệu từ python sang cổng COM (chú ý cổng COM tùy mỗi máy)

# pip install pyserial
import serial.tools.list_ports
import serial
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portsList = []
# Đoạn code này kiểm tra xem cổng COM nào đang có và lựa chọn cổng COM đang kết nối với con vi xử lý
for one in ports:
    portsList.append(str(one))
    print(str(one))

com = input("Chon cong COM #: ")

for i in range(len(portsList)):
    if portsList[i].startswith("COM" + str(com)):
        use = "COM" + str(com)
        print(use)

serialInst.baudrate = 9600 #baudrate mặc định
serialInst.port = use  #Cổng COM kết nối với vi điều khiển 
serialInst.open()
def serialwritedata(data):
    serialInst.write(data.encode('utf-8')) # gửi data từ camera qua cổng COM theo định dạng UTF-8
