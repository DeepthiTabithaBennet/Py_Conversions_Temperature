#TASK :
	#Convert the given temperature to Celsius
	
	#(Farenheit - 32) / 1.8 = Celsius

#INPUT FORMAT :
	#Temperature in Farenheit

#OUTPUT FORMAT :
	#Temperature in Celsius
	
#__________________________________________________________________________________#

Farenheit = float(input())

x = Farenheit - 32.0
y = x * 5.0
Celsius = y / 9.0

print(Farenheit, 'Farenheit in Celsius is', Celsius)
