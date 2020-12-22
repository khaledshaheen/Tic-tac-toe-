#Done by: Khaled Shaheen
#add X or O to the Matrix
class XOexception(Exception):
    def __init__(self):
        print("Please Enter an X or an O!")
#adds the user input in the correct postion in the matrix
def adduserinput(board):
    print("WELCOME TO TIC-TAC-Toe!")
    for x in range(10):
        userChar=input("Enter 'X' or 'O' :").upper()
        # raise an exception if the user entered anything other than X or O
        if userChar!="X" and userChar!="O":
            raise XOexception
        else:
            print(board[0],"\n",board[1],"\n",board[2])
            # take the place of X or O
            place=input("Enter place: ")
            # check if the user entered a numeric place
            if place.isnumeric():
                place=int(place)
                #converting user place input to the correct postion in the matrix
                if place==1:
                    board[0][0]=userChar
                elif place==2:
                    board[0][1]=userChar
                elif place==3:
                    board[0][2]=userChar
                elif place==4:
                    board[1][0]=userChar
                elif place==5:
                    board[1][1]=userChar
                elif place==6:
                    board[1][2]=userChar
                elif place==7:
                    board[2][0]=userChar
                elif place==8:
                    board[2][1]=userChar
                elif place==9:
                    board[2][2]=userChar
                print(board[0],"\n",board[1],"\n",board[2])
            # if the user input is not numeric break!
            else:
                print("Enter a number not a Letter!")
                break
       
        
      
# returns the winner when the board is complete
def Getthewinner(board): 
    
    if board[2][0] == board[2][1] == board[2][2] != ' ':#check row
        print("Winner is: ",board[2][0]) #
    elif board[1][0] == board[1][1] == board[1][2] != ' ':#check row
        print("Winner is: ",board[1][0]) #
    elif board[0][0] == board[0][1] == board[0][2] != ' ':#check row 
        print("Winner is: ", board[0][0])  
    elif board[0][0] == board[1][0] == board[2][0] != ' ': #check column
        print("Winner is: ",board[1][0])#      
    elif board[0][1] == board[1][1] == board[2][1] != ' ': #check column
        print("Winner is: ",board[0][1])        
    elif board[0][2] == board[1][2] == board[2][2] != ' ':#check column
        print("Winner is: ",board[0][2])#       
    elif board[0][0] == board[1][1] == board[2][2] != ' ': #check diagonally
        print("Winner is: ",board[0][0])#        
    elif board[0][2] == board[1][1] == board[2][0] != ' ': #check diagonally
        print("Winner is: ",board[1][1])       
    else:
        print("TIE! GAME OVER")

def main():
    
    board=[]
    #construct a matrix 
    board.append([1,2,3])
    board.append([4,5,6])
    board.append([7,8,9])
    # to avoid allowing the user to enter a letter other than X or O
    try:
        adduserinput(board)
        Getthewinner(board)
    except XOexception:
        print("enter X or O")
         
main()
   
            

        
     
     

    


    