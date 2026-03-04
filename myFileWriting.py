myfile = open('info.txt', 'w')
for i in range(0,5):
    nameinput = input('Input Name')
    postcodeinput = input('Input Postcode ')
    teleinput = input('Input Telephone No.  ')
    myfile.write(str(nameinput) + ' ' + str(postcodeinput) + ' ' + str(teleinput) + '\n'  )
myfile.close()
