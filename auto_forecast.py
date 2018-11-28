#set cumulative oil production
np = input("Enter starting cumulative oil (MMSTB): ")
np = int(np)

#set initial oil rate (stb/d)
#init_oil_rate = input("Enter starting field oil rate: ")
#init_oil_rate = int(init_oil_rate)

#set forecast time-frame
forecast_month = input("Enter the number of months to forecast: ")
forecast_month = int(forecast_month)

#set production efficiency
prod_eff = input("Enter the production efficiency: ")
prod_eff = float(prod_eff)

#set facilities limits
water_limit = input("Enter water limit: ")
liquid_limit = input("Enter liquid limit: ")
water_limit = float(water_limit)*prod_eff
liquid_limit = float(liquid_limit)*prod_eff

#reset month counter
month = 0

while month <= forecast_month:
	
	#define the oil rate potential vs cum oil relationship
	oil_rate_potential = (-0.00000000010822*np**6 + 0.000000075835*np**5 - 0.0000033209*np**4 - 0.0089157*np**3 + 3.2881*np**2 - 843.15*np + 137160)*prod_eff
	
	#define the wor vs cum oil relationship
	wor = 1.7413*2.71828182845904**(0.0082265*np)
	
	#calculate the water rate potential
	water_rate_potential = oil_rate_potential*wor
	
	#calculate the liquid rate potential
	liquid_rate_potential = oil_rate_potential + water_rate_potential

	#calculate ratios
	fw = water_rate_potential / liquid_rate_potential

#recalculate rates based on facilities limits

	#below liquid and water limits
	if water_rate_potential < water_limit and liquid_rate_potential < liquid_limit:
		oil_rate = oil_rate_potential
		water_rate = water_rate_potential
		liquid_rate = liquid_rate_potential

	#below liquid limit but above water limit
	elif water_rate_potential > water_limit and liquid_rate_potential < liquid_limit:
		water_rate = int(water_limit)
		oil_rate = int(water_rate / wor)
		liquid_rate = int(water_rate + oil_rate)

	#below water limit but above liquid limit
	elif water_rate_potential < water_limit and liquid_rate_potential > liquid_limit:
		liquid_rate = int(liquid_limit)
		water_rate = int(liquid_rate * fw)
		oil_rate = int(liquid_rate - water_rate)

	#above liquid and water limits
	else:
		liquid_rate = int(liquid_limit)
		water_rate = int(water_limit)
		oil_rate = int(liquid_rate*(1-fw))

	#print out new oil rate
	print("-----------------------------")
	print(f"Oil Rate: {oil_rate}")
	print(f"Water Rate: {water_rate}")
	print(f"Liquid Rate: {liquid_rate}")
	
	#update np
	np = np + oil_rate*30.5/1000000
	
	#increase the month counter
	month = month + 1