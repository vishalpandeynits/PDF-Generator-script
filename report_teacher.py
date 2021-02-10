### Python Script to generate PDF for course allocatement project for faculties
### and HODs of the all departments of NIT Silchar
## Written during learning reportlab

## Author: Vishal Pandey
## Date : 10/02/2021


from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime

core_course = [
    ('Preference 1','UG','1st','Microprocessor and Microcontroller'),
    ('Preference 2','UG','3rd','Microprocessor and Microcontroller'),
    ('Preference 3','UG','4th','Microprocessor and Microcontroller'),
]
elective_courses = [
    ('Preference 1','UG','1st','Microprocessor and Microcontroller'),
    ('Preference 2','UG','3rd','Microprocessor and Microcontroller'),
    ('Preference 3','UG','4th','Microprocessor and Microcontroller'),
]

page = canvas.Canvas("1.pdf")

page.setFont('Helvetica', 11)
page.drawString(0.6*inch,10.8*inch,'Name: Vishal Pandey')
page.drawString(0.6*inch,10.6*inch,'Email: vishalpandeyviptsk@gmail.com')
page.drawString(0.6*inch,10.4*inch,'Department: Compputer Science and Engineering.')
page.drawString(0.6*inch,10.2*inch,'Datetime: '+datetime.now().strftime('%d %b %Y %H:%M %p'))

page.drawInlineImage('https://upload.wikimedia.org/wikipedia/en/c/c6/NIT_Silchar_logo.png',6.4*inch,10*inch, width=100,height=100)

page.setFont('Helvetica', 22)
page.line(0.5*inch,10*inch,8*inch,10*inch)
page.drawString(3*inch,9.5*inch,"PREFERENCES")

page.drawCentredString(4*inch,8.9*inch,"Core Courses")
t=Table(core_course)
t.setStyle(TableStyle([
    ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
    ('BOX', (0,0), (-1,-1), 0.25, colors.black),
    ('LEFTPADDING', (0,0), (-1,-1), 0.1*inch),
    ('RIGHTPADDING', (0,0), (-1,-1), 0.1*inch),
    ('TOPPADDING', (0,0), (-1,-1), 0.1*inch),
    ('BOTTOMPADDING', (0,0), (-1,-1), 0.1*inch),
    ('FONTSIZE', (0,0), (-1,-1), 14),
]))
page.setFont('Helvetica', 18)
t.wrapOn(page, 1.3*inch, 7.5*inch)
t.drawOn(page, 1.3*inch, 7.5*inch)

page.drawCentredString(4*inch,6.9*inch,"Elective Courses")
x = Table(elective_courses)
x.setStyle(TableStyle([
    ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
    ('BOX', (0,0), (-1,-1), 0.25, colors.black),
    ('LEFTPADDING', (0,0), (-1,-1), 0.1*inch),
    ('RIGHTPADDING', (0,0), (-1,-1), 0.1*inch),
    ('TOPPADDING', (0,0), (-1,-1), 0.1*inch),
    ('BOTTOMPADDING', (0,0), (-1,-1), 0.1*inch),
    ('FONTSIZE', (0,0), (-1,-1), 14),
]))
x.wrapOn(page,1.3*inch, 5.5*inch)
x.drawOn(page,1.3*inch, 5.5*inch)

page.showPage()
page.save()

### FINISH 

## ABSOLUTE POSITIONING IS PAIN