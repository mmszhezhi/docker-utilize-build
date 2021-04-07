import numpy as np
import hashlib
import math

def main():
    i = 0
    while 1:

        x = abs(np.sin(i))*100
        sha  = hashlib.sha256()
        k = math.ceil(x)*100
        a = np.random.random(size=(k, k))
        result = np.linalg.inv(a)
        print(result)
        for  j in range(math.ceil(x)):
            sha.update(str(j).encode("utf8"))  # Hash the data.
            # print(sha.hexdigest())
        i+=1

if __name__ == '__main__':
    main()


