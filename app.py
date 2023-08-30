import random
import argparse
from fitness import fitness, BITCOUNT
from sklearn.skmetric import compute
import sys
from flask import Flask, render_template, request, make_response
import pandas as pd
import numpy as np
import json  # json request
from werkzeug.utils import secure_filename
import os
import csv  # reading csv
import geocoder
from random import randint
import os
from random import randint
from datetime import date
from sklearn import linear_model
global res

classrooms = ["Room1", "Room2", "Room3"]
sections = ["A", "B", "C", "D"]
'''
facultylist=["Harshitha K (HK)","Hamsaveni M (HM)","Pruthvi PR(PPR) ","Pavan Kumar S P(PSP)","Chethana HT (CHT)","Dr. Jahnavi V (JV)","Usha C S(UCS)","Nithin Kumar (NK)","Nagashree Nagaraj(NN) ","Meghana M(MM)","Vinay M G(VMG)","Anusha KS (AKS)"]

sem8=["15CS81","15CS82","15CS834/15CS832","15CSP85","15CSS86","15CS84"]
sem8subjects=["INTERNET OF THINGS TECHNOLOGY","BIG DATA ANALYTICS","SYSTEM MODELLING and SIMULATION/USER INTERFACE DESIGN","PROJECT WORK PHASE II","SEMINAR","INTERNSHIP/PROFESSIONAL PRACTICE"]

sem3=["15CS32","15CS33","15CS34","15CS35","15CS36","15CSL37","15CSL38","15MAT31"]
sem3subjects=["ANALOG AND DIGITAL ELECTRONICS","DATA STRUCTURES AND APPLICATION","COMPUTER ORGANIZATION","UNIX AND SHELL PROGRAMMING","DISCRETE MATHEMATICAL STRUCTURES","ANALOG AND DIGITAL ELECTRONICS LABORATORY","DATA STRUCTURES LABORATORY","ENGINEERING MATHEMATICS-III"]

sem4=["15CS42","15CS43","15CS44","15CS45","15CS46","15MAT41","15CSL47","15CSL48"]
sem4subjects=["Software Engineering","Design and Analysis of Algorithms","Microprocessors and microcontrollers","Object Oriented Programming with JAVA ","Data communications","ENGINEERING MATHEMATICS-IV"," Design and Analysis of Algorithm","Design and Analysis of Algorithm Laboratory","Microprocessors and microcontrollers Laboratory"]

sem5=["15CS51","15CS52","15CS53","15CS54","15CS554","15CS562","15CSL57","15CSL58"]
sem5subjects=["Management and Entrepreneurship for IT Industry","Computer Networks","Database Management System","Automata theory and Computability","ADVANCED ALGORITHMS","ARTIFICIAL INTELLIGENCE","Computer Network Laboratory","DBMS Laboratory with mini project"]

sem6=["15CS61","15CS62","15CS63","15CS64","15CS653","15CS661","15CSL67","15CSL68"]
sem6subjects=["Cryptography","Network Security and Cyber Law "," Computer Graphics and Visualization "
" System Software and Compiler Design  ","Operating Systems ","OPERATIONS RESEARCH","MOBILE APPLICATION DEVELOPMENT "," System Software and Operating System laboratory"," Computer Graphics Laboratory with mini project"]

sem7=["15CS71","15CS72","15CS73","15CS744","15CS754","15CSL76","15CSL77","15CSP78"]
sem7subjects=["Web Technology and its applications ","Advanced Computer Architectures","Machine Learning ","UNIX SYSTEM PROGRAMMING","UNIX SYSTEM PROGRAMMING","Machine Learning Laboratory","Web Technology Laboratory with mini project ","Project Phase 1 + Seminar "]

'''
semesters = ["1", "2", "3", "4", "5", "6", "7", "8"]


TRACE_ENABLED = True
"""Whether the debug trace is on."""

URANDOM_STRING_LENGTH = 32
"""Size of the entropy string provided from urandom."""


