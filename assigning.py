# 2017-2018 Programacao 1 (LTI)
# Grupo 
# 49983 Francisco Garcia
# 51628 Tiago Robalo

import filesReading
import constants

from copy import *
from dateTime import *

current_time = '15:00'

def finder(request, ops):
    """
    """
    #constants
    #language
    req_language = constants.REQ_INDEX_LANGUAGE
    op_language = constants.OP_INDEX_LANGUAGE

    #domain
    req_domain = constants.REQ_INDEX_DOMAIN
    op_domain = constants.OP_INDEX_DOMAIN

    #duration
    req_duration = constants.REQ_INDEX_DURATION
    op_mins = constants.OP_INDEX_DURATION

    #available time
    op_available_time = constants.OP_INDEX_AVAILABLE_TIME

    #variables
    check = False
    index = 0
    
    while not check and index < len(ops):
        if request[req_language] == ops[index][op_language] and request[req_domain] in ops[index][op_domain] and request[req_duration] + ops[index][op_mins] <= 240:

            # add duration of the request to the operator's accumulated minutes
            ops[index][op_mins] += request[req_duration]

            #add the request's duration to the operator's available time
            ops[index][op_available_time] = add_minutes(ops[index][op_available_time], request[req_duration])

            check = True
            
            # deepcopy so that the values of the operators added minutes is equal to
            # the sum of the operator's current accumulated minutes and the request's duration
            assigned_request = deepcopy([request, ops[index]])
            
        index += 1

    if not check:
        assigned_request = deepcopy([request, 'not assigned'])

    return assigned_request


def assign_tasks(operators, requests, current_time):
    """Assign operators to pending requests.

    Requires:
    - operators, a collection of operators, structured as the output of 
      filesReading.read_operators_file;
    - requests, a list of requests, structured as the output of filesReading.read_requests_file;
    - current_time, str with the HH:MM representation of the time for this update step.
    Ensures: a list of assignments of operators to requests, according to the conditions indicated 
    in the general specification (omitted here for the sake of readability).
    """

    #constants
    op_available_time = constants.OP_INDEX_AVAILABLE_TIME
    req_service = constants.REQ_SERVICE

    #turn list of tuples to list of lists
    lst_operators = [list(item) for item in operators]
    lst_requests = [list(item) for item in requests]

    #sort operators by availability
    lst_operators = sorted(lst_operators, key=lambda i: (i[op_available_time], i[0]))

    #sort requests by service
    lst_requests = sorted(lst_requests, key=lambda i: i[req_service], reverse=True)

    #assigning requests
    assigned_requests = []
    
    for item in lst_requests:
            assigned_requests.append(finder(item, lst_operators))
    
    return assigned_requests, sorted(lst_operators, key=lambda i: (i[op_available_time], i[0]))
