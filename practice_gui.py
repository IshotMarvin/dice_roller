import random
import PySimpleGUI as sg
import re

def diceroller(numset):
    '''
    Rolls numset[0] number of numset[1] dice, i.e. (num1)d(num2)
    Input:
    numset (array of 2 integers): first element is number of dice
                                  second element is type of die
    Output:
    list: first element is roll total
          second element is a list of the individual rolls
    '''
    randtotal = 0
    dice_set = []
    for i in range(numset[0]):
        die_val = random.randint(1,numset[1])
        randtotal += die_val
        dice_set.append(die_val)
    return [randtotal,dice_set]

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


# print(diceroller([4,6]))

sg.theme('DarkAmber')

layout = [[sg.Text('Type the dice you want to roll, using standard (number)d(number) notation:')],
          [sg.Input(key='-IN-')],
          [sg.Text('Your total roll:'), sg.Text(size=(12,1), key='-OUTPUT1-')],
          [sg.Text('Your individual dice roll(s):'),sg.Text(size=(40,1), key='-OUTPUT2-')],
          [sg.Button('Calculate',bind_return_key=True), sg.Button('Exit')]]

window = sg.Window('Dice Roller', layout, finalize=True)
window.bind("<Escape>",'Exit')

while True:  # Event Loop
    event, values = window.read()
    text = values['-IN-']
    nums = [int(s) for s in re.findall(r"\d+", text)]
    if len(nums) == 2:
        if event == 'Calculate':
            rolltot,eachroll = diceroller(nums)
            print([rolltot,eachroll])
            window['-OUTPUT1-'].update(rolltot)
            window['-OUTPUT2-'].update(eachroll)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif len(nums) != 2:
        sg.popup('Input should be of the form "xdy", where x is the number of y type dice to roll',
                 title='Invalid input',any_key_closes=True)
        window['-IN-'].update('')
    
window.close()
