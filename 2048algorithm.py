# Project started December 2023


###### INSTRUCTIONS ##############
# Install keyboard and pystyle if you do not already have them.
# This is a game of 2048! Individual players have their previous game saved. Use the Arrow keys to play, Backspace to rewind 1 move and esc to pause.
# The game also keeps track of the highscore and player that achieved that high score. Personal Bests are also displayed
# Obviously the code looks unnecessarily long, but theres a lot of string formatting and logic that goes into a game of 2048 that you can overlook. An example is not generating a new number when the previous move didnt change the board.
import random
from pystyle import Colors
import os
import time



#random.seed(69)
delay = 0

board = [['.','.','.','.'],
         ['.','.','.','.'],
         ['.','.','.','.'],
         ['.','.','.','.']]

def formatName(name):    #This function just correctly capitalizes peoples names

    name = name.capitalize()
    return name

#basic setup here and functions but the actual code is below

score = 0
gameOver = False
moves = 0
def getOverallHighscoreHolder():
    overallHighscore = 0
    if(os.path.exists('highscore.txt')):
        with open('highscore.txt', 'r') as file:    # Gets the highscore from the file and the person that holds the highscore.
            splitline = file.readline().split(':')
            overallHighscore = int(splitline[1])
            overallHighscoreHolder = splitline[0]
            overallHighscoreHolder = formatName(overallHighscoreHolder)
    else:
        overallHighscore = 0
        overallHighscoreHolder = 'Nobody'
    return overallHighscore, overallHighscoreHolder
overallHighscore,overallHighscoreHolder = getOverallHighscoreHolder()













#Each one of these functions looks pretty complicated, but its just moving everything to the respective side and then adding them then removing the space between the numbers. (This took the most time to make and I figured it would be the most challenging part) Exceptions such as adding numbers twice and correctly adding pairs of numbers have been fixed

def moveDown(board, score): 
    oldscore = score
    beforeboard = [row[:] for row in board]
    
    for jindex in range(4):
        
        for iindex in range(2, -1, -1):
            if board[iindex][jindex] != '.':
                for k in range(3, iindex, -1):
                    if board[k][jindex] == '.':
                        board[k][jindex] = board[iindex][jindex]
                        board[iindex][jindex] = '.'
                        break

    for jindex in range(4):
        for iindex in range(3, 0, -1):
            if board[iindex][jindex] == board[iindex - 1][jindex] and board[iindex][jindex] != '.':
                board[iindex][jindex] = str(int(board[iindex][jindex]) * 2)
                score += int(board[iindex][jindex]) 
                board[iindex - 1][jindex] = '.'
                
   
    for jindex in range(4):
        for iindex in range(2, -1, -1):
            if board[iindex][jindex] != '.':
                for k in range(3, iindex, -1):
                    if board[k][jindex] == '.':
                        board[k][jindex] = board[iindex][jindex]
                        board[iindex][jindex] = '.'

    return beforeboard, oldscore, score

def moveLeft(board,score): 
    oldscore = score
    beforeboard = [row[:] for row in board]
    
    for iindex, ivalue in enumerate(board):
       
        for jindex in range(1, 4):
            if board[iindex][jindex] != '.':
                for k in range(0, jindex):
                    if board[iindex][k] == '.':
                        board[iindex][k] = board[iindex][jindex]
                        board[iindex][jindex] = '.'
                        break

    
    for iindex, ivalue in enumerate(board):
        for jindex in range(0, 3):
            if board[iindex][jindex] == board[iindex][jindex + 1] and board[iindex][jindex] != '.':
                board[iindex][jindex] = str(int(board[iindex][jindex]) * 2)
                score += int(board[iindex][jindex]) 
                board[iindex][jindex + 1] = '.'
                
    
    for iindex, ivalue in enumerate(board):
        for jindex in range(1, 4):
            if board[iindex][jindex] != '.':
                for k in range(0, jindex):
                    if board[iindex][k] == '.':
                        board[iindex][k] = board[iindex][jindex]
                        board[iindex][jindex] = '.'

    return beforeboard, oldscore, score


