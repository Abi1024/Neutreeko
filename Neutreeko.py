#Neutreeko, by Abi
X = "X";
O = "O";
EMPTY = " ";
NUM_SQUARES = 25;
import random;
import copy;

#the board consists of 6 lists, each list having 2 elements denoting the coordinates of a piece. 1st 3 lists are for X, last 3 are for O.

#takes as input three pieces as a list, and returns them as a list ordered by their x-coordinate
def sort_x(pieces):
 result = []
 buffer = []
 for piece in pieces:
  buffer.append(piece);
 while buffer:
  max_index = 0;
  for i in range(0,len(buffer)):
      if buffer[i][0]>buffer[max_index][0]:
          max_index = i;
  result.append(buffer[max_index]);
  buffer.pop(max_index);
 return result;

def sort_y(pieces):
 result = []
 buffer = []
 for piece in pieces:
  buffer.append(piece);
 while buffer:
  max_index = 0;
  for i in range(0,len(buffer)):
      if buffer[i][1]>buffer[max_index][1]:
          max_index = i;
  result.append(buffer[max_index]);
  buffer.pop(max_index);
 return result;
 
def display_instruct():
    print("""Welcome to Neutreeko where we put you in an intellectual showdown with my
silicon processor.""");

def ask_yes_no(question):
    response = None;
    while response not in ("y","n"):
        response = input(question.lower());
    return response

def ask_number(question,low,high):
    response = None;
    while response not in range(low,high):
                             response = int(input(question));
                             if response not in range(low,high):
                                 print("Please enter a number from " + str(low) + " through " + str(high) + " inclusive.");
    return response;

def ask_player(question):
    response = None;
    while response not in [1,2]:
        response = int(input(question));
        if response not in [1,2]:
            print("Please enter a valid option.");
    return response;

def ask_coordinates(question,board):
    response = None;
    while response not in board:
        coordinates = input(question);
        if len(coordinates)==2:
            if (coordinates[0] in ["0","1","2","3","4","5","6","7","8","9"])and(coordinates[1] in ["0","1","2","3","4","5","6","7","8","9"]):
              response = [int(coordinates[0]),int(coordinates[1])];
        if response not in board:
            print("There is no piece on the board having those coordinates. Please try again.");
    return response;

def pieces():
 go_first = ask_yes_no("Do you require the first move? (y/n): ");
 if go_first == "y":
  print("\nThen take the first move. You will need it.");
  human = X;
  computer = O;
 else:
  print("\nYour bravery will be your undoing... I will go first.");
  computer = X;
  human = O;
 return computer, human;

def new_board():
    board = [[2,1],[4,1],[3,4],[3,2],[2,5],[4,5]];
    return board;

def display_board(board):
    print(board);
    print("\n");
    led_matrix = [" "]*25;
    for piece in board[:3]:
        led_matrix[5*(piece[1]-1)+piece[0]-1]="X"
    for piece in board[3:]:
        led_matrix[5*(piece[1]-1)+piece[0]-1]="O"
    print("\t|--------------------");
    for i in range(5):
        print("\t|",led_matrix[-5*i+20],"|",led_matrix[-5*i+21],"|",led_matrix[-5*i+22],"|",led_matrix[-5*i+23],"|",led_matrix[-5*i+24],"|");
        print("\t|--------------------");
    print("\n");
    
