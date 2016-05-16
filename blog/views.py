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
	cursor.execute('SELECT * FROM TRABAJADOR;')
	row = cursor.fetchone()
	while row:
		#print str(row[0]) + " " + str(row[1]) + " " + str(row[2])   
		#row = cursor.fetchone()
	    result += str(row[0]) + "  " + str(row[1]) + " " + str(row[2]) + " " + str(row[7])
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