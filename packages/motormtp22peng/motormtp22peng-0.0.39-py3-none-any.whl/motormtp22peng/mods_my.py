import femm
import math


def winding(Elemsize, top, x_ini1, y_ini1, x_ini2, y_ini2, slot_n, name, position, w_type):
    pitch = 2*math.pi/slot_n;
    if top is True :
        x_ini = x_ini1;
        y_ini = y_ini1;
    else:
        x_ini = x_ini2;
        y_ini = y_ini2;
    for i in position:
        xn = x_ini*math.cos((-0/2-i)*pitch) - y_ini*math.sin((-0/2-i)*pitch);
        yn = y_ini*math.cos((-0/2-i)*pitch) + x_ini*math.sin((-0/2-i)*pitch);
        femm.mi_addblocklabel(xn, yn);   						# add a new blocklabel at x,y
        femm.mi_selectlabel(xn, yn);     						# select the blocklabel closest to x,y
        femm.mi_setblockprop(name,0,Elemsize,"","",w_type,1);    # define the rotor 1 core properties
        femm.mi_clearselected();



def winding2(Elemsize, top, x_ini1, y_ini1, x_ini2, y_ini2, slot_n, name, position, w_type):
    pitch = 2*math.pi/slot_n;


    for m in range(len(position)):
        if top[m] is True :
            x_ini = x_ini1;
            y_ini = y_ini1;
        else:
            x_ini = x_ini2;
            y_ini = y_ini2;

        i = position[m];
        xn = x_ini*math.cos((-i)*pitch) - y_ini*math.sin((-i)*pitch);
        yn = y_ini*math.cos((-i)*pitch) + x_ini*math.sin((-i)*pitch);
        femm.mi_addblocklabel(xn, yn);   						# add a new blocklabel at x,y
        femm.mi_selectlabel(xn, yn);     						# select the blocklabel closest to x,y
        femm.mi_setblockprop(name,0,Elemsize,"","",w_type,1);    # define the rotor 1 core properties
        femm.mi_clearselected();







def winding1_2(Elemsize, top, x_ini1, y_ini1, x_ini2, y_ini2, slot_n, name, position, w_type):
    pitch = 2*math.pi/slot_n;


    for m in range(len(position)):
        if top[m] is True :
            x_ini = x_ini1;
            y_ini = y_ini1;
        else:
            x_ini = x_ini2;
            y_ini = y_ini2;

        i = position[m];
        xn = x_ini*math.cos((-1/2-i)*pitch) - y_ini*math.sin((-1/2-i)*pitch);
        yn = y_ini*math.cos((-1/2-i)*pitch) + x_ini*math.sin((-1/2-i)*pitch);
        femm.mi_addblocklabel(xn, yn);   						# add a new blocklabel at x,y
        femm.mi_selectlabel(xn, yn);     						# select the blocklabel closest to x,y
        femm.mi_setblockprop(name,0,Elemsize,"","",w_type,1);    # define the rotor 1 core properties
        femm.mi_clearselected();






def dup_seg(x1, y1, x2, y2, an, n):
    femm.mi_selectsegment(0.5*(x1+x2),0.5*(y1+y2));
    femm.mi_copyrotate2(0, 0, an, n, 1 );
    femm.mi_clearselected();

def add_seg_prop(x_old, y_old, x, y, g):
    femm.mi_selectsegment(0.5*(x_old+x),0.5*(y_old+y));
    femm.mi_setsegmentprop("",0.5,1,0,g);
    femm.mi_clearselected();


