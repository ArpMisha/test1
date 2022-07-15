from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, DateTimeField, IntegerField, TextField, SubmitField
from wtforms.validators import IPAddress, DataRequired 

class PostForm(FlaskForm):
    mask = SelectField('Маска сети', choices=(("/24", "/24"),("/25", "/25"),("/26", "/26"),("/27", "/27"),("/28", "/28"),("/29", "/29"),("/30", "/30"),("/31", "/31")))
    ip = StringField('сеть', validators = [IPAddress(ipv4=True, ipv6=False,  message = None), DataRequired()])
    vlan = IntegerField('Номер VLAN')
    vlan_name = StringField('Название VLAN')
    filial = SelectField('Организация/филиал', choices=(("АУП", "АУП"), ("АНУ", "АНУ"), ("ТНУ", "ТНУ"), ("КНУ", "КНУ"), ("ЧелНУ", "ЧелНУ"), ("ЧерНУ", "ЧерНУ"), ("СУПЛАВ", "СУПЛАВ")))
    ploshadka = StringField('Площадка (Введите правильно, в соответствии со  списком площадок организации):')
    ploshadka_det = StringField('Уточнения по сети (для чего, где используется)')
    getway = StringField('IP-адрес шлюза (Введите правильно, с учетом маски подсети):', validators = [IPAddress(ipv4=True, ipv6=False,  message = None), DataRequired()])

    primech = TextField('Комментарий')
    name = StringField('DNS имя')

    Submit_1 = SubmitField('Добавить сеть')

#ИС
class IsForm(FlaskForm):
    kr_name = StringField('Краткое наименование ИС', [DataRequired()]) # краткое имя
    name = StringField('Полное наименование ИС', [DataRequired()]) # полное имя
    kategor = SelectField('Категория обробарываемой информации', choices=(("K", "K"), ("KT", "KT"), ("ПНД", "ПНД"))) # категория обробарываемой информации (к/кт/ПНд)
    tip = SelectField('Тип системы', choices=(("локальная", "локальная"), ("корпоративная", "корпоративная"))) # тип системы (локальная/корпоративная)
    Submit_2 = SubmitField('Добавить ИС')

    #ip_is = StringField('IP-адрес сервера(-ов)', validators = [IPAddress(ipv4=True, ipv6=False,  message = None), DataRequired()])




    



    
