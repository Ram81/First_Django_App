import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

# Create your tests here.

class QuestionMethodTest(TestCase):
	
	def test_was_published_recently(self):
		t=timezone.now()+datetime.timedelta(days=30)
		future_date=Question(pub_date=t)
		self.assertIs(future_date.was_published_recently(),False)
	
