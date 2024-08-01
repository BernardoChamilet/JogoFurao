import graphics as gf
import time
import random
import math

janela = gf.GraphWin("Ladraozinho Fedido",900,780,autoflush=False)

#criando a lista com os frames dos personagens
def listando(nome,frames,x,y):
	listaF = []
	cont = 1
	while cont < frames:
		palavra = "imagens/"+nome+str(cont)+".gif"
		img = gf.Image(gf.Point(x,y),palavra)
		listaF.append(img)
		cont += 1
	return(listaF)

def onde_ta(X,Y):
    if X in range(575,837):
        if Y in range(314,673):
            return("sala")
    if X in range(254,627):
        if Y in range(313,415):
            return("sala")
    if X in range(530,837):
        if Y in range(55,313):
            return("cozinha")
    if X in range(352,530):
        if Y in range(52,148):
            return("lavanderia")
    if X in range(350,523):
        if Y in range(160,313):
            return("banheiro")
    if X in range(63,338):
        if Y in range(55,313):
            return("quarto cima")
    if X in range(63,338):
        if Y in range(415,676):
            return("quarto baixo casal")
    if X in range(352,562):
        if Y in range(415,676):
            return("quarto baixo solteiro")

def desenha_quadrados(lista_comodo):
	indice = 0
	while indice < len(lista_comodo):
		lista_comodo[indice].draw(janela)
		indice += 1 
	gf.update()

def apaga_quadrados(lista_comodo):
	indice = 0
	while indice < len(lista_comodo):
		lista_comodo[indice].undraw()
		indice += 1 

def colidiu(X,Y):
    if Y >= 671 or Y <= 55:
        return(True)
    if X >= 837 or X <= 64:
        return(True)
    if X in range(620,838):
        if Y in range(305,364):
            return(True)
    if X in range(662,731):
        if Y >= 595:
            return(True)
    if X in range(784,837):
        if Y in range(368,427):
            return(True)
        if Y in range(452,501):
            return(True)
        if Y in range(524,566):
            return(True)
    if X in range(697,738):
        if Y in range(489,520):
            return(True)
    if X in range(575,643):
        if Y in range(450,579):
            return(True)
    if X >= 784:
        if Y <= 302:
            return(True)
    if X in range(638,691):
        if Y in range(180,303):
            return(True)
    if X in range(606,786):
        if Y in range(54,115):
            return(True)
    if X in range(511,574):
        if Y in range(409,673):
            return(True)
    if X in range(412,551):
        if Y in range(307,320):
            return(True)
    if X in range(522,537):
        if Y in range(136,308):
            return(True)
    if X in range(352,524):
        if Y in range(148,161):
            return(True)
    if X in range(335,356):
        if Y in range(45,321):
            return(True)
    if X in range(52,352):
        if Y in range(44,97):
            return(True)
    if X in range(51,64):
        if Y in range(57,676):
            return(True)
    if X in range(61,262):
        if Y in range(304,427):
            return(True)
    if X in range(64,565):
        if Y >= 674:
            return(True)
    if X in range(338,353):
        if Y in range(411,675):
            return(True)
    if X in range(432,575):
        if Y in range(410,425):
            return(True)
    if X in range(353,402):
        if Y in range(103,147):
            return(True)
    if X in range(448,502):
        if Y in range(103,148):
            return(True)
    if X in range(351,420):
        if Y in range(162,207):
            return(True)
    if X in range(435,524):
        if Y in range(163,233):
            return(True)
    if X in range(470,517):
        if Y in range(258,293):
            return(True)
    if X in range(69,147):
        if Y in range(62,232):
            return(True)
    if X in range(258,334):
        if Y in range(62,232):
            return(True)
    if X in range(69,232):
        if Y in range(482,619):
            return(True)
    if X in range(69,104):
        if Y in range(623,671):
            return(True)
    if X in range(289,340):
        if Y in range(503,677):
            return(True)
    if X in range(353,407):
        if Y in range(523,655):
            return(True)
    if X in range(488,563):
        if Y in range(428,587):
            return(True)
    if X in range(500,561):
        if Y in range(591,677):
            return(True)
    if X in range(593,639):
        if Y in range(600,644):
            return(True)
    return(False)

