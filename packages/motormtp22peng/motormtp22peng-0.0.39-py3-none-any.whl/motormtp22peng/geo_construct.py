
import femm
import math
import sys
# sys.path.append('G:/motor_computing/Modules_my')
from motormtp22peng import mods_my

def stator_construct(nslots, pr, pt, ph, nprofo, nprofi, nprofs, nproft, nprofts, nprofsw ,rso, rro, rsh, g0, rsi, yorkh):
    pole = 2*math.pi/nslots;

    poleh = rsi*math.sin(pr*pole/2 ); # half pole face width *)

    p1=[-rso*math.sin(pole/2),rso*math.cos(pole/2)];
    p2=[-(rso-yorkh)*math.sin(pole/2),(rso-yorkh)*math.cos(pole/2)];

    th = rso - 30e-3 - rsi;
    R1in=rso;
    p4 = [-poleh, rsi*math.cos(pr*pole/2 )]; # inner pole face start points
    p5 = [ - poleh, (rsi + ph*th) *math.cos(pr*pole/2 )]

    p3 = [-poleh, (rso-yorkh)*math.cos(pr*pole/2 )];


    # group id

    # rotor: 3
    # stator: 1
    # shaft: 2
    # air bridgG:/ 4




    p1=[-rso*math.sin(pole/2),rso*math.cos(pole/2)];





    # outer stator construction

    #outer arc*)
    thetad=(pole)/(nprofo-1);
    xh_end = None # end points
    yh_end = None # end points

    coun = None
    for x in range(nprofo):
        theta =pole/2 -x *thetad
        xh=(rso*math.sin(theta));
        yh=(rso*math.cos(theta));
        femm.mi_addnode(xh,yh);
        femm.mi_selectnode(xh,yh);
        femm.mi_setnodeprop("",1);
        femm.mi_clearselected();

        if coun is None:
            coun = "go";
            xh_old = xh;
            yh_old = yh;
        elif coun is not None:
            femm.mi_addsegment(xh_old, yh_old, xh, yh);
            mods_my.add_seg_prop(xh_old, yh_old, xh, yh,1);
            femm.mi_selectsegment(0.5*(xh_old+ xh), 0.5*(yh_old+ yh)) ; #  Boundary Conditions
            femm.mi_setsegmentprop("A=0", 1, 0, 0, 1);
            femm.mi_clearselected();



            xh_old = xh;
            yh_old = yh;








    #inner arc*)
    xhh = -p4[0];
    yhh = p4[1];

    thetad=(2*math.atan2(xhh,yhh))/(nprofi-1);
    print(thetad)
    coun = None
    for x in range(nprofi):
        theta =-math.atan2(xhh,yhh)+ ( x * thetad);
        xh=(rsi*math.sin(theta));
        yh=abs((rsi*math.cos(theta)));
        femm.mi_addnode(xh,yh);
        femm.mi_selectnode(xh,yh);
        femm.mi_setnodeprop("",1);
        femm.mi_clearselected();
        if coun is None:
            coun = "go";
            xh_old = xh;
            yh_old = yh;
            xh_end3 = xh;
            yh_end3 = yh;
        elif coun is not None:
            femm.mi_addsegment(xh_old, yh_old, xh, yh);
            mods_my.add_seg_prop(xh_old, yh_old, xh, yh,1);
            xh_old = xh;
            yh_old = yh;






    #teeth face arc*)
    xhh = -p5[0];
    yhh = p5[1];

    thetad=0.5*(1-pt)*(2*math.atan2(xhh,yhh))/(nproft-1);
    print(thetad)
    coun = None
    for x in range(nproft):
        theta =-math.atan2(xhh,yhh)+ ( x * thetad);
        xh=((rsi + ph*th)*math.sin(theta));
        yh=abs(((rsi + ph*th)*math.cos(theta)));
        femm.mi_addnode(xh,yh);
        femm.mi_selectnode(xh,yh);
        femm.mi_setnodeprop("",1);
        femm.mi_clearselected();
        femm.mi_addnode(-xh,yh);
        femm.mi_selectnode(-xh,yh);
        femm.mi_setnodeprop("",1);
        femm.mi_clearselected();
        if coun is None:
            coun = "go";
            xh_old = xh;
            yh_old = yh;
        elif coun is not None:
            femm.mi_addsegment(xh_old, yh_old, xh, yh);
            mods_my.add_seg_prop(xh_old, yh_old, xh, yh,1);
            femm.mi_addsegment(-xh_old, yh_old, -xh, yh);
            mods_my.add_seg_prop(-xh_old, yh_old, -xh, yh,1);
            xh_old = xh;
            yh_old = yh;
            xh_end = xh;
            yh_end = yh;


    # solve inner start point for inner york face
    # new vector v = (xh_end, yh_end + a)

    # math.atan2(y, x)


    v = rso - yorkh;
    a = math.sqrt(math.pow(v,2) - math.pow(xh_end,2)) - yh_end;


    thetad=(0.5*(pole - 2*abs(math.atan2(xh_end,yh_end + a))))/(nprofs-1);
    print(math.atan2(xh_end,yh_end + a))
    print('pole', pole);
    print('thetad', thetad);






    coun = None
    for x in range(nprofs):
        theta =pole/2 -x *thetad
        xh=((rso - yorkh)*math.sin(theta));
        yh=((rso - yorkh)*math.cos(theta));
        femm.mi_addnode(xh,yh);
        femm.mi_selectnode(xh,yh);
        femm.mi_setnodeprop("",1);
        femm.mi_clearselected();
        femm.mi_addnode(-xh,yh);
        femm.mi_selectnode(-xh,yh);
        femm.mi_setnodeprop("",1);
        femm.mi_clearselected();
        if coun is None:
            coun = "go";
            xh_old = xh;
            yh_old = yh;
        elif coun is not None:
            femm.mi_addsegment(xh_old, yh_old, xh, yh);
            mods_my.add_seg_prop(xh_old, yh_old, xh, yh,1);
            femm.mi_addsegment(-xh_old, yh_old, -xh, yh);
            mods_my.add_seg_prop(-xh_old, yh_old, -xh, yh,1);
            xh_old = xh;
            yh_old = yh;



    dis= a/(nprofts-1);
    coun = None;
    for x in range(nprofts-1):
        yh=yh_end+x*dis;
        if coun is None:
            coun = "go";
            yh_old = yh;
        elif coun is not None:
            femm.mi_addnode(xh_end,yh);
            femm.mi_selectnode(xh_end,yh);
            femm.mi_setnodeprop("",1);
            femm.mi_clearselected();
            femm.mi_addsegment(xh_end, yh_old, xh_end, yh);
            mods_my.add_seg_prop(xh_end, yh_old, xh_end, yh,1);
            femm.mi_addnode(-xh_end,yh);
            femm.mi_selectnode(-xh_end,yh);
            femm.mi_setnodeprop("",1);
            femm.mi_clearselected();
            femm.mi_addsegment(-xh_end, yh_old, -xh_end, yh);
            mods_my.add_seg_prop(-xh_end, yh_old, -xh_end, yh,1);
            yh_old = yh;
    femm.mi_addsegment(xh_end, yh_old, xh_end, yh_old + dis);
    mods_my.add_seg_prop(xh_end, yh_old, xh_end, yh_old + dis,1);
    femm.mi_addsegment(-xh_end, yh_old, -xh_end, yh_old + dis);
    mods_my.add_seg_prop(-xh_end, yh_old, -xh_end, yh_old + dis,1);

    # also obtain points on teeth side wall for future winding construction

    ts_p = {}; #store points of side wall

    dis= a/(nprofsw-1);
    coun = None;
    for x in [1,nprofsw-2]:
        yh=yh_end+x*dis;
        ts_p[x] =[-xh_end,yh];

    print('ts_p', ts_p);

    # add york side wall (one side only)

    dis= yorkh/(nprofs-1);
    coun = None;
    for x in range(nprofs-1):
        xh=((rso - yorkh + x*dis)*math.sin(-pole/2));
        yh=((rso - yorkh + x*dis)*math.cos(-pole/2));
        if coun is None:
            coun = "go";
            yh_old = yh;
            xh_old = xh;
        elif coun is not None:
            femm.mi_addnode(xh,yh);
            femm.mi_selectnode(xh,yh);
            femm.mi_setnodeprop("",1);
            femm.mi_clearselected();
            femm.mi_addsegment(xh_old, yh_old, xh, yh);
            mods_my.add_seg_prop(xh_old, yh_old, xh, yh,1);
            yh_old = yh;
            xh_old = xh;
    femm.mi_addsegment(xh_old, yh_old, xh_old+ dis*math.sin(-pole/2), yh_old + dis*math.cos(-pole/2));
    mods_my.add_seg_prop(xh_old, yh_old, xh_old+ dis*math.sin(-pole/2), yh_old + dis*math.cos(-pole/2),1);







    # add pole face side wall

    dis= ph*yorkh/(nprofts-1);
    thetas=abs(math.atan2(xh_end3,yh_end3))
    coun = None;
    for x in range(nprofts-1):
        xh=((rsi + x*dis)*math.sin(-thetas));
        yh=((rsi + x*dis)*math.cos(-thetas));
        if coun is None:
            coun = "go";
            yh_old = yh;
            xh_old = xh;
        elif coun is not None:
            femm.mi_addnode(xh,yh);
            femm.mi_selectnode(xh,yh);
            femm.mi_setnodeprop("",1);
            femm.mi_clearselected();
            femm.mi_addsegment(xh_old, yh_old, xh, yh);
            mods_my.add_seg_prop(xh_old, yh_old, xh, yh,1);
            femm.mi_addnode(-xh,yh);
            femm.mi_selectnode(-xh,yh);
            femm.mi_setnodeprop("",1);
            femm.mi_clearselected();
            femm.mi_addsegment(-xh_old, yh_old, -xh, yh);
            mods_my.add_seg_prop(-xh_old, yh_old, -xh, yh,1);
            yh_old = yh;
            xh_old = xh;
    femm.mi_addsegment(xh_old, yh_old, xh_old+ dis*math.sin(-thetas), yh_old + dis*math.cos(-thetas));
    mods_my.add_seg_prop(xh_old, yh_old, xh_old+ dis*math.sin(-thetas), yh_old + dis*math.cos(-thetas),1);
    femm.mi_addsegment(-xh_old, yh_old, -(xh_old + dis*math.sin(-thetas)), yh_old + dis*math.cos(-thetas));
    mods_my.add_seg_prop(-xh_old, yh_old, -(xh_old + dis*math.sin(-thetas)), yh_old + dis*math.cos(-thetas),1);

    res = [ts_p, p3, p4];

    return (res);



