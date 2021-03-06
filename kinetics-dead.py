from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

# the maximum time of virus in days
maxtime = 365
# people in Idaho
N = 1754000
def kinetics(k1, k2, k3, a_0, b_0, c_0, d_0):
    def abc(t, y):
        ''' System of differential equations: y(t) = [A(t),B(t),C(t)]
            returns:
                A list containing [dA/dt, dB/dt, dC/dt]
        '''
# where A is uninfected, B is infected, C is recovered, and D is dead
        A,B,C,D = y
        return [-k1*A*B/(A+B+C+D), k1*A*B/(A+B+C+D)-k2*B-k3*B, k2*B, k3*B]
    return solve_ivp(abc, [0, maxtime], [a_0,b_0,c_0,d_0], t_eval=np.arange(0, maxtime, 1),method='Radau')

# Original k1 is 0.1
solution = kinetics(0.139,0.02,0.03074, N-1,1,0,0) # The numbers are 60 dead over 1952 infected currently as of 04-29-20 if there is a findings team member who has the actual death rate, go ahead and change it. Infection rate from www.worldometers.info/coronavirus.


plt.plot(solution.t,solution.y[0],label='Uninfected')
plt.plot(solution.t,solution.y[1],label='Infected',linestyle='dashed')
plt.plot(solution.t,solution.y[2],label='Recovered',linestyle='dotted')
plt.plot(solution.t,solution.y[3],label='Dead',linestyle= '-.',color='Black')
plt.xlabel('Time [days]')
plt.ylabel('Population infected')
plt.grid() 
plt.legend()
plt.title('State of Covid-19 in the Public')
plt.show()