def trace(*text):
    """Outputs a single chunk of text to stderr."""
    if not TRACE_ENABLED:
        return
    data = " ".join([str(chunk) for chunk in text])
    sys.stderr.write(data + "\n")
    sys.stderr.flush()


def decode(member):
    """Displays int as a binary string."""
    return bin(member)[2:].zfill(BITCOUNT)


def mutate(member, num_bits=None):
    if num_bits is None:
        num_bits = random.randint(1, BITCOUNT)
    elif num_bits < 0:
        raise Exception("Number of bits must be non-negative.")
    for pos in random.sample(range(0, BITCOUNT), num_bits):
        member ^= 1 << pos
    return member


def predictor():
    params = Params(**args_dict)
    ga = GeneticAlgo(params)
    ga.initialize()

    for i in ga.evolve():
        print("Generation", i + 1)
        ga.display()
        print("")


def argmax(values):
    """Returns the index of the largest value in a list."""
    return max(enumerate(values), key=lambda x: x[1])[0]


class Defaults:
    """Default values for params."""
    CROSSING_PROBABILITY = 0.9
    MUTATION_PROBABILITY = 0.01
    ITERATION_COUNT = 30
    INITIAL_POPULATION = 20
    RANDOM_SEED = None
    SELECTION_STRATEGY = "fitness-proportional"
    ELITISM = False


class Params(object):
    """Parameters of a genetic algorithm."""

    def __init__(self, crossing, mutation, iterations, population, random_seed,
                 selection_strategy, elitism):
        self.crossing = crossing
        self.mutation = mutation
        self.iterations = iterations
        self.population = population
        self.random_seed = random_seed
        self.selection_strategy = selection_strategy
        self.elitism = elitism


class SelectionStrategy(object):
    """Abstract class for a selection strategy."""

    def select_and_crossover(self, population, crossing):
        raise Exception("Method not implemented.")

even=['2','4','6','8']
odd=['1','3','5','7']
class FitnessProportionalSelection(SelectionStrategy):

    def _select(self, population):
            
        selection = []
        for i in range(len(odd)):
            delim=odd[i]
            selection.append(odd[i])
        for i in range(len(even)):
            delim=even[i]
            selection.append(even[i])
        fits = [fitness(member) for member in population]
        sum_fits = sum(fits)
        normalized_fits = [(member, fitness(member) / sum_fits)
                           for member in population]
        normalized_fits = list(sorted(normalized_fits, key=lambda x: x[1],
                                      reverse=True))
        accumulated = 0
        accumulated_fits = []
        for x in normalized_fits:
            accumulated += x[1]
            accumulated_fits.append((x[0], accumulated))

        used = set()
        # TODO(kburnik): This can be optimized.
        while len(selection) < len(population):
            value = random.random()
            for i, x in enumerate(accumulated_fits):
                value -= x[1]
                if value <= 0:
                    if i in used:
                        continue
                    used.add(i)
                    selection.append(x[0])
                    break
        return list(sorted(selection, key=lambda m: fitness(m), reverse=True))

    def _crossover(self, a, b):
        """Crosses over two members by cutting at radnom point pos (right to left).
        """
        pos = random.randint(1, BITCOUNT - 1)
        mask = (2 ** pos) - 1
        invmask = (2 ** BITCOUNT) - mask - 1
        na = (a & invmask) | (b & mask)
        nb = (b & invmask) | (a & mask)
        return (na, nb)

    def select_and_crossover(self, population, crossing):
        # 1) Select.
        selection = self._select(population)
        
        for i in range(len(odd)):
            delim=odd[i]
            selection.append(odd[i])
        for i in range(len(even)):
            delim=even[i]
            selection.append(even[i])
        # 2) Crossover.
        
        for i in range(len(odd)):
            delim=odd[i]
            selection.append(odd[i])
        for i in range(len(even)):
            delim=even[i]
            selection.append(even[i])
        for i in range(0, len(selection) - 1, 2):
            if random.random() < crossing:
                selection[i], selection[i + 1] = \
                    self._crossover(selection[i], selection[i + 1])
        return selection


