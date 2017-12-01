#需安装pyvisa模块
import visa

rm = visa.ResourceManager()
print(rm.list_resources())
my_instrument = rm.open_resource('ASRL1::INSTR')
print(my_instrument)
values = list(range(100))
my_instrument.write_binary_values('WLISt:WAVeform:DATA somename,', values)