def legal_moves(board):
    result = {}
    for i in range(6):
        result[i] = [];
    for i in range(6):
     fail = 0;
    #testing for 0
     if not( board[i][0]==5 ):
      for j in board:
       if (j[0]==board[i][0]+1)and(j[1]==board[i][1]):
        fail = 1;
      if not fail:
       result[i].append(0);
     fail = 0; 
    #testing for 1
     if not( (board[i][0]==5)or(board[i][1]==5) ):
      for j in board:
       if (j[0]==board[i][0]+1)and(j[1]==board[i][1]+1):
        fail = 1;
      if not fail:
       result[i].append(1);
     fail = 0;
    #testing for 7
     if not ( (board[i][0]==5)or(board[i][1]==1)):
      for j in board:
       if (j[0]==board[i][0]+1)and(j[1]==board[i][1]-1):
        fail = 1;
      if not fail:
       result[i].append(7);
     fail = 0;
    #testing for 2
     if not( board[i][1]==5 ):
      for j in board:
       if (j[1]==board[i][1]+1)and(j[0]==board[i][0]):
        fail = 1;
      if not fail:
       result[i].append(2);
     fail = 0;
    #testing for 3
     if not( (board[i][0]==1)or(board[i][1]==5) ):
      for j in board:
       if (j[0]==board[i][0]-1)and(j[1]==board[i][1]+1):
        fail = 1;
      if not fail:
       result[i].append(3);
     fail = 0;
    #testing for 4
     if not( board[i][0]==1 ):
      for j in board:
       if (j[0]==board[i][0]-1)and(j[1]==board[i][1]):
        fail = 1;
      if not fail:
       result[i].append(4);
     fail = 0;
    #testing for 5
     if not( (board[i][0]==1)or(board[i][1]==1) ):
      for j in board:
       if (j[0]==board[i][0]-1)and(j[1]==board[i][1]-1):
        fail = 1;
      if not fail:
       result[i].append(5);
     fail = 0;
    #testing for 6
     if not( board[i][1]==1 ):
      for j in board:
       if (j[0]==board[i][0])and(j[1]==board[i][1]-1):
        fail = 1;
      if not fail:
       result[i].append(6);
    return result;

def winner(board):
    x = sort_x(board[:3]);
    o = sort_x(board[3:]);
    #vertical test
    if board[0][0]==board[1][0]==board[2][0]:
        if sort_y(board[:3])[0][1]==sort_y(board[:3])[1][1]+1==sort_y(board[:3])[2][1]+2:
         return "X"
    if board[3][0]==board[4][0]==board[5][0]:
        if sort_y(board[3:])[0][1]==sort_y(board[3:])[1][1]+1==sort_y(board[3:])[2][1]+2:
         return "O"
    #horizontal test
    if board[0][1]==board[1][1]==board[2][1]:
       if x[0][0]==x[1][0]+1==x[2][0]+2: 
        return "X"
    if board[3][1]==board[4][1]==board[5][1]:
       if o[0][0]==o[1][0]+1==o[2][0]+2:   
        return "O"
    #diagonal test
    if ((x[0][0]==x[1][0]+1==x[2][0]+2)and((x[2][1]==x[1][1]+1==x[0][1]+2)or(x[2][1]+2==x[1][1]+1==x[0][1]))):
        return "X"
    if ((o[0][0]==o[1][0]+1==o[2][0]+2)and((o[2][1]==o[1][1]+1==o[0][1]+2)or(o[2][1]+2==o[1][1]+1==o[0][1]))):
        return "O"
    
def human_move(board,human):
    legal = legal_moves(board);
    invalid_move = 1;
    invalid_piece = 1;
    while invalid_piece:
       if human==X: 
        piece = ask_coordinates("Player 1, please enter the coordinates of the piece you wish to move in the format: xy \n",board);
       else:
        piece = ask_coordinates("Player 2, please enter the coordinates of the piece you wish to move in the format: xy \n",board);
       if ((human==X)and(board.index(piece)>2))or((human==O)and(board.index(piece)<2)):
            print("The coordinates you have entered belong to an opponent's piece. Please try again.");
       else:
            if (legal[board.index(piece)]):
                invalid_piece=0;
            else:
                print("The piece you have selected has no legal moves. Please try again.");
    while invalid_move:
        move = ask_number("""In what direction would you like to move that piece?
           0 = RIGHT
           1 = UP-RIGHT
           2 = UP
           3 = UP-LEFT
           4 = LEFT
           5 = DOWN-LEFT
           6 = DOWN
           7 = DOWN-RIGHT
           """,0,8);
        if move not in legal[board.index(piece)]:
            print("The move you have entered is not a legal move. Please try again.");
        else:
            invalid_move=0;
    return piece,move;

