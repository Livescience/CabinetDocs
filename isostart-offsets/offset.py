import datetime, sys

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

# 01/27/20 16:24:28.958
def parse_date(stringdate):
    return datetime.datetime.strptime(stringdate, '%m/%d/%y %H:%M:%S.%f')

with open(sys.argv[1], 'r') as fp:
   line = fp.readline()
   cnt = 1
   lastdate = parse_date(line.split()[0] +" "+ line.split()[1])

   while line:
       currentdate = parse_date(line.split()[0] +" "+ line.split()[1])
       diff = currentdate - lastdate 
       #print("Offset: {} {}".format(diff, line.strip()))
       print("Offset: {} {}".format(diff, " ".join(line.split(None, 3)[1:])), end="")
       line = fp.readline()
       lastdate=currentdate
       cnt += 1

