from django.shortcuts import render
from django.http import JsonResponse
import json
from todo_drf.settings import BASE_DIR
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin
import time

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer



# Create your views here.
json_file = "todo-django-d87c1-firebase-adminsdk-jvusb-26c6bef3d0.json"
cred = credentials.Certificate(json_file)
firebase_admin.initialize_app(cred)
db = firestore.client()

def list(request):
	return render(request, 'frontend/list.html')


def upload_to_firebase(request):

	doc_ref = db.collection('employee').document("empdoc")
	resp = doc_ref.set({
		'name': request.POST['text']
	})
	return JsonResponse(json.dumps(resp, default=str), safe=False)


@api_view(['POST'])
def upload_to_firebase(request):
	title = request.POST['title']
	text = request.POST['text']
	serializer = TaskSerializer({'title':title,"text": text})
	
	sbt = request.POST['submit']
	if sbt == "0":

		doc_ref = db.collection('task_firestore').document(str(time.time()))
		doc = doc_ref.get()
		if doc.exists:
			resp = False
		else:
			resp = doc_ref.set(
					serializer.data
				)
	else:
		doc_ref = db.collection('task_firestore').document(str(sbt))
		resp = doc_ref.set(
                    serializer.data
                )
	return JsonResponse(json.dumps(resp, default=str), safe=False)


@api_view(['GET'])
def get_from_firebase(request):
	docs = db.collection(u'task_firestore').stream()
	resp = []
	for doc in docs:
		id = {'id':doc.id}
		resp.append({**id , **doc.to_dict()})
	return JsonResponse(json.dumps(resp, default=str), safe=False)


@api_view(['DELETE'])
def delete_from_firebase(request, pk):
	resp = db.collection(u'task_firestore').document(pk).delete()
	return JsonResponse(json.dumps(resp,default=str),safe=False)
