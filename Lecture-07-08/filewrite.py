#this program writes three lines of data
#to a file
def main():
    #open a file named philosopher.txt
    outfile = open('philosophers.txt','w')

    #Write the names of the three philosophers
    #To the file
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund\n')

    #Close the file
    outfile.close()
main()