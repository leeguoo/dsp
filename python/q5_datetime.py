# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

from datetime import datetime

starttime = datetime.strptime(date_start, '%m-%d-%Y')
endtime = datetime.strptime(date_stop,'%m-%d-%Y')
print endtime-starttime

####b)  
date_start = '12312013'  
date_stop = '05282015'  

starttime = datetime.strptime(date_start,'%m%d%Y')
endtime = datetime.strptime(date_stop,'%m%d%Y')
print endtime-starttime

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

starttime = datetime.strptime(date_start,'%d-%b-%Y')
endtime = datetime.strptime(date_stop,'%d-%b-%Y')
print endtime-starttime
