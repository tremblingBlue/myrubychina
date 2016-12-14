from __future__ import unicode_literals

from django.db import models

class Node(models.Model):
    node_name = models.CharField(max_length=200)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    create_date = models.DateTimeField('date created')
    modify_date = models.DateTimeField('date modified')

    def __str__(self):
        return self.node_name

class Article(models.Model):
    title = models.CharField(max_length=300)
    content = models.CharField(max_length=30000)
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    create_date = models.DateTimeField('date created')
    pub_date = models.DateTimeField('date published')
    modify_date = models.DateTimeField('date modified')

    def __str__(self):
        return self.title


  