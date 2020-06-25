board = [' ' for i in range(10)]

# for i in range(10):
# 	board[i]='*'


# def insertcharac(ch,pos):
#     board [pos] = ch 
def insertcharac(letter,pos):
        board[pos] = letter

def printboard(board):
	print('   |   |   ')
	print(' '+board[1]+' | '+board[2]+' | '+board[3])
	print('   |   |   ')
	print('---------------')
	print('   |   |   ')
	print(' '+board[4]+' | '+board[5]+' | '+board[6])
	print('   |   |   ')
	print('---------------')
	print('   |   |   ')
	print(' '+board[7]+' | '+board[8]+' | '+board[9])
	print('   |   |   ')

def isfreespace(pos):
	return board[pos] == ' '

def isfullboard(board):
	if board.count(' ')>1:
		return False
	else:
		return True

def iswinner(b,ch):
	if ((b[1]==ch and b[2]==ch and b[3]==ch) or
	 (b[4]==ch and b[5]==ch and b[6]==ch) or 
	 (b[7]==ch and b[8]==ch and b[9]==ch) or 
	 (b[1]==ch and b[4]==ch and b[7]==ch) or 
	 (b[2]==ch and b[5]==ch and b[8]==ch) or 
	 (b[3]==ch and b[6]==ch and b[9]==ch) or 
	 (b[1]==ch and b[5]==ch and b[9]==ch) or 
	 (b[3]==ch and b[5]==ch and b[7]==ch)):
		return True
	else:
		return False

def player_move():
	flag=True
	while flag:
		move = input('Select a position to enter X between 1 to 9: ')
		
		try:
			move=int(move)
			if move>0 and move<10:
				if isfreespace(move):
					flag=False
					insertcharac('X', move)
				else:
					print('This space is occupied')
			else:
				print('Please enter character between 1 to 9')

		except:
			print('Please enter number')

def computer_move():
    possible_moves = [x for x, ch in enumerate(board) if ch == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possible_moves:
            temp=board[:]
            temp[i] = let
            if iswinner(temp, let):
                move = i
                return move

    corners_available=[]
    for i in possible_moves:
        if i in [1,3,7,9]:
            corners_available.append(i)
            
    if len(corners_available) > 0:
        move=selectrandom(corners_available)
        return move

    if 5 in possible_moves:
        move =5
        return move

    mid_edges=[]
    for i in possible_moves:
        if i in [2,4,6,8]:
            mid_edges.append(i)
            
    if len(mid_edges) > 0:
        move=selectrandom(mid_edges)
        
    return move

def selectrandom(lst):
	import random
	l=len(lst)
	r=random.randrange(0,l)
	return lst[r]

def main():
	print ('Welcome to Tic-Tac-Toe game')
	printboard(board)

	while not (isfullboard(board)):
		if not(iswinner(board,'O')):
			player_move()
			printboard(board)
		else:
			print('You lose the game')
			break

		if not (iswinner(board,'X')):
			move=computer_move()
			if move == 0:
				print('Tie game')
			else:
				insertcharac('O', move)
				print('Computer placed an O on position', move,':')
				printboard(board)

		else:
			print('You win the game')
			break

	if (isfullboard(board)):
		print('Tie game')
main()
while True:
	
    x = input('Do you want to play again? (y/n)')
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        print('Thank you')
        break

# printboard(board)
