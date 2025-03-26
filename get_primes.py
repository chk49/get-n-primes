cached_primes=[]

def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#Get n primes and send each found prime number to a receiving function.
def get_primes_stream(n:int, receiver:callable):
    global cached_primes
    receiver(2)
    primes=[]
    if len(cached_primes)!=0:
        primes=cached_primes.copy()
        del primes[0]
        for i in range(len(primes)):
            x=primes[i]
            receiver(x)
            primes[i]=[(x-1)/2, x]

    i=len(primes)    
    length=i + 1
    while length<n: #Iterating through all (odd_number-1)/2
        i+=1
        skip = any(not (i - a) % b for a, b in primes)
        if skip:
            continue
        
        num=(2*i)+1
        primes.append([i, num]) #[found_at, value]
        length+=1
        receiver(num)
    for i in range(len(primes)):
        primes[i]=primes[i][1]
    primes.insert(0, 2)

    cached_primes=primes.copy()
    return primes

def experimental_get_primes_stream(n:int, receiver:callable):
    global cached_primes
    receiver(2)
    primes=[]
    if len(cached_primes)!=0:
        primes=cached_primes.copy()
        del primes[0]
        for i in range(len(primes)):
            x=primes[i]
            primes[i]=[(x-1)/2, x]
            if (i<n-1):
                receiver(x)

    i=len(primes)    
    length=i + 1

    skips=0
    while length<n:
        i+=1
        skip=False
        if skips:
            skips-=1
            continue
        else:
            for a,b in primes:
                mod = (i-a)%b
                
                if mod:
                    if mod+1==skips+b:
                        skips+=1
                else:
                    skip=True
                    break
                
            
        if skip:
            continue
        
        num=(2*i)+1
        primes.append([i, num])
        length+=1
        receiver(num)
    for i in range(len(primes)):
        primes[i]=primes[i][1]
    primes.insert(0, 2)

    cached_primes=primes.copy()
    return primes

def get_primes(n):
    return get_primes_stream(n, lambda x: None)

def print_ordered_number(x):
        self=print_ordered_number
        if not hasattr(self, "counter"):
            self.counter=0
        self.counter+=1
        print(self.counter, ". ", x)

if __name__=="__main__":
    while True:
        print_ordered_number.counter=0
        inputted=input("How many primes to generate: ")
        try:
            n=int(inputted)
        except:
            break
        
        get_primes_stream(n,print_ordered_number)