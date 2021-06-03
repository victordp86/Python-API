""" Platzigram views """
from django.http import HttpResponse

#Utilitiees
from datetime import datetime
import json

def hello_world(request):
    """Return a greeting."""
    return HttpResponse('Hello, world!{now}'.format(
    	now=datetime.now().strftime('%b %dth, %Y : %M HttpResponses') 	
    	))


def sort_integers(request):
  """Return a JSON response with sorted integers"""
  numbers = request.GET['numbers']
  #numbers = [2,42,24]
  num = [int(x.strip()) for x in numbers.split(',')]
  data = {
  	'status': 'ok',
  	'numbers': num,
  	'message': 'Integers sorted succesfully.'
  }
  return HttpResponse(
  	json.dumps(data, indent = 4),
  	 content_type='application/json'
  )


def say_hi(request, name, age):
	"""Return a greeting"""
	if age<12:
		message = 'Sorryy {}, you are not allowed here'.format(name)
	else:
		message = 'Hello {}, Welcome to Platzigram'.format(name)
	return HttpResponse(message)