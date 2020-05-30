## Merlin.py disponibilizado pelo massanori
def enumerações(items):
    n = len(items)
    s = [0]*(n+1)
    k = 0
    while True:
        if s[k] < n:
            s[k+1] = s[k] + 1
            k += 1
        else:
            s[k-1] += 1
            k -= 1
        if k == 0:
            break
        else:
            lista = []
            for j in range(1, k+1):
                lista.append(items[s[j]-1])
            yield lista

def combinações(items, n):
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in combinações(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def permutações(items):
    return combinações(items, len(items))
print ('Enumerações')
for p in enumerações(['Jessica', 'Fernanda', 'Pamela', 'Renata']):
    print (p)
x = input('Digite algo...')
print ('Permutações')
for p in permutações(['Adriano','Bruno', 'Diogo', 'Eclis', 'Gabriel', 'Leandro', 'Walber']):
    print (p)


## Lógica proposta em aula
## Pelo Professor

def Table(bench, list):
    for x in range(len(bench)):
        if bench[i-1] not in list[bench[x]]:
            return False
    return True 

def Preferences(list):
    p = {}
    for x in list:
        p.update({1[0]: 1[1:]})
    return p

def Organize_names(set):
    names = []
    listed =  []
    for l in set:
        l = l.split('\n')
        l.append(l[0])

    for n in l:
        name = n.split()
        names.append(name)

    return Preferences(names)


## Damas!!!
reference = open('casamento.txt', 'r')
brides = Organize_names(reference)
brides_names = []

for y in brides:
    brides_names.append(y)

right = True
enumeration = enumerações(brides_names)
for listed in enumeration:
    l = []
    for bride in listed:
        l.extend([b for b in brides[bride]])
    if (len(set(l))) >= len(listed)): continue
    else: 
        print("Não a macho para todas")
        right = True
        break
if right:
    print("Deu certo, todas arrumaram machos")



## Cavaleiros!!!!!
reference2 = open('cavaleiros.txt', 'r')
knights = Organize_names(reference2)
knights_names = []

for x in knights:
    knights_names.append(x)

found = False
permutation = permutações(knights_names)
for z in permutation:
    if Table(z, knights) == True:
        print(z'\n', 'Távola Organizada')
        found = True
        break
if not found: print('Távola Desorganizada!')

### Esse código é um teste
### Código pode ser refatorado 
### Tentando fazer caso de testes e concertar erros