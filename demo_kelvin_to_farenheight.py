def KelvinToFarenheight(Temperature):
	assert(Temperature >=0), "Colder than absolute zero!"
	return((Temperature-273)*1.8)+32
print(KelvinToFarenheight(273))
print(int(KelvinToFarenheight(505.78)))
print(KelvinToFarenheight(-5))