def winding_construction(x1, y1, x2, y2, rro, theta_m, yorkh, pole, np):
    re = [];
    ps_f_x = x1*math.cos(theta_m) -  y1*math.sin(theta_m);
    ps_f_y = y1*math.cos(theta_m) +  x1*math.sin(theta_m);

    ps_e_x = x2*math.cos(theta_m) -  y2*math.sin(theta_m);
    ps_e_y = y2*math.cos(theta_m) +  x2*math.sin(theta_m);


    ps_mid_x = 0.5*(ps_f_x + ps_e_x);
    ps_mid_y = 0.5*(ps_f_y + ps_e_y);

    # point above



    ps_f_x2 = ps_mid_x;
    ps_f_y2 = ps_mid_y + 0.1*yorkh;
    ps_f_x2 = ps_f_x2*math.cos(theta_m) -  ps_f_y2*math.sin(theta_m);
    ps_f_y2 = ps_f_y2*math.cos(theta_m) +  ps_f_x2*math.sin(theta_m);



    # point below
    ps_e_x2 = ps_mid_x;
    ps_e_y2 = ps_mid_y - 0.1*yorkh;
    ps_e_x2 = ps_e_x2*math.cos(theta_m) -  ps_e_y2*math.sin(theta_m);
    ps_e_y2 = ps_e_y2*math.cos(theta_m) +  ps_e_x2*math.sin(theta_m);


    #define mirror line
    x1 = rro*math.sin(math.pi/180*pole/2);
    y1 = rro*math.cos(math.pi/180*pole/2);
    x2 = 0.5*rro*math.sin(math.pi/180*pole/2);
    y2 = 0.5*rro*math.cos(math.pi/180*pole/2);

    femm.mi_addnode(ps_f_x,ps_f_y);
    femm.mi_selectnode(ps_f_x,ps_f_y);
    femm.mi_setnodeprop("",5);
    femm.mi_clearselected();

    theta_m = 0.5*pole - math.atan2 (ps_f_x, ps_f_y);
    xh_n = ps_f_x*math.cos(-2*theta_m) -  ps_f_y*math.sin(-2*theta_m);
    yh_n = ps_f_y*math.cos(-2*theta_m) +  ps_f_x*math.sin(-2*theta_m);
    femm.mi_addnode(xh_n,yh_n);
    femm.mi_selectnode(xh_n,yh_n);
    femm.mi_setnodeprop("",5);
    femm.mi_clearselected();
    femm.mi_addsegment(xh_n,yh_n,ps_f_x,ps_f_y);
    add_seg_prop(xh_n,yh_n,ps_f_x,ps_f_y,5);



    femm.mi_addnode(ps_e_x2,ps_e_y2);
    femm.mi_selectnode(ps_e_x2,ps_e_y2);
    femm.mi_setnodeprop("",5);
    femm.mi_clearselected();
    theta_m = 0.5*pole - math.atan2 (ps_e_x2, ps_e_y2);
    xh_n2 = ps_e_x2*math.cos(-2*theta_m) -  ps_e_y2*math.sin(-2*theta_m);
    yh_n2 = ps_e_y2*math.cos(-2*theta_m) +  ps_e_x2*math.sin(-2*theta_m);
    femm.mi_addnode(xh_n2,yh_n2);
    femm.mi_selectnode(xh_n2,yh_n2);
    femm.mi_setnodeprop("",5);
    femm.mi_clearselected();
    femm.mi_addsegment(xh_n2,yh_n2,ps_e_x2,ps_e_y2);
    add_seg_prop(xh_n2,yh_n2,ps_e_x2,ps_e_y2,5);


    # vertical line
    femm.mi_addsegment(ps_f_x,ps_f_y,ps_e_x2,ps_e_y2);
    add_seg_prop(ps_f_x,ps_f_y,ps_e_x2,ps_e_y2,5);
    femm.mi_addsegment(xh_n,yh_n,xh_n2,yh_n2);
    add_seg_prop(xh_n,yh_n,xh_n2,yh_n2,5);

    # winding start point

    #upper start point
    ws_x = 0.5*(ps_f_x+ps_e_x2);
    ws_y = 0.5*(ps_f_y+ps_e_y2);
    ws_y = math.sqrt(ws_x * ws_x + ws_y*ws_y);
    ws_x = 0.;

    re.append(ws_x);
    re.append(ws_y);



    femm.mi_addnode(ps_f_x2,ps_f_y2);
    femm.mi_selectnode(ps_f_x2,ps_f_y2);
    femm.mi_setnodeprop("",5);
    femm.mi_clearselected();
    theta_m = 0.5*pole - math.atan2 (ps_f_x2, ps_f_y2);
    xh_n = ps_f_x2*math.cos(-2*theta_m) -  ps_f_y2*math.sin(-2*theta_m);
    yh_n = ps_f_y2*math.cos(-2*theta_m) +  ps_f_x2*math.sin(-2*theta_m);
    femm.mi_addnode(xh_n,yh_n);
    femm.mi_selectnode(xh_n,yh_n);
    femm.mi_setnodeprop("",5);
    femm.mi_clearselected();
    femm.mi_addsegment(xh_n,yh_n,ps_f_x2,ps_f_y2);
    add_seg_prop(xh_n,yh_n,ps_f_x2,ps_f_y2,5);






    femm.mi_addnode(ps_e_x,ps_e_y);
    femm.mi_selectnode(ps_e_x,ps_e_y);
    femm.mi_setnodeprop("",5);
    femm.mi_clearselected();
    theta_m = 0.5*pole - math.atan2 (ps_e_x, ps_e_y);
    xh_n2 = ps_e_x*math.cos(-2*theta_m) -  ps_e_y*math.sin(-2*theta_m);
    yh_n2 = ps_e_y*math.cos(-2*theta_m) +  ps_e_x*math.sin(-2*theta_m);
    femm.mi_addnode(xh_n2,yh_n2);
    femm.mi_selectnode(xh_n2,yh_n2);
    femm.mi_setnodeprop("",5);
    femm.mi_clearselected();
    femm.mi_addsegment(xh_n2,yh_n2,ps_e_x,ps_e_y);
    add_seg_prop(xh_n2,yh_n2,ps_e_x,ps_e_y,5);


    #lower start point
    ws2_x = 0.5*(xh_n+xh_n2);
    ws2_y = 0.5*(yh_n+yh_n2);
    ws2_y = math.sqrt(ws2_x * ws2_x + ws2_y*ws2_y);
    ws2_x = 0.;

    re.append(ws2_x);
    re.append(ws2_y);




    #femm.mi_addsegment(xh,yh,xh2,yh2);
    #add_seg_prop(xh,yh,xh2,yh2,4);
    #femm.mi_selectsegment(0.5*(xh+xh2),0.5*(yh+yh2));
    #femm.mi_mirror(x1,y1,x2,y2);
    #femm.mi_clearselected();

    # vertical line
    femm.mi_addsegment(ps_f_x2,ps_f_y2,ps_e_x,ps_e_y);
    add_seg_prop(ps_f_x2,ps_f_y2,ps_e_x,ps_e_y,5);
    femm.mi_addsegment(xh_n,yh_n,xh_n2,yh_n2);
    add_seg_prop(xh_n,yh_n,xh_n2,yh_n2,5);

    femm.mi_seteditmode("group");
    femm.mi_selectgroup(5);
    femm.mi_copyrotate2(0, 0, -360/np, np, 1 );
    femm.mi_clearselected();


    # femm.mi_selectgroup(5);
    # femm.mi_setgroup(1);
    # femm.mi_clearselected();


    return(re);

# end of function

