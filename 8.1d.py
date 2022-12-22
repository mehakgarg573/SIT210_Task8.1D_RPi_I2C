import smbus
import time

address = 0x23	
start = 0x01	
stop = 0x00	
reset = 0x07	

bus = smbus.SMBus(1)

def light_read():
	new_add = bus.read_i2c_block_data(address, address)
	value = conversion_of_light(new_add)
	return value
	
def conversion_of_light(new_add):
	converted = ((new_add[1] + (256 * new_add[0]))/1.2)
	return converted

try:
	while 1:
		intensity = light_read()
		print(f"Reading: {intensity}")
		
		print("Intensity:")
		if(intensity >= 4500):
			print("Intensity: Too bright")
		elif(intensity >= 500 and intensity < 4500):
			print("Intensity: Bright")
		elif(intensity >= 90 and intensity < 500):
			print("Intensity: Medium")
		elif(intensity > 50 and intensity < 90):
			print("Intensity: Dark")
		elif(intensity < 50):
			print("Intensity: Too dark")
		time.sleep(1)

except KeyboardInterrupt:
	print("Closing")