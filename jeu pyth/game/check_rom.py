from play import*
def check_room(plateau,lig,col):
    """retourne True si (lig,col) est une case du plateau(lig et col sont des indice valides"""
    verrif=True
    if lig >plateau['n'] or lig<0:
        if col>plateau['n']  or col<0:
            verrif=False
            
        verrif=False
        assert verrif==(-1,3),'ValueError'
    return verrif
p=init_play()
s=check_room(p,0,3)
print(s)
    