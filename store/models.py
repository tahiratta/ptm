from django.db import models

class User(models.Model):
    u_id = models.CharField(max_length=40, primary_key=True)
    profile_photo = models.ImageField(upload_to= 'Images/', default = 'Images/None/No-img.jpg')
    #cover_photo = models.ImageField(upload_to= 'Images/', default = 'Images/None/No-img.jpg')
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    cell_number = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    gender = models.CharField(max_length=40)
    date_of_birth = models.DateField(max_length=40, auto_now=True)
    type = models.CharField(max_length=40)


    def __str__(self):
        return self.name
    #class Meta:
    #   verbose_name_plural = 'categories'

class Post(models.Model):
    post_id = models.CharField(max_length=40, primary_key=True)
    add_photo = models.ImageField(upload_to= 'Images/', default = 'Images/None/No-img.jpg')
    status = models.TextField(max_length=50)
    files = models.FileField(upload_to= 'Docs/', default= 'docs/None/No-doc.pdf')
    comments = models.TextField(max_length=20)
    u_id = models.ForeignKey(User)

    def __str__(self):
        return self.post_id

class Group(models.Model):
    g_id = models.CharField(max_length=40, primary_key=True)
    g_name = models.CharField(max_length=40)
    cover_photo = models.ImageField(upload_to= 'Images/', default = 'Images/None/No-img.jpg')
    add_photo = models.ImageField(upload_to= 'Images/', default = 'Images/None/No-img.jpg')
    status = models.TextField(max_length=50)
    files = models.FileField(upload_to= 'Docs/', default= 'docs/None/No-doc.pdf')
    comments = models.TextField(max_length=20)
    u_id = models.ForeignKey(User)

    def __str__(self):
        return self.g_name

class Acadamic_Record(models.Model):
    a_id = models.CharField(max_length=40, primary_key=True)
    attendance = models.CharField(max_length=40)
    quiz_number = models.CharField(max_length=40)
    quiz_marks = models.CharField(max_length=40)
    u_id = models.ForeignKey(User)

    def __str__(self):
        return self.a_id