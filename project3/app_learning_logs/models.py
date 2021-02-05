from django.db import models

# Create your models here.

class Topic(models.Model):
     """ A topic the user is learning about."""
     text = models.CharField( max_length = 200)
     date_added = models.DateTimeField( auto_now_add = True)
     
     def __str__(self): #This function will show the default field when you query the 'Topic' from database. Here it will return text.
        """ Return a string representation of the model.""" 
        return self.text

class Entry(models.Model):
   """Something specific learned about the topic."""
   topic = models.ForeignKey(Topic, on_delete=models.CASCADE) #This line means topic is attached with the ID of another record in DB (Topic) and Entries should be 
   #deleted when Topic is deleted. This is called cascading.
   text = models.TextField()
   date_added = models.DateTimeField(auto_now_add=True)

   class Meta: #This is a nested class, inside Entry class. Here we are telling django to use 'Entries' not 'Entrys' when calling 'Entry' class multiple times.
      verbose_name_plural = 'entries'

   def __str__(self):
      """Return a string representation of the model."""
      if len(self.text) >= 50:
         return(f"{self.text[:50]}...")
      else:
          return(f"{self.text[:]}")





 