def moveUp(board,score):
    oldscore = score
    beforeboard = [row[:] for row in board]
    
    for jindex in range(4):
       
        for iindex in range(1, 4):
            if board[iindex][jindex] != '.':
                for k in range(0, iindex):
                    if board[k][jindex] == '.':
                        board[k][jindex] = board[iindex][jindex]
                        board[iindex][jindex] = '.'
                        break

   
    for jindex in range(4):
        for iindex in range(0, 3):
            if board[iindex][jindex] == board[iindex + 1][jindex] and board[iindex][jindex] != '.':
                board[iindex][jindex] = str(int(board[iindex][jindex]) * 2)
                score += int(board[iindex][jindex]) 
                board[iindex + 1][jindex] = '.'
                
    
    for jindex in range(4):
        for iindex in range(1, 4):
            if board[iindex][jindex] != '.':
                for k in range(0, iindex):
                    if board[k][jindex] == '.':
                        board[k][jindex] = board[iindex][jindex]
                        board[iindex][jindex] = '.'

    return beforeboard, oldscore, score

def moveRight(board,score): 
    oldscore = score
    beforeboard = [row[:] for row in board]
    
    for iindex, ivalue in enumerate(board):
        
        for jindex in range(2, -1, -1):
            if board[iindex][jindex] != '.':
                for k in range(3, jindex, -1):
                    if board[iindex][k] == '.':
                        board[iindex][k] = board[iindex][jindex]
                        board[iindex][jindex] = '.'
                        break

    
    for iindex, ivalue in enumerate(board):
        for jindex in range(3, 0, -1):
            if board[iindex][jindex] == board[iindex][jindex - 1] and board[iindex][jindex] != '.':
                board[iindex][jindex] = str(int(board[iindex][jindex]) * 2)
                score += int(board[iindex][jindex]) 
                board[iindex][jindex - 1] = '.'
                
    
    for iindex, ivalue in enumerate(board):
        for jindex in range(2, -1, -1):
            if board[iindex][jindex] != '.':
                for k in range(3, jindex, -1):
                    if board[iindex][k] == '.':
                        board[iindex][k] = board[iindex][jindex]
                        board[iindex][jindex] = '.'

    return beforeboard, oldscore, score




def printBoard(board): # Does a little string formatting and prints the board with the correct color of the elements in the 2D list based on the dictionary above
    colordict = {'.':Colors.white,'2':Colors.cyan,'4':Colors.yellow,'8':Colors.orange,'16':Colors.green,'32':Colors.blue, '64':Colors.red, '128':Colors.pink, '256':Colors.purple, '512':Colors.dark_green, '1024':Colors.turquoise,'2048':Colors.light_red,'4096':Colors.gray}
    for i in board:
        for j in i:
            if(len(j)!=1):
                numspaces = 9-len(j)#   ((len(j)-1)*4)   <-- old code didnt work
            else:
                numspaces = 8
            
            print(f'{colordict[j]}{j}',end=' '*numspaces) 
        for i in range(4): 
            print()

def getHighestTile(board):
    highest = 0
    for i in board:
        for j in i:
            if(j!='.'):
                if(int(j)>highest):highest=int(j)
    return highest

def possibleMovesCheck(board):   # A game of 2048 does not end when all spaces are full. This function checks to make sure that there are no more possible moves before returning 0.
    for index,value in enumerate(board):
        for jindex, jvalue in enumerate(value):
            if(jindex!=3):
                if(jvalue==board[index][jindex+1]):
                    return 'True'
            if(jvalue=='.'):
                return 'True'
    for index,value in enumerate(board):
        for jindex, jvalue in enumerate(value):
            if(index!=3):
                if(board[index][jindex]==board[index+1][jindex]):
                    return 'True'
    return 0


def getRandomPos(board):   # recursive function that finds a random position on the board that doesnt have a number in the slot 
    posX = random.randrange(4)
    posY = random.randrange(4)
    if(board[posX][posY] == '.'):
        return posX,posY
    else:
            try:
                return getRandomPos(board)
            except RecursionError:
                pass

