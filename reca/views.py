import pyodbc
from django.shortcuts import render



def dash(request):
	conn = pyodbc.connect(
		driver='{ODBC Driver 17 for SQL Server}',
		host='61.110.213.49,8453',
		Database='KANG_DB',
		user='sa',
		password='dkfmanetsa@dmin'
	)

	try:
		with conn.cursor() as cursor:
			cursor.execute("SELECT * FROM COUNSEL_MAIN_TBL WHERE IN_DATE = '20190416';")
			rows = cursor.fetchall()
	except Exception as msg:
		print(msg)
	finally:
		conn.close()

	return render(request, 'reca/dash.html', {'rows':rows})
