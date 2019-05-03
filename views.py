from django.shortcuts import render
import random
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .froms import Authform, Regform, Movform, Cinform, Schform, Desform
from .models import User, Movie, Admin, Cinema, Hall, Schedule, Ticket, Movdes
from django.forms.models import model_to_dict
def Auth(request):
	if request.method == "POST":
		log = request.POST.get("login")
		pas = request.POST.get("password")
		users = User.objects.all()
		admins = Admin.objects.all()
		for us in users:
			if us.log == log and us.pas == pas:
				request.session['cur'] = model_to_dict(us)
				return HttpResponseRedirect('user/')
		for ad in admins:
			if ad.log == log and ad.pas == pas:
				request.session['cur'] = model_to_dict(ad)
				return HttpResponseRedirect('admin/')
		return HttpResponseNotFound("<h2>Such User Not Found</h2>")
	forma = Authform()
	return render(request, 'index.html', {"form": forma})
def Reg(request):
	forma = Regform()
	if request.method == "POST":
		new = User()
		new.log = request.POST.get("log")
		new.pas = request.POST.get("pas")
		new.nam = request.POST.get("nam")
		new.sur = request.POST.get("sur")
		new.fac = request.POST.get("fac")
		new.age = int(request.POST.get("age"))
		new.save()
		return HttpResponseRedirect('/')
	return render(request, 'reg2.html', {"form": forma})
def getMov(request):
	list = Movie.objects.all()
	return render(request, 'movie.html', {'list': list})
def getSch(request):
	list = Schedule.objects.all()
	return render(request, 'schedule.html', {'list': list})
def getTic(request):
	list = Ticket.objects.all()
	return render(request, 'tickets.html', {'list': list})
def addMov(request):
	form = Movform()
	if request.method == "POST":
		new = Movie()
		new.nam = request.POST.get("nam")
		new.lim = request.POST.get("lim")
		new.dur = request.POST.get("dur")
		new.save()
		newd = Movdes()
		newd.fil = new
		newd.path = request.POST.get("path")
		newd.desc = request.POST.get("desc")
		newd.tag = request.POST.get("tag")
		newd.save()
		return HttpResponseRedirect('/admin')
	return render(request, 'addmov.html', {"form": form})
def addcin(request):
	form = Cinform()
	n = 1
	if request.method == "POST":
		new = Cinema()
		new.nam = request.POST.get("nam")
		new.add = request.POST.get("add")
		new.pho = request.POST.get("pho")
		new.save()
		num = 1
		halla = request.POST.get('sea'+str(num))
		while halla:
			newh = Hall()
			newh.num = num
			newh.sea = halla
			newh.cin = new
			newh.save()
			num = num + 1
			halla = request.POST.get('sea'+str(num))
		return HttpResponseRedirect('/admin')
	return render(request, 'addcin.html', {"form": form, 'num': n})
def addsch(request):
	form = Schform()
	clist = Cinema.objects.all()
	mlist = Movie.objects.all()
	hlist = Hall.objects.all()
	if request.method == "POST":
		news = Schedule()
		news.beg = request.POST.get("beg")
		news.end = request.POST.get("end")
		news.pri = request.POST.get("pri")
		news.fil = Movie.objects.get(id=int(request.POST.get("mov")))
		news.hal = Hall.objects.get(id=int(request.POST.get("hal")))
		news.save()
		for gh in range(news.hal.sea):
			newt = Ticket()
			if request.POST.get('che')==None:
				newt.ocu = False
				newt.hol = User.objects.get(id=1)
			else:
				zin = random.randint(0, 1)
				if zin == 1:
					newt.ocu = True
					newt.hol = User.objects.get(id=3)
				else:
					newt.ocu = False
					newt.hol = User.objects.get(id=1)
			newt.sea = gh+1
			newt.sch = news
			newt.save()
		return HttpResponseRedirect('/admin') 
	return render(request, 'addsch.html', {"form": form, 'clist': clist, 'mlist': mlist, 'hlist': hlist})
def viewM(request):
	mlist = Movie.objects.all()
	newd = Movdes()
	return render(request, 'viewM.html', {'mlist': mlist})
def viewS(request):
	slist = Schedule.objects.all()
	return render(request, 'viewS.html', {'slist': slist})
def viewT(request):
	tlist = Ticket.objects.all()
	return render(request, 'viewT.html', {'tlist': tlist})
def viewB(request):
	cur = User.objects.get(id=request.session.get('cur')['id'])
	blist = Ticket.objects.filter(hol=cur, ocu=True)
	return render(request, 'viewB.html', {'blist': blist})
def viewC(request):
	clist = Cinema.objects.all()
	hlist = Hall.objects.all()
	return render(request, 'viewC.html', {'clist': clist, 'hlist': hlist})
def admin(request):
	ad = Admin.objects.get(id=request.session.get('cur')['id'], log=request.session.get('cur')['log'], pas=request.session.get('cur')['pas'])
	if request.method == "POST":
		del request.session['cur']
		return HttpResponseRedirect('/')
	return render(request, 'admin.html', {'ad': ad})
def user(request):
	us = User.objects.get(id=request.session.get('cur')['id'], log=request.session.get('cur')['log'], pas=request.session.get('cur')['pas'])
	if request.method == "POST":
		del request.session['cur']
		return HttpResponseRedirect('/')
	return render(request, 'user.html', {'us': us})
def profA(request):
	cur = Admin.objects.get(id=request.session.get('cur')['id'])
	return render(request, 'prof.html', {'cur': cur})
def profU(request):
	cur = User.objects.get(id=request.session.get('cur')['id'])
	return render(request, 'profU.html', {'cur': cur})
def buyT(request):
	cur = User.objects.get(id=request.session.get('cur')['id'])
	tlist = Ticket.objects.all()
	zipo = list()
	dlist = Movdes.objects.all()
	if request.method == "POST":
		return HttpResponse("<h1>zero</h1>")
	for re in tlist:
		if re.ocu==False and re.sch not in zipo:
			zipo.append(re.sch)
	return render(request, 'buyT.html', {"cur": cur, "tlist": tlist, "zipo": zipo, "dlist": dlist})
def find(request):
	cur = User.objects.get(id=request.session.get('cur')['id'])
	ids = request.GET.get('sch')
	ob = Schedule.objects.get(id=str(ids))
	moj = Movdes.objects.get(fil=ob.fil)
	tlist = Ticket.objects.filter(sch=ob)
	if request.method=="POST":
		num = int(tlist[0].id)
		halla = request.POST.get(str(num))
		while halla:
			if int(halla)==1:
				sir = Ticket.objects.get(id = num)
				sir.hol = cur
				sir.ocu = True
				sir.save()
			num = num + 1
			halla = request.POST.get(str(num))
		return HttpResponseRedirect('/user')
	return render(request, 'findz.html', {'ob': ob, 'tlist': tlist, 'moj': moj})