def play_move(piece,move,board): #takes in a piece, a move, and a board, and returns the new position of the piece on that board
    piece = piece[:];
    no_conflict = 1;
    if move == 0:
     while no_conflict:
      if piece[0]==5:
       no_conflict = 0;
      else:
       piece[0]+=1; 
       for each_piece in board:
           if (each_piece[0]==piece[0]+1)and(each_piece[1]==piece[1]):
            no_conflict = 0;
    elif move == 1:
     while no_conflict:
      if (piece[0]==5)or(piece[1]==5):
       no_conflict = 0;
      else:
       piece[0]+=1;
       piece[1]+=1;
       for each_piece in board:
           if (each_piece[0]==piece[0]+1)and(each_piece[1]==piece[1]+1):
            no_conflict = 0;
    elif move == 2:
     while no_conflict:
      if (piece[1]==5):
       no_conflict = 0;
      else:
       piece[1]+=1;
       for each_piece in board:
           if (each_piece[0]==piece[0])and(each_piece[1]==piece[1]+1):
            no_conflict = 0;
    elif move == 3:
     while no_conflict:
      if (piece[0]==1)or(piece[1]==5):
       no_conflict = 0;
      else:
       piece[0]-=1;
       piece[1]+=1;
       for each_piece in board:
           if (each_piece[0]==piece[0]-1)and(each_piece[1]==piece[1]+1):
            no_conflict = 0;
    elif move == 4:
     while no_conflict:
      if (piece[0]==1):
       no_conflict = 0;
      else:
       piece[0]-=1;
       for each_piece in board:
           if (each_piece[0]==piece[0]-1)and(each_piece[1]==piece[1]):
            no_conflict = 0;
    elif move == 5:
     while no_conflict:
      if (piece[0]==1)or(piece[1]==1):
       no_conflict = 0;
      else:
       piece[0]-=1;
       piece[1]-=1;
       for each_piece in board:
           if (each_piece[0]==piece[0]-1)and(each_piece[1]==piece[1]-1):
            no_conflict = 0;
    elif move == 6:
     while no_conflict:
      if piece[1]==1:
       no_conflict = 0;
      else:
       piece[1]-=1;
       for each_piece in board:
           if (each_piece[0]==piece[0])and(each_piece[1]==piece[1]-1):
            no_conflict = 0;
    elif move == 7:
     while no_conflict:
      if (piece[0]==5)or(piece[1]==1):
       no_conflict = 0;
      else:
       piece[0]+=1;
       piece[1]-=1;
       for each_piece in board:
           if (each_piece[0]==piece[0]+1)and(each_piece[1]==piece[1]-1):
            no_conflict = 0;
    return piece;

def opening_sequence(board,computer):
 if computer == X:
  if board == [[2, 1], [4, 1], [3, 4], [3, 2], [2, 5], [4, 5]]:
   if random.randint(0,1)==0:
    return [2,1],0
   else:
    return [4,1],4
 else:
  if board == [[3, 1], [4, 1], [3, 4], [3, 2], [2, 5], [4, 5]]:
   return [3,2],0;
  elif board == [[2, 4], [4, 1], [3, 4], [3, 2], [2, 5], [4, 5]]:
   return [4,5],6;
  elif board == [[2, 4], [5, 2], [3, 4], [3, 2], [2, 5], [4, 2]]:
   return [3,2],1;

def random_move(board,computer,legal):
    possible = [];
    if computer==X:
        shift = 0;
    else:
        shift = 3;
    for i in range(0+shift,3+shift):
            if legal[i]:
                for j in legal[i]:
                    possible.append((board[i],j));
    return possible[random.randint(0,len(possible)-1)];

