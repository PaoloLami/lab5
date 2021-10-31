#Paolo Lami, ENME441 Lab 5
#!/usr/bin/python37all
import time
import cgi
import stepper

#Get data from html and create file
data = cgi.FieldStorage()
angle = data.getvalue('angle')
submit = data.getvalue('submit')

with open('angle.txt', 'w') as f:
  f.write(str(angle))
  if submit == 'zero':
    stepper.zero()
    f.truncate()

print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/stepper_control.cgi" method="POST">')
print('Angle:<br>')
print('<input type="text" name="angle"><br>')
print('<input type="submit" value="Submit">')
print('Reset angle to 0:<br>')
print('<input type="submit" value="zero">')
print('</form>')
print('<iframe width="400" height="250"
  style="border: 1px solid #cccccc;"
  src="http://api.thingspeak.com/channels/1550885/charts/1
    ?dynamic=true
    &api_key=GA4XGELVZMZ7IXTQ
    &xaxis=Time
    &yaxis=Motor angle (deg)
    &title=Motor Angle vs Time">
</iframe>')
print('<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1550885/widgets/374420"></iframe>')
print('</html>')
