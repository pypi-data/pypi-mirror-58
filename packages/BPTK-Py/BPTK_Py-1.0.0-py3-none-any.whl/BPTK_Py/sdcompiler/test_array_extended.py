
#      _                   _ _
#  _____| |__ ___ _ __  _ __(_| |___ _ _
# (_-/ _` / _/ _ | '  \| '_ | | / -_| '_|
# /__\__,_\__\___|_|_|_| .__|_|_\___|_|
#                      |_|
# Copyright (c) 2013-2016 transentis management & consulting. All rights reserved.
#
from BPTK_Py.sdcompiler.sdmodel import LERP, SDModel
import numpy as np
from scipy.interpolate import interp1d
from scipy.special import gammaln
import math, statistics
import random

def random_with_seed(seed):
    random.seed(seed)
    return random.random()

def beta_with_seed(a,b,seed):
    np.random.seed(seed)
    return np.random.beta(a,b)
    
def binomial_with_seed(n,p,seed):
    np.random.seed(seed)
    return np.random.binomial(n,p)
    
def gamma_with_seed(shape,scale,seed):
    np.random.seed(seed)
    return np.random.gamma(shape,scale)
    
def exprnd_with_seed(plambda,seed):
    np.random.seed(seed)
    return np.random.exponential(plambda)
    
def geometric_with_seed(p,seed):
    np.random.seed(seed)
    return np.random.geometric(p)
    


class simulation_model(SDModel):
    def __init__(self):
        # Simulation Buildins
        self.dt = 1
        self.starttime = 0
        self.stoptime = 120
        self.units = 'Days'
        self.method = 'Euler'
        self.equations = {

        # Stocks
        
    
        'closedTasks'          : lambda t: ( (0.0) if ( t  <=  self.starttime ) else (self.memoize('closedTasks',t-self.dt) + self.dt * ( self.memoize('completionRate',t-self.dt) )) ),
        'openTasks'          : lambda t: ( (self.memoize('initialOpenTasks', t)) if ( t  <=  self.starttime ) else (self.memoize('openTasks',t-self.dt) + self.dt * ( -1 * ( self.memoize('completionRate',t-self.dt) ) )) ),
        'staff'          : lambda t: ( (self.memoize('initialStaff', t)) if ( t  <=  self.starttime ) else (self.memoize('staff',t-self.dt) + self.dt * 0) ),
        
    
        # Flows
        'completionRate'             : lambda t: max( [0 , min([self.memoize('openTasks', t) , self.memoize('staff', t) * self.memoize('productivity', t) / self.memoize('effortPerTask', t)])]),
        
    
        # converters
        'currentDate'      : lambda t:  t ,
        'deadline'      : lambda t: 100.0,
        'effortPerTask'      : lambda t: 1.0,
        'initialOpenTasks'      : lambda t: 110.0,
        'initialStaff'      : lambda t: 1.0,
        'remainingTime'      : lambda t: max( [self.memoize('deadline', t) - self.memoize('currentDate', t) , 0.0]),
        'schedulePressure'      : lambda t: min([( self.memoize('openTasks', t) * self.memoize('effortPerTask', t) / self.memoize('staff', t) ) / max( [self.memoize('remainingTime', t) , 1.0]) , 2.5]),
        
    
        # gf
        'productivity' : lambda t: LERP( self.memoize('schedulePressure', t), self.points['productivity']),
        
    
        #constants
        
    
    
        }
    
        self.points = {
            'productivity' :  [(0.0, 0.093), (0.25, 0.093), (0.5, 0.093), (0.75, 0.086), (1.0, 1.0), (1.25, 1.186), (1.5, 1.236), (1.75, 1.25), (2.0, 1.25), (2.25, 1.25), (2.5, 1.25)]  , 
        }
    
    
        self.dimensions = {
        	'dimName1': {
                'labels': [ '1'  ],
                'variables': [  ]
            },
         }
    
        self.stocks = ['closedTasks',   'openTasks',   'staff'  ]
        self.flows = ['completionRate'  ]
        self.converters = ['currentDate',   'deadline',   'effortPerTask',   'initialOpenTasks',   'initialStaff',   'remainingTime',   'schedulePressure'  ]
        self.gf = ['productivity'  ]
        self.constants= []
        self.events = [
            ]
    
        self.memo = {}
        for key in list(self.equations.keys()):
          self.memo[key] = {}  # DICT OF DICTS!
    
    def specs(self):
        return self.starttime, self.stoptime, self.dt, 'Days', 'Euler'
    