def opponent(player):
    if player==X:
        return O;
    else:
        return X;

def computer_move(board,computer):
 legal = legal_moves(board);
 board = board[:];
 if opening_sequence(board,computer):
     return opening_sequence(board,computer);
 #depth_1
 if offense(board,computer,1,legal):
  return offense(board,computer,1,legal);
 #depth_2
 legal1 = defense(board,computer,1,legal);
 #depth_3
 if offense(board,computer,2,legal1):
  return offense(board,computer,2,legal1);
 #depth_4
 legal2 = defense(board,computer,2,legal1);
 #depth_5
 if offense(board,computer,3,legal2):
  return offense(board,computer,3,legal2);
 #depth_6
 #legal3 = defense(board,computer,3,legal2);
 #if has_legal(legal3,computer):
  #   return random_move(board,computer,legal3);
 if has_legal(legal2,computer):
     return random_move(board,computer,legal2);
 if has_legal(legal1,computer):
     return random_move(board,computer,legal1);
 else:
     return random_move(board,computer,legal);

def has_legal(legal,player):
    if player==X:
        shift = 0;
    else:
        shift = 3;
    for i in range(shift,3+shift):
        if legal[i]:
            return True;
    return False;

def offense(board,player,n,legal):
    if player==X:
        shift = 0;
    else:
        shift = 3;
    #base case
    if n==1:
     for i in range(0+shift,3+shift):
          for j in legal[i]:
           board4 = board[:];
           board4[i]=play_move(board4[i],j,board4)	   
           if winner(board4)==player:
             return board[i],j;
    #recursive case
    else:
     for i in range(0+shift,3+shift):
        for j in legal[i]:
            fail = 0;
            board2 = board[:];
            board2[i]=play_move(board2[i],j,board2)
            legal2 = legal_moves(board2);
            for k in range(3-shift,6-shift):
                for l in legal2[k]:
                    board3 = board2[:];
                    board3[k]=play_move(board3[k],l,board3)
                    if not offense(board3,player,n-1,legal_moves(board3)):
                        fail = 1;
            if not fail:
                return board[i],j

def defense(board,player,n,legal):
 result = copy.deepcopy(legal);
 if player==X:
     shift = 0;
 else:
     shift = 3;
 for i in range(0+shift,3+shift):
     for j in legal[i]:
         board2 = board[:];
         board2[i]=play_move(board2[i],j,board2);
         if offense(board2,opponent(player),n,legal_moves(board2)):          
          result[i].pop(result[i].index(j));
 return result
 
def next_turn(turn):
 if turn == X:
     return O;
 else:
     return X

def main():
 display_instruct();
 player2 = ask_player("""Do you wish to play against the computer, or against another human?
            1 = HUMAN
            2 = COMPUTER \n""");
 if player2==2:           
  computer,human = pieces();
 else:
  human,human2 = X,O;
 turn = X;
 board = new_board();
 display_board(board);

 while not winner(board):
     if turn == human:
         piece,move = human_move(board,human);
         board[board.index(piece)]=play_move(piece,move,board);
     else:
         if player2==2:
          piece,move = computer_move(board,computer);
         else:
          piece,move = human_move(board,human2);
         board[board.index(piece)]=play_move(piece,move,board);
     display_board(board);
     turn = next_turn(turn);
 the_winner = winner(board);
 print(the_winner,"won!\n");

 if (player2==1):
  if the_winner == human2:
      print("Player 2, congratulations!");
  else:
      print("Player 1, congratulations!");
 else:
     if the_winner == computer:
      print("As I predicted human, I am triumphant once more. \n");
     else:
      print("No!No!It cannot be!Somehow you tricked me, human!\n");
 
main();
input("\n\nPress Enter to exit.");



    
      
                           
