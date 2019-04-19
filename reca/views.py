import pyodbc
from django.shortcuts import render


conn = pyodbc.connect(
		driver='{ODBC Driver 17 for SQL Server}',
		host='61.110.213.49,8453',
		database='KANG_DB',
		user='sa',
		password='dkfmanetsa@dmin',
	)


def login(request):
	return render(request, 'reca/login.html', {})

def index(request):
	return render(request, 'reca/index.html', {})

"""
def dash(request):
	return render(request, 'reca/dash.html', {})
	"""

def rp_daily_cs(request):
	#return render(request, 'reca/rp_daily_cs.html', {})
	try:
		with conn.cursor() as cursor:
			cursor.execute("SELECT T.CUST_NO, T.CUST_NAME, T.COUNSEL_NO, T.YY, T.MM, T.DD, T.HH, T.IUN, T.PUN, T.CUN, T.CUST_CODE1, T.GL, T.C1N, T.C2N, T.PISS, T.CPSS FROM (SELECT A.CUST_NO, B.CUST_NAME, A.COUNSEL_NO, LEFT(A.IN_DATE, 4) AS YY, SUBSTRING(A.IN_DATE, 5, 2) AS MM, SUBSTRING(A.IN_DATE, 7, 2) AS DD, LEFT(A.IN_TIME, 2) AS HH, A.SEND_USER, (SELECT USER_NAME FROM USER_TBL WHERE LOGIN_USER = A.SEND_USER) AS IUN, A.IN_DATE, A.IN_TIME, A.PROC_USER, (SELECT USER_NAME FROM USER_TBL WHERE LOGIN_USER = A.PROC_USER) AS PUN, A.PROC_DATE, A.PROC_TIME, A.COMP_USER, (SELECT USER_NAME FROM USER_TBL WHERE LOGIN_USER = A.COMP_USER) AS CUN, A.COMP_DATE, A.COMP_TIME, B.CUST_CODE1, C.CUST_NAME AS GL, B.CUST_CODE2, B.CUST_CODE3, B.PLACE_FG2, A.CALL1_CODE, (SELECT CALL1_NAME FROM CALL1_CODE_TBL WHERE CALL1_CODE = A.CALL1_CODE) AS C1N , A.CALL2_CODE, (SELECT CALL2_NAME FROM CALL2_CODE_TBL WHERE CALL1_CODE = A.CALL1_CODE AND CALL2_CODE = A.CALL2_CODE ) AS C2N, DATEDIFF(SS, A.IN_DATE, A.PROC_DATE)+ (((LEFT(A.PROC_TIME, 2) * 3600) + (SUBSTRING(A.PROC_TIME,3,2) * 60) + (SUBSTRING(A.PROC_TIME, 5,2)))- ((LEFT(A.IN_TIME, 2) * 3600) + (SUBSTRING(A.IN_TIME,3,2) * 60) + (SUBSTRING(A.IN_TIME, 5,2))) ) AS PISS, DATEDIFF(SS, A.PROC_DATE, A.COMP_DATE)+ (((LEFT(A.COMP_TIME, 2) * 3600) + (SUBSTRING(A.COMP_TIME,3,2) * 60) + (SUBSTRING(A.COMP_TIME, 5,2)))- ((LEFT(A.PROC_TIME, 2) * 3600) + (SUBSTRING(A.PROC_TIME,3,2) * 60) + (SUBSTRING(A.PROC_TIME, 5,2))) ) AS CPSS FROM COUNSEL_MAIN_TBL A LEFT JOIN CUST_INFO_TBL B ON A.CUST_NO = B.CUST_NO LEFT JOIN CUST_LEVEL1_TBL C ON B.CUST_CODE1 = C.CUST_LEVEL1 WHERE A.DEL_FG = 'N' AND A.IN_DATE = '20190418') T ORDER BY T.COUNSEL_NO DESC")
			drpt = cursor.fetchall()
	except Exception as msg:
		print(msg)
	#finally:
		#conn.close()
	return render(request, 'reca/rp_daily_cs.html', {'drpt':drpt})

	
def card_pm(request):
	return render(request, 'reca/card_pm.html', {})


def dash(request):
	try:
		with conn.cursor() as cursor:
			cursor.execute("SELECT * FROM COUNSEL_MAIN_TBL WHERE IN_DATE = '20190416';")
			rows = cursor.fetchall()
	except Exception as msg:
		print(msg)
	#finally:
		#conn.close()

	return render(request, 'reca/dash.html', {'rows':rows})


