import matplotlib.pyplot as plt

years=[1990,1992,1994,1996,1998,2000,2003,2005,2007,2010]
runs = [500,700,1100,1500,1800,1200,1700,1300,900,1500]
Kohli = [0,0,500,800,1100,1300,1500,1800,1900,2100]
Sehwag = [0,300,800,1200,1500,1700,1600,1400,1000,0]

with plt.xkcd():
    plt.plot(years,Kohli,color="orange",linestyle="--",label="Virat kohli")
    plt.plot(years,Sehwag,color="green",linestyle="-.",linewidth=2,label="Virendeer Sehwag")
    plt.plot(years,runs,color="blue",label="Tendulkar")
    plt.tight_layout()
    plt.grid(True)
    plt.legend()