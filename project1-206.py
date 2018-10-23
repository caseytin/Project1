import os
import filecmp
from dateutil.relativedelta import *
from datetime import date

def getData(file):
# get a list of dictionary objects from the file
#Input: file name
#Output: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows
	inFile = open(file, "r")
	lines = inFile.readlines()
	inFile.close()

	dictList = []

	#Separate first row into dict
	dict_keys = lines[0].split(',') 
	first_key = dict_keys[0]
	last_key = dict_keys[1]
	email_key = dict_keys[2]
	class_key = dict_keys[3]
	dob_key = dict_keys[4].rstrip('\n')

	for line in lines[1:]:
		newDict = {}
		values= line.split(',') 
		newDict[first_key] = values[0] 
		newDict[last_key] = values[1]
		newDict[email_key] = values[2]
		newDict[class_key] = values[3]
		newDict[dob_key] = values[4]

		dictList.append(newDict)
	return dictList

def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName
	top_dict = sorted(data, key=lambda x:x[col], reverse=True)
	for item in top_dict:
		firstName = item['First']
		lastName = item['Last']
	output = firstName + " " + lastName
	return output

def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	classDict = {}
	senior_count = 0
	junior_count = 0
	sophomore_count = 0
	freshman_count = 0
	for dct in data:
		class_standing = dct['Class']
		if (class_standing == 'Senior'):
			senior_count += 1
		elif (class_standing == 'Junior'):
			junior_count += 1
		elif (class_standing == 'Sophomore'):
			sophomore_count += 1
		elif (class_standing == 'Freshman'):
			freshman_count += 1
	classDict['Senior'] = senior_count
	classDict['Junior'] = junior_count
	classDict['Sophomore'] = sophomore_count
	classDict['Freshman'] = freshman_count

	sortedList = sorted(classDict.items(), key=lambda x:x[1], reverse=True)
	return(sortedList)

def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data
	monthsDict = {}
	for dct in a:
		date_of_birth = dct['DOB']
		month = date_of_birth[:2].rstrip('/')
		if month in monthsDict:
			monthsDict[month] += 1
		else:
			monthsDict[month] = 1
	sortedList = sorted(monthsDict.items(), key=lambda x:x[1], reverse=True)
	common_month = sortedList[0]
	#print(common_month)
	return int(common_month[0])

def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written
	outFile = open(fileName, 'w')
	top_dict = sorted(a, key=lambda x:x[col])
	for item in top_dict:
		firstName = item['First']
		lastName = item['Last']
		email = item['Email']
		results = "{},{},{}\n".format(firstName, lastName, email)
		outFile.write(results)
	outFile.close()

#Extra credit - 10 pts
def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.
	pass


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)
	
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)
	
	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	
	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)
	

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
