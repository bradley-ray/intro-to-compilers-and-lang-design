#!/usr/bin/env python3

import graphviz as gv

# Problem 5a: for | [a-z]+ | [xb]?[0-9]+
p5a = gv.Digraph(comment='Problem 5a')
p5a.node('start')
p5a.node('1', label='1,2,7,9,12')
p5a.node('2', label='end{3}')
p5a.node('3', label='end{4}')
p5a.node('4', label='end{6,8}')
p5a.node('5', label='end{5,6,7,12}')
p5a.node('6', label='end{6,13}')
p5a.node('7', label='end{10}')
p5a.node('8', label='end{11},12}')


p5a.edge('start', '1')
p5a.edge('1', '2', label='f')
p5a.edge('2', '3', label='o')
p5a.edge('3', '5', label='r')
# i'm not writing this out for each letter
# but basically, any letter but 'f' and 'x'
p5a.edge('1', '4', label='a-e | g-w | y-z')
p5a.edge('4', '5', label='a-z')
p5a.edge('5', '4', label='a-z')
p5a.edge('5', '6', label='0-9')
p5a.edge('6', '5', label='0-9')
p5a.edge('1', '6', label='0-9')
p5a.edge('1', '7', label='x')
p5a.edge('7', '8', label='b')
p5a.edge('8', '6', label='0-9')

p5a.render('p5a.gv')


# Problem 5b: a ( bc*d | ed) d*
p5b = gv.Digraph(comment='Problem 5b')
p5b.node('start')
p5b.node('1', label='1,2')
p5b.node('2', label='3,4,5,10')
p5b.node('3', label='6,7')
p5b.node('4', label='11')
p5b.node('5', label='end{8,9,13,14}')
p5b.node('6', label='end{12,9,13,14}')

p5b.edge('start', '1')
p5b.edge('1', '2', label='a')
p5b.edge('2', '3', label='b')
p5b.edge('3', '3', label='c')
p5b.edge('2', '4', label='e')
p5b.edge('3', '5', label='d')
p5b.edge('4', '6', label='d')
p5b.edge('5', '5', label='d')
p5b.edge('6', '6', label='d')

p5b.render('p5b.gv')

# Problem 5c: ( a*b | b*a | ba )*
p5c = gv.Digraph(comment='Problem 5c')
p5c.node('start')
p5c.node('1', label='end{1,2,3,5,6,8,9}')
p5c.node('2', label='end{3,7,8}')
p5c.node('3', label='end{4,6,10}')
p5c.node('4', label='end{4,8}')
p5c.node('5', label='end{7,8,11}')

p5c.edge('start','1')
p5c.edge('1','2', label='a')
p5c.edge('1','3', label='b')
p5c.edge('2','4', label='b')
p5c.edge('3','5', label='a')

p5c.render('p5c.gv')

