import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def population(n_0,rate,nmax,time_max):
    p=[n_0]
    for i in range(time_max):
        add=p[i]*(rate-p[i]*(rate/nmax))
        p.append(add)
    return p



initial_population=0.5
tmax=60
nmax=10000000
rate=2.5


time=range(0,tmax+1)

fig,ax=plt.subplots()
plt.subplots_adjust(left=0.1,bottom=0.35)
p,=plt.plot(time,population(initial_population,rate,nmax,tmax),'C1')
plt.ylim(0,10000000)

plt.xlabel("Time in years")
plt.ylabel("Population")

print(population(initial_population,rate,nmax,tmax))

axSlider=plt.axes([0.1,0.02,0.8,0.05])
slider=Slider(axSlider,'rate',valmin=0,valmax=4,valinit=2.79,valstep=0.00002)

def new_plot(val):
    value=slider.val
    p.set_ydata(population(initial_population,value,nmax,tmax))
    plt.draw()

slider.on_changed(new_plot)



plt.show()