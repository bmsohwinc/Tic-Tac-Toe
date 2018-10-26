                    # PROJECT TIC-TAC-TOE

WAYS_TO_TIE = ((0,6,5),
               (0,2,7),
               (1,6,8),
               (2,8,3)
              )
human = ''
comp = ''
EMPTY = ' ' #space 
X = 'X'
O = 'O'
TIE = 'T'
MAX = 9
turn = X

def set_board():
    legal = []
    board = []
    for i in range(MAX):
        print("\ti=",i)
        board.append(EMPTY)
        legal.append(i)
    return board,legal

def show_board(board):                    
    print(" ___ ___ ___")
    print("|",board[0],"|",board[1],"|",board[2],"|")
    print("|___|___|___|")
    print("|",board[3],"|",board[4],"|",board[5],"|")
    print("|___|___|___|")
    print("|",board[6],"|",board[7],"|",board[8],"|")
    print("|___|___|___|")

def ask_key():          
    ans = input("Will you start(y/n)?" )
    return ans

def put_key(ans,i,b,l): 
    global human
    global comp                      
    if ans=='y':
        human = X
        comp = O    
        if i%2==0:
            human_move(b,l)           # indirect legal required => to be imported
        else:                       #       ^
            comp_move(b,l)            #_______|
    elif ans=='n':
        comp = X
        human = O
        if i%2==0:
            comp_move(b,l)        # indirect legal
        else:
            human_move(b,l)
    
#def nxt(turn):
#    if turn==X:
#        return O
#    else:
#        return X

def human_move(board,legal):              
    pos = int(input("Which place will you choose?<0-8> "))
    if pos in legal:
        print("Fine!")
        board[pos] = human
        #delete pos in legal
        for i in range(len(legal)):
            if legal[i]==pos:
                del legal[i]
                break   
    else:
        print("Move Invalid")
        human_move(board,legal)     # RECURSION!!!!! Whoaaaaaa!!
        
def comp_move(board,legal):              
    BEST_MOVE = (4,0,2,6,8,1,3,5,7)
    DIA = ((0,8),(2,6))
    OTH = (1,3,5,7)
    brd = board[:]
    print("Now, I'll pick")
    flag = 0
    if flag == 0:
        for pos in legal:
            brd[pos] = human
            if win(brd,legal) == human:
                board[pos] = comp
                print(pos)
                flag = 1
                break
            brd[pos] = comp
            if win(brd,legal) == comp:
                board[pos] = comp
                print(pos)
                flag = 1
                break
            brd[pos] = EMPTY
    f2 = 0
    if len(legal)==6:
        for row in DIA:
            if board[row[0]]==board[row[1]]==human:
                for j in legal:
                    if j in OTH:
                        f2 = 1
                        board[j] = comp
                        pos = j
                        print(j)
                        break
            if f2==1:
                break
    if flag == 0 and f2 == 0:
        for j in BEST_MOVE:
            if j in legal:                
                board[j] = comp
                pos = j
                print(j)
                break
    for i in range(len(legal)):
        if legal[i]==pos:
            del legal[i]
            break    

def win(board,legal):               
    WAYS_TO_WIN = ((0,1,2),
               (0,3,6),
               (0,4,8),
               (1,4,7),
               (2,4,6),
               (2,5,8),
               (3,4,5),
               (6,7,8)
               )
    ans = None
    for row in WAYS_TO_WIN:
        if board[row[0]]==board[row[1]]==board[row[2]]!=EMPTY:
            ans = board[row[0]]
            return board[row[0]]
    if ans == None and len(legal)==0:
        return TIE
    #for row in WAYS_TO_TIE:
     #   if board[row[0]]==board[row[1]]==board[row[2]]!=EMPTY:
      #      return TIE
    for i in legal:
        if board[i] == EMPTY:
            return None
            
def winner(board,legal):          # le
    ans = win(board,legal)
    return ans

def main():
    print("\t\t>> WELCOME TO THE UNBEATABLE TIC-TAC-TOE <<")
    b,l = set_board()
    show_board(b)
    ans = ask_key()
    res = None
    i = 0
    while res not in (X,O,TIE):
        put_key(ans,i,b,l)
        show_board(b)
        i+=1
        res = winner(b,l)
    if res == X or res == O:    
        print("Congrats,",res,"wins")
    else:
        print("Oh, it's a Tie")

main()

input("press enter")
