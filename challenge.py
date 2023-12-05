weirdstar = "~~~~~~"


def star():
   global weirdstar
   for val in range(6):
      weirdstar = (weirdstar[0:-2])
      print(weirdstar)
      weirdstar += "~"




star()