def shaft_construct(rso, rsh, n_div):


    femm.mi_addnode(0.,rsh);
    femm.mi_addnode(0.,-rsh);
    femm.mi_addarc(0.,rsh,0.,-rsh,180,n_div);
    femm.mi_addarc(0.,-rsh,0.,rsh,180,n_div);
    femm.mi_addblocklabel(0., 0.);                           # add a new blocklabel at x,y
    femm.mi_selectlabel(0., 0.);
    R1in = rso/10.;                             # select the blocklabel closest to x,y
    Elemsize=R1in/4;
    femm.mi_setblockprop("air",0,Elemsize,"","",1,2);    # define the rotor 1 core properties
    femm.mi_clearselected();


#end of function




def rotor_smpm(npr, rso,rro, rsh, yorkr_h, mag_h, mag_ratio, mag_span, poler_span,mags_ratio, n_div):
    R1in = rso/10.;

    p1=[(rro)*math.sin(mag_span/2),(rro)*math.cos(mag_span/2)]; # magnet surface
    femm.mi_addnode(p1[0],p1[1]);
    femm.mi_addnode(-p1[0],p1[1]);
    femm.mi_selectnode(p1[0],p1[1]);
    femm.mi_setnodeprop("",3);
    femm.mi_clearselected();
    femm.mi_selectnode(-p1[0],p1[1]);
    femm.mi_setnodeprop("",3);
    femm.mi_clearselected();



    femm.mi_addarc(p1[0],p1[1],-p1[0],p1[1],30,n_div);
    femm.mi_selectarcsegment(0.,p1[1]);
    femm.mi_setarcsegmentprop(5,"",0,3);
    femm.mi_copyrotate2(0, 0, poler_span*180/math.pi, npr, 3 );
    femm.mi_clearselected();

    p2=[(rro-mag_h)*math.sin(mag_span/2),(rro-mag_h)*math.cos(mag_span/2)];
    femm.mi_addnode(p2[0],p2[1]);
    femm.mi_addnode(-p2[0],p2[1]);
    femm.mi_selectnode(p2[0],p2[1]);
    femm.mi_setnodeprop("",3);
    femm.mi_clearselected();
    femm.mi_selectnode(-p2[0],p2[1]);
    femm.mi_setnodeprop("",3);
    femm.mi_clearselected();



    femm.mi_addarc(p2[0],p2[1],-p2[0],p2[1],30,n_div);
    femm.mi_selectarcsegment(0.,p2[1]);
    femm.mi_setarcsegmentprop(5,"",0,3);
    femm.mi_copyrotate2(0, 0, poler_span*180/math.pi, npr, 3 );
    femm.mi_clearselected();

    # create side points
    p3 =[ p2[0] + mags_ratio*(p1[0] - p2[0]), p2[1] + mags_ratio*(p1[1] - p2[1]) ];
    femm.mi_addnode(p3[0],p3[1]);
    femm.mi_addnode(-p3[0],p3[1]);
    femm.mi_selectnode(p3[0],p3[1]);
    femm.mi_setnodeprop("",3);
    femm.mi_clearselected();
    femm.mi_selectnode(-p3[0],p3[1]);
    femm.mi_setnodeprop("",3);
    femm.mi_clearselected();





    femm.mi_addsegment(p3[0],p3[1], p1[0], p1[1]);
    mods_my.add_seg_prop(p3[0],p3[1], p1[0], p1[1],3);
    femm.mi_addsegment(p3[0],p3[1], p2[0], p2[1]);
    mods_my.add_seg_prop(p3[0],p3[1], p2[0], p2[1],3);
    femm.mi_addsegment(-p3[0],p3[1], -p1[0], p1[1]);
    mods_my.add_seg_prop(-p3[0],p3[1], -p1[0], p1[1],3);
    femm.mi_addsegment(-p3[0],p3[1], -p2[0], p2[1]);
    mods_my.add_seg_prop(-p3[0],p3[1], -p2[0], p2[1],3);
    # add a point
    p4 =[ -p3[0]*math.cos(-poler_span) - p3[1]*math.sin(-poler_span), p3[1]*math.cos(-poler_span) - p3[0]*math.sin(-poler_span)];

    femm.mi_addnode(p4[0],p4[1]);
    femm.mi_selectnode(p4[0],p4[1]);
    femm.mi_setnodeprop("",3);
    femm.mi_clearselected();


    femm.mi_addsegment(p3[0],p3[1], p4[0], p4[1]);
    mods_my.add_seg_prop(p3[0],p3[1], p4[0], p4[1],3);



    femm.mi_seteditmode("group");
    femm.mi_selectgroup(3);
    femm.mi_copyrotate2(0, 0, -360/npr, npr, 4 );
    femm.mi_clearselected();



    x1 = 0.;
    y1 = rro-0.5*mag_h;
    xn = x1*math.cos(poler_span) - y1*math.sin(poler_span);
    yn = y1*math.cos(poler_span) + x1*math.sin(poler_span);
    femm.mi_addblocklabel(xn, yn);                           # add a new blocklabel at x,y
    femm.mi_selectlabel(xn, yn);                             # select the blocklabel closest to x,y
    Elemsize=R1in/4;
    femm.mi_setblockprop("NdFeB32",0,Elemsize,"",90 + 180*poler_span/math.pi,8,0);    # define the rotor 1 core properties
    femm.mi_clearselected();
                                       # clear previous selections

    femm.mi_seteditmode("group");
    femm.mi_selectgroup(8);
    femm.mi_copyrotate2(0, 0, -2*360/npr, npr/2, 4 );
    femm.mi_clearselected();

    x1 = 0.;
    y1 = rro-0.5*mag_h;
    femm.mi_addblocklabel(x1, y1);                           # add a new blocklabel at x,y
    femm.mi_selectlabel(x1, y1);                             # select the blocklabel closest to x,y
    Elemsize=R1in/4;
    femm.mi_setblockprop("NdFeB32",0,Elemsize,"",-90,9,0);    # define the rotor 1 core properties
    femm.mi_clearselected();

    femm.mi_seteditmode("group");
    femm.mi_selectgroup(9);
    femm.mi_copyrotate2(0, 0, -2*360/npr, npr/2, 4 );
    femm.mi_clearselected();


    x1 = 0.;
    y1 = 0.5*(rro+rsh);
    femm.mi_addblocklabel(x1, y1);                           # add a new blocklabel at x,y
    femm.mi_selectlabel(x1, y1);                             # select the blocklabel closest to x,y
    Elemsize=R1in/4;
    femm.mi_setblockprop("iron",0,Elemsize,"","",3,0);    # define the rotor 1 core properties
    femm.mi_clearselected();
    #femm.mi_modifymaterial("PlusRed",4,0.)
    #femm.mi_modifymaterial("MinusRed",4,0.)
    #femm.mi_modifymaterial("PlusYellow",4,0.)
    #femm.mi_modifymaterial("MinusYellow",4,0.)
    #femm.mi_modifymaterial("PlusBlue",4,0.)
    #femm.mi_modifymaterial("MinusBlue",4,0.)




    # relabel magnet's group number
    x1 = 0.;
    y1 = rro-0.5*mag_h;
    xn = x1*math.cos(poler_span) - y1*math.sin(poler_span);
    yn = y1*math.cos(poler_span) + x1*math.sin(poler_span);
    for x in range(math.floor(npr/2)):
        xnew = xn*math.cos(x*(math.pi/180)*(-2*360/npr)) - yn*math.sin(x*(math.pi/180)*(-2*360/npr));
        ynew = yn*math.cos(x*(math.pi/180)*(-2*360/npr)) + xn*math.sin(x*(math.pi/180)*(-2*360/npr));
        femm.mi_selectlabel(xnew, ynew);
        #femm.mi_deleteselectedlabels();
        femm.mi_setgroup(3);
        femm.mi_clearselected();

    x1 = 0.;
    y1 = rro-0.5*mag_h;
    xn = x1;
    yn = y1;
    for x in range(math.floor(npr/2)):
        xnew = xn*math.cos(x*(math.pi/180)*(-2*360/npr)) - yn*math.sin(x*(math.pi/180)*(-2*360/npr));
        ynew = yn*math.cos(x*(math.pi/180)*(-2*360/npr)) + xn*math.sin(x*(math.pi/180)*(-2*360/npr));
        femm.mi_selectlabel(xnew, ynew);
        #femm.mi_deleteselectedlabels();
        femm.mi_setgroup(3);
        femm.mi_clearselected();

    #end of function



