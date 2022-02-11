from hashlib import sha256
import csv
i = 0

with open('C:/Users/hashlist.csv' , 'w') as out: #edit address
   
    for r in range(0,9999+1):
        r = '{0:04}'.format(r)
        this = sha256(str(r).encode())
        this = this.hexdigest()
        out.write(r + ',' + str(this) + '\n')
        i += 1
    #print('4 digit numbers Done')

    for t in range(0,99999+1):
        t = '{0:05}'.format(t)
        this = sha256(str(t).encode())
        this = this.hexdigest()
        out.write(t + ',' + str(this) + '\n')
        i += 1
    #print('5 digit numbers Done')

    for y in range(0,999999+1):
        y = '{0:06}'.format(y)
        this = sha256(str(y).encode())
        this = this.hexdigest()
        out.write(y + ',' + str(this) + '\n')
        i += 1
    #print('6 digit numbers Done')
    
print('All Done')