def doGameOver(board,score, moves):
    colordict = {'.':Colors.white,'2':Colors.cyan,'4':Colors.yellow,'8':Colors.orange,'16':Colors.green,'32':Colors.blue, '64':Colors.red, '128':Colors.pink, '256':Colors.purple, '512':Colors.dark_green, '1024':Colors.turquoise,'2048':Colors.light_red,'4096':Colors.gray}
    print(f'{Colors.light_red}{trialnum}){Colors.white} Reached {Colors.green}{score} {Colors.white}and tile {colordict[str(getHighestTile(board))]}{getHighestTile(board)} {Colors.white} on {Colors.turquoise} {randomseed}')
    
    with open('savedAI.txt','a') as file:
        file.write(f'{trialnum} {score} {getHighestTile(board)} {moves} {randomseed}\n')

def getNextNum():    #Simple function that returns whether the next number generated is a 2 or 4. There is a 1/8 chance of it being a 4 and 7/8 chance of the next number being a 2
    randomnum = random.randrange(10)
    if(randomnum == 0):
        return 4
    else:
        return 2

def addNextNum(board):   # Uses the getRandomPos and getNextNum functions to place the number on the board 
    try:
        posX, posY = getRandomPos(board)
        board[posX][posY] = str(getNextNum())
    except:
        pass

def saveBoard(name, board, filename, score, moves):  # Saves the board, score and number of moves to the respective player's file.
    
    path = f'{name.lower()}/{filename}'
    with open(path, 'w') as file:
        filestring = str(board)
        file.write(filestring)
        file.write('\n' + str(score))
        file.write('\n' + str(moves))

def saveOverallHighscore(name,score):  # Saves the overall highscore to the file.
    with open('highscore.txt', 'w') as file:
        file.write(name + ':' + str(score))

def savePersonalHighscore(name,score): # Saves the personal highscore to the file.
    path = f'{name.lower()}/highscore.txt'
    with open(path, 'w') as file:
        file.write(str(score))

def getNameInput(validNameInput):
    while validNameInput==False:
        name = input(f'{Colors.green}Enter your name: ')
        if(name!=''):
            acceptedCharacters = 'abcdefghijklmnopqrstuvwxyz-1234567890 '
            validNameInput = True
            for i in name:
                if(i.lower() not in acceptedCharacters):
                    print(f'{Colors.red}Try again! Enter a valid name!')
                    validNameInput = False
                    break
        else:
            continue
    return name

def combinationsExistBetweenRows(board,row1,row2):
    for i in range(4):
        if(board[row1][i]==board[row2][i] and board[row1][i]!='.'): return True
    return False

def boardSetup(board):
     for i in range(2):
            addNextNum(board)

def combinationsExistInRow(board,row):
    for index,value in enumerate(board[row]):
        if(index==len(board[row])-1):break
        if(board[row][index+1]==board[row][index] and board[row][index]!='.'):return True
    return False

def combinationsExistInColumn(board,col):
    for i in range(3):
        if(board[i+1][col]==board[i][col] and board[i][col]!='.'):return True
        return False

def rowInAscendingOrder(board,row):
    newlist,otherlist = [],[]
    for i in board[row]:
        if(i!='.'):
            newlist.append(int(i))
            otherlist.append(int(i))
    otherlist.sort()
    if(otherlist==newlist):return True
    return False
    
def checkScores(name,score,personalHighScore, overallHighscore, overallHighscoreHolder):
    if(score>=personalHighScore):
        personalHighScore = score
        savePersonalHighscore(name,score)
    if(score>=overallHighscore):
        overallHighscore = score
        overallHighscoreHolder = formatName(name)
        saveOverallHighscore(name,score)
   
    return personalHighScore, overallHighscore, overallHighscoreHolder

def getPersonalHighScore(highscorePath):
    if(os.path.exists(highscorePath)):
        with open(highscorePath) as file:
            personalHighScore = int(file.readline())
    else:
        personalHighScore = 0

    return personalHighScore

