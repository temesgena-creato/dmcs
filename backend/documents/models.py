from django.db import models

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    # Using IntegerField instead of a formal ForeignKey
    user_id = models.IntegerField(null=True, blank=True) 
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Document(models.Model):
    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    document_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50)
    file_size = models.BigIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    version = models.CharField(max_length=20)
    approval_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Draft')
    
    # Simple integer IDs for User and Entity
    user_id = models.IntegerField(null=True, blank=True) # Created by
    application_id = models.IntegerField(null=True, blank=True)
    api_catalog_id = models.IntegerField(null=True, blank=True)
     #application = models.ForeignKey(
        # 'application.application', 
         #on_delete=models.SET_NULL, 
         #null=True, 
         #blank=True,
         #related_name='documents'
    # )
    
    # Link to API Catalog (Replace 'app_name.APICatalog' with actual path)
     #api_catalog = models.ForeignKey(
        # 'APICatalog.API_catalog', 
         #on_delete=models.SET_NULL, 
         #null=True, 
         #blank=True,
        # related_name='documents'
    # )
    
    file_location = models.FileField(upload_to='documents/') 
    
    created_date = models.DateTimeField(auto_now_add=True)
    approved_by = models.IntegerField(null=True, blank=True) # User ID of approver
    approved_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name