#colisao que retorna nova coordenada para as linhas de visao da vovo acabarem
def colidiuVovo(X,Y,xInicial,yInicial):
	if Y >= 671:
		return(["True","colidiuY",671])
	if Y <= 55:
		return(["True","colidiuY",55])
	if X >= 837:
		return(["True","colidiuX",837])
	if X <= 64:
		return(["True","colidiuX",64])
	if X in range(654,838):
		if Y > 321 and yInicial < 353:
			return(["True","colidiuY",321])
		if Y < 353 and yInicial > 321:
			return(["True","colidiuY",353])
	if Y in range(321,363):
		if X > 628 and xInicial < 653:
			return(["True","colidiuX",628])
		if X < 653 and xInicial > 628:
			return(["True","colidiuX",653])
	if X in range(662,731):
		if Y >= 595:
			return(["True","colidiuY",595])
	if X in range(784,837):
		if Y < 427 and yInicial > 368:
			return(["True","colidiuY",427])
		if Y > 368 and yInicial < 427:
			return(["True","colidiuY",368])
		if Y < 501 and yInicial > 452:
			return(["True","colidiuY",501])
		if Y > 452 and yInicial < 501:
			return(["True","colidiuY",452])
		if Y < 566 and yInicial > 524:
			return(["True","colidiuY",566])
		if Y > 524 and yInicial < 566:
			return(["True","colidiuY",524])
	if Y in range(489,520):
		if X < 728 and xInicial > 697:
			return(["True","colidiuX",728])
		if X > 697 and xInicial < 728:
			return(["True","colidiuX",697])
	if Y in range(450,579):
		if X > 575 and xInicial < 643:
			return(["True","colidiuX",575])
		if X < 643 and xInicial > 575:
			return(["True","colidiuX",643])
	if X >= 784:
		if Y <= 302:
			return(["True","colidiuY",302])
	if Y in range(180,303):
		if X > 638 and xInicial < 691:
			return(["True","colidiuX",638])
		if X < 691 and xInicial > 638:
			return(["True","colidiuX",691])
	if X in range(606,786):
		if Y > 54 and yInicial < 115:
			return(["True","colidiuY",54])
		if Y < 115 and yInicial > 54:
			return(["True","colidiuY",115])
	if Y in range(409,673):
		if X > 511 and xInicial < 574:
			return(["True","colidiuX",511])
		if X < 574 and xInicial > 511:
			return(["True","colidiuX",574])		
	if X in range(412,551):
		if Y > 307 and yInicial < 320:
			return(["True","colidiuY",307])
		if Y < 320 and yInicial > 307:
			return(["True","colidiuY",320])		
	if Y in range(136,308):
		if X > 522 and xInicial < 537:
			return(["True","colidiuX",522])
		if X < 537 and xInicial > 522:
			return(["True","colidiuX",537])
	if X in range(352,524):
		if Y > 148 and yInicial < 161:
			return(["True","colidiuY",148])
		if Y < 161 and yInicial > 148:
			return(["True","colidiuY",161])
	if Y in range(45,321):
		if X > 335 and xInicial < 356:
			return(["True","colidiuX",335])
		if X < 356 and xInicial > 335:
			return(["True","colidiuX",356])
	if X in range(52,352):
		if Y > 44 and yInicial < 97:
			return(["True","colidiuY",44])
		if Y < 97 and yInicial > 44:
			return(["True","colidiuY",97])
	if Y in range(57,676):
		if X > 51 and xInicial < 64:
			return(["True","colidiuX",51])
		if X < 64 and xInicial > 51:
			return(["True","colidiuX",64])
	if X in range(61,239):
		if Y > 412 and yInicial < 422:
			return(["True","colidiuY",412])
		if Y < 422 and yInicial > 412:
			return(["True","colidiuY",422])
	if Y in range(304,427):
		if X > 249 and xInicial < 263:
			return(["True","colidiuX",249])
		if X < 262 and xInicial > 249:
			return(["True","colidiuX",263])
	if Y in range(315,411):
		if X > 61 and xInicial < 240:
			return(["True","colidiuX",61])
		if X < 240 and xInicial > 61:
			return(["True","colidiuX",240])
	if X in range(64,565):
		if Y >= 674:
			return(["True","colidiuY",674])
	if Y in range(411,675):
		if X > 338 and xInicial < 353:
			return(["True","colidiuX",338])
		if X < 353 and xInicial > 338:
			return(["True","colidiuX",353])
	if X in range(432,575):
		if Y > 410 and yInicial < 425:
			return(["True","colidiuY",410])
		if Y < 425 and yInicial > 410:
			return(["True","colidiuY",425])
	if X in range(353,402):
		if Y > 103 and yInicial < 147:
			return(["True","colidiuY",103])
		if Y < 147 and yInicial > 103:
			return(["True","colidiuY",147])
	if X in range(448,502):
		if Y > 103 and yInicial < 148:
			return(["True","colidiuY",103])
		if Y < 148 and yInicial > 103:
			return(["True","colidiuY",148])
	if X in range(351,420):
		if Y > 162 and yInicial < 207:
			return(["True","colidiuY",162])
		if Y < 207 and yInicial > 162:
			return(["True","colidiuY",207])
	if X in range(435,524):
		if Y > 163 and yInicial < 233:
			return(["True","colidiuY",163])
		if Y < 233 and yInicial > 163:
			return(["True","colidiuY",233])
	if X in range(470,517):
		if Y > 258 and yInicial < 293:
			return(["True","colidiuY",258])
		if Y < 293 and yInicial > 258:
			return(["True","colidiuY",293])
	if Y in range(62,232):
		if X > 69 and xInicial < 147:
			return(["True","colidiuX",69])
		if X < 147 and xInicial > 69:
			return(["True","colidiuX",147])
	if Y in range(62,232):
		if X > 258 and xInicial < 334:
			return(["True","colidiuX",258])
		if X < 334 and xInicial > 258:
			return(["True","colidiuX",334])
	if X in range(69,232):
		if Y > 482 and yInicial < 619:
			return(["True","colidiuY",482])
		if Y < 619 and yInicial > 482:
			return(["True","colidiuY",619])
	if Y in range(623,671):
		if X > 69 and xInicial < 104:
			return(["True","colidiuX",69])
		if X < 104 and xInicial > 69:
			return(["True","colidiuX",104])
	if X in range(289,340):
		if Y > 503 and yInicial < 677:
			return(["True","colidiuY",503])
		if Y < 677 and yInicial > 503:
			return(["True","colidiuY",677])
	if Y in range(523,655):
		if X > 353 and xInicial < 407:
			return(["True","colidiuX",353])
		if X < 407 and xInicial > 353:
			return(["True","colidiuX",407])
	if Y in range(428,587):
		if X > 488 and xInicial < 563:
			return(["True","colidiuX",488])
		if X < 563 and xInicial > 488:
			return(["True","colidiuX",563])
	if Y in range(591,677):
		if X > 500 and xInicial < 561:
			return(["True","colidiuX",500])
		if X < 561 and xInicial > 500:
			return(["True","colidiuX",561])
	if X in range(593,639):
		if Y > 600 and yInicial < 644:
			return(["True","colidiuY",600])
		if Y < 644 and yInicial > 600:
			return(["True","colidiuY",644])
	return("False")

def geraLinhaX(angulo,xInicial,yInicial,xFinal):
	angulo = math.pi/180 * angulo
	yFinal = yInicial - (xFinal - xInicial) * math.tan(angulo)
	linha = gf.Line(gf.Point(xInicial,yInicial),gf.Point(xFinal,yFinal))
	linha.setFill("yellow")
	return([linha,yFinal])

def geraLinhaY(angulo,xInicial,yInicial,yFinal):
	angulo = math.pi/180 * angulo
	xFinal = xInicial - (yInicial - yFinal) * math.tan(angulo)
	linha = gf.Line(gf.Point(xInicial,yInicial),gf.Point(xFinal,yFinal))
	linha.setFill("yellow")
	return([linha,xFinal])

def achaEquacao(xInicial,yInicial,xFinal,yFinal):
	deltaX = xFinal - xInicial
	if deltaX == 0:
		deltaX = 0.00000000000001
	a = (yFinal - yInicial)/deltaX
	b = yInicial - a * xInicial
	return([a,b])

def moveTudo(x,y,lista):
	cont = 0
	while cont < len(lista):
		lista[cont].move(x,y)
		cont += 1

#escolhe uma das posiçoes possiveis de frango pra desenhar na tela
def gerandoFrango():
	n = random.randint(0,4)
	frangos[n].draw(janela)
	return(frangos[n])
	
