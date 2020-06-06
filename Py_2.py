import datetime
import uuid

print ("Python 2")
x = datetime.datetime.now()
print (x.day)
print (x.weekday())
print (x.date())
print (x.strftime("%A"))
test = uuid.uuid4()
print (test)
print ("EndOfProgram_ServerSideEdit")