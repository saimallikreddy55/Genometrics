from django.shortcuts import render
from django.http import HttpResponse
import joblib
import numpy as np


def diabetes(request):
     return render(request, 'diabetes.html')

def result(request):

	cls=joblib.load('saved_model.sav')

	lis=[]
	lis.append(request.GET['Pregnancies'])
	lis.append(request.GET['Glucose'])
	lis.append(request.GET['Blood Pressure'])
	lis.append(request.GET['Skin Thickness'])
	lis.append(request.GET['Insulin'])
	lis.append(request.GET['BMI'])
	lis.append(request.GET['DPF'])
	lis.append(request.GET['Age'])

	print(lis)
	data_array = np.asarray(lis)
	arr= data_array.reshape(1,-1)
	

	ans = cls.predict(arr)
	print(ans)
	finalans=''
	if(ans==1):
		finalans='You may have diabetes'
	elif(ans==0):
		finalans = 'You do not have diabetes'
	return render(request, "result.html",{'ans':finalans})



