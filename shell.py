import datetime
from user.models import Student, Mentor, Language, Course

# lang1 = Language.objects.create(name='Python', month_to_learn=6)
# lang2 = Language.objects.create(name='Java Script', month_to_learn=6)
# lang3 = Language.objects.create(name='UX-UI', month_to_learn=2)
#
# stud1 = Student.objects.create(name='Amanov Aman', email='aman@mail.ru', phone_number='+996700989898',
#                                work_study_place='School №13', has_own_notebook=True, preferred_os='windows')
# stud2 = Student.objects.create(name='Apina Alena', email='aapina@bk.ru', phone_number='+0550888888',
#                                work_study_place='TV', has_own_notebook=True, preferred_os='mac')
# stud3 = Student.objects.create(name='Phil Spencer', email='spencer@microsoft.com', phone_number='0503312312',
#                                work_study_place='Microsoft Gaming', has_own_notebook=False, preferred_os='linux')
#
# mentor1 = Mentor.objects.create(name='Ilona Maskova', email='imask@gmail.com', phone_number='0500545454',
#                                 main_work=None, experience=datetime.date(year=2021, month=10, day=23))
# mentor2 = Mentor.objects.create(name='Halil Nurmuhametov', email='halil@gmail.com', phone_number='0709989876',
#                                 main_work='Univer of Fort Colin', experience=datetime.date(year=2010, month=9, day=18))

course1 = Course.objects.create(mentor = 'Halil')