def greatestInCorner(board):
    greatest = 0
    for i in board:
        for j in i:
            if(j!='.'):
                if(int(j)>greatest):greatest = int(j)
    if(board[3][3]!='.'):
        if(greatest==int(board[3][3])):return True
    return False

def columnFilled(board,column):
    for i in range(4):
        if(board[i][column]=='.'):return False
    return True

def smallestInRowPos(board,row):
    smallest = 10000
    pos = 10000
    for index,value in enumerate(board[row]):
        if(value!='.'):
            if(int(value)<smallest):
                smallest = int(value)
                pos = index
    return pos

def combinationsToGetTo(num1, num2):
    combinations = 0
    while num1<num2:
        num1*=2  
        combinations+=1
    return combinations

def checkRemove(board,score,move):
    testboard1 = [row[:] for row in board]
    if(move=='DOWN'):
        beforeboarddown, oldscore, score = moveDown(testboard1,score)
        score = oldscore
        if(beforeboarddown==testboard1):
            return True
        return False
    if(move=='RIGHT'):
        beforeboardright, oldscore, score = moveRight(testboard1,score)
        score = oldscore
        if(beforeboardright==testboard1):
            return True
        return False
    if(move=='LEFT'):
        beforeboardleft, oldscore, score = moveLeft(testboard1,score)
        score = oldscore
        if(beforeboardleft==testboard1):
            return True
        return False

def getCombinationValue(board):
    combinationValue = 0
    for row in board:
        for i in range(len(row) - 1):
            if row[i] == row[i + 1] and row[i] != '.':
                combinationValue += int(row[i]) * 2
    for col in range(len(board[0])):
        for row in range(len(board) - 1):
            if board[row][col] == board[row + 1][col] and board[row][col] != '.':
                combinationValue += int(board[row][col]) * 2

    return combinationValue

def tryMove(board,score,move):
    testboard1 = [row[:] for row in board]
    if(move=='DOWN'):
        beforeboarddown, oldscore, score = moveDown(testboard1,score)
        score = oldscore
        return getCombinationValue(testboard1)
    if(move=='RIGHT'):
        beforeboardright, oldscore, score = moveRight(testboard1,score)
        score = oldscore
        return getCombinationValue(testboard1)
    if(move=='LEFT'):
        beforeboardleft, oldscore, score = moveLeft(testboard1,score)
        score = oldscore
        return getCombinationValue(testboard1)
    if(move=='UP'):
        beforeboardup, oldscore, score = moveUp(testboard1,score)
        score = oldscore
        return getCombinationValue(testboard1)


# def tryMovePotentials(board,score,move):
#     testboard1 = [row[:] for row in board]
#     if(move=='DOWN'):
#         beforeboarddown, oldscore, score = moveDown(testboard1,score)
#         score = oldscore
#         return calcMovePotential(testboard1)
#     if(move=='RIGHT'):
#         beforeboardright, oldscore, score = moveRight(testboard1,score)
#         score = oldscore
#         return calcMovePotential(testboard1)
#     if(move=='LEFT'):
#         beforeboardleft, oldscore, score = moveLeft(testboard1,score)
#         score = oldscore
#         return calcMovePotential(testboard1)
#     if(move=='UP'):
#         beforeboardup, oldscore, score = moveUp(testboard1,score)
#         score = oldscore
#         return calcMovePotential(testboard1)

def getBestPossibleMove(possibleMoves,board):
    bestMove = 'NONE'
    bestMoveVal = -100000
    # equalscores = []
    for move in possibleMoves:
        # if(tryMove(board,score,move)==bestMoveVal):
        #     equalscores.append(bestMove)
        #     equalscores.append(move)
        if(tryMove(board,score,move)>bestMoveVal):
            bestMoveVal = tryMove(board,score,move)
            bestMove = move
    # if(len(equalscores)>1):
    #     print("RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
    #     if(tryMove(board,score,equalscores[0])==bestMoveVal):
    #         print('SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')
    #         maxPotentialMove = 'NONE'
    #         maxPotential = -100000
    #         for move in equalscores:
    #             if(tryMovePotentials(board,score,move)>maxPotential):
    #                 maxPotentialMove = move
    #                 maxPotential = tryMovePotentials(board,score,move)
    #         bestMove = maxPotentialMove

    return [bestMove]

