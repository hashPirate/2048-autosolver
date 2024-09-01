# Project started October 2023


###### INSTRUCTIONS ##############
# Install keyboard and pystyle if you do not already have them.
# This is a game of 2048! Individual players have their previous game saved. Use the Arrow keys to play, Backspace to rewind 1 move and esc to pause.
# The game also keeps track of the highscore and player that achieved that high score. Personal Bests are also displayed
# Obviously the code looks unnecessarily long, but theres a lot of string formatting and logic that goes into a game of 2048 that you can overlook. An example is not generating a new number when the previous move didnt change the board.
import random
from pystyle import Colors
import keyboard
import os




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
    colordict = {'.':Colors.white,'2':Colors.cyan,'4':Colors.yellow,'8':Colors.orange,'16':Colors.green,'32':Colors.blue, '64':Colors.red, '128':Colors.pink, '256':Colors.purple, '512':Colors.dark_green, '1024':Colors.turquoise,'2048':Colors.gray,'4096':Colors.light_red}
    for i in board:
        for j in i:
            if(len(j)!=1):
                numspaces = 9-len(j)#   ((len(j)-1)*4)   <-- old code didnt work
            else:
                numspaces = 8
            
            print(f'{colordict[j]}{j}',end=' '*numspaces) 
        for i in range(4): 
            print()


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

def doGameOver(name,board,score,personalHighScore,overallHighscore):
    print(f'{Colors.cyan}Game Over! Here are your stats: ')
    print(f'You scored {Colors.white}{score}{Colors.cyan} in {Colors.white}{moves}{Colors.cyan} moves')
    if(personalHighScore==score):
        print(f'{Colors.pink}YOU SET A NEW PERSONAL BEST!')
    if(overallHighscore==score):
        print(f'{Colors.light_blue}YOU SET A NEW OVERALL HIGH SCORE!!!!!')

    print('\n\n\n')
    printBoard(board)
    os.remove(f'{name}/savedgame.txt')

def getNextNum():    #Simple function that returns whether the next number generated is a 2 or 4. There is a 1/8 chance of it being a 4 and 7/8 chance of the next number being a 2
    randomnum = random.randrange(8)
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
            acceptedCharacters = 'abcdefghijklmnopqrstuvwxyz- '
            validNameInput = True
            for i in name:
                if(i.lower() not in acceptedCharacters):
                    print(f'{Colors.red}Try again! Enter a valid name!')
                    validNameInput = False
                    break
        else:
            continue
    return name


def boardSetup(board):
     for i in range(2):
            addNextNum(board)

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
        print('\n\n\n\n\n\n\n')

def checkBreakLoop(board, gameOver,moves,beforeboard):
    breakloop = False
    if(possibleMovesCheck(board)==0):
            gameOver=True
            breakloop = True
    if beforeboard != board: 
        addNextNum(board)
    else:
        moves -= 1
    return board, gameOver, moves, breakloop


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

board, score, moves = askLoadSaveGame(board, score, moves, savedGamePath)


personalHighScore = getPersonalHighScore(highscorePath)

    
             


while(gameOver==False):
    personalHighScore, overallHighscore, overallHighscoreHolder = checkScores(name, score, personalHighScore, overallHighscore, overallHighscoreHolder)
    numspaces = 8
    printFormattedScores(score,moves,numspaces)      # String formatting here so everything looks neat.
    printFormattedBoard(board)
    saveBoard(name,board,'savedgame.txt', score, moves)   # Saves the board after every move
    key = True
    moves +=1
    backspace = False

    while(key==True):
        docheck = True
        event = keyboard.read_event()                         # Learning how to get the keyboard input without it counting it as multiple key presses took a while
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'up':
                beforeboard, oldscore,score = moveUp(board,score)
                key,docheck = False,True
            elif event.name == 'down':
                beforeboard, oldscore,score = moveDown(board,score)
                key,docheck = False,True
            elif event.name == 'left':
                beforeboard, oldscore,score  = moveLeft(board,score)
                key,docheck = False,True
            elif event.name == 'right':
                beforeboard, oldscore, score = moveRight(board,score)
                key,docheck = False,True
            elif event.name == 'esc':
                print(f'{Colors.turquoise} GAME HAS BEEN PAUSED!')
                a = input('Type Q to quit the game or anything else to return to the game: ')
                if(a=='Q' or a== 'q'):
                    printBoard(board)
                    print(f'\n SEE YOU NEXT TIME {formatName(name)}!')
                    quit()
                else:
                    printBoard(board)
            elif event.name == 'backspace':                       # Logic for going back a move.
                 if(backspace == False):
                    try:
                        board = [row[:] for row in beforeboard]
                        printBoard(board)
                        moves -= 2
                        score = oldscore
                        printFormattedScores(score,moves,numspaces) 
                        printFormattedBoard(board)
                        moves += 1
                        backspace = True
                        docheck = False
                    except:
                        printFormattedScores(score,moves,numspaces) 
                        print('\n\n')
                        printBoard(board)
                        print(f'\n\n\n{Colors.red}You cant go backwards on this move!\n\n\n')
                        docheck = False
                        
                    
            
            else:
                continue
                
            if(docheck):  # Checks if the loop is currently in the backspace state
                board, gameOver, moves, breakloop = checkBreakLoop(board,gameOver,moves,beforeboard)
                if(breakloop): break



if(gameOver):
    doGameOver(name,board,score,personalHighScore,overallHighscore)





