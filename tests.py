import main
import pytest
from astropy import units as u
from astropy import constants as const

class TestConversions:
  def test_one(self):
    assert 1==1
  def test_ParallaxToDist(self):
    assert main.ParallaxToDistance(10) == (0.1 * u.pc)
  