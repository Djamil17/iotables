import sys
with open(sys.argv[1]) as f:
    data = f.read()

data=data.replace('and', '_')
data=data.replace(' ', '_')
data=data.replace(',_', '_')
data=data.replace('___', '_')
data=data.replace('"','')
data=data.replace(","," bigint," )
data=data.replace("Name bigint,"," Name text," )
data=data.replace("(","")
data=data.replace(")","")
data=data.replace("/", "")
data=data.replace("Total_product_supply_purchaser_prices","Total_product_supply_purchaser_prices bigint")
with open('{}.txt'.format(sys.argv[2]), "w+") as f2:
    f2.write(data)
