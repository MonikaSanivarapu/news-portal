from django.shortcuts import render
def news_info(request):
    return render(request,'testapp/moni.html')
# Create your views here.
def Movies_info(request):
    head="MOVIES INFORMATION"
    msg1='BRO is a family drama that tells about the relationship between a father and his son, friends, and emotions'
    msg2="If a Disney film can make you laugh and cry, then Mickey and the company have you hooked."
    msg3="OG revolves around a ruthless don named Ojas Gambheera OG who returns to Mumbai following his ten year disappearance, to kill another crime boss, Omi Bhau."
    type = "movies"
    return render (request,'testapp/moni1.html',{'head':head,'msg1':msg1,'msg2':msg2,'msg3':msg3,'type':type})
def Sports_info(request):
    head="SPORTS INFORMATION"
    msg1="Sports helps them improve their self-esteem, social interaction, and a more positive outlook on life."
    msg2=" Develops Life Skills - Playing sports not only helps in developing physical and mental health, but it also develops the life skills of a student."
    msg3="Sports play a major part in improving our physical and mental fitness"
    type="sports"
    return render(request , 'testapp/moni1.html',{'head':head,'msg1':msg1,'msg2':msg2,'msg3':msg3,'type':type})
def Politics_info(request):
    head="POLITICS INFORMATION"
    msg1="Rajni Kothari (1970). Politics in India. Orient Blackswan. ISBN 978-81-250-0072-3 ."
    msg2="Politics of India works within the framework of the country's Constitution."
    msg3="Politics is about making agreements between people so that they can live together in groups such as tribes, cities, or countries."
    type="politics"
    return render(request,'testapp/moni1.html',{'head':head,'msg1':msg1,'msg2':msg2,'msg3':msg3,'type':type})