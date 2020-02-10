from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
#from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
	def create_user(self, email, password):
		"Creates and saves a user with the given email and password"
		if not email:
			raise ValueError('User must have an email address')

		user = self.model(
			email = self.normalize_email(email),

		)
		user.set_password(password)
		
		user.save(using=self._db)
		return user

	def create_staffuser(self, email, password):
		"Creates and saves a staff user with the given email and password"
		user = self.create_user(
			email, password = password,
		)
		user.staff = True
		user.admin = True
		user.save(using = self._db)
		return user

	def create_superuser(self, email, password):
		"Creates and saves a superuser with the given email and password"
		user = self.create_user(
			email, password = password,

		)
		user.staff = True
		user.admin = True
		user.save(using = self._db)
		return user		


# Using custom user model
class User(AbstractBaseUser):
	username=models.CharField(max_length = 20,default = None,null=True)
	email=models.EmailField(unique=True)
	date_joined=models.DateTimeField(default = timezone.now)
	last_login = models.DateTimeField(default = timezone.now)
	admin = models.BooleanField(default = False)
	active = models.BooleanField(default = True)
	staff = models.BooleanField(default = False)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	objects = UserManager()

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer : Yes, alaways
		return True

	def has_module_perms(self, app_label):
		"Does the user have permission to view the app 'app_label' ?"
		#Simplest possbile answer: Yes, always
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff ?"

		return self.staff

	@property
	def is_admin(self):
		"Is user a admin member ?"
		return self.admin

	@property
	def is_active(self):
		"Is the user active ?"
		return self.active		


# Item models
class Item(models.Model):
	item_title = models.CharField(max_length= 50)
	user=models.ManyToManyField(User)
	
	def __str__(self):
		return self.item_title
			

# Comment models
class Comment(models.Model):
	msg=models.CharField(max_length=200)
	commented_by = models.ForeignKey(User, on_delete = models.CASCADE)
	item=models.ForeignKey(Item,on_delete=models.CASCADE,related_name='comments')
	cr_data = models.DateTimeField(auto_now = True)
	
	def __str__(self):
		return self.msg


# Recipe models
class Recipe(models.Model):
	recipe_title = models.CharField(max_length = 50)
	recipe_description = models.TextField()
	recipe_category = models.CharField(max_length = 50)
	recipe_favorites = models.BooleanField()
	recipe_image = models.FileField(upload_to="recipes/")
	item=models.ForeignKey(Item, on_delete=models.CASCADE)
	date_time = models.DateTimeField(auto_now= True)


	def __str__(self):
		return self.recipe_title		