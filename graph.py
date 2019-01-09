from __future__ import print_function

import os
from subprocess import Popen
from sys import stderr
from uuid import uuid4


def generate_graphviz_graph(entity_relations, organizations, output_filename='out'):
    graph = list()
    graph.append('digraph prof {')
    graph.append('rankdir = LR;')
    graph.append('ratio = fill;')
    graph.append('node [style=filled];')

    # start -> main [color="0.002 0.999 0.999", label="33"];
    all_entities = set()
    for er in entity_relations:
        graph.append('"{}" -> "{}" [ label="{}" ];'.format(er[0], er[2], er[1]))
        all_entities.add(er[0])
        all_entities.add(er[2])

    for entity in all_entities:
        if entity in organizations:
            graph.append('"{}" [color="0.901 0.753 1.000"];'.format(entity))
        else:
            graph.append('"{}" [color="0.650 0.200 1.000"];'.format(entity))
    graph.append('}')

    uid = str(uuid4())
    output_dot_filename = '/tmp/out_{}.dot'.format(uid)
    with open(output_dot_filename, 'w') as output_file:
        output_file.writelines(graph)

    command = 'dot -Tpng {} -o {}'.format(output_dot_filename, output_filename)
    print('Executing command = {}'.format(command))
    dot_process = Popen(command, stdout=stderr, shell=True)
    dot_process.wait()
    assert not dot_process.returncode, 'ERROR: Call to dot exited with a non-zero code status.'
    os.remove(output_dot_filename)


if __name__ == '__main__':
    import pickle

    filtered_relations = pickle.load(open('filtered_relations.pkl', 'r'))
    organizations = pickle.load(open('organizations.pkl', 'r'))

    generate_graphviz_graph(filtered_relations, organizations)
