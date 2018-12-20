data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data))
print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))

x = 12343523457848324355146124363464
print(x.to_bytes(16,'big'))
print(x.to_bytes(16, 'little'))
