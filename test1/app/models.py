from app import db
import re
from datetime import datetime
from flask_security import UserMixin, RoleMixin



def slugify(s):
    patern = r'[^\w+]'
    return re.sub(patern, '-', s)


kkss_iss = db.Table('kkss_iss',
        db.Column('kkss_id', db.Integer(), db.ForeignKey('kkss.id')),
        db.Column('iss_id', db.Integer(), db.ForeignKey('iss.id'))
    )

class kkss(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    mask = db.Column(db.String()) # маска сети
    subnet = db.Column(db.String()) # сеть
    ip = db.Column(db.String()) 
    name = db.Column(db.String()) # имя хоста
    getway = db.Column(db.String()) 
    broadcast = db.Column(db.String())
    filial = db.Column(db.String()) # филиал 
    ploshadka = db.Column(db.String()) # площадка в филиале
    primech = db.Column(db.Text) # уточнения по конкретному IP-адресу 
    flag = db.Column(db.String()) # вывод площадки для html
    vlan = db.Column(db.Integer()) # номер влана
    vlan_name = db.Column(db.String()) # имя влана
    ploshadka_det = db.Column(db.String()) # уточнение по площадке этаж и тд

    is_ip = db.relationship('iss', secondary=kkss_iss, backref=db.backref('ip_is', lazy='dynamic'))

    def __init__(self, *args, **kwargs):
        super(kkss, self).__init__(*args, **kwargs)
    

class iss(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    kr_name = db.Column(db.String()) # краткое имя
    name = db.Column(db.String()) # полное имя
    kategor = db.Column(db.String()) # категория обробарываемой информации (к/кт/ПНд)
    tip = db.Column(db.String()) # тип системы (локальная/корпоративная)
    naznach = db.Column(db.String())# Назначение ИС (прикладная/инфраструктурная/СЗИ)
    data_vvoda = db.Column(db.String()) # Дата ввода ИС в ПЭ
    zakazchik = db.Column(db.String()) # Наименование организации (подразделения), отвечающего за ИС
    data_ib = db.Column(db.String()) # Дата последнего проведения ИБ ИС
    primech = db.Column(db.String()) # Примечание

    
    def __init__(self, *args, **kwargs):
        super(iss, self).__init__(*args, **kwargs)

  

# авторизация flask_security
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
    )

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key = True)
    password = db.Column(db.String())
    email = db.Column(db.String(), unique = True)
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(32), unique = True)
    description = db.Column(db.String(255))

    
class events(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String()) #varchar(255) NOT NULL,
    start_event = db.Column(db.String())
    end_event = db.Column(db.String())
    
    def __init__(self, *args, **kwargs):
        super(events, self).__init__(*args, **kwargs)


    




