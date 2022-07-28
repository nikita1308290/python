from multiprocessing.pool import ApplyResult


product = input("what did you buy?")
price = float(input("howw muuch did you pay?"))
qty = int(input("how many did you buy?"))
print('you purchased', qty,product,'for', price)