'''
digraph prof {
	ratio = fill;
	node [style=filled];
	start -> main [color="0.002 0.999 0.999", label="33"];
	start -> on_exit [color="0.649 0.701 0.701"];
	main -> sort [color="0.348 0.839 0.839"];
	main -> merge [color="0.515 0.762 0.762"];
	main -> term [color="0.647 0.702 0.702"];
	main -> signal [color="0.650 0.700 0.700"];
	main -> sbrk [color="0.650 0.700 0.700"];
	main -> unlink [color="0.650 0.700 0.700"];
	main -> newfile [color="0.650 0.700 0.700"];
	main -> fclose [color="0.650 0.700 0.700"];
	main -> close [color="0.650 0.700 0.700"];
	main -> brk [color="0.650 0.700 0.700"];
	main -> setbuf [color="0.650 0.700 0.700"];
	main -> copyproto [color="0.650 0.700 0.700"];
	main -> initree [color="0.650 0.700 0.700"];
	main -> safeoutfil [color="0.650 0.700 0.700"];
	main -> getpid [color="0.650 0.700 0.700"];
	main -> sprintf [color="0.650 0.700 0.700"];
	main -> creat [color="0.650 0.700 0.700"];
	main -> rem [color="0.650 0.700 0.700"];
	main -> oldfile [color="0.650 0.700 0.700"];
	sort -> msort [color="0.619 0.714 0.714"];
	sort -> filbuf [color="0.650 0.700 0.700"];
	sort -> newfile [color="0.650 0.700 0.700"];
	sort -> fclose [color="0.650 0.700 0.700"];
	sort -> setbuf [color="0.650 0.700 0.700"];
	sort -> setfil [color="0.650 0.700 0.700"];
	msort -> qsort [color="0.650 0.700 0.700"];
	msort -> insert [color="0.650 0.700 0.700"];
	msort -> wline [color="0.650 0.700 0.700"];
	msort -> div [color="0.650 0.700 0.700"];
	msort -> cmpsave [color="0.650 0.700 0.700"];
	merge -> insert [color="0.650 0.700 0.700"];
	merge -> rline [color="0.650 0.700 0.700"];
	merge -> wline [color="0.650 0.700 0.700"];
	merge -> unlink [color="0.650 0.700 0.700"];
	merge -> fopen [color="0.650 0.700 0.700"];
	merge -> fclose [color="0.650 0.700 0.700"];
	merge -> setfil [color="0.650 0.700 0.700"];
	merge -> mul [color="0.650 0.700 0.700"];
	merge -> setbuf [color="0.650 0.700 0.700"];
	merge -> cmpsave [color="0.650 0.700 0.700"];
	insert -> cmpa [color="0.650 0.700 0.700"];
	wline -> flsbuf [color="0.649 0.700 0.700"];
	qsort -> cmpa [color="0.650 0.700 0.700"];
	rline -> filbuf [color="0.649 0.700 0.700"];
	xflsbuf -> write [color="0.650 0.700 0.700"];
	flsbuf -> xflsbuf [color="0.649 0.700 0.700"];
	filbuf -> read [color="0.650 0.700 0.700"];
	term -> unlink [color="0.650 0.700 0.700"];
	term -> signal [color="0.650 0.700 0.700"];
	term -> setfil [color="0.650 0.700 0.700"];
	term -> exit [color="0.650 0.700 0.700"];
	endopen -> open [color="0.650 0.700 0.700"];
	fopen -> endopen [color="0.639 0.705 0.705"];
	fopen -> findiop [color="0.650 0.700 0.700"];
	newfile -> fopen [color="0.634 0.707 0.707"];
	newfile -> setfil [color="0.650 0.700 0.700"];
	fclose -> fflush [color="0.642 0.704 0.704"];
	fclose -> close [color="0.650 0.700 0.700"];
	fflush -> xflsbuf [color="0.635 0.707 0.707"];
	malloc -> morecore [color="0.325 0.850 0.850"];
	malloc -> demote [color="0.650 0.700 0.700"];
	morecore -> sbrk [color="0.650 0.700 0.700"];
	morecore -> getfreehdr [color="0.650 0.700 0.700"];
	morecore -> free [color="0.650 0.700 0.700"];
	morecore -> getpagesize [color="0.650 0.700 0.700"];
	morecore -> putfreehdr [color="0.650 0.700 0.700"];
	morecore -> udiv [color="0.650 0.700 0.700"];
	morecore -> umul [color="0.650 0.700 0.700"];
	on_exit -> malloc [color="0.325 0.850 0.850"];
	signal -> sigvec [color="0.650 0.700 0.700"];
	moncontrol -> profil [color="0.650 0.700 0.700"];
	getfreehdr -> sbrk [color="0.650 0.700 0.700"];
	free -> insert [color="0.650 0.700 0.700"];
	insert -> getfreehdr [color="0.650 0.700 0.700"];
	setfil -> div [color="0.650 0.700 0.700"];
	setfil -> rem [color="0.650 0.700 0.700"];
	sigvec -> sigblock [color="0.650 0.700 0.700"];
	sigvec -> sigsetmask [color="0.650 0.700 0.700"];
	doprnt -> urem [color="0.650 0.700 0.700"];
	doprnt -> udiv [color="0.650 0.700 0.700"];
	doprnt -> strlen [color="0.650 0.700 0.700"];
	doprnt -> localeconv [color="0.650 0.700 0.700"];
	sprintf -> doprnt [color="0.650 0.700 0.700"];
cmpa [color="0.000 1.000 1.000"];
wline [color="0.901 0.753 1.000"];
insert [color="0.305 0.625 1.000"];
rline [color="0.355 0.563 1.000"];
sort [color="0.408 0.498 1.000"];
qsort [color="0.449 0.447 1.000"];
write [color="0.499 0.386 1.000"];
read [color="0.578 0.289 1.000"];
msort [color="0.590 0.273 1.000"];
merge [color="0.603 0.258 1.000"];
unlink [color="0.628 0.227 1.000"];
filbuf [color="0.641 0.212 1.000"];
open [color="0.641 0.212 1.000"];
sbrk [color="0.647 0.204 1.000"];
signal [color="0.647 0.204 1.000"];
moncontrol [color="0.647 0.204 1.000"];
xflsbuf [color="0.650 0.200 1.000"];
flsbuf [color="0.650 0.200 1.000"];
div [color="0.650 0.200 1.000"];
cmpsave [color="0.650 0.200 1.000"];
rem [color="0.650 0.200 1.000"];
setfil [color="0.650 0.200 1.000"];
close [color="0.650 0.200 1.000"];
fclose [color="0.650 0.200 1.000"];
fflush [color="0.650 0.200 1.000"];
setbuf [color="0.650 0.200 1.000"];
endopen [color="0.650 0.200 1.000"];
findiop [color="0.650 0.200 1.000"];
fopen [color="0.650 0.200 1.000"];
mul [color="0.650 0.200 1.000"];
newfile [color="0.650 0.200 1.000"];
sigblock [color="0.650 0.200 1.000"];
sigsetmask [color="0.650 0.200 1.000"];
sigvec [color="0.650 0.200 1.000"];
udiv [color="0.650 0.200 1.000"];
urem [color="0.650 0.200 1.000"];
brk [color="0.650 0.200 1.000"];
getfreehdr [color="0.650 0.200 1.000"];
strlen [color="0.650 0.200 1.000"];
umul [color="0.650 0.200 1.000"];
doprnt [color="0.650 0.200 1.000"];
copyproto [color="0.650 0.200 1.000"];
creat [color="0.650 0.200 1.000"];
demote [color="0.650 0.200 1.000"];
exit [color="0.650 0.200 1.000"];
free [color="0.650 0.200 1.000"];
getpagesize [color="0.650 0.200 1.000"];
getpid [color="0.650 0.200 1.000"];
initree [color="0.650 0.200 1.000"];
insert [color="0.650 0.200 1.000"];
localeconv [color="0.650 0.200 1.000"];
main [color="0.650 0.200 1.000"];
malloc [color="0.650 0.200 1.000"];
morecore [color="0.650 0.200 1.000"];
oldfile [color="0.650 0.200 1.000"];
on_exit [color="0.650 0.200 1.000"];
profil [color="0.650 0.200 1.000"];
putfreehdr [color="0.650 0.200 1.000"];
safeoutfil [color="0.650 0.200 1.000"];
sprintf [color="0.650 0.200 1.000"];
term [color="0.650 0.200 1.000"];
}'''