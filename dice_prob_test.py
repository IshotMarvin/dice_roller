import numpy as np
import scipy.special as sps
import matplotlib.pyplot as plt

def dice_roll_prob(r,n,s):
    '''
    Computes the probability of rolling r from n s-sided dice (nds colloquially)
    Equation taken from https://www.omnicalculator.com/statistics/dice
    Values tested against https://anydice.com/
    Input:
        r (int): sum of dice rolls you want to find the probability of
        n (int): number of dice you're rolling
        s (int): number of faces on each die (assuming all the same)
    Output:
        (float): probability of rolling r from nds
    '''
    prob = 0
    for k in range(int(np.floor((r-n)/s))+1):
        prob += (-1)**k*sps.binom(n,k)*sps.binom(r-s*k-1,n-1)
    return (1/s**n)*prob

def dice_roll_prob_all(n,s):
    '''
    Computes the probability of rolling all possible values from
    n s-sided dice (nds colloquially) 
    Input:
        n (int): number of dice you're rolling
        s (int): number of faces on each die (assuming all the same)
    Output:
        (list): list of probabilities of rolling nds, ordered by increasing
                rolls, i.e. 2d6 -> [prob(2),prob(3),...]
    '''
    prob_list = []
    for i in range(n,n*s+1):
        prob = 0
        prob += dice_roll_prob(i,n,s)
        prob_list.append(prob)
    return prob_list

def dice_roll_prob_plotter(r,n,s,prob_list):
    '''
    Plots the given dice probability distribution as a bar graph, highlighting
    a particular value
    Input:
        r (int): particular total dice value to be highlighted
        n (int): number of dice you're rolling
        s (int): number of faces on each die (assuming all the same)
        prob_list (list): probability distribution to be plotted
    '''
    x = [i for i in range(n,n*s+1)]
    blu = '#1f77b4'
    orng = '#ff7f0e'
    color = [blu for i in range(n,n*s+1)] #set all bar colors to blue
    color[r-n] = orng                     #except the highlighted one to orange

    prob_percent = [str(round(i*100,2))+'%' for i in prob_list]
    plt.bar(x,prob_list,color=color)
    for i in range(len(x)):
        plt.text(x[i],prob_list[i]+0.003,prob_percent[i],ha='center')
    plt.xticks(x)
    plt.yticks([])
    plt.show()
    return

l = 55
m = 20
n = 4

num = dice_roll_prob(l,m,n)

lst = dice_roll_prob_all(m,n)

dice_roll_prob_plotter(l,m,n,lst)

# x = [i for i in range(3,19)]
# label = [str(i) for i in range(3,19)]

# blu = '#1f77b4'
# orng = '#ff7f0e'
# color = [blu for i in range(3,19)]
# color[7-3] = orng

# prob = dice_roll_prob_all(3,6)
# prob_percent = [str(round(i*100,2))+'%' for i in prob]

# # x_ticks = [str(x[i]) + '\n' + prob_percent[i] for i in range(len(x))]
# # print(x_ticks)

# plt.bar(x,prob,color=color)
# for i in range(len(x)):
#     plt.text(x[i],prob[i]+0.003,prob_percent[i],ha='center')
# plt.xticks(x)
# plt.yticks([])
# plt.show()
