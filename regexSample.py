import os
import re
import keyboard
# import shutil


# Changing working directory
currentDirectory = os.path.dirname(__file__)

# Define file here , preferably in same folder as script
datafile = os.path.join(currentDirectory, "regexpractise.txt")
outputFile = os.path.join(currentDirectory, "OutputResultData.txt")
phoneNumbers = []
basicWebsites = []
emails = []
generalWebsites = []

print("""Regex Extraction on sample data
provided though external file.
================================== \n""")
print("Current working directory: \n{} \n".format(os.getcwd()))
print("Suppied DataFile: {} \n".format(datafile))
print("===Results=== \n")
# print("regex sample exits: ", os.path.exists("regexpractise.txt"))
# print("regex sample isfile: ", os.path.isfile("regexpractise.txt"))
# print("All files in current dir", os.listdir())
# print("Make backup of regexpractise", shutil.copy(
#     "regexpractise.txt", "regexpractiseBCKP.txt"))


# Open file and store all data in variable
with open(datafile, "r") as regexpractise:
    regexSampleData = regexpractise.read()

# Regex core body


def RegexOperations():
    # Regex for finding 10 digit phone number
    basicPhoneFormat = re.compile(r"\d{10}")
    phoneResults = basicPhoneFormat.findall(regexSampleData)
    # Store each result in global storage
    for items in phoneResults:
        phoneNumbers.append(str(items+"\n"))
    print(f"\nPhone numbers found:\n {phoneResults}")

    # Regex for 3 characters then dot then any characters then dot
    # and then 2 or 3 ending characters only
    basicWebsiteFormat = re.compile(r"w{3}\.\w*\.\w{2,3}")
    basicWebsiteResults = basicWebsiteFormat.findall(regexSampleData)
    # Store each result in global storage
    for items in basicWebsiteResults:
        basicWebsites.append(str(items+"\n"))
    print(f"\nComplete website adresses:\n {basicWebsiteResults}")

    # Regex for 3 or more characters then dot then 2-3 ending characters
    generalWebsiteFormat = re.compile(r"\w{4,}\.\w{2,3}")
    generalWebsiteResults = generalWebsiteFormat.findall(regexSampleData)
    # Store each result in global storage
    for items in generalWebsiteResults:
        generalWebsites.append(str(items+"\n"))
    print(f"\nGeneral website adresses:\n {generalWebsiteResults}")

    # Regex for any email, it should start with atleast a word
    # then upto @ it can be anything and then
    # any domain with a 2-3 word ending
    emailFormat = re.compile(r"\w{2,}.*@\w*.\w{2,3}")
    emailResults = emailFormat.findall(regexSampleData)
    # Store each result in global storage
    for items in emailResults:
        emails.append(str(items+"\n"))
    print(f"\nEmail adresses:\n {emailResults}")


RegexOperations()

regexpractise.close()

# Create Output file
try:
    open(outputFile, "x")

    print("\nOutput File created.\n")
except Exception as e:
    pass
    # print("\nTrying to create output file-\n", e)

# Write the regex results data to output File
# Open file as write mode
outputFile = open(outputFile, "a")
# clear the file before inputting
outputFile.truncate(0)
# Writing data


def WriteToOutputFile():
    outputFile.write("\nPhone numbers found:\n")
    for elements in phoneNumbers:
        outputFile.write(str(elements))
    outputFile.write("\nComplete website addresses:\n")
    for elements in basicWebsites:
        outputFile.write(str(elements))
    outputFile.write("\nGeneral website addresses:\n")
    for elements in generalWebsites:
        outputFile.write(str(elements))
    outputFile.write("\nEmail addresses:\n")
    for elements in emails:
        outputFile.write(str(elements))
    print("\nWritten all data to Output file.\n")


WriteToOutputFile()

outputFile.close()

while True:
    if(keyboard.is_pressed("esc")):
        break
# Complete website addresses:\n{}\n

# General website addresses:\n{}\n
# Email addresses:\n{}\n
# .format(phoneResults,basicWebsiteResults,generalWebsiteResults, emailResults))
