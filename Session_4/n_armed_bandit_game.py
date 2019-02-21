# coding: utf-8

from ipywidgets import widgets # Widget definitions
from IPython.display import display # Used to display widgets in the notebook


counter = []


import numpy



class Problem:

    def __init__(self,n=4):

        self.n = n
        self.gamma = 0.5

        import numpy
        import numpy.random

        means = numpy.linspace(0,1,n)
        self.means = means[ numpy.random.permutation(n) ]
        self.deviations = numpy.ones(n, dtype=float)


    def play(self,i):

        from numpy import exp
        gamma = self.gamma
        rnd = numpy.random.randn()
        rew = rnd*self.deviations[i] + self.means[i]
        rew = exp(rew)
        util = (rew)**(1-gamma)/(1-gamma)
        return util


class HumanPlayer():

    def __init__(self, n):
        self.n = n
        self.restart()
        self.beta = 0.9
        self.gamma = 0.5

    def restart(self):

        self.problem = Problem(self.n)
        self.n = self.problem.n

        self.results = [[] for i in range(self.n)]
        self.create_gui()
        self.total = 0
        self.step = 0
        self.average = [0 for i in range(self.n)]
        self.evaluations = [0 for i in range(self.n)]

    def play(self,x):

        i = self.buttons_numbers[x]
        rew = self.problem.play(i)
        self.total += self.beta**self.step*rew
        hh = self.total_widget
        hh.value="Total Discounted value {}".format(self.total)
        self.evaluations[i] += 1
        k = self.evaluations[i]
        self.average[i] = (self.average[i]*(k-1) + rew)/k
        b = self.average[i]
        buton = self.lines[i].children[1]
        buton.value = "&nbsp;&nbsp;&nbsp;&nbsp;{}".format(b)
        self.step += 1

    def create_gui(self):

        from ipywidgets import widgets
        self.buttons = []
        self.lines = []
        self.last_results = []
        self.buttons_numbers = {}


        for i in range(self.n):
            b = widgets.Button(description='Bandit {}'.format(i))
            self.buttons_numbers[b] = i
            b.on_click(lambda x: self.play(x))
            self.last_results.append(numpy.nan)
            self.buttons.append(b)

            t1 =  widgets.HTML(value="&nbsp;&nbsp;&nbsp;&nbsp;{}".format(numpy.nan))
            line = widgets.VBox(children=[b,t1])
            self.lines.append(line)


        total_widget = widgets.HTML(value="Total Discounted value {}".format(numpy.nan))
        self.total_widget = total_widget
        container = widgets.VBox( [widgets.HBox(self.lines), total_widget])
#         container.children = self.lines 

#         container.children += ((widgets.Button(description='Share on Facebook')),)

        self.gui = container



    def display(self):
        display(self.gui)
