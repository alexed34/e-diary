import random
from datacenter.models import Schoolkid, Lesson, Mark, Chastisement, Commendation
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist




def create_commendation(name, lesson):
    try:
        student = Schoolkid.objects.get(full_name__contains=name)
        year = student.year_of_study
        letter = student.group_letter
        lessons = Lesson.objects.filter(year_of_study=year, group_letter=letter, subject__title=lesson).order_by('-date')
        one_lesson = lessons[0]
        text_chastisements = [
            'Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!', 'Великолепно!',
            'Прекрасно!', 'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!', 'Сказано здорово – просто и ясно!',
            'Ты, как всегдаточен!', 'Очень хороший ответ!', 'Талантливо!', 'Ты сегодня прыгнул выше головы!', 'Я поражен!',
            'Уже существенно лучше!', 'Потрясающе!', 'Замечательно!', 'Прекрасное начало!', 'Так держать!', 'Ты на верном пути!', 'Здорово!',
            'Это как раз то, что нужно!', 'Я тобой горжусь!', 'С каждым разом у тебя получается всё лучше!', 'Мы с тобой не зря поработали!',
            'Я вижу, как ты стараешься!', 'Ты растешь над собой!', 'Ты многое сделал, я это вижу!', 'Теперь у тебя точно все получится!'
        ]
        text_chastisement = random.choice(text_chastisements)
        Commendation.objects.create(text=text_chastisement, schoolkid=student, teacher=one_lesson.teacher, created=one_lesson.date,
                                    subject=one_lesson.subject)
    except MultipleObjectsReturned:
        print('Учеников больше одного, уточните ФИО')
    except IndexError:
        print('Нет такого предмета')
    except ObjectDoesNotExist:
        print('Нет такого ученика')


def fix_marks(name):
    try:
        student = Schoolkid.objects.get(full_name__contains=name)
        Mark.objects.filter(schoolkid=student, points__lt=4).update(points=5)
    except MultipleObjectsReturned:
        print('Учеников больше одного, уточните ФИО')
    except ObjectDoesNotExist:
        print('Нет такого ученика')




def remove_chastisements(name):
    try:
        student = Schoolkid.objects.get(full_name__contains=name)
        chastisements = Chastisement.objects.filter(schoolkid=student)
        chastisements.delete()
    except MultipleObjectsReturned:
        print('Учеников больше одного, уточните ФИО')
    except ObjectDoesNotExist:
        print('Нет такого ученика')








