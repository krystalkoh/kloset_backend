from django.db import models
import uuid

class Users(models.Model):
    email = models.EmailField(max_length=254, primary_key=True) #autoField is the serial
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.PositiveIntegerField
    address = models.CharField(max_length=100)
    postal_code = models.PositiveIntegerField
    wallet = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, editable=False)
    # cart_id = models.ForeignKey(Carts, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.postal_code
#
class Clothes(models.Model):
    # SEGREGATED TABLE
    TOP = 'TO'
    SKIRT = 'SK'
    SHORTS = 'SH'
    PANTS = 'PA'
    DRESS = 'DR'
    SET = 'SE'
    OUTERWEAR = 'OU'
    ACCESSORIES = 'AC'
    TAGS_CHOICES = [
        (TOP, 'Top'),
        (SKIRT, 'Skirt'),
        (SHORTS, 'Shorts'),
        (PANTS, 'Pants'),
        (DRESS, 'Dress'),
        (SET, 'Set'),
        (OUTERWEAR, 'Outerwear'),
        (ACCESSORIES, 'Accessories'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_of_item = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    description = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    tags = models.CharField(max_length=2, choices=TAGS_CHOICES, default=TOP,)
    date_listed = models.DateField (auto_now=True)
    availability = models.BooleanField()
    user_email = models.ForeignKey(Users, on_delete=models.DO_NOTHING, null=True)
    clothes_image = models.ImageField(upload_to='post_images', null=True)
    #clothes_images
    clothes_images_url = models.TextField(max_length=1000, null=True)
    #need to either give default or null
    def __str__(self):
        return self.name_of_item
#     #one member can have more than one address.. .so addresses have a foreign key to members
# class Addresses(models.Model):
#     id = models.AutoField(primary_key=True) #got smallautofield bigautofield
#     street_name = models.CharField(max_length=550)
#     level = models.SmallIntegerField()
#     unit = models.SmallIntegerField()
#     member = models.ForeignKey(Members, on_delete=models.DO_NOTHING, null=True)
#     #on_delete is needed for foreign keys
#     #null=true means this column can be empty
#     #on_delete_cascade: means if i delete anything in the foreign key in address, everything related to the member in member table is deleted
#     #on_delete_set_null: on delete set null
#     def __str__(self):
#         return self.street_name
#
#
# # ForeignKey(class_name, on_delete=...)
#
# # ManyToManyField(class_name)
#
# #OneToOneField(class_name, on_delete=...)
#
