from flask import Blueprint, render_template, request, redirect, url_for
from flask_security import login_required
from models import kkss, iss, mertik, ip_invit
from .forms import PostForm, IsForm
import ipaddress
from app import db



kks = Blueprint('kks', __name__, template_folder='templates')

@kks.route('/net_create', methods = ['POST', 'GET'])
@login_required
def net_create():
    form2 = IsForm()
    form = PostForm()
    if form.Submit_1.data:
        mask = request.form['mask']
        ip = request.form['ip']
        filial = request.form['filial'] 
        ploshadka = request.form['ploshadka']
        vlan = request.form['vlan']
        vlan_name = request.form['vlan_name']
        ploshadka_det = request.form['ploshadka_det']
        getway = request.form['getway']
        net = ipaddress.ip_network(ip + mask)
        broadcast = net.broadcast_address
        sr = kkss.query.filter(kkss.ploshadka == ploshadka, kkss.filial == filial).first()
        q = 0
        if sr is None:
            flag = '1'
        else:
            flag = '0'
        try:
            for ipp in net:
                if flag == "1" and q == 0:
                    setka = kkss(ip = str(ipp), broadcast = str(broadcast), mask = mask, subnet = str(net), getway = getway, filial = filial, ploshadka = ploshadka, flag = '1', vlan = vlan, vlan_name = vlan_name, ploshadka_det = ploshadka_det)
                    db.session.add(setka)  
                    db.session.commit()
                    q = q + 1
                else:
                    setka = kkss(ip = str(ipp), broadcast = str(broadcast), mask = mask, subnet = str(net), getway = getway, filial = filial, ploshadka = ploshadka, flag = '0', vlan = vlan, vlan_name = vlan_name, ploshadka_det = ploshadka_det)
                    db.session.add(setka)  
                    db.session.commit()
            return redirect(url_for('kks.index'))
        except:
            print('Something wrong s setkami')
    elif form2.Submit_2.data:
        kr_name = request.form['kr_name']
        name = request.form['name']
        kategor = request.form['kategor']
        tip =  request.form['tip']
        try:
            sistema = iss(kr_name = str(kr_name), name = str(name), kategor = str(kategor), tip = str(tip))
            db.session.add(sistema)
            db.session.commit()
            return redirect(url_for('kks.index'))
        except:
            print('Something wrong s ISami')
    else:
        return render_template('kks/net_create.html', form=form, form2 = form2)
    
        

@kks.route('/kks')
@login_required
def index():
    q = request.args.get('q')
    q1 = request.args.get('q1')
    if q:
        searchs = kkss.query.filter(kkss.ip.contains(q) | kkss.name.contains(q)).all()
        return render_template('kks/searchs.html', searchs = searchs)
    if q1:
        sistema = iss.query.filter(iss.kr_name.contains(q1)).all()
        return render_template('kks/perech_is.html', sistema = sistema)
    xs = kkss.query.filter(kkss.filial == "АУП", kkss.flag == "1").all()
    ans = kkss.query.filter(kkss.filial == "АНУ", kkss.flag == "1").all()
    chels = kkss.query.filter(kkss.filial == "ЧелНУ", kkss.flag == "1").all()
    cher = kkss.query.filter(kkss.filial == "ЧерНУ", kkss.flag == "1").all()
    return render_template('kks/index.html', xs = xs, ans = ans, chels = chels, cher = cher)





@kks.route('/<plosh_detail>_<fil>')
@login_required
def ploshadka_detail(plosh_detail, fil):
    infos = kkss.query.filter(kkss.ploshadka == str(plosh_detail), kkss.ip == kkss.broadcast, kkss.filial == str(fil)).all()
    ips = kkss.query.filter(kkss.ploshadka == str(plosh_detail)).all()
    ipy = kkss.query.filter(kkss.ploshadka == str(plosh_detail), kkss.filial == str(fil)) # все ip с площадки например Черну АУП
    return render_template('kks/ploshadka_detail.html', infos = infos, ips = ips)




@kks.route('/<ip_detail> ', methods = ['POST', 'GET'])
@login_required
def ip_detail(ip_detail):
    ipp = kkss.query.filter(kkss.id == ip_detail).first()
    isy = ipp.is_ip
    x1 = kkss.query.filter(kkss.ip == str(ipaddress.ip_address(ipp.ip) + 1)).first()
    x2 = kkss.query.filter(kkss.ip == str(ipaddress.ip_address(ipp.ip) - 1)).first()
    ip_metrik = ip_invit.query.filter(ip_invit.ip == ipp.ip).all() # берем все данные по инвинтаризации
    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=ipp)
        form.populate_obj(ipp)
        db.session.commit()
        return redirect(url_for('kks.ip_detail', ip_detail = ipp.id))
    else:
        form = PostForm(obj = ipp)
        return render_template('kks/ip_detail.html', ipp = ipp, form = form, x1 = x1, x2 = x2, isy = isy, ip_metrik = ip_metrik)
    



@kks.route('/perech_is_<is_det>', methods = ['POST', 'GET'])  
@login_required
def is_det(is_det):
    isss = iss.query.filter(iss.id == is_det).first()
    q2 = request.args.get('q2')
    if q2:
        x = kkss.query.filter(kkss.ip.contains(q2)).first() # добавить alert если ip нет в списке ККС
        x.is_ip.append(isss) # связываем ИП ККС и ИС
        db.session.add(x)  
        db.session.commit()
        return redirect(url_for('kks.is_det', is_det = isss.id)) 
    if request.method == 'POST':
        form = IsForm(formdata=request.form, obj=isss)
        form.populate_obj(isss)
        db.session.commit()
        return redirect(url_for('kks.is_det', is_det = isss.id))
    else:
        form = IsForm(obj = isss)
        return render_template('kks/is_det.html', form = form, isss = isss, ipy = ipy)   



@kks.route('/perech_is')
@login_required
def perech_is():
    sistema = iss.query.all()
    return render_template('kks/perech_is.html', sistema = sistema)



 



    