def material_def():


    femm.mi_addmaterial('air',1.,1.,0.,0.,0.,0,0,0,0,0)
    femm.mi_addmaterial("NdFeB32", 1.099, 1.099, 890000, 0, 0.625)
    femm.mi_addmaterial("aluminum", 1, 1, 0, 0, 37.7)


    # first-set windings
    femm.mi_addmaterial("PlusRed", 1, 1, 0, 0, 59.6)
    femm.mi_addmaterial("MinusRed", 1, 1, 0, 0, 59.6)
    femm.mi_addmaterial("PlusYellow", 1, 1, 0, 0, 59.6)
    femm.mi_addmaterial("MinusYellow", 1, 1, 0, 0, 59.6)
    femm.mi_addmaterial("PlusBlue", 1, 1, 0, 0, 59.6)
    femm.mi_addmaterial("MinusBlue", 1, 1, 0, 0, 59.6)

    # second-set windings
    femm.mi_addmaterial("PlusRed2", 1, 1, 0, 0, 59.6)
    femm.mi_addmaterial("MinusRed2", 1, 1, 0, 0, 59.6)
    femm.mi_addmaterial("PlusYellow2", 1, 1, 0, 0, 59.6)
    femm.mi_addmaterial("MinusYellow2", 1, 1, 0, 0, 59.6)
    femm.mi_addmaterial("PlusBlue2", 1, 1, 0, 0, 59.6)
    femm.mi_addmaterial("MinusBlue2", 1, 1, 0, 0, 59.6)


    lam_d=0.5; # thickness of lamination
    lam_f=0.95; # lamination fill factor



    #
    femm.mi_addmaterial("iron", 5000,5000,0,0,2,lam_d,0, lam_f,0, 0,0)
    # #steel_1008
    femm.mi_addbhpoint("iron",0 ,    0 )
    femm.mi_addbhpoint("iron",0.2402 , 159.19999999999999)
    femm.mi_addbhpoint("iron",0.86539999999999995 , 318.30000000000001)
    femm.mi_addbhpoint("iron",1.1106 ,  477.5 )
    femm.mi_addbhpoint("iron",1.2458 ,  636.60000000000002)
    femm.mi_addbhpoint("iron",1.331  ,  795.79999999999995 )
    femm.mi_addbhpoint("iron",1.5  , 1591.5 )
    femm.mi_addbhpoint("iron",1.6000000000000001 , 3183.0999999999999)
    femm.mi_addbhpoint("iron",1.6830000000000001 ,  4774.6000000000004)
    femm.mi_addbhpoint("iron",1.7410000000000001 ,  6366.1999999999998 )
    femm.mi_addbhpoint("iron",1.78  ,  7957.6999999999998 )
    femm.mi_addbhpoint("iron",1.905 , 15915.5 )
    femm.mi_addbhpoint("iron",2.0249999999999999 , 31831)
    femm.mi_addbhpoint("iron",2.085 , 47746.5 )
    femm.mi_addbhpoint("iron",2.1299999999999999 , 63662)
    femm.mi_addbhpoint("iron",2.165 , 79577.5 )
    femm.mi_addbhpoint("iron",2.2799999999999998 ,  159155)
    femm.mi_addbhpoint("iron",2.4849999999999999 ,  318310 )
    femm.mi_addbhpoint("iron",2.5851000000000002 ,  397887 )