def winding_positions(nslots, pole_pairs):
    nslots = int(nslots);
    pole_pairs = int(pole_pairs);



    position_PR =[]
    position_MR = []
    position_PY =[]
    position_MY = []
    position_PB =[]
    position_MB = []
    top_PR =[]
    top_MR =[]
    top_PY =[]
    top_MY =[]
    top_PB =[]
    top_MB = []

    pos_sring = "no yet"




    if ((nslots == 9) & (pole_pairs == 4)):
        pos_ori = 'aa|Ab|BB|bb|Bc|CC|cc|Ca|AA';
        pos_sring = pos_ori.replace('|', "")
    elif ((nslots == 15) & (pole_pairs == 5)):
        pos_ori = 'aB|bC|cA|aB|bC|cA|aB|bC|cA|aB|bC|cA|aB|bC|cA';
        pos_sring = pos_ori.replace('|', "")
    elif ((nslots == 27) & (pole_pairs == 2)):
        pos_ori = 'AA|AA|cc|cc|BB|BB|aa|aa|aC|CC|CC|bb|bb|AA|AA|cc|cc|cB|BB|BB|aa|aa|CC|CC|bb|bb|bA';
        pos_sring = pos_ori.replace('|', "")
    elif ((nslots == 9) & (pole_pairs == 14)):
        pos_ori = 'aa|Ac|CC|cc|Cb|BB|bb|Ba|AA';
        pos_sring = pos_ori.replace('|', "")
    elif ((nslots == 9) & (pole_pairs == 5)):
        pos_ori = 'aa|Ac|CC|cc|Cb|BB|bb|Ba|AA';
        pos_sring = pos_ori.replace('|', "")
    elif ((nslots == 9) & (pole_pairs == 4)):
        pos_ori = 'aa|Ab|BB|bb|Bc|CC|cc|Ca|AA';
        pos_sring = pos_ori.replace('|', "")
    elif ((nslots == 12) & (pole_pairs == 5)):
        pos_ori = 'aa|Ab|BB|bC|cc|Ca|AA|aB|bb|Bc|CC|cA';
        pos_sring = pos_ori.replace('|', "")
    elif ((nslots == 12) & (pole_pairs == 7)):
        pos_ori = 'aC|cc|Cb|BB|bA|aa|Ac|CC|cB|bb|Ba|AA';
        pos_sring = pos_ori.replace('|', "")
    elif ((nslots == 24) & (pole_pairs == 2)):
        pos_ori = 'AA|Ac|cc|cB|BB|Ba|aa|aC|CC|Cb|bb|bA|AA|Ac|cc|cB|BB|Ba|aa|aC|CC|Cb|bb|bA';
        pos_sring = pos_ori.replace('|', "")
    elif ((nslots == 6) & (pole_pairs == 2)):
        pos_ori = 'aB|bC|cA|aB|bC|cA';
        pos_sring = pos_ori.replace('|', "")
    else:
        print('No slot and pole combinations!!');
        print('');
        print('No slot and pole combinations!!');


    print('pos_sring',pos_sring)

    for m in range(nslots*2):
        if (pos_sring[m] =='A'):
            position_PR.append(math.floor(m/2)+1);
            if (m%2 == 0):
                top_PR.append(True);
            else:
                top_PR.append(False);
        elif (pos_sring[m] =='a'):
            position_MR.append(math.floor(m/2)+1);
            if (m%2 == 0):
                top_MR.append(True);
            else:
                top_MR.append(False);
        elif (pos_sring[m] =='B'):
            position_PY.append(math.floor(m/2)+1);
            if (m%2 == 0):
                top_PY.append(True);
            else:
                top_PY.append(False);
        elif (pos_sring[m] =='b'):
            position_MY.append(math.floor(m/2)+1);
            if (m%2 == 0):
                top_MY.append(True);
            else:
                top_MY.append(False);
        elif (pos_sring[m] =='C'):
            position_PB.append(math.floor(m/2)+1);
            if (m%2 == 0):
                top_PB.append(True);
            else:
                top_PB.append(False);
        elif (pos_sring[m] =='c'):
            position_MB.append(math.floor(m/2)+1);
            if (m%2 == 0):
                top_MB.append(True);
            else:
                top_MB.append(False);

    print('position_PR', position_PR)
    print('position_MR', position_MR)
    print('position_PY', position_PY)
    print('position_MY', position_MY)
    print('position_PB', position_PB)
    print('position_MB', position_MB)

    print('top_PR', top_PR)
    print('top_MR', top_MR)
    print('top_PY', top_PY)
    print('top_MY', top_MY)
    print('top_PB', top_PB)
    print('top_MB', top_MB)



    return position_PR, position_MR, position_PY, position_MY, position_PB, position_MB, top_PR, top_MR, top_PY, top_MY, top_PB, top_MB







def winding3(Elemsize, top, x_ini1, y_ini1, x_ini2, y_ini2, slot_n, name, position, w_type):
    pitch = 2*math.pi/slot_n;
    for m in range(len(position)):
        if top[m]:
            x_ini = x_ini1;
            y_ini = y_ini1;
        else:
            x_ini = x_ini2;
            y_ini = y_ini2;

        xn = x_ini*math.cos((-position[m])*pitch) - y_ini*math.sin((-position[m])*pitch);
        yn = y_ini*math.cos((-position[m])*pitch) + x_ini*math.sin((-position[m])*pitch);
        femm.mi_addblocklabel(xn, yn);   						# add a new blocklabel at x,y
        femm.mi_selectlabel(xn, yn);     						# select the blocklabel closest to x,y
        femm.mi_setblockprop(name,0,Elemsize,"","",w_type,1);    # define the rotor 1 core properties
        femm.mi_clearselected();




def winding_4layer(Elemsize, layer, x_ini1, y_ini1, x_ini2, y_ini2, x_ini3, y_ini3, x_ini4, y_ini4, slot_n, name, position, w_type):
    pitch = 2*math.pi/slot_n;
    def f(x):
        return {
        1: [x_ini1, y_ini1],
        2: [x_ini2, y_ini2],
        3: [x_ini3, y_ini3],
        4: [x_ini4, y_ini4],
        }[x]

    x_ini = f(layer)[0];
    y_ini = f(layer)[1];






    for i in position:
            xn = x_ini*math.cos((-1/2-i)*pitch) - y_ini*math.sin((-1/2-i)*pitch);
            yn = y_ini*math.cos((-1/2-i)*pitch) + x_ini*math.sin((-1/2-i)*pitch);
            femm.mi_addblocklabel(xn, yn);   						# add a new blocklabel at x,y
            femm.mi_selectlabel(xn, yn);     						# select the blocklabel closest to x,y
            femm.mi_setblockprop(name,0,Elemsize,"","",w_type,1);    # define the rotor 1 core properties
            femm.mi_clearselected();



def winding_4layer3(Elemsize, layer, x_ini1, y_ini1, x_ini2, y_ini2, x_ini3, y_ini3, x_ini4, y_ini4, slot_n, name, position, w_type):
    pitch = 2*math.pi/slot_n;
    def f(x):
        return {
        1: [x_ini1, y_ini1],
        2: [x_ini2, y_ini2],
        3: [x_ini3, y_ini3],
        4: [x_ini4, y_ini4],
        }[x]

    for m in range(len(position)):
        x_ini = f(layer[m])[0];
        y_ini = f(layer[m])[1];
        xn = x_ini*math.cos((-1/2-position[m])*pitch) - y_ini*math.sin((-1/2-position[m])*pitch);
        yn = y_ini*math.cos((-1/2-position[m])*pitch) + x_ini*math.sin((-1/2-position[m])*pitch);
        femm.mi_addblocklabel(xn, yn);   						# add a new blocklabel at x,y
        femm.mi_selectlabel(xn, yn);     						# select the blocklabel closest to x,y
        femm.mi_setblockprop(name,0,Elemsize,"","",w_type,1);    # define the rotor 1 core properties
        femm.mi_clearselected();




