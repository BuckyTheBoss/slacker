from main.models import *
from faker import Faker
from django.contrib.auth.models import User
import random

fake = Faker()


def gen_fname():
	return fake.first_name()

def gen_lname():
	return fake.last_name()

def gen_password():
	return fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)

def gen_paragraph():
	return fake.paragraph(nb_sentences=5, variable_nb_sentences=True, ext_word_list=None)

def gen_sentance():
	return fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)


def create_users():
	'''create as many users as first names given, randomly selecting the last name from the lnames list'''
	fnames = ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten']
	lnames = ['Apple','Microsoft','Twitter']
	passwords = []
	for i in range(0, len(fnames)):
		password = gen_password()
		fname = fnames[i]
		lname = random.choice(lnames)
		username = fname.lower() + lname.lower()
		user = User.objects.create_user(username=username, password=password, first_name=fname, last_name=lname)
		user.save()
		user.profile.bio = gen_paragraph()
		user.save()
		passwords.append(password)
	print(passwords)

def pick_user():
	return random.choice(User.objects.all())

def create_groups():
	lnames = ['Microsoft','Twitter']
	for name in lnames:
		profiles = Profile.objects.filter(user__last_name=name)
		gc = GroupChat(name=f'{name} Group')
		gc.save()
		for profile in profiles:
			gc.profiles.add(profile)

	gc = GroupChat(name='Global Chat')
	gc.save()
	for profile in Profile.objects.all():
		gc.profiles.add(profile)
	