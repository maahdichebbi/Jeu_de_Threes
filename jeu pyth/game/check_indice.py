from play import*
def check_indice(plateau,indice):
    """ retourne True si indice correspond a un indice valide de case pour le plateau(entre 0 et n-1"""
    mot=True
    if indice>plateau['n'] or indice<0:
        mot=False
        assert mot<0,"ValueError"
    return mot  
p=init_play()
a=check_indice(p,1)
print(a)