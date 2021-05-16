#TASK :
	#Convert the given temperature to Farenheit
	
	#(Celsius * 9/5) + 32 = Farenheit

#INPUT FORMAT :
	#Temperature in Celsius

#OUTPUT FORMAT :
	#Temperature in Farenheit
	
#__________________________________________________________________________________#

Celsius = float(input())

x = Celsius * 9.0
y = x / 5.0
Farenheit = y + 32.0

print (Celsius, 'Celsius in Farenheit is', Farenheit)
