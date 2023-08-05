# encoding: utf-8

import math
import numpy as np


class Sequence(object):

    
    def __init__(self):

        # self._seq  = np.array(values)
        self._seq  = []



    def index(self, value):

        # return np.where(self._seq == value)[0][0]
        return self._seq.index(value)



    def tail_index(self):

        return math.floor((len(self._seq)+1)/2) - 1 



    def tail(self):

        return self._seq[self.tail_index()]



    def last(self):

        return self._seq[-1]



    def last_drop(self):

        self._seq = self._seq[:-1]



    def __getitem__(self, key):

        try:
            return self._seq[key]
        except:
            return None



    def __setitem__(self, key, value):
        
        if list == type(key):
            for k, v in zip(key, value):
                self._seq[k] = v

        else:
            self._seq[key] = value



    def append(self, value):

        # self._seq = np.concatenate((self._seq, [value]))
        self._seq.append(value)



    def __repr__(self):

        return '\n'.join([v.__repr__() for v in self._seq])


    def __len__(self):

        return len(self._seq)