# end of function



def wall_construct(rw_o, rw_i, angle_w, ra_w, acr_dg, acr_dg2, np):

    R1in = rw_o/10.;


    # construct wall
    #rw_o  # wall outer
    #rw_i  # wall inner

    x = rw_o*math.sin(ra_w*2*math.pi/np/2);
    y = rw_o*math.cos(ra_w*2*math.pi/np/2);
    x1 = rw_o*math.sin(ra_w*2*math.pi/np/2 + (1-ra_w)*2*math.pi/np);
    y1 = rw_o*math.cos(ra_w*2*math.pi/np/2 + (1-ra_w)*2*math.pi/np);

    x_s = x*math.cos(0.1*acr_dg*math.pi/180) - y*math.sin(0.1*acr_dg*math.pi/180);
    y_s = y*math.cos(0.1*acr_dg*math.pi/180) + x*math.sin(0.1*acr_dg*math.pi/180);

    femm.mi_addnode(x,y);
    femm.mi_addnode(-x,y);
    femm.mi_selectnode(x,y);
    femm.mi_setgroup(55);
    femm.mi_clearselected();

    femm.mi_selectnode(-x,y);
    femm.mi_setgroup(55);
    femm.mi_clearselected();


    n_div = 6;
    femm.mi_addarc(x,y,-x,y,acr_dg,n_div);
    femm.mi_selectarcsegment(x_s,y_s)
    femm.mi_setarcsegmentprop(5,"",0,55)
    femm.mi_clearselected();

    femm.mi_addnode(x1,y1);
    femm.mi_selectnode(x1,y1);
    femm.mi_setgroup(55);
    femm.mi_clearselected();

    x_s = x1*math.cos(0.1*acr_dg*math.pi/180) - y1*math.sin(0.1*acr_dg*math.pi/180);
    y_s = y1*math.cos(0.1*acr_dg*math.pi/180) + x1*math.sin(0.1*acr_dg*math.pi/180);

    n_div = 6;
    femm.mi_addarc(x1,y1,x,y,acr_dg,n_div);
    femm.mi_selectarcsegment((x+x1)/2,(y+y1)/2)
    femm.mi_setarcsegmentprop(5,"",0,55)
    femm.mi_clearselected();




    xx = rw_i*math.sin(ra_w*2*math.pi/np/2) ;
    yy = rw_i*math.cos(ra_w*2*math.pi/np/2) ;
    xx1 = rw_i*math.sin(ra_w*2*math.pi/np/2 + (1-ra_w)*2*math.pi/np) ;
    yy1 = rw_i*math.cos(ra_w*2*math.pi/np/2 + (1-ra_w)*2*math.pi/np) ;


    # add air gap
    # femm.mi_addblocklabel(0., rw_i +0.0002);                           # add a new blocklabel at x,y
    # femm.mi_selectlabel(0., rw_i +0.0002);                             # select the blocklabel closest to x,y
    # Elemsize=R1in/4;
    # femm.mi_setblockprop("air",0,Elemsize,"","",1,0);    # define the rotor 1 core properties
    # femm.mi_clearselected();
    #
    #
    # femm.mi_addblocklabel(0., rsi -0.0001);                           # add a new blocklabel at x,y
    # femm.mi_selectlabel(0., rsi -0.0001);                             # select the blocklabel closest to x,y
    # Elemsize=R1in/4;
    # femm.mi_setblockprop("air",0,Elemsize,"","",1,0);    # define the rotor 1 core properties
    # femm.mi_clearselected();



    x_s = xx*math.cos(0.1*acr_dg2*math.pi/180) - yy*math.sin(0.1*acr_dg2*math.pi/180);
    y_s = yy*math.cos(0.1*acr_dg2*math.pi/180) + xx*math.sin(0.1*acr_dg2*math.pi/180);

    femm.mi_addnode(xx,yy);
    femm.mi_addnode(-xx,yy);
    femm.mi_selectnode(xx,yy);
    femm.mi_setgroup(55);
    femm.mi_clearselected();
    femm.mi_selectnode(-xx,yy);
    femm.mi_setgroup(55);
    femm.mi_clearselected();





    n_div = 6;
    femm.mi_addarc(xx,yy,-xx,yy,acr_dg2,n_div);
    femm.mi_selectarcsegment(x_s,y_s)
    femm.mi_setarcsegmentprop(5,"",0,55)
    femm.mi_clearselected();

    femm.mi_addnode(xx1,yy1);
    femm.mi_selectnode(xx1,yy1);
    femm.mi_setgroup(55);
    femm.mi_clearselected();


    x_s = xx1*math.cos(0.1*acr_dg2*math.pi/180) - yy1*math.sin(0.1*acr_dg2*math.pi/180);
    y_s = yy1*math.cos(0.1*acr_dg2*math.pi/180) + xx1*math.sin(0.1*acr_dg2*math.pi/180);


    n_div = 6;
    femm.mi_addarc(xx1,yy1,xx,yy,acr_dg2,n_div);
    femm.mi_selectarcsegment(x_s,y_s);
    femm.mi_setarcsegmentprop(5,"",0,55);
    femm.mi_clearselected();


    femm.mi_addsegment(-x, y, -xx, yy);
    mods_my.add_seg_prop(-x, y, -xx, yy,55);

    femm.mi_addsegment(x, y, xx, yy);
    mods_my.add_seg_prop(x, y, xx, yy,55);


    # add magnet

    ra_m = 0.1; # ratio of wall contain magnetic materials

    acr_dgm = 5;
    acr_dgm2 = 7;

    # top postion of magnet
    mag_off_top = 1e-3*0.1;
    mag_off_bot = 1e-3*0.5;


    xm = (rw_o-mag_off_top)*math.sin(ra_m*2*math.pi/np/2) ;
    ym = (rw_o-mag_off_top)*math.cos(ra_m*2*math.pi/np/2) ;


    # femm.mi_addnode(xm,ym);
    # femm.mi_addnode(-xm,ym);
    # n_div = 6;
    # femm.mi_addsegment(xm,ym,-xm,ym);
    # add_seg_prop(xm,ym,-xm,ym,88)





    xxm = (rw_i+mag_off_bot)*math.sin(ra_m*2*math.pi/np/2) ;
    yym = (rw_i+mag_off_bot)*math.cos(ra_m*2*math.pi/np/2) ;


    # femm.mi_addnode(xxm,yym);
    # femm.mi_addnode(-xxm,yym);
    # n_div = 6;
    # femm.mi_addsegment(xxm,yym,-xxm,yym);
    # add_seg_prop(xxm,yym,-xxm,yym,88)





    # add aluminum
    femm.mi_addblocklabel((x+xx+x1+xx1)/4, (y+yy+y1+yy1)/4);                           # add a new blocklabel at x,y
    femm.mi_selectlabel((x+xx+x1+xx1)/4, (y+yy+y1+yy1)/4);                             # select the blocklabel closest to x,y
    Elemsize=R1in/4;
    femm.mi_setblockprop("aluminum",0,Elemsize,"","",55,0);    # define the rotor 1 core properties
    femm.mi_clearselected();


    print('x',x);
    print('xx',xx);
    print('x1',x1);
    print('xx1',xx1);

    # add iron
    femm.mi_addblocklabel((x+xx)/2 -0.001 , (y+yy)/2);                           # add a new blocklabel at x,y
    femm.mi_selectlabel((x+xx)/2 -0.001, (y+yy)/2);                             # select the blocklabel closest to x,y
    Elemsize=R1in/4;
    femm.mi_setblockprop("iron",0,Elemsize,"","",55,0);    # define the rotor 1 core properties
    femm.mi_clearselected();



    # # put magnet label
    #
    # an_offset = 0.;
    # femm.mi_addblocklabel(0., (ym+yym)/2.);                           # add a new blocklabel at x,y
    # femm.mi_selectlabel(0., (ym+yym)/2.);                             # select the blocklabel closest to x,y
    # Elemsize=R1in/4;
    # femm.mi_setblockprop("iron",0,Elemsize,"","",88,0);    # define the rotor 1 core properties
    # femm.mi_copyrotate2(0, 0, 2*360/np, np-1, 2 );
    # femm.mi_clearselected();
    #
    # an_m = (360/np)*math.pi/180;
    # xm_new = 0.*math.cos(an_m) -  (ym+yym)/2.*math.sin(an_m);
    # ym_new = (ym+yym)/2.*math.cos(an_m) +  0.*math.sin(an_m);
    #
    # femm.mi_addblocklabel(xm_new, ym_new);                           # add a new blocklabel at x,y
    # femm.mi_selectlabel(xm_new, ym_new);                             # select the blocklabel closest to x,y
    # Elemsize=R1in/4;
    # femm.mi_setblockprop("iron",0,Elemsize,"","",88,0);    # define the rotor 1 core properties
    # femm.mi_copyrotate2(0, 0, 2*360/np, np-1, 2 );
    # femm.mi_clearselected();



    femm.mi_seteditmode("group");
    femm.mi_selectgroup(55);
    femm.mi_copyrotate2(0, 0, -360/np, np-1  , 4 );
    femm.mi_clearselected();

    femm.mi_seteditmode("group");
    femm.mi_selectgroup(55);
    femm.mi_setgroup(1);
    femm.mi_clearselected();
    #end of function
