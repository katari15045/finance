class Main:

	@staticmethod
	def main():
		fv = Main.compute_fv_annuity(a=150000, r=0.08, n=23)	
		print("FV: " + str(int(fv)) + " INR")

	# a( ((1+r)^n)-1 )/r = fv; => a = (fv*r) / ( ((1+r)^n)-1 )
	@staticmethod	
	def compute_annuity(r, n, fv):
		r = float(r)
		n = float(n)
		fv = float(fv)
		numerator = fv*r
		denominator = ((1+r)**n)-1
		return numerator/denominator

	# fv = a( ((1+r)^n)-1 )/r
	@staticmethod
	def compute_fv_annuity(a, r, n):
		a = float(a)
		r = float(r)
		n = float(n)
		numerator = (1+r)**n
		numerator = (numerator-1)*a
		return numerator/r

Main.main()
