#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    
    @always_comb
    def comb():
        soma.next = (a and not b) or (not a and b)
        carry.next = (a and b)

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    soma1 = Signal(bool(0))
    carry1 = Signal(bool(0))
    carry2 = Signal(bool(0))

    ha1 = halfAdder(a, b, soma1, carry1)
    ha2 = halfAdder(soma1, c, soma, carry2)

    @always_comb
    def comb():
        carry.next = carry1 or carry2  

    components = [ha1, ha2, comb]

    return components


@block
def adder2bits(x, y, soma, VaiUm):

    carry0 = Signal(bool(0))

    ha0 = halfAdder(x[0], y[0], soma[0], carry0)
    fa1 = fullAdder(x[1], y[1], carry0, soma[1], VaiUm)

    return instances()


@block
def adder(x, y, soma, carry):
    @always_comb
    def comb():
        pass

    return instances()