def winding_positions_4layer(nslots, pole_pairs):
    position_PR =[]
    position_MR = []
    position_PY =[]
    position_MY = []
    position_PB =[]
    position_MB = []
    top_PR =[]
    top_MR =[]
    top_PY =[]
    top_MY =[]
    top_PB =[]
    top_MB = []


    pos_sring = "no yet"




    if ((nslots == 9) & (pole_pairs == 4)):
        pos_ori = 'aa|Ab|BB|bb|Bc|CC|cc|Ca|AA';
        pos_sring = pos_ori.replace('|', "")
        double_layer = True
    elif ((nslots == 15) & (pole_pairs == 5)):
        pos_ori = 'aB|bC|cA|aB|bC|cA|aB|bC|cA|aB|bC|cA|aB|bC|cA';
        pos_sring = pos_ori.replace('|', "")
        double_layer = True
    elif ((nslots == 27) & (pole_pairs == 2)):
        pos_ori = 'AA|AA|cc|cc|BB|BB|aa|aa|aC|CC|CC|bb|bb|AA|AA|cc|cc|cB|BB|BB|aa|aa|CC|CC|bb|bb|bA';
        pos_sring = pos_ori.replace('|', "")
        double_layer = True
    elif ((nslots == 9) & (pole_pairs == 14)):
        pos_ori = 'aa|Ac|CC|cc|Cb|BB|bb|Ba|AA';
        pos_sring = pos_ori.replace('|', "")
        double_layer = True
    elif ((nslots == 9) & (pole_pairs == 5)):
        pos_ori = 'aa|Ac|CC|cc|Cb|BB|bb|Ba|AA';
        pos_sring = pos_ori.replace('|', "")
        double_layer = True
    elif ((nslots == 9) & (pole_pairs == 4)):
        pos_ori = 'aa|Ab|BB|bb|Bc|CC|cc|Ca|AA';
        pos_sring = pos_ori.replace('|', "")
        double_layer = True
    elif ((nslots == 12) & (pole_pairs == 5)):
        pos_ori = 'aa|Ab|BB|bC|cc|Ca|AA|aB|bb|Bc|CC|cA';
        pos_sring = pos_ori.replace('|', "")
        double_layer = True
    elif ((nslots == 12) & (pole_pairs == 7)):
        # pos_ori = 'aC|cc|Cb|BB|bA|aa|Ac|CC|cB|bb|Ba|AA';
        # pos_ori = 'AA|aa|cc|CC|BB|bb|aa|AA|CC|cc|bb|BB';
        pos_ori = 'Cc|ca|aA|AB|Bb|bc|cC|CA|Aa|ab|bB|BC';


        pos_sring = pos_ori.replace('|', "")
        double_layer = True
    else:
        print('No slot and pole combinations!!');
        print('');
        print('No slot and pole combinations!!');


    print('pos_sring',pos_sring)






    if (double_layer):
        print('here')
        for m in range(nslots*2):
            if (pos_sring[m] =='A'):
                position_PR.append(math.floor(m/2)+1);
                if (m%2 == 0):
                    top_PR.append(2);
                else:
                    top_PR.append(1);
            elif (pos_sring[m] =='a'):
                position_MR.append(math.floor(m/2)+1);
                if (m%2 == 0):
                    top_MR.append(2);
                else:
                    top_MR.append(1);
            elif (pos_sring[m] =='B'):
                position_PY.append(math.floor(m/2)+1);
                if (m%2 == 0):
                    top_PY.append(2);
                else:
                    top_PY.append(1);
            elif (pos_sring[m] =='b'):
                position_MY.append(math.floor(m/2)+1);
                if (m%2 == 0):
                    top_MY.append(2);
                else:
                    top_MY.append(1);
            elif (pos_sring[m] =='C'):
                position_PB.append(math.floor(m/2)+1);
                if (m%2 == 0):
                    top_PB.append(2);
                else:
                    top_PB.append(1);
            elif (pos_sring[m] =='c'):
                position_MB.append(math.floor(m/2)+1);
                if (m%2 == 0):
                    top_MB.append(2);
                else:
                    top_MB.append(1);
        print('position_PR', position_PR)
        print('position_MR', position_MR)
        print('position_PY', position_PY)
        print('position_MY', position_MY)
        print('position_PB', position_PB)
        print('position_MB', position_MB)

        print('top_PR', top_PR)
        print('top_MR', top_MR)
        print('top_PY', top_PY)
        print('top_MY', top_MY)
        print('top_PB', top_PB)
        print('top_MB', top_MB)
        return position_PR, position_MR, position_PY, position_MY, position_PB, position_MB, top_PR, top_MR, top_PY, top_MY, top_PB, top_MB
    else:
        for m in range(nslots):
            if (pos_sring[m] =='A'):
                position_PR.append(m);
                position_PR.append(m);
                top_PR.append(2);
                top_PR.append(1);
            elif (pos_sring[m] =='a'):
                position_MR.append(m);
                position_MR.append(m);
                top_MR.append(2);
                top_MR.append(1);
            elif (pos_sring[m] =='B'):
                position_PY.append(m);
                position_PY.append(m);
                top_PY.append(2);
                top_PY.append(1);
            elif (pos_sring[m] =='b'):
                position_MY.append(m);
                position_MY.append(m);
                top_MY.append(2);
                top_MY.append(1);
            elif (pos_sring[m] =='C'):
                position_PB.append(m);
                position_PB.append(m);
                top_PB.append(2);
                top_PB.append(1);
            elif (pos_sring[m] =='c'):
                position_MB.append(m);
                position_MB.append(m);
                top_MB.append(2);
                top_MB.append(1);
        return position_PR, position_MR, position_PY, position_MY, position_PB, position_MB, top_PR, top_MR, top_PY, top_MY, top_PB, top_MB