# def calcMovePotential(board):
#     move_potential = 0
#     for row in board:
#         for i in range(len(row) - 1):
#             if row[i] != '.' and row[i + 1] != '.':
#                 if int(row[i]) * 2 == int(row[i + 1]):
#                     move_potential += int(row[i])
#                 elif int(row[i + 1]) * 2 == int(row[i]):
#                     move_potential += int(row[i + 1])

#     for col in range(len(board[0])):
#         for row in range(len(board) - 1):
#             if board[row][col] != '.' and board[row + 1][col] != '.':
#                 if int(board[row][col]) * 2 == int(board[row + 1][col]):
#                     move_potential += int(board[row][col])
#                 elif int(board[row + 1][col]) * 2 == int(board[row][col]):
#                     move_potential += int(board[row + 1][col])

#     return move_potential


def hasNumber(list):
    for i in list:
        if i !='.':return True
    return False   

def columnEmpty(board,column):
    for i in range(4):
        if(board[i][column]!='.'):return False
    return True

def isPyramidCase(board):
    if(board[3][0]=='.' and board[3][1]!='.' and board[3][2]!='.' and board[3][3]!='.'):
        if(columnEmpty(board,0)==False): return True
    return False
def isDoubleDownCase(board,col):
        if(board[1][col]!='.' and board[2][col]!='.' and board[3][col]!='.'):
            if((int(board[1][col]) + int(board[2][col]))==int(board[3][col])): return True
        return False
def isPerfectBottom(board):
    if('.' not in board[3]):
        if( int(board[3][0])*2==int(board[3][1]) and int(board[3][1])*2==int(board[3][2]) and int(board[3][2])*2==int(board[3][3])):return True
    return False
def isPartialPerfectBottom(board):
    if('.' not in board[3]):
        if(int(board[3][1])*2==int(board[3][2]) and int(board[3][2])*2==int(board[3][3])):return True
    return False


