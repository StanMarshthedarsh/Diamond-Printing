while True:
    pattern = input("Input the letter, number, or symbol to be used in printing the diamond: ") # Input the character to be printed
    if len(pattern) > 1 or len(pattern) <= 0:
        print("Please input exactly one character") # There should be EXACTLY ONE character
    else:
        break
    
while True:
    try:
        height = int(input("Input the diamond's height: ")) # Get height of each diamond
        if (height % 2) == 0:
            print("Height must be an odd number") # Height must be odd
        elif height < 1:
            print("Please input a valid height") # Height must be 1 or greater
        else:
            break
    except ValueError:
        print("Invalid height, please try again")

while True:
    try:
        overall_width = int(input("Input the number of diamonds to be printed horizontally: ")) # Get width of diamond grid (# of diamonds printed horizontally)
        if overall_width < 1:
            print("Please input a valid number") # Number must be 1 or greater
        else:
            break
    except ValueError:
        print("Invalid number, please try again")

while True:
    try:
        overall_height = int(input("Input the number of diamonds to be printed vertically: ")) # Get height of diamond grid (# of diamonds printed vertically)
        if overall_height < 1:
            print("Please input a valid number") # Number must be 1 or greater
        else:
            break
    except ValueError:
        print("Invalid number, please try again")

x = 1
y = int(((height - 1) / 2))
rowcount = 0
sets = 0

while True:
    for i in range(height): # Iterate until height - 1
        rowcount = rowcount + 1
        for a in range(overall_width): # Size of the overall width

            if i == height - 1 and sets + 1 != overall_height:
                continue

            for j in range(y): # Nested loops          
                print(" ", end="")  
            
            for k in range(x):     
                print(f"{pattern}", end="")  

            for j in range(y): # Nested loops  
                print(" ", end="")
                
        if i != height - 1:
            print("")
       
        if x == height or rowcount > height / 2: # If it reaches the middle or goes past halfway reduce amount of # printed by 2         
            x = x - 2          
        else: 
            x = x + 2    
        if y >= 0 and rowcount < (height / 2): # If y greater than or equal to 0 and number of rows not yet past halfway point, subtract y by 1
            y = y - 1 
        else:
            y = y + 1

    if rowcount == height: # If a set is completed or a diamond of the desired height is printed out overall_width times, repeat the process again in a new line
        sets = sets + 1
        x = 1
        y = int(((height - 1) / 2))
        rowcount = 0
        if sets == overall_height: # If the number of sets is equal to the overall_height, break
            print("")
            break     