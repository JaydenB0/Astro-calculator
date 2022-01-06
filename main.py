from astropy import units as u
from astropy import constants as const
import math

from astropy.units import equivalencies
def ParallaxToDistance(angle):
  distance = (angle*u.arcsec).to(u.parsec, equivalencies=u.parallax())
  return distance
def StellarLuminosity(radius, kelvinTemp):
  luminosity = const.sigma_sb * 4 * radius^2 * math.pi * kelvinTemp
  return luminosity
def WavelengthToTemperature(wavelength):
  return const.b_wien/(wavelength * u.nm)
def LuminosityToDistance(apparent, absolute):
  distModulus = apparent - absolute
  calc = 10*math.sqrt(100**(distModulus/5))
  return calc 
#def GalaxyVelocity


#if __name__ == '__main__':
# 