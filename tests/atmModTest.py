from cfatmos import Atmosphere

atm = Atmosphere()

air1 = {}
air2 = {"test": 5}

atm.get_atmosphere_data(altitude=10, mach=3)

atm.get_atmosphere_data(air1, altitude=10, mach=3)

atm.get_atmosphere_data(altitude=10, mach=3, container=air2)

assert air1["Pressure"] == air2["Pressure"], print("Test failed")
assert air1["Temperature"] == air2["Temperature"], print("Test failed")
