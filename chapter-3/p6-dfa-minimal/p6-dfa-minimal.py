#!/usr/bin/env python3

import graphviz as gv

# Problem 5a: for | [a-z]+ | [xb]?[0-9]+
p6a = gv.Digraph(comment='Problem 5a')
p6a.node('1', label='1')
p6a.node('2', label='end{2,3,4,5,6,7,8}')

p6a.edge('1','2', label='a-e|g-w|y-z')
p6a.edge('1','2', label='f,o,r')
p6a.edge('1','2', label='x,b')
p6a.edge('1','2', label='0-9')
p6a.render('p6a.gv')


# Problem 5b: a ( bc*d | ed) d*
p6b = gv.Digraph(comment='Problem 5b')
p6b.node('1', label='1')
p6b.node('2', label='2')
p6b.node('3', label='3')
p6b.node('4', label='4')
p6b.node('5', label='endl{5,6}')
p6b.edge('1','2', label='a')
p6b.edge('2','3', label='b')
p6b.edge('3','3', label='c')
p6b.edge('2','4', label='e')
p6b.edge('3','5', label='d')
p6b.edge('4','5', label='d')
p6b.render('p6b.gv')


# Problem 5c: ( a*b | b*a | ba )*
p6c = gv.Digraph(comment='Problem 5c')
p6c.node('1', label='endl{1,2,3,4,5}')
p6c.render('p6c.gv')