def deitando(frame):
	deitandoF[frame].draw(janela)
	gf.update()
		
def dormindo(frame):
	dormindoF[frame].draw(janela)
	gf.update()

def deitandoEsquerda(frame):
	deitandoE[frame].draw(janela)
	gf.update()

def dormindoEsquerda(frame):
	dormindoE[frame].draw(janela)
	gf.update()

def vovoAndaDireita():
	x = 5
	moveTudo(x,0,direitaV)
	moveTudo(x,0,esquerdaV)
	moveTudo(x,0,frenteV)
	moveTudo(x,0,costasV)

def vovoAndaEsquerda():
	x = -5
	moveTudo(x,0,direitaV)
	moveTudo(x,0,esquerdaV)
	moveTudo(x,0,frenteV)
	moveTudo(x,0,costasV)
				
def vovoAndaCima():	
	y = -5
	moveTudo(0,y,direitaV)
	moveTudo(0,y,esquerdaV)
	moveTudo(0,y,frenteV)
	moveTudo(0,y,costasV)			
					
def vovoAndaBaixo():
	y = 5
	moveTudo(0,y,direitaV)
	moveTudo(0,y,esquerdaV)
	moveTudo(0,y,frenteV)
	moveTudo(0,y,costasV)	

#FUNÇOES QUE MOVEM O FURAO RETORNAM UMA LISTA DE FRAMES(COM OU SEM O FRANGO NA BOCA)
def movendoDireita(frame,pegouFrango):
	furaoAnchor = direitaF[0].getAnchor()
	coordenadaFurao = [int(furaoAnchor.getX()),int(furaoAnchor.getY())]
	if colidiu((coordenadaFurao[0]+16),(coordenadaFurao[1]+16)) or colidiu((coordenadaFurao[0]+16),coordenadaFurao[1]):
		x = 0
	else:
		x = 1
	moveTudo(x,0,direitaF)
	moveTudo(x,0,esquerdaF)
	moveTudo(x,0,frenteF)
	moveTudo(x,0,costasF)
	moveTudo(x,0,deitandoF)
	moveTudo(x,0,dormindoF)
	moveTudo(x,0,deitandoE)
	moveTudo(x,0,dormindoE)
	moveTudo(x,0,frangoD)
	moveTudo(x,0,frangoE)
	moveTudo(x,0,frangoC)
	moveTudo(x,0,frangoF)
	if pegouFrango == False:
		lista = direitaF
	else:
		lista = frangoD
	lista[frame].draw(janela)
	gf.update
	return(lista)

def movendoEsquerda(frame,pegouFrango):
	furaoAnchor = direitaF[0].getAnchor()
	coordenadaFurao = [int(furaoAnchor.getX()),int(furaoAnchor.getY())]
	if colidiu((coordenadaFurao[0]-16),coordenadaFurao[1]) or colidiu((coordenadaFurao[0]-16),(coordenadaFurao[1]+16)):
		x = 0
	else:
		x = -1
	moveTudo(x,0,direitaF)
	moveTudo(x,0,esquerdaF)
	moveTudo(x,0,frenteF)
	moveTudo(x,0,costasF)
	moveTudo(x,0,deitandoF)
	moveTudo(x,0,dormindoF)
	moveTudo(x,0,deitandoE)
	moveTudo(x,0,dormindoE)
	moveTudo(x,0,frangoD)
	moveTudo(x,0,frangoE)
	moveTudo(x,0,frangoC)
	moveTudo(x,0,frangoF)
	if pegouFrango == False:
		lista = esquerdaF
	else:
		lista = frangoE
	lista[frame].draw(janela)
	gf.update()
	return(lista)

def movendoCima(frame,pegouFrango):
	furaoAnchor = direitaF[0].getAnchor()
	coordenadaFurao = [int(furaoAnchor.getX()),int(furaoAnchor.getY())]
	if colidiu(coordenadaFurao[0],(coordenadaFurao[1]-16)):
		y = 0
	else:
		y = -1
	moveTudo(0,y,direitaF)
	moveTudo(0,y,esquerdaF)
	moveTudo(0,y,frenteF)
	moveTudo(0,y,costasF)
	moveTudo(0,y,deitandoF)
	moveTudo(0,y,dormindoF)
	moveTudo(0,y,deitandoE)
	moveTudo(0,y,dormindoE)
	moveTudo(0,y,frangoD)
	moveTudo(0,y,frangoE)
	moveTudo(0,y,frangoC)
	moveTudo(0,y,frangoF)
	if pegouFrango == False:
		lista = costasF
	else:
		lista = frangoC
	lista[frame].draw(janela)
	gf.update()
	return(lista)

def movendoBaixo(frame,pegouFrango):
	furaoAnchor = direitaF[0].getAnchor()
	coordenadaFurao = [int(furaoAnchor.getX()),int(furaoAnchor.getY())]
	if colidiu(coordenadaFurao[0],(coordenadaFurao[1]+18)):
		y = 0
	else:
		y = 1
	moveTudo(0,y,direitaF)
	moveTudo(0,y,esquerdaF)
	moveTudo(0,y,frenteF)
	moveTudo(0,y,costasF)
	moveTudo(0,y,deitandoF)
	moveTudo(0,y,dormindoF)
	moveTudo(0,y,deitandoE)
	moveTudo(0,y,dormindoE)
	moveTudo(0,y,frangoD)
	moveTudo(0,y,frangoE)
	moveTudo(0,y,frangoC)
	moveTudo(0,y,frangoF)
	if pegouFrango == False:
		lista = frenteF
	else:
		lista = frangoF
	lista[frame].draw(janela)
	gf.update()
	return(lista)

