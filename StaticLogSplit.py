import time,re,os
from datetime import datetime
 

regexp = re.compile(r'[\D{3}\s\d{2},\s\d{4}\s\d:\d:\d\s\w]')
date_format = "%Y-%m-%d"
 

def get_log_date(log_line):
    match = re.search(r'\D{3}\s\d{2},\s\d{4}',log_line)
    date = datetime.strptime(match.group(),'%b %d, %Y')
    return date
    
def follow(thefile):
  line_counter = ""
  lines_array = []
  line=""
  previous_line=""
  while True:
    
    line = thefile.readline()
    
    if not line:
      
      previous_line=lines_array[-1]
      
      match = re.search(r'\D{3}\s\d{2},\s\d{4}\s\d*:\d*:\d*\s\w{2}',previous_line)
      date = datetime.strptime(match.group(),'%b %d, %Y %I:%M:%S %p')
      print(date.strftime('%Y-%b-%d_%I-%M-%S(%p)'))
      
      log_file_name = '{}/{}/IDL.log.{}'.format(date.year,date.strftime("%b"),date.strftime('%Y-%b-%d_%I-%M-%S(%p)'))
      os.makedirs(os.path.dirname(log_file_name), exist_ok=False)
      with open(log_file_name, mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(lines_array))
      break
      
    regexp = re.compile(r'\D{3}\s\d{2},\s\d{4}\s\d*:\d*:\d*\s\w*]')
    if not regexp.search(line):
      lines_array.append(line)
      continue

 

    if line_counter == "" :
      line_counter=get_log_date(line)
      lines_array.append(line)
      continue
    
    if (line_counter==get_log_date(line)):
      lines_array.append(line) 
    else:
      previous_line=lines_array[-1]
      match = re.search(r'\D{3}\s\d{2},\s\d{4}\s\d*:\d*:\d*\s\w{2}',previous_line)
      date = datetime.strptime(match.group(),'%b %d, %Y %I:%M:%S %p')
      print(date.strftime('%Y-%b-%d_%I-%M-%S(%p)'))
      
      log_file_name = '{}/{}/IDL.log.{}'.format(date.year,date.strftime("%b"),date.strftime('%Y-%b-%d_%I-%M-%S(%p)'))
      os.makedirs(os.path.dirname(log_file_name), exist_ok=True)
      with open(log_file_name, mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(lines_array))
      lines_array = []
      line_counter = None
      line_counter=get_log_date(line)
      lines_array.append(line) 


logfile = open("log")
follow(logfile)