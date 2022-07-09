# Sales Tax Challenge

wall_space = int(input('Enter square feet of wall spaces to be painted: '))
paint_price = int(input('Enter price of paint per gallon: '))
print()

gallons_of_paint = wall_space / 115
hours_of_labour = gallons_of_paint * 8
cost_of_labour = hours_of_labour * 20

print('Number of gallons of paint required: ',round(gallons_of_paint,2))
print('Hours of labour required: ',round(hours_of_labour,2))

paint_cost = paint_price * gallons_of_paint 
print('Cost of the paint: $',round(paint_cost,2))
print('Labour charges: $',round(cost_of_labour,2))

total_cost = paint_cost + cost_of_labour 
print('Total cost of the paint job: $',round(total_cost,2))