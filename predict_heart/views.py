from django.http import HttpResponse
from django.shortcuts import render
import joblib
import numpy as np

def heart(request):
	return render(request, "heart.html")


def result2(request):

	cls=joblib.load('heartSaved_model.sav')

	lis=[]
	lis.append(request.GET['age'])
	lis.append(request.GET['sex'])
	lis.append(request.GET['cp'])
	lis.append(request.GET['trestbps'])
	lis.append(request.GET['chol'])
	lis.append(request.GET['fbs'])
	lis.append(request.GET['restecg'])
	lis.append(request.GET['thalach'])
	lis.append(request.GET['exang'])
	lis.append(request.GET['oldpeak'])
	lis.append(request.GET['slope'])
	lis.append(request.GET['ca'])
	lis.append(request.GET['thal'])

	print(lis)
	
	data_array = np.asarray(lis, dtype='float64')
	arr= data_array.reshape(1,-1)
	ans = cls.predict(arr)


	print(ans)
	finalans=''
	if(ans==1):
		finalans='You may have a heart disease'
	elif(ans==0):
		finalans = 'You do not have a heart disease'
	return render(request, "result.html",{'ans':finalans})
