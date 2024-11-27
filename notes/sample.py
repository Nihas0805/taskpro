def sap_dec(fn):

    def wrapper(n1,n2):

        if n1<n2:
            (n1,n2)=(n2,n1)

        return fn(n1,n2)

    return wrapper



def smart_sub(n1,n2):

    return n1-n2

def smart_div(n1,n2):

    return n1/n2

print(smart_sub(10,5))
print(smart_sub(5,10))