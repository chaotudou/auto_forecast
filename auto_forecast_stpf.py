#notify the user of the starting month
print("This forecast is set up to start from 1st January 2019.")

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
init_water_limit = input("Enter water limit: ")
init_liquid_limit = input("Enter liquid limit: ")
init_water_limit = float(init_water_limit)*prod_eff
init_liquid_limit = float(init_liquid_limit)*prod_eff

#reset month counter
month = 0

#monthly growth production wedge
jan_oil = 2540
feb_oil = 3197
mar_oil = 2871
apr_oil = 5650
may_oil = 9413
jun_oil = 7713
jul_oil = 7794
aug_oil = 10517
sep_oil = 9058
oct_oil = 16039
nov_oil = 16024
dec_oil = 15672

jan_wat = 0
feb_wat = 0
mar_wat = 0
apr_wat = 138
may_wat = 1804
jun_wat = 2758
jul_wat = 3154
aug_wat = 3479
sep_wat = 3753
oct_wat = 5485
nov_wat = 6741
dec_wat = 6841

jan_liq = 2540
feb_liq = 3197
mar_liq = 2871
apr_liq = 5788
may_liq = 11217
jun_liq = 10471
jul_liq = 10948
aug_liq = 13996
sep_liq = 12811
oct_liq = 21524
nov_liq = 22765
dec_liq = 22513


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

	if month == 0:
		water_limit = init_water_limit - jan_wat
		liquid_limit = init_liquid_limit - jan_liq
	elif month == 1:
		water_limit = init_water_limit - feb_wat
		liquid_limit = init_liquid_limit - feb_liq
	elif month == 2:
		water_limit = init_water_limit - mar_wat
		liquid_limit = init_liquid_limit - mar_liq
	elif month == 3:
		water_limit = init_water_limit - apr_wat
		liquid_limit = init_liquid_limit - apr_liq
	elif month == 4:
		water_limit = init_water_limit - may_wat
		liquid_limit = init_liquid_limit - may_liq
	elif month == 5:
		water_limit = init_water_limit - jun_wat
		liquid_limit = init_liquid_limit - jun_liq
	elif month == 6:
		water_limit = init_water_limit - jul_wat
		liquid_limit = init_liquid_limit - jul_liq
	elif month == 7:
		water_limit = init_water_limit - aug_wat
		liquid_limit = init_liquid_limit - aug_liq
	elif month == 8:
		water_limit = init_water_limit - sep_wat
		liquid_limit = init_liquid_limit - sep_liq
	elif month == 9:
		water_limit = init_water_limit - oct_wat
		liquid_limit = init_liquid_limit - oct_liq
	elif month == 10:
		water_limit = init_water_limit - nov_wat
		liquid_limit = init_liquid_limit - nov_liq
	elif month == 11:
		water_limit = init_water_limit - dec_wat
		liquid_limit = init_liquid_limit - dec_liq

#recalculate rates based on facilities limits

	#below liquid and water limits
	if water_rate_potential < water_limit and liquid_rate_potential < liquid_limit:
		oil_rate = oil_rate_potential
		water_rate = water_rate_potential
		liquid_rate = liquid_rate_potential
		print("***NO FACILITY CONSTRAINTS***")

	#below liquid limit but above water limit
	elif water_rate_potential > water_limit and liquid_rate_potential < liquid_limit:
		water_rate = int(water_limit)
		oil_rate = int(water_rate / wor)
		liquid_rate = int(water_rate + oil_rate)
		print("***WATER RATE CONSTRAINED***")

	#below water limit but above liquid limit
	elif water_rate_potential < water_limit and liquid_rate_potential > liquid_limit:
		liquid_rate = int(liquid_limit)
		water_rate = int(liquid_rate * fw)
		oil_rate = int(liquid_rate - water_rate)
		print("***LIQUID RATE CONSTRAINED***")

	#above liquid and water limits
	else:
		water_rate = int(water_limit)
		water_limited_oil_rate = int(water_rate / wor)
		liquid_rate_check = water_rate + water_limited_oil_rate
		print(liquid_rate_check)
		liquid_rate = int(liquid_limit)
		oil_rate = int(liquid_rate - (liquid_rate_check - liquid_limit) - water_rate)
		print("***WATER & LIQUID RATE CONSTRAINED***")

	#add growth production back in
	if month == 0:
		oil_total = oil_rate + jan_oil
		water_total = water_rate + jan_wat
		liquid_total = liquid_rate + jan_liq
	elif month == 1:
		oil_total = oil_rate + feb_oil
		water_total = water_rate + feb_wat
		liquid_total = liquid_rate + feb_liq
	elif month == 2:
		oil_total = oil_rate + mar_oil
		water_total = water_rate + mar_wat
		liquid_total = liquid_rate + mar_liq
	elif month == 3:
		oil_total = oil_rate + apr_oil
		water_total = water_rate + apr_wat
		liquid_total = liquid_rate + apr_liq
	elif month == 4:
		oil_total = oil_rate + may_oil
		water_total = water_rate + may_wat
		liquid_total = liquid_rate + may_liq
	elif month == 5:
		oil_total = oil_rate + jun_oil
		water_total = water_rate + jun_wat
		liquid_total = liquid_rate + jun_liq
	elif month == 6:
		oil_total = oil_rate + jul_oil
		water_total = water_rate + jul_wat
		liquid_total = liquid_rate + jul_liq
	elif month == 7:
		oil_total = oil_rate + aug_oil
		water_total = water_rate + aug_wat
		liquid_total = liquid_rate + aug_liq
	elif month == 8:
		oil_total = oil_rate + sep_oil
		water_total = water_rate + sep_wat
		liquid_total = liquid_rate + sep_liq
	elif month == 9:
		oil_total = oil_rate + oct_oil
		water_total = water_rate + oct_wat
		liquid_total = liquid_rate + oct_liq
	elif month == 10:
		oil_total = oil_rate + nov_oil
		water_total = water_rate + nov_wat
		liquid_total = liquid_rate + nov_liq
	elif month == 11:
		oil_total = oil_rate + dec_oil
		water_total = water_rate + dec_wat
		liquid_total = liquid_rate + dec_liq

	#print out new oil rate
	print(f"Oil Rate: {oil_total}")
	print(f"Water Rate: {water_total}")
	print(f"Liquid Rate: {liquid_total}")
	print("-----------------------------")
	
	#update np
	np = np + oil_rate*30.5/1000000
	
	#increase the month counter
	month = month + 1