from forex_python.converter import CurrencyRates
import numpy
from matplotlib import pyplot as plt
c = CurrencyRates()

import datetime
date_obj1 = datetime.datetime(2019, 5, 23, 18, 36, 28, 151012)
date_obj2 = datetime.datetime(2018, 5, 23, 18, 36, 28, 151012)
date_obj3 = datetime.datetime(2017, 5, 23, 18, 36, 28, 151012)
date_obj4 = datetime.datetime(2016, 5, 23, 18, 36, 28, 151012)
date_obj5 = datetime.datetime(2015, 5, 23, 18, 36, 28, 151012)
date_obj6 = datetime.datetime(2014, 5, 23, 18, 36, 28, 151012)
date_obj7 = datetime.datetime(2013, 5, 23, 18, 36, 28, 151012)
date_obj8 = datetime.datetime(2012, 5, 23, 18, 36, 28, 151012)
date_obj9 = datetime.datetime(2011, 5, 23, 18, 36, 28, 151012)
date_obj10 = datetime.datetime(2010, 5, 23, 18, 36, 28, 151012)
date_obj11 = datetime.datetime(2009, 5, 23, 18, 36, 28, 151012)
date_obj12 = datetime.datetime(2008, 5, 23, 18, 36, 28, 151012)
date_obj13 = datetime.datetime(2007, 5, 23, 18, 36, 28, 151012)
date_obj14 = datetime.datetime(2006, 5, 23, 18, 36, 28, 151012)
date_obj15 = datetime.datetime(2005, 5, 23, 18, 36, 28, 151012)
rate = [c.get_rate('USD','THB',date_obj15), c.get_rate('USD','THB',date_obj14),c.get_rate('USD','THB',date_obj13),c.get_rate('USD','THB',date_obj12),c.get_rate('USD','THB',date_obj11),c.get_rate('USD','THB',date_obj10),c.get_rate('USD','THB',date_obj9),c.get_rate('USD','THB',date_obj8),c.get_rate('USD','THB',date_obj7),c.get_rate('USD','THB',date_obj6),c.get_rate('USD','THB',date_obj5),c.get_rate('USD','THB',date_obj4),c.get_rate('USD','THB',date_obj3),c.get_rate('USD','THB',date_obj2),c.get_rate('USD','THB',date_obj1)]  # get_rate('USD', 'INR', date_obj)
year = [2005,
        2006,
        2007,
        2008,
        2009,
        2010,
        2011,
        2012,
        2013,
        2014,
        2015,
        2016,
        2017,
        2018,
        2019]
plt.style.use('ggplot')
plt.plot(year,rate,marker='x')

plt.xlabel('Year')
plt.ylabel('Currency Exchange Rate')
plt.show()