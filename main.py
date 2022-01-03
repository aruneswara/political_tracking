#make sure to pip install quiverquant
import numpy
import quiverquant
import config

#connect token
quiver = quiverquant.quiver(config.token)
dfCongress = quiver.congress_trading()
