# A way in python to change the functionality of a function 
# For eg if we want our div function to divede if a > b else reverse the order and do the operation
# i.e b/a and show the output



def reverse(func):

    def inner_func(a, b):
        if(a<b):
            a,b = b,a
        return func(a,b)

    return inner_func
      
    return func(b,a)

@reverse
def div(a,b):
    return a/b


print(div(2, 10))