def stator_construction_innerWithPM(w_hs,Rslotbase, slotwidth_top, Rslottop, R1out, R1in, opening_angle2 , opening_angle, slotpitch_deg,nslots, angle_hs, Hy1, n_sub, ang_pr):
        #Construction
    # Master slot first

    Elemsize=Hy1/10

    x1=w_hs
    y1=Rslotbase
    femm.mi_addnode(x1,y1)
    femm.mi_selectnode(x1,y1)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()


    x2=-w_hs
    y2=Rslotbase
    femm.mi_addnode(x2,y2)
    femm.mi_selectnode(x2,y2)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()
    x3=-slotwidth_top/2.
    y3=Rslottop
    femm.mi_addnode(x3,y3)
    femm.mi_selectnode(x3,y3)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()
    x4=slotwidth_top/2.
    y4=Rslottop
    femm.mi_addnode(x4,y4)
    femm.mi_selectnode(x4,y4)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()


    # add nodes to divide slot

    xs_mid = (x4+ x1)/2;
    ys_mid = (y4+ y1)/2;

    xs_mid2 = (xs_mid+ x1)/2;
    ys_mid2 = (ys_mid+ y1)/2;


    xs_mid3 = (x4+ xs_mid)/2;
    ys_mid3 = (y4+ ys_mid)/2;




    femm.mi_addnode(xs_mid,ys_mid)
    femm.mi_selectnode(xs_mid,ys_mid)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()
    femm.mi_addnode(-xs_mid,ys_mid)
    femm.mi_selectnode(-xs_mid,ys_mid)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()



    femm.mi_addnode(xs_mid2,ys_mid2)
    femm.mi_selectnode(xs_mid2,ys_mid2)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()
    femm.mi_addnode(-xs_mid2,ys_mid2)
    femm.mi_selectnode(-xs_mid2,ys_mid2)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()



    femm.mi_addnode(xs_mid3,ys_mid3)
    femm.mi_selectnode(xs_mid3,ys_mid3)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()
    femm.mi_addnode(-xs_mid3,ys_mid3)
    femm.mi_selectnode(-xs_mid3,ys_mid3)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()



    femm.mi_addsegment(x1,y1,x2,y2)
    xmean=(x1+x2)/2.
    ymean=(y1+y2)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)




    femm.mi_addsegment(x2,y2,x3,y3)
    xmean=(x2+x3)/2.
    ymean=(y2+y3)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
    femm.mi_addsegment(x3,y3,x4,y4)
    xmean=(x3+x4)/2.
    ymean=(y3+y4)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
    femm.mi_addsegment(x4,y4,xs_mid3,ys_mid3)
    xmean=(x4+xs_mid3)/2.
    ymean=(y4+ys_mid3)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)

    femm.mi_addsegment(x3,y3,-xs_mid3,ys_mid3)
    xmean=(x3-xs_mid3)/2.
    ymean=(y3+ys_mid3)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)

    femm.mi_addsegment(x1,y1,xs_mid2,ys_mid2)
    xmean=(x1+xs_mid2)/2.
    ymean=(y1+ys_mid2)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)

    femm.mi_addsegment(x2,y2,-xs_mid2,ys_mid2)
    xmean=(x2-xs_mid2)/2.
    ymean=(y2+ys_mid2)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)



    femm.mi_addsegment(xs_mid,ys_mid,xs_mid2,ys_mid2)
    xmean=(xs_mid+xs_mid2)/2.
    ymean=(ys_mid+ys_mid2)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)

    femm.mi_addsegment(-xs_mid,ys_mid,-xs_mid2,ys_mid2)
    xmean=(-xs_mid-xs_mid2)/2.
    ymean=(ys_mid+ys_mid2)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)


    femm.mi_addsegment(xs_mid,ys_mid,xs_mid3,ys_mid3)
    xmean=(xs_mid+xs_mid3)/2.
    ymean=(ys_mid+ys_mid3)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)


    femm.mi_addsegment(-xs_mid,ys_mid,-xs_mid3,ys_mid3)
    xmean=(-xs_mid-xs_mid3)/2.
    ymean=(ys_mid+ys_mid3)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)


    x7=-R1out*math.sin(opening_angle2)
    y7=R1out*math.cos(opening_angle2)
    femm.mi_addnode(x7,y7)
    femm.mi_selectnode(x7,y7)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()

    x8=R1out*math.sin(opening_angle2)
    y8=R1out*math.cos(opening_angle2)
    femm.mi_addnode(x8,y8)
    femm.mi_selectnode(x8,y8)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()

    x9=x7
    # y9=(R1out-Hp2/2)
    y9 = (y3+ y7)/2

    x10=x8
    # y10=(R1out-Hp2/2)
    y10 = (y4+ y8)/2
    femm.mi_addnode(x9,y9)
    femm.mi_selectnode(x9,y9)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()

    femm.mi_addnode(x10,y10)
    femm.mi_selectnode(x10,y10)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()


    femm.mi_addsegment(x3,y3,x9,y9)
    xmean=(x3+x9)/2.
    ymean=(y3+y9)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
    femm.mi_clearselected()
    femm.mi_addsegment(x4,y4,x10,y10)
    xmean=(x4+x10)/2.
    ymean=(y4+y10)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
    femm.mi_clearselected()
    femm.mi_addsegment(x9,y9,x7,y7)
    xmean=(x9+x7)/2.
    ymean=(y9+y7)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
    femm.mi_clearselected()
    femm.mi_addsegment(x10,y10,x8,y8)
    xmean=(x10+x8)/2.
    ymean=(y10+y8)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
    femm.mi_clearselected()
    x12=R1out*math.sin(angle_hs)
    y12=R1out*math.cos(angle_hs)
    delta=(angle_hs-opening_angle2)*180/math.pi
    femm.mi_addnode(x12,y12)
    femm.mi_selectnode(x12,y12)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()





    # add slot dividing lines

    femm.mi_addsegment(xs_mid,ys_mid,-xs_mid,ys_mid)
    xmean=0.
    ymean=ys_mid
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
    femm.mi_clearselected()


    femm.mi_addsegment(xs_mid2,ys_mid2,-xs_mid2,ys_mid2)
    xmean=0.
    ymean=ys_mid2
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
    femm.mi_clearselected()

    femm.mi_addsegment(xs_mid3,ys_mid3,-xs_mid3,ys_mid3)
    xmean=0.
    ymean=ys_mid3
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
    femm.mi_clearselected()

    #
    #
    x1_old = x8;
    y1_old = y8;
    for x in range(2*n_sub + 1):
        x1_t=R1out*math.sin(opening_angle2 + (x+1)* opening_angle)
        y1_t=R1out*math.cos(opening_angle2 + (x+1)*opening_angle)
        femm.mi_addnode(x1_t,y1_t)
        femm.mi_selectnode(x1_t,y1_t)
        femm.mi_setnodeprop("",1)
        femm.mi_clearselected()

        femm.mi_addarc(x1_t,y1_t,x1_old,y1_old,delta,ang_pr)
        xmean=(x1_t+x1_old)/2.
        ymean=(y1_t+y1_old)/2.
        femm.mi_selectarcsegment(xmean,ymean)
        femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,3)
        femm.mi_clearselected()
        x1_old = x1_t
        y1_old = y1_t


        print('x1', x1, y1)
        print('x2', x2, y2)
        print('x3', x3, y3)
        print('x4', x4, y4)


        print('x7', x7, y7)
        print('x8', x8, y8)
        print('x9', x9, y9)
        print('x10', x10, y10)






    # #create PM in slot


    p_thick = 2e-3 #PM thickness
    for x in range(n_sub):
        x1_t=R1out*math.sin(opening_angle2 + (2*x+2)* opening_angle)
        y1_t=R1out*math.cos(opening_angle2 + (2*x+2)*opening_angle)
        nx = -x1_t /(math.sqrt(x1_t*x1_t + y1_t*y1_t))
        ny = -y1_t /(math.sqrt(x1_t*x1_t + y1_t*y1_t))
        x2_t = x1_t + nx*p_thick;
        y2_t = y1_t + ny*p_thick;
        x3_t=R1out*math.sin(opening_angle2 + (2*x + 1)* opening_angle)
        y3_t=R1out*math.cos(opening_angle2 + (2*x+ 1)*opening_angle)
        nx = -x3_t /(math.sqrt(x3_t*x3_t + y3_t*y3_t))
        ny = -y3_t /(math.sqrt(x3_t*x3_t + y3_t*y3_t))
        x4_t = x3_t + nx*p_thick;
        y4_t = y3_t + ny*p_thick;
        femm.mi_addnode(x2_t,y2_t)
        femm.mi_selectnode(x2_t,y2_t)
        femm.mi_setnodeprop("",1)
        femm.mi_clearselected()



        femm.mi_addnode(x4_t,y4_t)
        femm.mi_selectnode(x4_t,y4_t)
        femm.mi_setnodeprop("",1)
        femm.mi_clearselected()

        femm.mi_addsegment(x2_t,y2_t,x4_t,y4_t)
        xmean=(x2_t+x4_t)/2.
        ymean=(y2_t+y4_t)/2.
        femm.mi_selectsegment(xmean,ymean)
        femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
        femm.mi_clearselected()
        femm.mi_addsegment(x3_t,y3_t,x4_t,y4_t)
        xmean=(x3_t+x4_t)/2.
        ymean=(y3_t+y4_t)/2.
        femm.mi_selectsegment(xmean,ymean)
        femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
        femm.mi_clearselected()
        femm.mi_addsegment(x2_t,y2_t,x1_t,y1_t)
        xmean=(x2_t+x1_t)/2.
        ymean=(y2_t+y1_t)/2.
        femm.mi_selectsegment(xmean,ymean)
        femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
        femm.mi_clearselected()
        femm.mi_addblocklabel((x1_t+x2_t+x3_t+x4_t)/4,(y1_t+y2_t+y3_t+y4_t)/4)                                    #defining the material of rotor 3 second PM
        femm.mi_selectlabel((x1_t+x2_t+x3_t+x4_t)/4,(y1_t+y2_t+y3_t+y4_t)/4)                # select the blocklabel closest to x,y
        dir = math.atan((y1_t+y2_t+y3_t+y4_t)/(x1_t+x2_t+x3_t+x4_t))*180/math.pi

        print('dir1', dir)




         # PM in slot setting #1
        # femm.mi_setblockprop("NdFeB32",1,ElemSize,0,dir,0,1)  # define rotor 3 core properties

    # PM in slot setting #2
        # femm.mi_setblockprop("NdFeB32",1,ElemSize,0,dir,0,1)  # define rotor 3 core properties
        # print('1', dir)

    # PM in slot setting #3
        femm.mi_setblockprop("air",0,Elemsize,"","",1,1)

    # PM in slot setting #4

        # femm.mi_setblockprop("NdFeB32",1,ElemSize,0,dir+90,0,1)  # define rotor 3 core properties




        femm.mi_copyrotate2(0.,0.,2*slotpitch_deg,nslots/2,2)
        femm.mi_clearselected()


        x_m = (x1_t+x2_t+x3_t+x4_t)/4
        y_m = (y1_t+y2_t+y3_t+y4_t)/4

        b_r = math.sqrt(x_m*x_m + y_m*y_m)
        #rotate by one slot
        x_m_new = x_m*math.cos(-slotpitch_deg*math.pi/180) - y_m*math.sin(-slotpitch_deg*math.pi/180)
        y_m_new = y_m*math.cos(-slotpitch_deg*math.pi/180) + x_m*math.sin(-slotpitch_deg*math.pi/180)
        femm.mi_addblocklabel(x_m_new,y_m_new)                                    #defining the material of rotor 3 second PM
        femm.mi_selectlabel(x_m_new,y_m_new)                # select the blocklabel closest to x,y
        dir2 = math.atan(y_m_new/x_m_new)*180/math.pi






    # PM in slot setting #1
        # femm.mi_setblockprop("NdFeB32",1,ElemSize,180,dir2,0,1)  # define rotor 3 core properties

    # PM in slot setting #2
        # femm.mi_setblockprop("NdFeB32",1,ElemSize,0,dir2,0,1)
        # print('2', dir)

    # PM in slot setting #3
        femm.mi_setblockprop("air",0,Elemsize,"","",1,1)



    # PM in slot setting #4
        # femm.mi_setblockprop("NdFeB32",1,ElemSize,0, dir2 + 90,0,1)



        femm.mi_copyrotate2(0.,0.,2*slotpitch_deg,nslots/2,2)
        femm.mi_clearselected()






        #Define iron coreback
    xlabel=0
    ylabel=(R1in+Rslotbase)/2
    femm.mi_addblocklabel(xlabel,ylabel)
    femm.mi_selectlabel(xlabel,ylabel)

    femm.mi_setblockprop("iron",0,Elemsize,"","",1,1)
    femm.mi_clearselected()

    res = []
    res.append(x1)
    res.append(y1)
    res.append(x4)
    res.append(y4)
    return (res)




