

width = int(input()) #This must be an odd number
c = 'H'
#Top Cone
for i in range(width):
    print((c*i).rjust(width-1)+c+(c*i).ljust(width-1))

#Top Pillars
for i in range(width+1):
    print((c*width).center(width*2)+(c*width).center(width*6))

#Middle Belt
for i in range((width+1)//2):
    print((c*width*5).center(width*6))    

#Bottom Pillars
for i in range(width+1):
    print((c*width).center(width*2)+(c*width).center(width*6))    

#Bottom Cone
for i in range(width):
    print(((c*(width-i-1)).rjust(width)+c+(c*(width-i-1)).ljust(width)).rjust(width*6))