def getNextMove(board,beforeboard,prevMove,score,moves):
    possibleMoves = ['DOWN','RIGHT']
    if(beforeboard==board and prevMove!='' and prevMove in possibleMoves):
        possibleMoves.remove(prevMove)
    if('DOWN' in possibleMoves):
        if(checkRemove(board,score,'DOWN')): possibleMoves.remove('DOWN')
    if((('.' not in board[3]) and combinationsExistInRow(board,3)==False) or len(possibleMoves)==0):possibleMoves.append('LEFT')
    if('LEFT' in possibleMoves):
        if(checkRemove(board,score,'LEFT')): possibleMoves.remove('LEFT')
    if(board[3][3]=='.' and prevMove!=''): possibleMoves = ['RIGHT']
    if('RIGHT' in possibleMoves):
        if(checkRemove(board,score,'RIGHT')): possibleMoves.remove('RIGHT')
    if(combinationsExistInRow(board,3)):
        possibleMoves = ['RIGHT']
    if(combinationsExistInRow(board,3)==False and combinationsExistBetweenRows(board,2,3)):
        possibleMoves = ['DOWN']
    if(len(possibleMoves)==0):
        if('.' in board[3] and hasNumber(board[3])): 
            possibleMoves = ['LEFTR']
        else:
            possibleMoves = ['UPD']
    if(prevMove=='UPD'):
        possibleMoves = ['DOWN']

    # if(rowInAscendingOrder(board,3)==False and greatestInCorner(board) and columnFilled(board,3) and smallestInRowPos(board,3)==2 and combinationsToGetTo(int(board[3][2]),int(board[3][3]))>3 and combinationsExistInColumn(board,3)==False  and (columnFilled(board,2)==False or combinationsExistInColumn(board,2))):
    #         possibleMoves = ['UPR']

    if(prevMove=='LEFTR' or prevMove=='UPR'):
        possibleMoves = ['RIGHT']
    if(prevMove=='RIGHTL'):
        possibleMoves = ['LEFT']
  #  print(possibleMoves)
    if(len(possibleMoves)>1 and ((getHighestTile(board)>1024 and isPartialPerfectBottom(board)))):
        possibleMoves = ['LEFT','DOWN']
        if(combinationsExistInRow(board,2)): possibleMoves = ['LEFT']
        if(combinationsExistInRow(board,2)==False and (combinationsExistBetweenRows(board,1,2))): possibleMoves=['DOWN']
        if(checkRemove(board,score,'LEFT') and 'LEFT' in possibleMoves):possibleMoves.remove('LEFT')
        if(checkRemove(board,score,'DOWN') and 'DOWN' in possibleMoves):possibleMoves.remove('DOWN')
        
        if(combinationsExistInRow(board,2)==False and combinationsExistBetweenRows(board,1,2)==False and ('.' not in board[2]) and checkRemove(board,score,'RIGHT')==False): possibleMoves.append('RIGHT')
        if(board[2][0]!='.' and board[2][1]!='.'):
            if(checkRemove(board,score,'LEFT')==False and int(board[2][0])<int(board[2][1])): possibleMoves = ['LEFT']
        if(len(possibleMoves)==0 and checkRemove(board,score,'RIGHT')==False): possibleMoves = ['RIGHTL']
  #  print(possibleMoves)
    if(len(possibleMoves)>1 and moves>50):
       possibleMoves = getBestPossibleMove(possibleMoves,board)
    if(len(possibleMoves)>1 and moves<50 and (isPyramidCase(board))): #or (isDoubleDownCase(board,2) and greatestInCorner(board)))):
        possibleMoves = ['DOWN']
    if(len(possibleMoves)==0):
        possibleMoves = ['UPD']
    
    return random.choice(possibleMoves)





def playMove(board,move,score):
    if(move=='RIGHT' or move=='RIGHTL'):
        beforeboard,oldscore,score = moveRight(board,score)
        return beforeboard,oldscore,score
    elif(move=='UP' or move=='UPD' or move=='UPR'):
        beforeboard,oldscore,score = moveUp(board,score)
        return beforeboard,oldscore,score
    elif(move=='DOWN'):
        beforeboard,oldscore,score = moveDown(board,score)
        return beforeboard,oldscore,score
    elif(move=='LEFT' or move == 'LEFTR'):
        beforeboard,oldscore,score = moveLeft(board,score)
        return beforeboard,oldscore,score
    


def askLoadSaveGame(board,score,moves,savedGamePath):

    if(os.path.exists(savedGamePath)):
        loadsavedgame = input('Would you like to load your saved game? (Y/N): ')
        if(loadsavedgame == 'Y' or loadsavedgame=='y'):
            with open(savedGamePath, 'r') as file:
                board = eval(file.readline())
                score = int(file.readline())
                moves = int(file.readline())
        else:
            boardSetup(board)
    else:
        boardSetup(board) 
    
    return board,score,moves

def printFormattedScores(score,moves,numspaces):
    print(f'{Colors.green}Your score: {score}' + ((numspaces+1) - len(str(score)))*' ' + f'Personal Highscore: {personalHighScore}')
    print(f'{Colors.pink}Your moves: {moves}' + ((numspaces+1) - len(str(moves)))*' ' + f'Overall Highscore: {overallHighscore} held by {Colors.white}{overallHighscoreHolder}') 

def printFormattedBoard(board):
        print('\n\n')
        printBoard(board)
        print('\n\n\n\n\n\n')

def checkBreakLoop(board, gameOver,moves,beforeboard):
    if(possibleMovesCheck(board)==0):
            gameOver=True
    if beforeboard != board: 
        addNextNum(board)
    else:
        moves -= 1
    return board, gameOver, moves

