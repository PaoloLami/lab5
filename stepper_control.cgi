#!/usr/bin/python37all
import cgi
import stepper

#Get data from html and create file
data = cgi.FieldStorage()

if ('angle' in data):
  with open('angle.txt', 'w') as f:
    f.write(str(angle)) 
elif ('zero' in data):
  with open('angle.txt', 'w') as f: 
    f.write(str(0)) 

print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/stepper_control.cgi" method="POST">')
print('Angle:<br>')
print('<input type="text" name="angle"><br>')
print('<input type="submit" value="Submit"><br>')
print('Reset angle to 0:<br>')
print('<input type="submit" value="zero">')
print('</form>')
print('<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1550885/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&title=Motor+Angle+vs+Time&type=line&xaxis=Time&yaxis=Motor+Angle"></iframe>')
print('<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1550885/widgets/374420"></iframe>')
print('</html>')


