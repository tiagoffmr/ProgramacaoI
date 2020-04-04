# 2017-2018 Programacao 1 (LTI)
# Grupo 
# 49983 Francisco Garcia
# 51628 Tiago Robalo

import constants

def read_operators_file(file_name):
        """Read a file with requests into a collection.
        Requires: file_name, str with the name of a text file with a list of operators.
        Ensures: list, with the operators in the file; each operator is a tuple with the various element
        concerning that operator, in the order provided in the file.
        """
        in_file = open(file_name, 'r')
        
        for i in range(constants.HEADER_TOTAL_LINES):  # read some lines to skip the header
                in_file.readline()
            
        operators = []
        
        for line in in_file:
                name, language, domain, last_call, mins_done = line.strip().split(', ')
                mins_done = int(mins_done)
                operators.append((name, language, domain, last_call, mins_done))
        in_file.close()

        return operators


def read_requests_file(file_name):
        """Read a file with requests into a collection.

        Requires: file_name, str with the name of a text file with a list of requests.
        Ensures: list, with the requests in the file; each request is a tuple with the various element 
        concerning that request, in the order provided in the file.
        """
        in_file = open(file_name, 'r')
        
        for i in range(constants.HEADER_TOTAL_LINES):  # read some lines to skip the header
                in_file.readline()
            
        requests = []
        
        for line in in_file:
                name, language, domain, service, duration = line.strip().split(', ')
                duration = int(duration)
                requests.append((name, language, domain, service, duration))
            
        in_file.close()

        return requests

def readDate(file_name):
        in_file = open(file_name, 'r')
        lines = in_file.readlines()
        lines = list(map(lambda i: i.rstrip(), lines))
        return lines[constants.HEADER_LINE2]

def readTime(file_name):
        in_file = open(file_name, 'r')
        lines = in_file.readlines()
        lines = list(map(lambda i: i.rstrip(), lines))
        return lines[constants.HEADER_LINE4]

def readHeader(file_name):
        in_file = open(file_name, 'r')
        lines = in_file.readlines()
        return lines[:constants.HEADER_TOTAL_LINES]
        