class UniformSelection(SelectionStrategy):
    """A Uniform selection strategy, all members of the population are equally
       likely to be chosen for crossover. The crossover is done by keeping same
       bits of parents and randomly choosing a the bit that differs."""

    def _crossover(self, a, b):
        # Create mask of different bits from both parents.
        diffmask = a ^ b
        # Copy the same bits to child.
        child = a & b
        parents = [a, b]
        val = 1
        while diffmask > 0:
            # Check if the bit is set.
            if diffmask % 2 == 1:
                # Choose parent randomly. 50/50 chance.
                parent = parents[random.randint(0, 1)]
                # Copy the set bit from the chosen parent to the child.
                child |= (parent & val)
            diffmask /= 2
            val *= 2
        return child

    def select_and_crossover(self, population, crossing):
        selection = set()
        used_pairs = set()
        selection=[]
        
        for i in range(len(odd)):
            delim=odd[i]
            selection.append(odd[i])
        for i in range(len(even)):
            delim=even[i]
            selection.append(even[i])
        while len(selection) < len(population):
            pair = tuple(random.sample(population, 2))
            if pair in used_pairs:
                continue
            used_pairs.add(pair)
            if random.random() < crossing:
                child = self._crossover(*pair)
                selection.add(child)
            else:
                selection.add(pair[0])
                selection.add(pair[1])
        selection = list(selection)
        while len(selection) > len(population):
            selection.pop()
        return selection


class GeneticAlgo(object):
    """Represents a genetic algorithm"""

    def __init__(self, params):
        self.params = params
        self.population = []
        self.elite_member = None
        if params.selection_strategy == "fitness-proportional":
            self.selection_strategy = FitnessProportionalSelection()
        elif params.selection_strategy == "uniform":
            self.selection_strategy = UniformSelection()
        else:
            raise Exception("Invalid strategy %s" % params.selection_strategy)

    def initialize(self):
        """Initializes the population."""
        seed = self.params.random_seed
        if seed is None:
            seed = hash(os.urandom(URANDOM_STRING_LENGTH))
        random.seed(seed)
        trace("Using random seed", seed)
        for i in range(self.params.population):
            member = random.randint(0, (2 ** BITCOUNT) - 1)
            self.population.append(member)

    def evolve(self):
        """Generator where each iteration is an evolution step."""
        for generation in range(self.params.iterations):
            # 1) Select and 2) Crossover.
            selection = self.selection_strategy.select_and_crossover(
                self.population, self.params.crossing)

            # Find the elite member if elitism is enabled.
            elite_index = -1
            self.elite_member = None
            if self.params.elitism:
                elite_index = argmax([fitness(member) for member in selection])
                self.elite_member = selection[elite_index]

            # 3) Mutation.
            for i in range(len(selection)):
                # If elitism is enabled, don't mutate no matter the odds.
                if i != elite_index and random.random() < self.params.mutation:
                    selection[i] = mutate(selection[i])

            self.population = list(sorted(selection,
                                          key=lambda x: fitness(x),
                                          reverse=True))
            yield generation

    def display(self):
        """Prints the current population"""
        print("%10s %4s %7s %6s" % ("bin", "int", "fitness", "elite"))
        for member in self.population:
            if self.elite_member == member:
                elite = "ELITE"
            elif self.params.elitism:
                elite = "-"
            else:
                elite = "n/a"
        fits = [fitness(member) for member in self.population]
        minval = min(fits)
        maxval = max(fits)
        avgval = sum(fits) / len(fits)
        print("min = %.2f, max = %2.f, avg = %.2f" % (minval, maxval, avgval))


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/index')
def indexnew():
    return render_template('home.html')


@app.route('/home')
def homenew():
    return render_template('home.html', semesters=semesters, sections=sections)


