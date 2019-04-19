from django import template

register = template.Library()

from ..models import Course


@register.simple_tag
def topic_count_tag(pk):
	return Course.objects.get(pk=pk).topics.count()


@register.simple_tag
def subtopic_count_tag(pk):
	count = 0;
	course = Course.objects.get(pk=pk)
	for topic in course.topics.all():
		count+=topic.subtopics.count()
	return str(count);