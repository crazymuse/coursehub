from course.models import Course,Topic,SubTopic
from django.utils import timezone
from django.contrib.auth.models import User

u = User(username='jaley',password='jaley123')
u.save()


c = Course(title='NLP for everyone',desc='NLP is important',created_on=timezone.now(),publisher=u)
t1 = c.topics.create(title="Morphological Analysis of Text")
s1t1 = t1.subtopics.create(title="Stemming")
s2t1 = t1.subtopics.create(title="Lemmetization")
s3t1 = t1.subtopics.create(title="Text processing")
t2 = c.topics.create(title="Deep Learning and Text")
s1t2 = t2.subtopics.create(title="Word Embedding")
s2t2 = t2.subtopics.create(title="Skip Gram Model")
s3t2 = t2.subtopics.create(title="Continuous Bag of Words")
c.save()