def stator_construction_innerWithPM_single(w_hs,Rslotbase, slotwidth_top, Rslottop, R1out, R1in, opening_angle2 , opening_angle, slotpitch_deg,nslots, angle_hs, Hy1, n_sub, ang_pr):
        #Construction
    # Master slot first

    Elemsize=Hy1/10

    x1=w_hs
    y1=Rslotbase
    femm.mi_addnode(x1,y1)
    femm.mi_selectnode(x1,y1)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()


    x2=-w_hs
    y2=Rslotbase
    femm.mi_addnode(x2,y2)
    femm.mi_selectnode(x2,y2)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()
    x3=-slotwidth_top/2.
    y3=Rslottop
    femm.mi_addnode(x3,y3)
    femm.mi_selectnode(x3,y3)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()
    x4=slotwidth_top/2.
    y4=Rslottop
    femm.mi_addnode(x4,y4)
    femm.mi_selectnode(x4,y4)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()


    # add nodes to divide slot

    xs_mid = (x4+ x1)/2;
    ys_mid = (y4+ y1)/2;

    xs_mid2 = (xs_mid+ x1)/2;
    ys_mid2 = (ys_mid+ y1)/2;


    xs_mid3 = (x4+ xs_mid)/2;
    ys_mid3 = (y4+ ys_mid)/2;




    femm.mi_addnode(xs_mid,ys_mid)
    femm.mi_selectnode(xs_mid,ys_mid)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()
    femm.mi_addnode(-xs_mid,ys_mid)
    femm.mi_selectnode(-xs_mid,ys_mid)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()








    femm.mi_addsegment(x1,y1,x2,y2)
    xmean=(x1+x2)/2.
    ymean=(y1+y2)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)




    femm.mi_addsegment(x2,y2,x3,y3)
    xmean=(x2+x3)/2.
    ymean=(y2+y3)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
    femm.mi_addsegment(x3,y3,x4,y4)
    xmean=(x3+x4)/2.
    ymean=(y3+y4)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
    femm.mi_addsegment(x4,y4,xs_mid,ys_mid)
    xmean=(x4+xs_mid)/2.
    ymean=(y4+ys_mid)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)

    femm.mi_addsegment(x3,y3,-xs_mid,ys_mid)
    xmean=(x3-xs_mid)/2.
    ymean=(y3+ys_mid)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)

    femm.mi_addsegment(x1,y1,xs_mid,ys_mid)
    xmean=(x1+xs_mid)/2.
    ymean=(y1+ys_mid)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)

    femm.mi_addsegment(x2,y2,-xs_mid,ys_mid)
    xmean=(x2-xs_mid)/2.
    ymean=(y2+ys_mid)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)



    x7=-R1out*math.sin(opening_angle2)
    y7=R1out*math.cos(opening_angle2)
    femm.mi_addnode(x7,y7)
    femm.mi_selectnode(x7,y7)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()

    x8=R1out*math.sin(opening_angle2)
    y8=R1out*math.cos(opening_angle2)
    femm.mi_addnode(x8,y8)
    femm.mi_selectnode(x8,y8)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()

    x9=x7
    # y9=(R1out-Hp2/2)
    y9 = (y3+ y7)/2

    x10=x8
    # y10=(R1out-Hp2/2)
    y10 = (y4+ y8)/2
    femm.mi_addnode(x9,y9)
    femm.mi_selectnode(x9,y9)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()

    femm.mi_addnode(x10,y10)
    femm.mi_selectnode(x10,y10)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()


    femm.mi_addsegment(x3,y3,x9,y9)
    xmean=(x3+x9)/2.
    ymean=(y3+y9)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
    femm.mi_clearselected()
    femm.mi_addsegment(x4,y4,x10,y10)
    xmean=(x4+x10)/2.
    ymean=(y4+y10)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
    femm.mi_clearselected()
    femm.mi_addsegment(x9,y9,x7,y7)
    xmean=(x9+x7)/2.
    ymean=(y9+y7)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
    femm.mi_clearselected()
    femm.mi_addsegment(x10,y10,x8,y8)
    xmean=(x10+x8)/2.
    ymean=(y10+y8)/2.
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
    femm.mi_clearselected()
    x12=R1out*math.sin(angle_hs)
    y12=R1out*math.cos(angle_hs)
    delta=(angle_hs-opening_angle2)*180/math.pi
    femm.mi_addnode(x12,y12)
    femm.mi_selectnode(x12,y12)
    femm.mi_setnodeprop("",1)
    femm.mi_clearselected()





    # add slot dividing lines

    femm.mi_addsegment(xs_mid,ys_mid,-xs_mid,ys_mid)
    xmean=0.
    ymean=ys_mid
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
    femm.mi_clearselected()


    femm.mi_addsegment(xs_mid2,ys_mid2,-xs_mid2,ys_mid2)
    xmean=0.
    ymean=ys_mid2
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
    femm.mi_clearselected()

    femm.mi_addsegment(xs_mid3,ys_mid3,-xs_mid3,ys_mid3)
    xmean=0.
    ymean=ys_mid3
    femm.mi_selectsegment(xmean,ymean)
    femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
    femm.mi_clearselected()

    #
    #
    x1_old = x8;
    y1_old = y8;
    for x in range(2*n_sub + 1):
        x1_t=R1out*math.sin(opening_angle2 + (x+1)* opening_angle)
        y1_t=R1out*math.cos(opening_angle2 + (x+1)*opening_angle)
        femm.mi_addnode(x1_t,y1_t)
        femm.mi_selectnode(x1_t,y1_t)
        femm.mi_setnodeprop("",1)
        femm.mi_clearselected()

        femm.mi_addarc(x1_t,y1_t,x1_old,y1_old,delta,ang_pr)
        xmean=(x1_t+x1_old)/2.
        ymean=(y1_t+y1_old)/2.
        femm.mi_selectarcsegment(xmean,ymean)
        femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,3)
        femm.mi_clearselected()
        x1_old = x1_t
        y1_old = y1_t


        print('x1', x1, y1)
        print('x2', x2, y2)
        print('x3', x3, y3)
        print('x4', x4, y4)


        print('x7', x7, y7)
        print('x8', x8, y8)
        print('x9', x9, y9)
        print('x10', x10, y10)






    # #create PM in slot


    p_thick = 2e-3 #PM thickness
    for x in range(n_sub):
        x1_t=R1out*math.sin(opening_angle2 + (2*x+2)* opening_angle)
        y1_t=R1out*math.cos(opening_angle2 + (2*x+2)*opening_angle)
        nx = -x1_t /(math.sqrt(x1_t*x1_t + y1_t*y1_t))
        ny = -y1_t /(math.sqrt(x1_t*x1_t + y1_t*y1_t))
        x2_t = x1_t + nx*p_thick;
        y2_t = y1_t + ny*p_thick;
        x3_t=R1out*math.sin(opening_angle2 + (2*x + 1)* opening_angle)
        y3_t=R1out*math.cos(opening_angle2 + (2*x+ 1)*opening_angle)
        nx = -x3_t /(math.sqrt(x3_t*x3_t + y3_t*y3_t))
        ny = -y3_t /(math.sqrt(x3_t*x3_t + y3_t*y3_t))
        x4_t = x3_t + nx*p_thick;
        y4_t = y3_t + ny*p_thick;
        femm.mi_addnode(x2_t,y2_t)
        femm.mi_selectnode(x2_t,y2_t)
        femm.mi_setnodeprop("",1)
        femm.mi_clearselected()



        femm.mi_addnode(x4_t,y4_t)
        femm.mi_selectnode(x4_t,y4_t)
        femm.mi_setnodeprop("",1)
        femm.mi_clearselected()

        femm.mi_addsegment(x2_t,y2_t,x4_t,y4_t)
        xmean=(x2_t+x4_t)/2.
        ymean=(y2_t+y4_t)/2.
        femm.mi_selectsegment(xmean,ymean)
        femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
        femm.mi_clearselected()
        femm.mi_addsegment(x3_t,y3_t,x4_t,y4_t)
        xmean=(x3_t+x4_t)/2.
        ymean=(y3_t+y4_t)/2.
        femm.mi_selectsegment(xmean,ymean)
        femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
        femm.mi_clearselected()
        femm.mi_addsegment(x2_t,y2_t,x1_t,y1_t)
        xmean=(x2_t+x1_t)/2.
        ymean=(y2_t+y1_t)/2.
        femm.mi_selectsegment(xmean,ymean)
        femm.mi_copyrotate2(0.,0.,slotpitch_deg,nslots,1)
        femm.mi_clearselected()
        femm.mi_addblocklabel((x1_t+x2_t+x3_t+x4_t)/4,(y1_t+y2_t+y3_t+y4_t)/4)                                    #defining the material of rotor 3 second PM
        femm.mi_selectlabel((x1_t+x2_t+x3_t+x4_t)/4,(y1_t+y2_t+y3_t+y4_t)/4)                # select the blocklabel closest to x,y
        dir = math.atan((y1_t+y2_t+y3_t+y4_t)/(x1_t+x2_t+x3_t+x4_t))*180/math.pi

        print('dir1', dir)




         # PM in slot setting #1
        # femm.mi_setblockprop("NdFeB32",1,ElemSize,0,dir,0,1)  # define rotor 3 core properties

    # PM in slot setting #2
        # femm.mi_setblockprop("NdFeB32",1,ElemSize,0,dir,0,1)  # define rotor 3 core properties
        # print('1', dir)

    # PM in slot setting #3
        femm.mi_setblockprop("air",0,Elemsize,"","",1,1)

    # PM in slot setting #4

        # femm.mi_setblockprop("NdFeB32",1,ElemSize,0,dir+90,0,1)  # define rotor 3 core properties




        femm.mi_copyrotate2(0.,0.,2*slotpitch_deg,nslots/2,2)
        femm.mi_clearselected()


        x_m = (x1_t+x2_t+x3_t+x4_t)/4
        y_m = (y1_t+y2_t+y3_t+y4_t)/4

        b_r = math.sqrt(x_m*x_m + y_m*y_m)
        #rotate by one slot
        x_m_new = x_m*math.cos(-slotpitch_deg*math.pi/180) - y_m*math.sin(-slotpitch_deg*math.pi/180)
        y_m_new = y_m*math.cos(-slotpitch_deg*math.pi/180) + x_m*math.sin(-slotpitch_deg*math.pi/180)
        femm.mi_addblocklabel(x_m_new,y_m_new)                                    #defining the material of rotor 3 second PM
        femm.mi_selectlabel(x_m_new,y_m_new)                # select the blocklabel closest to x,y
        dir2 = math.atan(y_m_new/x_m_new)*180/math.pi






    # PM in slot setting #1
        # femm.mi_setblockprop("NdFeB32",1,ElemSize,180,dir2,0,1)  # define rotor 3 core properties

    # PM in slot setting #2
        # femm.mi_setblockprop("NdFeB32",1,ElemSize,0,dir2,0,1)
        # print('2', dir)

    # PM in slot setting #3
        femm.mi_setblockprop("air",0,Elemsize,"","",1,1)



    # PM in slot setting #4
        # femm.mi_setblockprop("NdFeB32",1,ElemSize,0, dir2 + 90,0,1)



        femm.mi_copyrotate2(0.,0.,2*slotpitch_deg,nslots/2,2)
        femm.mi_clearselected()






        #Define iron coreback
    xlabel=0
    ylabel=(R1in+Rslotbase)/2
    femm.mi_addblocklabel(xlabel,ylabel)
    femm.mi_selectlabel(xlabel,ylabel)

    femm.mi_setblockprop("iron",0,Elemsize,"","",1,1)
    femm.mi_clearselected()

    res = []
    res.append(x1)
    res.append(y1)
    res.append(x4)
    res.append(y4)
    return (res)
