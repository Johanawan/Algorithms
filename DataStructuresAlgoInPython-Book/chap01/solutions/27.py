# n Section 1.8, we provided three different implementations of a generator
# that computes factors of a given integer. The third of those implementations, from page 41, was the most efficient, but we noted that it did not
# yield the factors in increasing order. Modify the generator so that it reports
# factors in increasing order, while maintaining its general performance advantages.

def factors1(n):
    for k in range(1, n+1):
        if n%k == 0: yield(k)
    
#Approach 3
def factors2(n):
    k = 1
    while k*k<n:
        if n%k == 0:
            yield k
            yield n//k
        k+=1
        if k*k == n:
            yield k
    
    
def factors_new(n):
    k = 1
    higher_factors = []
    while k*k <n:
        if n%k == 0:
            yield k
            higher_factors.append(n//k)
        k+=1
        if k*k == n:
            yield k
    for factor in reversed(higher_factors):
        yield factor
    
    
            
def gen_tester(fun, n = 100):
    gen = fun(100)
    for _ in range(n):
        
        try:
            print(next(gen), end = ',')
        except StopIteration as e:
            print ('   Reached the end of the generator')
            return
        
gen_tester(factors1, 100)
gen_tester(factors2, 100)   
gen_tester(factors_new, 100)