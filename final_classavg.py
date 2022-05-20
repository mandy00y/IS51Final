
"""
First, we will have to open the file 'Final.txt' that contains the students' grades.
We will then write a program that displays the number of grades, the average grade, 
and the percentage of grades that are above the average grade.


In order to find the number of grades, 
output the total count of grades in the list.

In order to find the average grade, 
create a loop through the list of grades
add all the grades / total count of grades
then output the average grade.

Then, initiate an iterator (counter), and an accumulator
In order to find the percentage of grades above the average grade,
create loop through the list of grades
add all grades > average grade, 
increment the counter by 1, 
then divide it by total count of grades, and
multiply 100 to get the percentage.

"""


"""
def main(): 

open file "Final.txt"
grades = [line.rstrip()]
close file

create loop
    add all grades / total count of grades
    output average

def calculate_percent_above_average():

initiate an iterator
create a loop
    grade > average grade:
        add / total count of grades
        increment counter by 1
        multiply by 100

print "Number if grades: "
print "Average grade: "
print "Percentage of grades above average: "


main()
"""




def main():
    infile = open("Final.txt", 'r')
    grades = [line.rstrip() for line in infile]
    infile.close()

    for i in range(len(grades)):
        grades [i] = int(grades[i])
    average = sum(grades) / len(grades)

    def calculate_percent_above_average():
        above = 0
        for grade in grades:
            if grade > average:
                above += 1

        print("Number of grades: ", len(grades))
        print("Average grade: ", average)
        print("Percentage of grades above the average: {0:.2f}%".format(100 * above / len(grades)))
    calculate_percent_above_average()

main()