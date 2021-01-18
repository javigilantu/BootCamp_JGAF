# Esta directorio contiene finciones
def get_root_path(n):
    path = os.getcwd()
    for i in range(n):
        path = os.path.dirname(path)
        print(path)
    sys.path.append(path)

def flatter(L):
    if len(L) == 1:
            if type(L[0]) == list or type(L[0]) == dict or type(L[0]) == tuple :
                    result = flatten(L[0])
            else:
                    result = L
    elif ype(L[0]) == list or type(L[0]) == dict or type(L[0]) == tuple:
            result = flatten(L[0]) + flatten(L[1:])
    else:
            result = [L[0]] + flatten(L[1:])
        
    return result

get_root_path(4)

