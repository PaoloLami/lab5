#Paolo Lami, ENME441 Lab 5
#!/usr/bin/python37all
import time
import cgi
import stepper

#Get data from html and create file
data = cgi.FieldStorage()
angle = data.getvalue('angle')
submit = data.getvalue('submit')

with open('angle.txt', 'w') as f: #writes in file
  f.write(str(angle))
  if submit == 'zero':
    stepper.zero()
    f.truncate()

print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/stepper_control.cgi" method="POST">')
print('Angle:<br>')
print('<input type="text" name="angle"><br>')
print('<input type="submit" value="Submit">\n')
print('Reset angle to 0:<br>')
print('<input type="submit" value="zero">')
print('</form>')
print('<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1550885/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&title=Motor+Angle+vs+Time&type=line&xaxis=Time&yaxis=Motor+Angle"></iframe>')
print('<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1550885/widgets/374420"></iframe>')
print('</html>')
