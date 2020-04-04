# 2017-2018 Programacao 1 (LTI)
# Grupo 
# 49983 Francisco Garcia
# 51628 Tiago Robalo

import assigning
import filesReading
import filesWriting

from sys import argv

current_time = '15:00'

filesWriting.write_assignments_file(assigning.assign_tasks(filesReading.read_operators_file(argv[1]), filesReading.read_requests_file(argv[2]), current_time)[0], filesReading.readHeader(argv[2]), argv[2])
filesWriting.write_operators_file(assigning.assign_tasks(filesReading.read_operators_file(argv[1]), filesReading.read_requests_file(argv[2]), current_time)[1], filesReading.readHeader(argv[1]), argv[1])
