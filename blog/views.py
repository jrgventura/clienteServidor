from django.shortcuts import render_to_response
from forms import PostForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here.

def post_list(request):
	#posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # Connect
	import pymssql
	conn = pymssql.connect(server='servidor12.database.windows.net', user='chuchurro@servidor12', password='Pa$$w0rd', database='Planilla')
	cursor = conn.cursor()
	result = ""
	#Select
	#cursor.execute('SELECT IDTRABAJADOR,APELLIDOS,NOMBRES FROM TRABAJADOR;')

	#cursor.execute ('select mes from MESproceso;')


	#cursor.execute('SELECT * FROM PLANILLA;')
	cursor.execute('select tra.idTrabajador, tra.Apellidos, tra.Nombres, afp.descripcion, pla.idMes, pla.diasFalta,pla.horasfalta, pla.totalingresos, pla.totalingresos from planilla as pla  inner join Trabajador as tra  on pla.idTrabajador = tra.idTrabajador  inner join Afp as afp on pla.idAfp = afp.idAfp;')

	row = cursor.fetchone()
	while row:
	 	#print str(row[0]) + " " + str(row[1]) + " " + str(row[2])   
	 	#row = cursor.fetchone()
	     result += str(row[0]) + "  " + str(row[1]) + " " + str(row[2]) + " " + str(row[3])
	     result += str("\n")
	     row = cursor.fetchone()
	 #print result
	return render(request, 'blog/post_list.html', {'result': result})

	#ret = cursor.callproc("dbo._CalcularPlanillaPagos_G3_s2", (5))
	#cursor.execute('SELECT * FROM PLANILLA;')

	#cursor.close()
     #   return ret


def fecha_list(request):
	import pymssql
	conn = pymssql.connect(server='servidor12.database.windows.net', user='chuchurro@servidor12', password='Pa$$w0rd', database='Planilla')
	cursor = conn.cursor()
	result = ""

	cursor.execute ('select mes from mesproceso;')

	row = cursor.fetchone()
	while row:
	 	#print str(row[0]) + " " + str(row[1]) + " " + str(row[2])   
	 	#row = cursor.fetchone()
	     result += str(row[0])
	     result += str("\n")
	     row = cursor.fetchone()
	 #print result
	return render(request, 'blog/post_list.html', {'result': result})


def crear(request):
    if request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = PostForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('crear_articulo.html', args)


def listar_datos_completos (request):
	import pymssql
	conn = pymssql.connect(server='servidor12.database.windows.net', user='chuchurro@servidor12', password='Pa$$w0rd', database='Planilla')
	cursor = conn.cursor()
	result = ""
	#Select
	#cursor.execute('SELECT IDTRABAJADOR,APELLIDOS,NOMBRES FROM TRABAJADOR;')

	#cursor.execute ('select mes from MESproceso;')


	cursor.execute('select tra.idTrabajador, tra.Apellidos, tra.Nombres, afp.descripcion, pla.idMes, pla.diasFalta,pla.horasfalta, pla.totalingresos, pla.totalingresos from planilla as pla  inner join Trabajador as tra  on pla.idTrabajador = tra.idTrabajador  inner join Afp as afp on pla.idAfp = afp.idAfp;')
	row = cursor.fetchone()
	while row:
	 	#print str(row[0]) + " " + str(row[1]) + " " + str(row[2])   
	 	#row = cursor.fetchone()
	     result += str(row[0]) + "  " + str(row[1]) + " " + str(row[2]) + " " + str(row[3])
	     result += str("\n")
	     row = cursor.fetchone()
	 #print result
	return render(request, 'blog/post_list.html', {'result': result})

	

# import pymssql
# conn = pymssql.connect(server='servidor12.database.windows.net', user='chuchurro@servidor12', password='Pa$$w0rd', database='Planilla')
# cursor = conn.cursor()
# cursor.execute('SELECT IDTRABAJADOR,APELLIDOS,NOMBRES FROM TRABAJADOR;')
# row = cursor.fetchone()
# while row:
#     print str(row[0]) + " " + str(row[1]) + " " + str(row[2])   
#     row = cursor.fetchone()


# # Connect
# import pymssql
# conn = pymssql.connect(server='test.database.windows.net', user='newuser@test', password='yourpassword', database='sampledatabase')
# cursor = conn.cursor()
# #Select
#  cursor.execute('SELECT * FROM votes')
#      result = ""
#      row = cursor.fetchone()
#      while row:
#          result += str(row[0]) + str(" : ") + str(row[1]) + str(" votes")
#          result += str("\n")
#          row = cursor.fetchone()
#      print result