sair = False
while sair == False:
	#criando listas com frames
	direitaF = listando("furao direita ",5,770,617)
	esquerdaF = listando("furao esquerda ",5,770,617)
	costasF = listando("furao costas ",5,770,617)
	frenteF = listando("furao frente ",5,770,617)
	deitandoF = listando("furao deitando ",5,770,617)
	dormindoF = listando("furao dormindo ",3,770,617)
	frangoD = listando("frango direita ",5,770,617)
	frangoE = listando("frango esquerda ",5,770,617)
	frangoC = listando("frango costas ",5,770,617)
	frangoF = listando("frango frente ",5,770,617)
	direitaV = listando("vovo direita ",5,106,450)
	esquerdaV = listando("vovo esquerda ",5,106,450)
	costasV = listando("vovo costas ",5,106,450)
	frenteV = listando("vovo frente ",5,106,450)
	deitandoE = listando("furao deitandoE ",5,770,617)
	dormindoE = listando("furao dormindoE ",3,770,617)
	#criando frangos nas posiçoes diversas
	frangos = []
	frango1 = gf.Image(gf.Point(131,651),"imagens/frango.png")
	frangos.append(frango1)
	frango2 = gf.Image(gf.Point(428,647),"imagens/frango.png")
	frangos.append(frango2)
	frango3 = gf.Image(gf.Point(216,116),"imagens/frango.png")
	frangos.append(frango3)
	frango4 = gf.Image(gf.Point(381,62),"imagens/frango.png")
	frangos.append(frango4)
	frango5 = gf.Image(gf.Point(739,286),"imagens/frango.png")
	frangos.append(frango5)
	#criando retangulos pretos de formas diversas para tampar a parte certa do mapa
	cozinha = gf.Rectangle(gf.Point(537,55),gf.Point(834,305))
	cozinha.setFill("black")
	quartocima = gf.Rectangle(gf.Point(64,55),gf.Point(338,305))
	quartocima_pt2 = gf.Rectangle(gf.Point(64,300),gf.Point(247,356))
	quartocima_pt2.setFill("black")
	quartocima.setFill("black")
	quartobaixo_casal = gf.Rectangle(gf.Point(62,422),gf.Point(337,673))
	quartobaixo_casal_pt2 = gf.Rectangle(gf.Point(62,371),gf.Point(247,424))
	quartobaixo_casal_pt2.setFill("black")
	quartobaixo_casal.setFill("black")
	quartobaixo_solteiro = gf.Rectangle(gf.Point(352,422),gf.Point(560,673))
	quartobaixo_solteiro.setFill("black")
	corredor = gf.Rectangle(gf.Point(261,320),gf.Point(835,409))
	sala = gf.Rectangle(gf.Point(574,407),gf.Point(835,672))
	sala.setFill("black")
	corredor.setFill("black")
	porta_quartocima = gf.Rectangle(gf.Point(263,304),gf.Point(335,320))
	porta_quartocima.setFill("black")
	porta_quartobaixo_casal = gf.Rectangle(gf.Point(263,408),gf.Point(336,421))
	porta_quartobaixo_casal.setFill("black")
	porta_quartobaixo_solteiro = gf.Rectangle(gf.Point(359,408),gf.Point(433,421))
	porta_quartobaixo_solteiro.setFill("black")
	R1 = gf.Rectangle(gf.Point(62,354),gf.Point(248,372))
	R1.setFill("black")
	R2 = gf.Rectangle(gf.Point(337,423),gf.Point(351,673))
	R2.setFill("black")
	R3 = gf.Rectangle(gf.Point(337,55),gf.Point(835,305))
	R3.setFill("black")
	R4 = gf.Rectangle(gf.Point(332,56),gf.Point(521,320))
	R4.setFill("black")
	R5 = gf.Rectangle(gf.Point(334,403),gf.Point(576,673))
	R5.setFill("black")
	R6 = gf.Rectangle(gf.Point(63,292),gf.Point(269,426))
	R6.setFill("black")
	R7 = gf.Rectangle(gf.Point(63,160),gf.Point(834,673))
	R7.setFill("black")
	R8 = gf.Rectangle(gf.Point(333,55),gf.Point(538,148))
	R8.setFill("black")
	R9 = gf.Rectangle(gf.Point(537,304),gf.Point(835,319))
	R9.setFill("black")
	R10 = gf.Rectangle(gf.Point(246,373),gf.Point(263,423))
	R10.setFill("black")
	R11 = gf.Rectangle(gf.Point(351,54),gf.Point(835,319))
	R11.setFill("black")
	R12 = gf.Rectangle(gf.Point(63,54),gf.Point(835,365))
	R12.setFill("black")
	R13 = gf.Rectangle(gf.Point(430,407),gf.Point(576,672))
	R13.setFill("black")
	#separando os retangulos pretos que cada comodo requere desenho em tela
	lista_sala = [R1,R2,R3,quartocima,quartocima_pt2,quartobaixo_solteiro,quartobaixo_casal,quartobaixo_casal_pt2]
	lista_cozinha = [R4,R5,R6,sala,corredor,quartocima,quartobaixo_casal,porta_quartocima,porta_quartobaixo_casal]
	lista_lavanderia = [R7,quartocima,cozinha]
	lista_banheiro = [R8,R9,R5,R6,cozinha,sala,corredor,quartocima,quartobaixo_casal,porta_quartobaixo_casal,porta_quartocima]
	lista_quartocima = [R5,R10,R11,sala,corredor,quartobaixo_casal,quartobaixo_casal_pt2,porta_quartobaixo_casal]
	lista_quartobaixo_casal = [R12,R13,sala,corredor,quartobaixo_solteiro,porta_quartobaixo_solteiro]
	lista_quartobaixo_solteiro = [R12,R6,sala,corredor,quartobaixo_casal,porta_quartobaixo_casal]
	sair = False
	comoJogar = False
	velocidade = 777
	#retangulo branco para ficar atras da tela inicial
	tampaMapa = gf.Rectangle(gf.Point(0,0),gf.Point(900,780))
	tampaMapa.setFill("white")
	tampaMapa.setOutline("white")
	tampaMapa.draw(janela)
	#telas do jogo sem ser a de gameplay
	frangoAjustes = gf.Image(gf.Point(670,605),"imagens/frango.png")
	telaInicial = gf.Image(gf.Point(450,390),"imagens/telainicial.gif")
	comoJogar = gf.Image(gf.Point(450,390),"imagens/comojogar.png")
	ganhou = gf.Image(gf.Point(450,390),"imagens/ganhou.png")
	perdeu = gf.Image(gf.Point(450,390),"imagens/perdeu.png")
	ajustes = gf.Image(gf.Point(450,390),"imagens/ajustes.png")
	#TELA INICIAL
	telaInicial.draw(janela)
	while True:
		tecla = janela.getMouse()
		if int(tecla.getX()) in range(300,597):
			#JOGAR
			if int(tecla.getY()) in range(265,338):
				telaInicial.undraw()
				break
			#COMO JOGAR
			if int(tecla.getY()) in range(363,435):
				telaInicial.undraw()
				comoJogar.draw(janela)
				while True:
					tecla = janela.getMouse()
					if int(tecla.getX()) in range(631,761):
						#VOLTAR
						if int(tecla.getY()) in range(615,675):
							comoJogar.undraw()
							telaInicial.draw(janela)
							break
			#AJUSTES
			if int(tecla.getY()) in range(461,533):
				telaInicial.undraw()
				ajustes.draw(janela)
				cont4 = 0
				clicouMais = False
				clicouMenos = False
				while True:
					botao = janela.checkMouse()
					if botao != None:
						#MENOS
						if int(botao.getX()) in range(297,374) and int(botao.getY()) in range(487,562):
							if clicouMenos == False:
								velocidade += 222
							else:
								velocidade += 111
								clicouMenos = False
							clicouMais = True
							print(velocidade)
						#MAIS
						if int(botao.getX()) in range(112,190) and int(botao.getY()) in range(487,562):
							if velocidade >= 333:
								if clicouMais == False:
									velocidade -= 222
								else:
									velocidade -= 111
									clicouMais = False
								clicouMenos = True
							print(velocidade)
						#CONCLUIR
						if int(botao.getX()) in range(680,853) and int(botao.getY()) in range(636,687):
							ajustes.undraw()
							telaInicial.draw(janela)
							break
					#FRANGO MOVENDO
					if cont4 >= velocidade*5:
						cont4 = 0
						frangoAjustesAnchor = frangoAjustes.getAnchor()
						coordenadaFrangoAjustes = int(frangoAjustesAnchor.getY())
						if coordenadaFrangoAjustes == 165:
							deslocamento = 5
						if coordenadaFrangoAjustes == 605:
							deslocamento = -5
						frangoAjustes.undraw()
						frangoAjustes.move(0,deslocamento)
						frangoAjustes.draw(janela)
					cont4 += 1
				print(velocidade)
			#SAIR				
			if int(tecla.getY()) in range(558,631):
				telaInicial.undraw()
				sair = True
				break
	if sair == False:
		listaTrocaDirecaoVovo = [39,58,115,162,163,164,218,245,246,273,280,318,344,356,357,369,395,414,433,453,454,474,511,550]
		camaFurao = gf.Image(gf.Point(770,650),"imagens/cama.png")
		mapa3 = gf.Image(gf.Point(450,390),"imagens/casa 3.gif")
		pausa = gf.Image(gf.Point(450,365),"imagens/pause.gif")
		mapa3.draw(janela)
		camaFurao.draw(janela)
		costasF[0].draw(janela)
		furaoAnchor = costasF[0].getAnchor()
		coordenadaFurao = [int(furaoAnchor.getX()),int(furaoAnchor.getY())]
		frango = gerandoFrango()
		frangoAnchor = frango.getAnchor()
		coordenadaFrango = [int(frangoAnchor.getX()),int(frangoAnchor.getY())]
		cont2 = 0
		cont3 = 0
		listaLinhas = []
		passosVovo = 0
		frameVovo = 0
		ultimoFrameVovo = direitaV[0]
		desenha_quadrados(lista_sala)
		ultimoComodo = lista_sala
		tempoInativo = 0
		mesmoComodo = False
		pegouFrango = False
		perdeuJogo = False
		ultimoFrame = costasF[0]
		frameD = 0
		frameE = 0
		frameC = 0
		frameB = 0
		frameDormindo = 0
		tecla = janela.getKey()
		while sair == False:
			#PAUSA
			if tecla == "Escape":
				pausa.draw(janela)
				while True:
					tecla = janela.getMouse()
					#DESPAUSAR
					if int(tecla.getX()) in range(320,580):
						if int(tecla.getY()) in range(295,365):
							pausa.undraw()
							break
					#COMO JOGAR
					if int(tecla.getY()) in range(385,453):
						pausa.undraw()
						comoJogar.draw(janela)
						while True:
							tecla = janela.getMouse()
							if int(tecla.getX()) in range(631,761):
								#VOLTAR
								if int(tecla.getY()) in range(615,675):
									comoJogar.undraw()
									pausa.draw(janela)
									break
					#AJUSTES
					if int(tecla.getY()) in range(470,540):
						pausa.undraw()
						ajustes.draw(janela)
						cont4 = 0
						clicouMais = False
						clicouMenos = False
						while True:
							botao = janela.checkMouse()
							if botao != None:
								#MENOS
								if int(botao.getX()) in range(297,374) and int(botao.getY()) in range(487,562):
									if clicouMenos == False:
										velocidade += 222
									else:
										velocidade += 111
										clicouMenos = False
									clicouMais = True
									print(velocidade)
								#MAIS
								if int(botao.getX()) in range(112,190) and int(botao.getY()) in range(487,562):
									if velocidade >= 333:
										if clicouMais == False:
											velocidade -= 222
										else:
											velocidade -= 111
											clicouMais = False
										clicouMenos = True
									print(velocidade)
								#CONCLUIR
								if int(botao.getX()) in range(680,853) and int(botao.getY()) in range(636,687):
									ajustes.undraw()
									frangoAjustes.undraw()
									pausa.draw(janela)
									break
							#FRANGO MOVENDO
							if cont4 >= velocidade*5:
								cont4 = 0
								frangoAjustesAnchor = frangoAjustes.getAnchor()
								coordenadaFrangoAjustes = int(frangoAjustesAnchor.getY())
								if coordenadaFrangoAjustes == 165:
									deslocamento = 5
								if coordenadaFrangoAjustes == 605:
									deslocamento = -5
								frangoAjustes.undraw()
								frangoAjustes.move(0,deslocamento)
								frangoAjustes.draw(janela)
							cont4 += 1
						print(velocidade)
					#SAIR					
					if int(tecla.getY()) in range(560,630):
						pausa.undraw()
						sair = True
						break
			#FURAO MOVE DIREITA
			if tecla == "Right":
				tempoInativo = 0
				frameE = 0
				frameC = 0
				frameB = 0
				frameDormindo = 0
				if frameD == 4:
					frameD = 0
				ultimoFrame.undraw()
				listaD = movendoDireita(frameD,pegouFrango)
				ultimoFrame = listaD[frameD]
				furaoAnchor = listaD[0].getAnchor()
				coordenadaFurao = [int(furaoAnchor.getX()),int(furaoAnchor.getY())]
				#VENDO SE ELE PEGOU FRANGO
				if ((coordenadaFurao[0] in range((coordenadaFrango[0] - 30),(coordenadaFrango[0] + 30))) and (coordenadaFurao[1] in range((coordenadaFrango[1] - 24),(coordenadaFrango[1] + 24)))):
					pegouFrango = True
				#VENDO SE ELE GANHOU
				if (coordenadaFurao[0] in range(730,810)) and (coordenadaFurao[1] in range(620,680)) and pegouFrango:
					ganhou.draw(janela)
					gf.update()
					time.sleep(2)
					ganhou.undraw()
					mapa3.undraw()
					ultimoFrame.undraw()
					camaFurao.undraw()
					break
				frameD += 1
			#FURAO MOVENDO ESQUERDA
			elif tecla == "Left":
				tempoInativo = 0
				frameD = 0
				frameC = 0
				frameB = 0
				frameDormindo = 0
				if frameE == 4:
					frameE = 0
				ultimoFrame.undraw()
				listaE = movendoEsquerda(frameE,pegouFrango)
				ultimoFrame = listaE[frameE]
				furaoAnchor = listaE[0].getAnchor()
				coordenadaFurao = [int(furaoAnchor.getX()),int(furaoAnchor.getY())]
				#VENDO SE ELE PEGOU O FRANGO
				if ((coordenadaFurao[0] in range((coordenadaFrango[0] - 30),(coordenadaFrango[0] + 30))) and (coordenadaFurao[1] in range((coordenadaFrango[1] - 24),(coordenadaFrango[1] + 24)))):
					pegouFrango = True
				#VENDO SE ELE GANHOU
				if (coordenadaFurao[0] in range(730,810)) and (coordenadaFurao[1] in range(620,680)) and pegouFrango:
					ganhou.draw(janela)
					gf.update()
					time.sleep(2)
					ganhou.undraw()
					mapa3.undraw()
					ultimoFrame.undraw()
					camaFurao.undraw()
					break
				frameE += 1
			#FURAO MOVENDO CIMA
			elif tecla == "Up":
				tempoInativo = 0
				frameE = 0
				frameD = 0
				frameB = 0
				frameDormindo = 0
				if frameC == 4:
					frameC = 0
				ultimoFrame.undraw()
				listaC = movendoCima(frameC,pegouFrango)
				ultimoFrame = listaC[frameC]
				furaoAnchor = listaC[0].getAnchor()
				coordenadaFurao = [int(furaoAnchor.getX()),int(furaoAnchor.getY())]
				#VENDO SE ELE PEGOU O FRANGO
				if ((coordenadaFurao[0] in range((coordenadaFrango[0] - 30),(coordenadaFrango[0] + 30))) and (coordenadaFurao[1] in range((coordenadaFrango[1] - 24),(coordenadaFrango[1] + 24)))):
					pegouFrango = True
				#VENDO SE ELE GANHOU
				if (coordenadaFurao[0] in range(730,810)) and (coordenadaFurao[1] in range(620,680)) and pegouFrango:
					ganhou.draw(janela)
					gf.update()
					time.sleep(2)
					ganhou.undraw()
					mapa3.undraw()
					ultimoFrame.undraw()
					camaFurao.undraw()
					break
				frameC += 1
			#FURAO MOVENDO BAIXO
			elif tecla == "Down":
				tempoInativo = 0
				frameE = 0
				frameC = 0
				frameD = 0
				frameDormindo = 0
				if frameB == 4:
					frameB = 0
				ultimoFrame.undraw()
				listaB = movendoBaixo(frameB,pegouFrango)
				ultimoFrame = listaB[frameB]
				furaoAnchor = listaB[0].getAnchor()
				coordenadaFurao = [int(furaoAnchor.getX()),int(furaoAnchor.getY())]
				#VENDO SE ELE PEGOU O FRANGO
				if ((coordenadaFurao[0] in range((coordenadaFrango[0] - 30),(coordenadaFrango[0] + 30))) and (coordenadaFurao[1] in range((coordenadaFrango[1] - 24),(coordenadaFrango[1] + 24)))):
					pegouFrango = True
				#VENDO SE ELE GANHOU
				if (coordenadaFurao[0] in range(730,810)) and (coordenadaFurao[1] in range(620,680)) and pegouFrango:
					ganhou.draw(janela)
					gf.update()
					time.sleep(2)
					ganhou.undraw()
					mapa3.undraw()
					ultimoFrame.undraw()
					camaFurao.undraw()
					break
				frameB += 1
			#NENHUMA TECLA FOI CLICADA
			else:
				tempoInativo += 1
				tecla = "nenhuma"
				#DEITA(PRA DIREITA(IF) OU PRA ESQUERDA(ELSE))
				if tempoInativo == velocidade*540 and pegouFrango == False:
					ultimoFrame.undraw()
					if ultimoFrame == direitaF[frameD - 1] or ultimoFrame == costasF[frameC - 1]:
						deitando(0)
						ultimoFrame = deitandoF[0]
					else:
						deitandoEsquerda(0)
						ultimoFrame = deitandoE[0]
					frameE = 0
					frameC = 0
					frameD = 0
					frameB = 0
				if tempoInativo == velocidade*576 and pegouFrango == False:
					ultimoFrame.undraw()
					if ultimoFrame == deitandoF[0]:
						deitando(1)
						ultimoFrame = deitandoF[1]
					else:
						deitandoEsquerda(1)
						ultimoFrame = deitandoE[1]
				if tempoInativo == velocidade*612 and pegouFrango == False:
					ultimoFrame.undraw()
					if ultimoFrame == deitandoF[1]:
						deitando(2)
						ultimoFrame = deitandoF[2]
					else:
						deitandoEsquerda(2)
						ultimoFrame = deitandoE[2]
				if tempoInativo == velocidade*648 and pegouFrango == False:
					ultimoFrame.undraw()
					if ultimoFrame == deitandoF[2]:
						deitando(3)
						ultimoFrame = deitandoF[3]
					else:
						deitandoEsquerda(3)
						ultimoFrame = deitandoE[3]
				#DORME(PRA DIREITA(IF) OU PRA ESQUERDA(ELSE))
				if tempoInativo > velocidade*648 and pegouFrango == False:
					if ultimoFrame == deitandoF[3] or ultimoFrame == dormindoF[0] or ultimoFrame == dormindoF[1]:
						if cont2 >= velocidade*100:
							ultimoFrame.undraw()
							dormindo(frameDormindo)
							ultimoFrame = dormindoF[frameDormindo]
							frameDormindo += 1
							cont2 = 0
						if frameDormindo == 2:
							frameDormindo = 0
					else:
						if cont2 == velocidade*100:
							ultimoFrame.undraw()
							dormindoEsquerda(frameDormindo)
							ultimoFrame = dormindoE[frameDormindo]
							frameDormindo += 1
							cont2 = 0	
						if frameDormindo == 2:
							frameDormindo = 0
					cont2 += 1
			#APAGA FRANGO DA TELA QUANDO O FURAO PEGA ELE NA BOCA
			if pegouFrango == True:
				frango.undraw()
			#PARTE DA VOVO
			if cont3 >= velocidade*10:
				vovoAnchor = direitaV[frameVovo].getAnchor()
				coordenadaVovo = [int(vovoAnchor.getX()),int(vovoAnchor.getY())]
				comodoVovo = onde_ta(coordenadaVovo[0],coordenadaVovo[1])
				comodoFurao = onde_ta(coordenadaFurao[0],coordenadaFurao[1])
				#VOVO ANDA DIREITA
				if passosVovo < 39 or passosVovo in range(58,115) or passosVovo == 163 or passosVovo in range(218,245) or passosVovo in range(344,356) or passosVovo in range(454,474):	
					vovoAndaDireita()
					ultimoFrameVovo.undraw()
					#GERA CONE E VE COLISAO DAS LINHAS
					for linha in listaLinhas:
						linha.undraw()
					listaLinhas = []
					angulo = 30
					x1 = coordenadaVovo[0] + 15
					y1 = coordenadaVovo[1]
					xFinal = x1 + 50
					while angulo >= -30:
						retorno = geraLinhaX(angulo,x1,y1,xFinal)
						linha = retorno[0]
						yFinal = retorno[1]
						linha.move(5,0)
						colisaoLinha = colidiuVovo(xFinal+5,round(yFinal),x1+5,y1)
						if colisaoLinha[0] == "True":
							if colisaoLinha[1] == "colidiuY":
								yFinal = colisaoLinha[2]
								retorno = geraLinhaY(angulo,x1+5,y1,yFinal)
								linha = retorno[0]
								xFinal = retorno[1]
							if colisaoLinha[1] == "colidiuX":
								xFinal = colisaoLinha[2]
								retorno = geraLinhaX(angulo,x1+5,y1,xFinal)
								linha = retorno[0]
								yFinal = retorno[1]
						equacao = achaEquacao(x1+5,y1,xFinal,yFinal)
						a = equacao[0]
						b = equacao[1]
						#VE SE O FURAO PERDEU
						if coordenadaFurao[0] in range(x1+5,round(xFinal)):
							yTeste = a*coordenadaFurao[0]+b
							if yTeste in range(coordenadaFurao[1]-15,coordenadaFurao[1]+15):
								perdeu.draw(janela)
								gf.update()
								time.sleep(2)
								perdeu.undraw()
								mapa3.undraw()
								ultimoFrame.undraw()
								camaFurao.undraw()
								perdeuJogo = True
								break
						listaLinhas.append(linha)
						angulo -= 1
					if perdeuJogo:
						break
					x1 += 5
					#VE SE TEM QUE DESENHAR A VOVO E O CONE
					if comodoVovo == comodoFurao:
						direitaV[frameVovo].draw(janela)
						for linha in listaLinhas:
							linha.draw(janela)
						gf.update()
					ultimoFrameVovo = direitaV[frameVovo]
					frameVovo += 1
					cont3 = 0
					passosVovo += 1
					if frameVovo == 4:
						frameVovo = 0
				#VOVO ANDA CIMA
				elif passosVovo in range(39,58) or passosVovo in range(115,162) or passosVovo in range(273,280) or passosVovo in range(369,395) or passosVovo in range(414,433) or passosVovo == 453:
					vovoAndaCima()
					ultimoFrameVovo.undraw()
					#GERA CONE E VE COLISAO DAS LINHAS
					for linha in listaLinhas:
						linha.undraw()
					listaLinhas = []
					angulo = -30
					y1 = coordenadaVovo[1] - 23
					x1 = coordenadaVovo[0]
					yFinal = y1 - 50
					while angulo <= 30:
						retorno = geraLinhaY(angulo,x1,y1,yFinal)
						linha = retorno[0]
						xFinal = retorno[1]
						linha.move(0,-5)
						colisaoLinha = colidiuVovo(round(xFinal),yFinal-5,x1,y1-5)
						if colisaoLinha[0] == "True":
							if colisaoLinha[1] == "colidiuY":
								yFinal = colisaoLinha[2]
								retorno = geraLinhaY(angulo,x1,y1-5,yFinal)
								linha = retorno[0]
								xFinal = retorno[1]
							if colisaoLinha[1] == "colidiuX":
								xFinal = colisaoLinha[2]
								retorno = geraLinhaX(angulo,x1,y1-5,xFinal)
								linha = retorno[0]
								yFinal = retorno[1]
						equacao = achaEquacao(x1,y1-5,xFinal,yFinal)
						a = equacao[0]
						b = equacao[1]
						#VE SE O FURAO PERDEU
						if coordenadaFurao[1] in range(round(yFinal),y1-5):
							xTeste = (coordenadaFurao[1]-b)/a
							if xTeste in range(coordenadaFurao[0]-15,coordenadaFurao[0]+15):
								perdeu.draw(janela)
								gf.update()
								time.sleep(2)
								perdeu.undraw()
								mapa3.undraw()
								ultimoFrame.undraw()
								camaFurao.undraw()
								perdeuJogo = True
								break
						listaLinhas.append(linha)
						angulo += 1
					if perdeuJogo:
						break
					y1 -= 5
					#VE SE TEM QUE DESENHAR A VOVO E O CONE
					if comodoVovo == comodoFurao:
						costasV[frameVovo].draw(janela)
						for linha in listaLinhas:
							linha.draw(janela)
						gf.update()
					ultimoFrameVovo = costasV[frameVovo]
					frameVovo += 1
					cont3 = 0
					passosVovo += 1
					if frameVovo == 4:
						frameVovo = 0
				#VOVO ANDA BAIXO
				elif passosVovo in range(164,218) or passosVovo == 245 or passosVovo in range(318,344) or passosVovo == 356 or passosVovo in range(474,511):
					vovoAndaBaixo()
					ultimoFrameVovo.undraw()
					#GERANDO CONE E TESTANDO COLISAO DAS LINHAS
					for linha in listaLinhas:
						linha.undraw()
					listaLinhas = []
					angulo = 150
					y1 = coordenadaVovo[1] + 23
					x1 = coordenadaVovo[0]
					yFinal = y1 + 50
					while angulo <= 210:
						retorno = geraLinhaY(angulo,x1,y1,yFinal)
						linha = retorno[0]
						xFinal = retorno[1]
						linha.move(0,5)
						colisaoLinha = colidiuVovo(round(xFinal),yFinal+5,x1,y1+5)
						if colisaoLinha[0] == "True":
							if colisaoLinha[1] == "colidiuY":
								yFinal = colisaoLinha[2]
								retorno = geraLinhaY(angulo,x1,y1+5,yFinal)
								linha = retorno[0]
								xFinal = retorno[1]
							if colisaoLinha[1] == "colidiuX":
								xFinal = colisaoLinha[2]
								retorno = geraLinhaX(angulo,x1,y1+5,xFinal)
								linha = retorno[0]
								yFinal = retorno[1]
						equacao = achaEquacao(x1,y1+5,xFinal,yFinal)
						a = equacao[0]
						b = equacao[1]
						#VE SE O FURAO PERDEU
						if coordenadaFurao[1] in range(y1+5,round(yFinal)):
							xTeste = (coordenadaFurao[1]-b)/a
							if xTeste in range(coordenadaFurao[0]-15,coordenadaFurao[0]+15):
								perdeu.draw(janela)
								gf.update()
								time.sleep(2)
								perdeu.undraw()
								mapa3.undraw()
								ultimoFrame.undraw()
								camaFurao.undraw()
								perdeuJogo = True
								break
						listaLinhas.append(linha)
						angulo += 1
					if perdeuJogo:
						break
					y1 += 5
					#VE SE TEM QUE DESENHAR A VOVO E O CONE
					if comodoVovo == comodoFurao:
						frenteV[frameVovo].draw(janela)
						for linha in listaLinhas:
							linha.draw(janela)
						gf.update()
					ultimoFrameVovo = frenteV[frameVovo]
					frameVovo += 1
					cont3 = 0
					passosVovo += 1
					if frameVovo == 4:
						frameVovo = 0
				#VOVO ANDA ESQUERDA
				elif passosVovo == 162 or passosVovo in range(246,273) or passosVovo in range(280,318) or passosVovo in range(357,369) or passosVovo in range(395,414) or passosVovo in range(433,453) or passosVovo in range(511,550):
					vovoAndaEsquerda()
					ultimoFrameVovo.undraw()
					#GERA CONE E VE COLISAO DAS LINHAS
					for linha in listaLinhas:
						linha.undraw()
					listaLinhas = []
					angulo = 150
					x1 = coordenadaVovo[0] - 15
					y1 = coordenadaVovo[1]
					xFinal = x1 - 50
					while angulo <= 210:
						retorno = geraLinhaX(angulo,x1,y1,xFinal)
						linha = retorno[0]
						yFinal = retorno[1]
						linha.move(-5,0)
						colisaoLinha = colidiuVovo(xFinal-5,round(yFinal),x1-5,y1)
						if colisaoLinha[0] == "True":
							if colisaoLinha[1] == "colidiuY":
								yFinal = colisaoLinha[2]
								retorno = geraLinhaY(angulo,x1-5,y1,yFinal)
								linha = retorno[0]
								xFinal = retorno[1]
							if colisaoLinha[1] == "colidiuX":
								xFinal = colisaoLinha[2]
								retorno = geraLinhaX(angulo,x1-5,y1,xFinal)
								linha = retorno[0]
								yFinal = retorno[1]
						equacao = achaEquacao(x1-5,y1,xFinal,yFinal)
						a = equacao[0]
						b = equacao[1]
						#VE SE O FURAO PERDEU
						if coordenadaFurao[0] in range(round(xFinal),x1-5):
							yTeste = a*coordenadaFurao[0]+b
							if yTeste in range(coordenadaFurao[1]-15,coordenadaFurao[1]+15):
								perdeu.draw(janela)
								gf.update()
								time.sleep(2)
								perdeu.undraw()
								mapa3.undraw()
								ultimoFrame.undraw()
								camaFurao.undraw()
								perdeuJogo = True
								break
						listaLinhas.append(linha)
						angulo += 1
					if perdeuJogo:
						break
					x1 -= 5
					#VE SE TEM QUE DESENHAR A VOVO E O CONE
					if comodoVovo == comodoFurao:
						esquerdaV[frameVovo].draw(janela)
						for linha in listaLinhas:
							linha.draw(janela)
						gf.update()
					ultimoFrameVovo = esquerdaV[frameVovo]
					frameVovo += 1
					cont3 = 0
					passosVovo += 1
					if frameVovo == 4:
						frameVovo = 0
				else:
					teste = "balela"
				if passosVovo in listaTrocaDirecaoVovo:
					frameVovo = 0
				if passosVovo == 550:
					passosVovo = 0
			cont3 += 1
			#VE EM QUE COMODO O FURAO TA
			if tecla != "nenhuma":
				comodoFurao = onde_ta(coordenadaFurao[0],coordenadaFurao[1])
				if comodoFurao == "sala":
					apaga_quadrados(ultimoComodo)
					desenha_quadrados(lista_sala)
					ultimoComodo = lista_sala
				elif comodoFurao == "cozinha":
					apaga_quadrados(ultimoComodo)
					desenha_quadrados(lista_cozinha)
					ultimoComodo = lista_cozinha
				elif comodoFurao == "lavanderia":
					apaga_quadrados(ultimoComodo)
					desenha_quadrados(lista_lavanderia)
					ultimoComodo = lista_lavanderia
				elif comodoFurao == "banheiro":
					apaga_quadrados(ultimoComodo)
					desenha_quadrados(lista_banheiro)
					ultimoComodo = lista_banheiro
				elif comodoFurao == "quarto cima":
					apaga_quadrados(ultimoComodo)
					desenha_quadrados(lista_quartocima)
					ultimoComodo = lista_quartocima
				elif comodoFurao == "quarto baixo casal":
					apaga_quadrados(ultimoComodo)
					desenha_quadrados(lista_quartobaixo_casal)
					ultimoComodo = lista_quartobaixo_casal
				else:
					apaga_quadrados(ultimoComodo)
					desenha_quadrados(lista_quartobaixo_solteiro)
					ultimoComodo = lista_quartobaixo_solteiro
			tecla = janela.checkKey()