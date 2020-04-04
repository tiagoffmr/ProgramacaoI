# 2017-2018 Programação 1 (LTI)
# Grupo 943
# 55123 Belarmina Crisálida
# 55456 Idalécio Vicentino

from dateTime import *
from constants import *
from assigning import *
from filesReading import *
from sys import argv

def write_operators_file(operators, header, file_name):
	new_file = open(('operators'+ add_minutes(readTime(file_name),5).replace(':', 'h') + '.txt'), "w")
	
	header[1] = readDate(file_name) + '\n'
	header[3] = add_minutes(readTime(file_name),5) + '\n'
	
	for line in header:
		new_file.write(str(line))
		
	for item in operators:
                if not item[-1] >= 240:
                        new_file.write(', '.join(str(i) for i in item) + '\n')
		
	new_file.close()
	
def write_assignments_file(assignments, header, file_name):
	#constants
	op_available_time = constants.OP_INDEX_AVAILABLE_TIME
		
	new_file = open(('timetable'+ add_minutes(readTime(file_name),5).replace(':', 'h') + '.txt'), "w")
	
	header[1] = readDate(file_name) + '\n'
	header[3] = add_minutes(readTime(file_name),5) + '\n'
	header[-1] = 'Timetable:\n'
	
	for line in header:
		new_file.write(str(line))
		
	for item in assignments:
		sorted(item, key=lambda i: (i[op_available_time], i[0]))
		
		if 'not assigned' in item:
			new_file.write(str(readTime(file_name)) + ', ' + ', ' + item[0][0] + str('not assigned') + '\n')
		else:     
			new_file.write(str(item[1][-2]) + ', ' + str(item[0][0]) + ', ' + str(item[1][0]) + '\n')
			
	new_file.close()

