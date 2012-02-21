from celery.task import task

from howl import *


@task
def send_howl(application_name, event_name, event_title, event_description, username, password):
	"""Sends an Howl alert."""

	event = HowlEvent(application_name, event_name, event_title, event_description)
	request = event.request(username, password)

	if request.status_code == 401:
		return False
	return True
