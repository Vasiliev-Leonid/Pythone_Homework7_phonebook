
from os.path import exists
from download import creating_contact
from data_writen import writing_scv
from data_writen import writing_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating_contact()

writing_scv()
writing_txt()
