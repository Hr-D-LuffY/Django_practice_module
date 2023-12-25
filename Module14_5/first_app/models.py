from django.db import models

# Create your models here.
class example(models.Model):
    title = models.CharField(max_length = 200) 
    description = models.TextField() 
    last_modified = models.DateTimeField(auto_now_add = True)
    file_field = models.FileField(upload_to='files/') 
    img = models.ImageField(upload_to = "images/") 
    auto_field = models.AutoField(primary_key=True)
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    duration_field = models.DurationField()
    float_field = models.FloatField()
    generic_ip_address_field = models.GenericIPAddressField()
    # foreign_key = models.ForeignKey(OtherModel, on_delete=models.CASCADE)
    # many_to_many_field = models.ManyToManyField(OtherModel)
    # one_to_one_field = models.OneToOneField(OtherModel, on_delete=models.CASCADE)
    slug_field = models.SlugField()
    url_field = models.URLField()





    def __str__(self): 
        return self.title 