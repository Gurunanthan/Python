from datetime import datetime

currTime = datetime.now()
formatted_currTime = currTime.strftime("%y-%m-%d %H:%M:%S")
print( formatted_currTime)
