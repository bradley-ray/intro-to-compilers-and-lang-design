#!/usr/bin/env python3

import graphviz as gv

# Problem 4a: for | [a-z]+ | [xb]?[0-9]+
p4a = gv.Digraph(comment='Problem 4a')
p4a.node('start')
p4a.node('1', label='')
p4a.node('2', label='')
p4a.node('3', label='')
p4a.node('4', label='')
p4a.node('5', label='')
p4a.node('6', label='')
p4a.node('7', label='')
p4a.node('8', label='')
p4a.node('9', label='')
p4a.node('10', label='')
p4a.node('11', label='')
p4a.node('12', label='')
p4a.node('13', label='')
p4a.node('14', label='')
p4a.node('15', label='')

p4a.node('end', label='end')

p4a.edge('start', '1')

# for
p4a.edge('1', '2', label='eps')
p4a.edge('2', '3', label='f')
p4a.edge('3', '4', label='o')
p4a.edge('4', '5', label='r')
p4a.edge('5', '6', label='eps')

# [a-z]+
# to keep graph clean im condensing this to just one transition
# instead of 26 transistions in parallel
p4a.edge('1', '7', label='eps')
p4a.edge('7', '8', label='a-z')
p4a.edge('8', '6', label='eps')
p4a.edge('6', '7', label='eps')

#[xb]?[0-9]+
# same as above, [0-9] condsed as one transition
# instead of 10 parallel transistions
p4a.edge('1', '9', label='eps')
p4a.edge('9', '10', label='x')
p4a.edge('10', '11', label='b')
p4a.edge('11', '12', label='eps')
p4a.edge('9', '12', label='eps')
p4a.edge('12', '13', label='0-9')
p4a.edge('13', '6', label='eps')
p4a.edge('6', '12', label='eps')

p4a.edge('6', 'end')

p4a.render('p4a.gv')


# Problem 4b: a ( bc*d | ed) d*
p4b = gv.Digraph(comment='Problem 4b')
p4b.node('start')
p4b.node('1', label='')
p4b.node('2', label='')
p4b.node('3', label='')
p4b.node('4', label='')
p4b.node('5', label='')
p4b.node('6', label='')
p4b.node('7', label='')
p4b.node('8', label='')
p4b.node('9', label='')
p4b.node('10', label='')
p4b.node('11', label='')
p4b.node('12', label='')
p4b.node('13', label='')
p4b.node('14', label='')
p4b.node('15', label='')

p4b.edge('start', '1')

# a
p4b.edge('1', '2', label='eps')
p4b.edge('2', '3', label='a')
p4b.edge('3', '4', label='eps')

# bc*d
p4b.edge('4', '5', label='eps')
p4b.edge('5', '6', label='b')
p4b.edge('6', '7', label='c')
p4b.edge('7', '6', label='eps')
p4b.edge('6', '7', label='eps')
p4b.edge('7', '8', label='d')
p4b.edge('8', '9', label='eps')

# ed
p4b.edge('4', '10', label='eps')
p4b.edge('10', '11', label='e')
p4b.edge('11', '12', label='d')
p4b.edge('12', '9', label='eps')

# d*
p4b.edge('9', '13', label='eps')
p4b.edge('13', '14', label='d')
p4b.edge('14', '15', label='eps')
p4b.edge('14', '13', label='eps')
p4b.edge('13', '14', label='eps')

p4b.edge('15', 'end')

p4b.render('p4b.gv')


# Problem 4c: ( a*b | b*a | ba )*
p4c = gv.Digraph(comment='Problem 4c')
p4c.node('start')
p4c.node('1', label='')
p4c.node('2', label='')
p4c.node('3', label='')
p4c.node('4', label='')
p4c.node('5', label='')
p4c.node('6', label='')
p4c.node('7', label='')
p4c.node('8', label='')
p4c.node('9', label='')
p4c.node('10', label='')
p4c.node('11', label='')
p4c.node('end')

p4c.edge('start','1')

# a*b
p4c.edge('1','2', label='eps')
p4c.edge('2','3', label='a')
p4c.edge('2','3', label='eps')
p4c.edge('3','2', label='eps')
p4c.edge('3','4', label='b')
p4c.edge('4','8', label='eps')

# b*a
p4c.edge('1','5', label='eps')
p4c.edge('5','6', label='b')
p4c.edge('5','6', label='eps')
p4c.edge('6','5', label='eps')
p4c.edge('6','7', label='a')
p4c.edge('7','8', label='eps')

# ba
p4c.edge('1','9', label='eps')
p4c.edge('9','10', label='b')
p4c.edge('10','11', label='a')
p4c.edge('11','8', label='eps')

p4c.edge('1','8', label='eps')
p4c.edge('8','1', label='eps')
p4c.edge('8','end')


p4c.render('p4c.gv')

