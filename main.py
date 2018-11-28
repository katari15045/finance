class Main:

	@staticmethod
	def main():
		annuity = Main.compute_annuity(r=0.035, n=23, fv=10000000)	
		print("Annuity: " + str(int(annuity)) + " INR")

	# a( ((1+r)^n)-1 )/r = fv; => a = (fv*r) / ( ((1+r)^n)-1 )
	@staticmethod	
	def compute_annuity(r, n, fv):
		r = float(r)
		n = float(n)
		fv = float(fv)
		numerator = fv*r
		denominator = ((1+r)**n)-1
		return numerator/denominator

Main.main()
