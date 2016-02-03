#Greeting
print """Welcome to the Load File Splitter. 
Please run in the same directory as the load file and expected outputs."""

while True:
    try:
        #Requests name of file to split.
        filename = raw_input("What is the full file name of the load file, including extension?\n")
        #Counts the number of lines in the prompted file
        num_lines = sum(1 for line in open(filename))
        break
    except:
        pass
    print "Please ensure the load file and script are in the same directory."

#Prints the number of lines in the target file.
print "There are %r lines in %r." % (num_lines,filename)
#Requests the number of lines per split file (must be integer).
while True:
    try:
        requested_linecount = int(raw_input("How many non-header lines would you like per file?\n"))
        #If the input does not return an error when converting to int, break the loop.
        break
    except:
        #If the input is not an int, retry input.
        pass
    #Let the user know what went wrong, before prompting for new input.
    print "\nPlease enter a valid integer (no decimals or characters)."

#Calculates the minimum number of files
num_files = (int(num_lines) - 1 ) / int(requested_linecount)
#Calculates any remainder
num_remainder = (int(num_lines) - 1 ) % int(requested_linecount)

#Confirmation of the number of files/remainder.
if num_remainder == 0:
    print 'This script will create %s files with %s non-header lines.' % (num_files,requested_linecount)
else:
    num_files += 1
    #Changes grammar of print line based on how many documents in last file.
    if num_remainder == 1:
        remainder_sufix = ""
    else:
        remainder_sufix = "s"
    print 'This script will create %s files with %s non-header lines, and 1 file with %s line%s.' % (num_files - 1,requested_linecount,num_remainder,remainder_sufix)

#Requests a prefix for each new file.
out_prefix = raw_input("What prefix would you like for the new files?\n")
#Requests a file extension for each new file.
while True:
    requested_extension = raw_input("What extension would you like for the files? No period necessary.\n")
    #Verifies that the extension is 3 or 4 characters long, else requests new input.
    if 3 <= len(requested_extension) <= 4:
        break
    #Alerts user as to reason for asking for new input.
    print "File extension should be 3-4 characters, without punctuation."

#Opens the target text file and reads the lines.
lines = open(filename).readlines()

#Saves the load file header as a variable and prints confirmation.
header = lines[0]
print "The header row is:\n%s" % lines[0],

#New function to copy a flexible number of lines per file.
def line_copy(lines_to_copy):
    for line_counter in range(lines_to_copy):
        file_lines = lines[((out_sufix - 1) * int(requested_linecount)) + line_counter +1]
        #Writes the current line to the new file.
        out_file.write(file_lines)

#Primary loop creates each new file.
for out_sufix in range(1,num_files+1):
    #Creates a new file based on user's prefix and interated sufix with write permissions.
    out_file = open(out_prefix + str(out_sufix) + '.' + requested_extension, 'w')
    #Writes the load file header to the new file.
    out_file.write(header)
    #Uses the new function, copies the requested number of non-header lines in most cases.
    if out_sufix < num_files or (num_remainder == 0 and out_sufix == num_files):
        line_copy(int(requested_linecount))
    #Copies the remainder of non-header lines for non-evenly split files.
    elif out_sufix == num_files:
        line_copy(int(num_remainder))
    #Closes the finished new file.
    out_file.close()

print "You have successfully created %s new files." % num_files