def playGame(gameOver,board,moves,score):

    #personalHighScore = getPersonalHighScore(highscorePath)
    #overallHighscore,overallHighscoreHolder = getOverallHighscoreHolder()
    prevMove = ''
    boardSetup(board)
    beforeboard = [row[:] for row in board]
    
    while(gameOver==False):
       # personalHighScore, overallHighscore, overallHighscoreHolder = checkScores(name, score, personalHighScore, overallHighscore, overallHighscoreHolder)
        # printFormattedScores(score,moves,numspaces)      # String formatting here so everything looks neat.
        # printFormattedBoard(board)
        #saveBoard(name,board,'savedgame.txt', score, moves)   # Saves the board after every move
        moves +=1
        currentMove = getNextMove(board,beforeboard,prevMove,score,moves)
        #print(f'{Colors.green}{currentMove}')
        beforeboard,oldscore,score = playMove(board,currentMove,score)
        prevMove = currentMove
        
        board, gameOver, moves = checkBreakLoop(board,gameOver,moves,beforeboard)
        



    if(gameOver):
        doGameOver(board,score,moves)



#Functions end
#Program starts here

os.system('cls')
splash2048 = f"""

{Colors.cyan}.d888b.  {Colors.white}.d88b. {Colors.yellow}   j88D  {Colors.orange}.d888b. 
{Colors.cyan}VP  `8D {Colors.white}.8P  88.  {Colors.yellow}j8~88  {Colors.orange}88   8D 
{Colors.cyan}  odD' {Colors.white}88  d'88 {Colors.yellow}j8' 88  {Colors.orange}`VoooY' 
{Colors.cyan} .88'   {Colors.white}88 d' 88 {Colors.yellow}V88888D {Colors.orange}.d~~~b. 
{Colors.cyan}j88.    {Colors.white}`88  d8'     {Colors.yellow}88  {Colors.orange}88   8D 
{Colors.cyan}888888D  {Colors.white}`Y88P'      {Colors.yellow}VP  {Colors.orange}`Y888P' 
             {Colors.turquoise} by RS


 """
print(splash2048)
validNameInput = False
name = getNameInput(validNameInput)
      
userpath = f'{name.lower()}'
os.makedirs(userpath, exist_ok=True)
savedGamePath = f'{name.lower()}/savedgame.txt'
highscorePath = f'{name.lower()}/highscore.txt'
randomseed = random.randint(1, 100000000)
random.seed(randomseed)

board, score, moves = askLoadSaveGame(board, score, moves, savedGamePath)


#personalHighScore = getPersonalHighScore(highscorePath)

#printFormattedScores(score,moves,8)      # String formatting here so everything looks neat.
#printFormattedBoard(board)
trialnum = 1

prevMove = ''
beforeboard = [row[:] for row in board]
while(gameOver==False):
    #personalHighScore, overallHighscore, overallHighscoreHolder = checkScores(name, score, personalHighScore, overallHighscore, overallHighscoreHolder)
    #numspaces = 8
   # printFormattedScores(score,moves,numspaces)      # String formatting here so everything looks neat.
  #  printFormattedBoard(board)
   # saveBoard(name,board,'savedgame.txt', score, moves)   # Saves the board after every move
    moves +=1
    currentMove = getNextMove(board,beforeboard,prevMove,score,moves)
    print(f'{Colors.green}{currentMove}')
    beforeboard,oldscore,score = playMove(board,currentMove,score)
    prevMove = currentMove
  #  time.sleep(delay)
    
    board, gameOver, moves = checkBreakLoop(board,gameOver,moves,beforeboard)
   # time.sleep(delay)
    



if(gameOver):
    doGameOver(board,score,moves)


for i in range(1000000):
    randomseed = random.randint(1, 1000000000000)
    random.seed(randomseed)
    board = [['.','.','.','.'],
         ['.','.','.','.'],
         ['.','.','.','.'],
         ['.','.','.','.']]
    playGame(False,board,0,0)
    trialnum+=1


