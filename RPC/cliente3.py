import rpyc
import sys
import time

# start = time.time()
if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]
conn = rpyc.connect(server, 18861)

n = int(input("Insira n: "))
start = time.time()
print(conn.root.soma_vetor(n))
end = time.time()
print(end-start)
# end = time.time()
# print(end-start)
