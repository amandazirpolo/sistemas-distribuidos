import rpyc
import sys
import os
import time

#start = time.time()
if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]
conn = rpyc.connect(server,18861)

print(conn.get_question)
#print(conn.root.get_question())
#end = time.time()
#print(end-start)