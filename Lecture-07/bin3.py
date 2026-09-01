<<<<<<< HEAD
import struct
with open("records.bin","rb")as file:
    data=file.read(struct.calcsize('i20sif'))
    record=struct.unpack('i20sif',data)
    record=(record[0],record[1].decode().strip('x\00'),record[2],record[3])
=======
import struct
with open("records.bin","rb")as file:
    data=file.read(struct.calcsize('i20sif'))
    record=struct.unpack('i20sif',data)
    record=(record[0],record[1].decode().strip('x\00'),record[2],record[3])
>>>>>>> 0c8a140320000645ebb57b05ba11c74ce7305e4c
    print(f"ID: {record[0]},Name: {record[1]},Age: {record[2]},GPA: {record[3]}")