@app.route('/generate', methods=['POST'])
def generate():
    sem = request.form["sem"]
    sec = request.form["sec"]
    print(sem)
    subfile = request.files['subfile']
    filename = secure_filename(subfile.filename)
    subfile.save(os.path.join("./static/Upload/", filename))
    sublist = []
    file1 = open('./static/Upload/'+filename, 'r')
    Lines = file1.readlines()
    for line in Lines:
        sublist.append(line)

    subnames = []
    for i in range(len(sublist)):
        val = sublist[i]
        a1 = val.split('-')
        print(a1)
        sublist[i]=a1[0]+"-"+a1[1]
        subnames.append(a1[1])

    print(subnames)
    facfile = request.files['facfile']
    filename = secure_filename(facfile.filename)
    facfile.save(os.path.join("./static/Upload/", filename))
    faclist = []
    file1 = open('./static/Upload/'+filename, 'r')
    Lines = file1.readlines()
    for line in Lines:
        faclist.append(line)

    '''
    sffile = request.files['sffile']
    filename = secure_filename(sffile.filename)
    sffile.save(os.path.join("./static/Upload/", filename))
    '''

    maplist = []
    file1 = open('./static/Upload/'+filename, 'r')
    Lines = file1.readlines()
    for line in Lines:
        maplist.append(line)

    asecfac = []
    bsecfac = []
    csecfac = []
    secfac1 = []
    secfac2 = []
    secfac3 = []
    secfac4 = []
    secfac5 = []
    secfac6 = []
    secfac7 = []
    secfac8 = []
    for i in range(len(maplist)):
        print(i)
        val = maplist[i]
        a1 = val.split('-')
        a2 = a1[1].split(',')
        demo = []
        demo.append(a1[0])
        demo.append(subnames[i])
        demo.append(a2[0])
        asecfac.append(demo)
        if a1[2]=="2":
            demo2 = []
            demo2.append(a1[0])
            demo2.append(subnames[i])
            demo2.append(a2[0])
            secfac2.append(demo2)
        if a1[2]=="3":
            demo2 = []
            demo2.append(a1[0])
            demo2.append(subnames[i])
            demo2.append(a2[0])
            secfac3.append(demo2)
        if a1[2]=="4":
            demo2 = []
            demo2.append(a1[0])
            demo2.append(subnames[i])
            demo2.append(a2[0])
            secfac4.append(demo2)
        if a1[2]=="5":
            demo2 = []
            demo2.append(a1[0])
            demo2.append(subnames[i])
            demo2.append(a2[0])
            secfac5.append(demo2)
        if a1[2]=="6":
            demo2 = []
            demo2.append(a1[0])
            demo2.append(subnames[i])
            demo2.append(a2[0])
            secfac6.append(demo2)
        if a1[2]=="7":
            demo2 = []
            demo2.append(a1[0])
            demo2.append(subnames[i])
            demo2.append(a2[0])
            secfac7.append(demo2)
        if a1[2]=="8":
            demo2 = []
            demo2.append(a1[0])
            demo2.append(subnames[i])
            demo2.append(a2[0])
            secfac8.append(demo2)

    print(asecfac)
    print(bsecfac)
    print(csecfac)
    print('-------------------------------------------------')
    print(sublist)
    print(sem)
    subjectslist = compute.select_and_crossover(sublist, sem)
    import pandas as pd
    print('Subjects List')
    print(subjectslist)
    print(subjectslist[1])

    secfac = ''
    room = ''
    if sec == "A":
        secfac = asecfac
        room = "Room 1"
    elif sec == "B":
        secfac = asecfac
        room = "Room 2"
    elif sec == "C":
        secfac = asecfac
        room = "Room 3"
    else:
        secfac = asecfac
        room = "Room1"

    return render_template('home.html', subjectslist=subjectslist, sem=sem, secfac=secfac, sec=sec, room=room)


@app.route('/predict', methods=['GET', 'POST'])
def procs():
    print("hit")
    key = request.args['data']
    print(key)
    msg = key
    print(msg, flush=True)
    return render_template('predict.html', msg=msg)
