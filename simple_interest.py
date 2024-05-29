
def simple_interest(p,t,r):
	si = (p * t * r)/100
	print('The Simple Interest is', si)
	return si

p=int(input('Enter the principal amount:'))
t=int(input('Enter the time period:'))
r=int(input('Enter the of interest:'))

simple_interest(p,t,r)