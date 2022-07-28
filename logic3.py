amt = int(input('How much kg. of apples you want?'))

if amt >= 5 :
    price = 80
else :
    price = 90
total = amt*price
print(f'you have to pay Rs.{total} for {amt} kg. of apples')