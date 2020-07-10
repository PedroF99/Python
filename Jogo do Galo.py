
tl = 1
tm = 2
tr = 3
ml = 4
mm = 5
mr = 6
dl = 7
dm = 8
dr = 9
jogada = 0
jogador = 1
jogadas = 0




def verifica():
    global tl,tm,tr,ml,mm,mr,dl,dm,dr,jogadas
    
    if tl==tm and tm==tr and tm!=2:
        return 1
    if ml==mm and mm==mr and mm!=5:
        return 1
    if dl==dm and dm==dr and dm!=8:
        return 1
    if tl==ml and ml==dl and ml!=4:
        return 1
    if tm==mm and mm==dm and mm!=5:
        return 1
    if tr==mr and mr==dr and mr!=6:
        return 1
    if tl==mm and mm==dr and mm!=5:
        return 1
    if tr==mm and mm==dl and mm!=5:
        return 1
    if jogadas== 9:
        return 3
        
    return 0



def tabu():
    
    global tl,tm,tr,ml,mm,mr,dl,dm,dr,jogador,jogador1,jogador2
    
    print(" _ _ _" "\n""|" + str(tl) + "|" + str(tm) + "|" + str(tr) + "|" "\n" "|" + str(ml) + "|" + str(mm) + "|" + str(mr) + "|" "\n" "|" + str(dl) + "|" + str(dm) + "|" + str(dr) + "|" "\n" )
    
    veri= verifica()
    if veri== 0:
        joga()
    elif veri== 1:
        if jogador==1:
            print ("O Jogador "+ jogador2 + " ganhou!! Muitos Parabens")
        else:
            print ("O Jogador "+ jogador1 + " ganhou!! Muitos Parabens")
    else:
        print("O Joga acabou empatado!!")

def verjogada():
    global jogada
    
    if jogada!="1" and jogada!="2" and jogada!="3" and jogada!="4" and jogada!="5" and jogada!="6" and jogada!="7" and jogada!="8" and jogada!="9":
        
        return 0
    else:
        if jogada=="1":
            if tl!=1:
                return 0
                
        if jogada=="2":
            if tm!=2:
                return 0
                
        if jogada=="3":
            if tr!=3:
                return 0
                
        if jogada=="4":
            if ml!=4:
                return 0
                
        if jogada=="5":
            if mm!=5:
                return 0
                
        if jogada=="6":
            if mr!=6:
                return 0
                
        if jogada=="7":
            if dl!=7:
                return 0
                
        if jogada=="8":
            if dm!=8:
                return 0
                
        if jogada=="9":
            if dr!=9:
                return 0
        return 1
    

def joga():
    
    global tl,tm,tr,ml,mm,mr,dl,dm,dr
    global jogada,jogador,jogadas
    
    jogada = input (' intoduza o numero da casa que pertende jogar: ')
    jog = verjogada()
    if jog== 1:
        
        if jogada=="1":
            
            if jogador==1:
                tl = "X"
                jogador = 2
            else:
                tl = "O"
                jogador = 1
                
        if jogada=="2":
            
           if jogador==1:
                tm = "X"
                jogador = 2
           else:
                tm = "O"
                jogador = 1
                
        if jogada=="3":
            
            if jogador==1:
                tr = "X"
                jogador = 2
            else:
                tr = "O"
                jogador = 1
                
        if jogada=="4":
            
           if jogador==1:
                ml = "X"
                jogador = 2
           else:
                ml = "O"
                jogador = 1
                
        if jogada=="5":
            
            if jogador==1:
                mm = "X"
                jogador = 2
            else:
                mm = "O"
                jogador = 1
                
        if jogada=="6":
            
           if jogador==1:
                mr = "X"
                jogador = 2
           else:
                mr = "O"
                jogador = 1
                
        if jogada=="7":
            
           if jogador==1:
                dl = "X"
                jogador = 2
           else:
                dl = "O"
                jogador = 1
                
        if jogada=="8":
            
           if jogador==1:
                dm = "X"
                jogador = 2
           else:
                dm = "O"
                jogador = 1
                
        if jogada=="9":
            
           if jogador==1:
                dr = "X"
                jogador = 2
           else:
                dr = "O"
                jogador = 1
        jogadas =jogadas + 1  
        print (jogadas)
    else:
        joga()
    
    tabu()

print("\n \n JOGO DO GALO!!! \n")
print("Introduza o numero 1 para jogar")
print("Introduza o numero 0 ou outro para sair")
com = input ("Escolha: ")
if com== "1":
    jogador1 = input ("Introduza o nome do primeiro jogador: ")
    jogador2 = input ("Introduza o nome do segundo jogador: ")
    print(" _ _ _" "\n" "|" + str(tl) + "|" + str(tm) + "|" + str(tr) + "|" "\n" "|" + str(ml) + "|" + str(mm) + "|" + str(mr) + "|" "\n" "|" + str(dl) + "|" + str(dm) + "|" + str(dr) + "|" "\n" )   
    joga()
    
    
    
    
    
    
    
    
    
