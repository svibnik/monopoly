
from tkinter import *
from tkinter import ttk
from MonopolyConstants import *
import MonopolyConstants
import random
import time
def hide(widget,*args,**kwargs):
    try:
       widget = globals()[widget]
       pi = widget.place_info()
       pis[widget] = pi
       widget.place_forget()
    except KeyError:
       pi = widget.place_info()
       pis[widget] = pi
       widget.place_forget()
def hide_pack(widget):
    try:
        pi = widget.pack_info()
        pis[widget] = pi
        widget.pack_forget()
    except TclError:
        pass
def hide_grid(widget):
    pi = widget.grid_info()
    pis[widget] = pi
    widget.grid_forget()
def show(widget,*args,**kwargs):
    try:
       widget = globals()[widget]
       widget.place(pis[widget])
    except KeyError:
        widget.place(pis[widget])
def show_pack(widget):
    widget.pack(pis[widget])
def show_grid(widget):
    widget.grid(pis[widget])
def debt_update(player, amount, to):
    p_debts[player][to] += amount
    info['status'].configure(text='You cant afford to pay. Your debt increaced.')
    if(sum(p_debts[player].values()) > p_worths[player]):
        info['status'].configure(text='You are bankrupt!')
def transaction(player,amount):
    p_bals[player] += amount
    p_worths[player] += amount
    info[player + '_prop_box'].delete(0)
    info[player + '_prop_box'].insert(0, 'Player '+player[1]+' Balance: £{}'.format(p_bals[player]))
    info[player + '_prop_box'].delete(1)
    info[player + '_prop_box'].insert(1, 'Player '+player[1]+' Worth: £{}'.format(p_worths[player]))
def hide_enlarge():
    hide_pack(info['prop_enlarge_name'])
    hide_pack(info['prop_enlarge_gap'])
    hide_pack(info['prop_enlarge_cost'])
    hide_pack(info['prop_enlarge_rent'])
    hide_pack(info['prop_enlarge_rent1'])
    hide_pack(info['prop_enlarge_rent2'])
    hide_pack(info['prop_enlarge_rent3'])
    hide_pack(info['prop_enlarge_rent4'])
    hide_pack(info['prop_enlarge_rent5'])
    hide_pack(info['prop_enlarge_gap2'])
    hide_pack(info['prop_enlarge_hcost'])
    hide_pack(info['prop_enlarge_mortgage'])
    hide_grid(info['prop_enlarge'])
def show_enlarge():
    show_pack(info['prop_enlarge_name'])
    show_pack(info['prop_enlarge_gap'])
    show_pack(info['prop_enlarge_cost'])
    show_pack(info['prop_enlarge_rent'])
    show_pack(info['prop_enlarge_rent1'])
    show_pack(info['prop_enlarge_rent2'])
    show_pack(info['prop_enlarge_rent3'])
    show_pack(info['prop_enlarge_rent4'])
    show_pack(info['prop_enlarge_rent5'])
    show_pack(info['prop_enlarge_gap2'])
    show_pack(info['prop_enlarge_hcost'])
    show_pack(info['prop_enlarge_mortgage'])
    show_grid(info['prop_enlarge'])
def enlarge_update():
    prop = cur_pos[MonopolyConstants.cur_player]
    if(info[prop]['type'] == 'property'):
        show_enlarge()
        info['prop_enlarge_c'].configure(bg=info[prop]['colour'])
        info['prop_enlarge_name'].configure(text=prop)
        info['prop_enlarge_cost'].configure(text='Cost: £'+info[prop]['cost'])
        info['prop_enlarge_rent'].configure(text='Rent: £'+info[prop]['rent'])
        info['prop_enlarge_rent1'].configure(text='1 House: £'+info[prop]['rent1'])
        info['prop_enlarge_rent2'].configure(text='2 Houses: £'+info[prop]['rent2'])
        info['prop_enlarge_rent3'].configure(text='3 Houses: £'+info[prop]['rent3'])
        info['prop_enlarge_rent4'].configure(text='4 Houses: £'+info[prop]['rent4'])
        info['prop_enlarge_rent5'].configure(text='Hotel: £'+info[prop]['rent5'])
        info['prop_enlarge_hcost'].configure(text='House/Hotel Cost: £'+info[prop]['HCost'])
        info['prop_enlarge_mortgage'].configure(text='Mortgage: £'+info[prop]['mortgage'])
    elif(info[prop]['type'] == 'railroad'):
        show_enlarge()
        info['prop_enlarge_c'].configure(bg=info[prop]['colour'], highlightthickness=0)
        info['prop_enlarge_name'].configure(text=prop)
        info['prop_enlarge_cost'].configure(text='Cost: £'+info[prop]['cost'])
        info['prop_enlarge_rent'].configure(text='1 Railroad: £'+info[prop]['rent'])
        info['prop_enlarge_rent1'].configure(text='2 Railroads: £'+info[prop]['rent1'])
        info['prop_enlarge_rent2'].configure(text='3 Railroads: £'+info[prop]['rent2'])
        info['prop_enlarge_rent3'].configure(text='4 Railroads: £'+info[prop]['rent3'])
        info['prop_enlarge_rent4'].configure(text='')
        info['prop_enlarge_rent5'].configure(text='')
        info['prop_enlarge_hcost'].configure(text='')
        info['prop_enlarge_mortgage'].configure(text='Mortgage: £'+info[prop]['mortgage'])
    elif(info[prop]['type'] == 'utility'):
        show_enlarge()
        info['prop_enlarge_c'].configure(bg=info[prop]['colour'], highlightthickness=0)
        info['prop_enlarge_name'].configure(text=prop)
        info['prop_enlarge_cost'].configure(text='Cost: £'+info[prop]['cost'])
        info['prop_enlarge_rent'].configure(text='If 1 Utility owned then rent is\n 4 times amount\n shown on dice.')
        info['prop_enlarge_rent1'].configure(text='If 2 Utilities owned then rent is\n 10 times amount\n shown on dice.')
        info['prop_enlarge_rent2'].configure(text='')
        info['prop_enlarge_rent3'].configure(text='')
        info['prop_enlarge_rent4'].configure(text='')
        info['prop_enlarge_rent5'].configure(text='')
        info['prop_enlarge_hcost'].configure(text='')
        info['prop_enlarge_mortgage'].configure(text='Mortgage: £'+info[prop]['mortgage'])
    elif(info[prop]['type'] == 'chance'):
        show_enlarge()
        info['prop_enlarge_c'].configure(bg=info[prop]['colour'], highlightthickness=0)
        info['prop_enlarge_name'].configure(text='Chance')
        info['prop_enlarge_cost'].configure(text='')
        info['prop_enlarge_rent'].configure(text='')
        info['prop_enlarge_rent1'].configure(text='')
        info['prop_enlarge_rent2'].configure(text='')
        info['prop_enlarge_rent3'].configure(text='')
        info['prop_enlarge_rent4'].configure(text='')
        info['prop_enlarge_rent5'].configure(text='')
        info['prop_enlarge_hcost'].configure(text='')
        info['prop_enlarge_mortgage'].configure(text='')
    elif(info[prop]['type'] == 'community'):
        show_enlarge()
        info['prop_enlarge_c'].configure(bg=info[prop]['colour'], highlightthickness=0)
        info['prop_enlarge_name'].configure(text='Community Chest')
        info['prop_enlarge_cost'].configure(text='')
        info['prop_enlarge_rent'].configure(text='')
        info['prop_enlarge_rent1'].configure(text='')
        info['prop_enlarge_rent2'].configure(text='')
        info['prop_enlarge_rent3'].configure(text='')
        info['prop_enlarge_rent4'].configure(text='')
        info['prop_enlarge_rent5'].configure(text='')
        info['prop_enlarge_hcost'].configure(text='')
        info['prop_enlarge_mortgage'].configure(text='')
def isFree(prop):
    tot=1
    for i in po_props:
        if(i != MonopolyConstants.cur_player):
            if(prop not in po_props[i]):
                tot+=1
            else:
                ond = i
    if(tot==len(ps)):
        return True
    else:
        return ond
def rent(payer, payee, am):
    if(info[cur_pos[payer]]['type'] == 'property'):
        rentn='rent'+str(hs[cur_pos[payer]])
        if(rentn=='rent0'):
            rentn='rent'
        rentt = int(info[cur_pos[payer]][rentn])
    elif(info[cur_pos[payer]]['type'] == 'railroad'):
        t=0
        for i in po_props[payee]:
            if(info[i]['type'] == 'railroad'):
                t+=1
        if(t==1):
            rentt = int(info[cur_pos[payer]]['rent'])
        else:
            rentt = int(info[cur_pos[payer]]['rent'+str(t-1)])
    else:
        t=0
        for i in po_props[payee]:
            if(info[i]['type'] == 'utility'):
                t+=1
        if(t==1):
            rentt = 4*am
        else:
            rentt = 10*am
    if(p_bals[payer] >= rentt):
        info['status'].configure(text='You payed Player {} \n£{} in Rent!'.format(payee[1], rentt))
        transaction(payer,rentt*-1)
        transaction(payee,rentt)
    else:
        debt_update(payer, rentt)
def hide_house(wid):
    hide(wid)
def all_house(p):
    hide_house(info[p]['h1'])
    hide_house(info[p]['h2'])
    hide_house(info[p]['h3'])
    hide_house(info[p]['h4'])
def show_house(h, p):
    if(h==0):
        all_house(p)
        info[p]['h1'].place(pis[info[p]['h1']])
        info[p]['h1'].configure(bg='dark green')
        hide_house(info[p]['h1'])
    elif(h==5):
        all_house(p)
        info[p]['h1'].place(pis[info[p]['h1']])
        info[p]['h1'].configure(bg='dark red')
    else:
        for i in range(1, h+1):
            info[p]['h'+str(i)].place(pis[info[p]['h'+str(i)]])
def add_house(p):
    global hs
    hs[p] += 1
    if(hs[p]==6):
        hs[p]=0
    show_house(hs[p], p)
def hide_player(prop,*args,**kwargs):
    for player in args:
        hide(info[prop][player])
def show_player(prop,*args,**kwargs):
    for player in args:
        show(info[prop][player])
def hide_all_players(name):
    hide_player(name,'p1')
    hide_player(name,'p2')
def show_all_players(name):
    show_player(name,'p1')
    show_player(name,'p2')
def move_to_jail():
    hide_player(cur_pos[MonopolyConstants.cur_player],MonopolyConstants.cur_player)
    show_player('Just Vsitng',MonopolyConstants.cur_player+'_jail')
    cur_pos[MonopolyConstants.cur_player] = 'In Jail'
    p_in_j[MonopolyConstants.cur_player] = 0
def jail_checks(Free):
    if(p_in_j[MonopolyConstants.cur_player] == 4):
        Free = True
    if(Free):
        hide_player('Just Vsitng', MonopolyConstants.cur_player+'_jail')
        show_player('Just Vsitng', MonopolyConstants.cur_player)
        cur_pos[MonopolyConstants.cur_player] = 'Just Vsitng'
        del p_in_j[MonopolyConstants.cur_player]
        info['status'].configure(text='You are free from jail.')
        change_turn()
def pay_50():
    if(p_bals[MonopolyConstants.cur_player] >= 50):
        transaction(MonopolyConstants.cur_player,-50)
        jail_checks(True)
def checkEvents(am, current):
    prop = cur_pos[MonopolyConstants.cur_player]
    enlarge_update()
    if(info[prop]['type'] == 'property' or info[prop]['type'] == 'railroad' or info[prop]['type'] == 'utility'):
        other = isFree(cur_pos[MonopolyConstants.cur_player])
        if(other != True):
            rent(MonopolyConstants.cur_player, other, am)
        else:
            show_enlarge()
    else:
        hide_enlarge()
    lb = names.index(current)
    ub = names.index(current) + am
    for i in range(lb+1, ub+1):
        if(i >= len(names)):
            i -= 40
        if(names[i]=='Go'):
            transaction(MonopolyConstants.cur_player, 200)
            info['status'].configure(text='You passed Go collect £200')
            break
    if(prop == 'Go To Jail'):
        move_to_jail()
    elif(prop == 'In Jail'):
        jail_checks()
    if(prop == 'Super Tax'):
        transaction(MonopolyConstants.cur_player, -100)
        info['status'].configure(text='Pay £100 in Super Tax!')
    elif(prop == 'Income Tax'):
        transaction(MonopolyConstants.cur_player, -200)
        info['status'].configure(text='Pay £200 in Income Tax!')
def move_player(player, am, self,Free):
    global can_buy_right_now
    current=cur_pos[player]
    if(current != 'In Jail'):
        c = names.index(current)
        can_buy_right_now = False
        for i in range(am):
            hide_player(cur_pos[player],player)
            c+=1
            if(c>39):
                c-=40
            cur_pos[player] = names[c]
            show_player(cur_pos[player],player)
            self.update()
            time.sleep(0.3)
        info['status'].configure(text='You landed on {}.'.format(cur_pos[player]))
        can_buy_right_now = True
        checkEvents(am, current)
    else:
        jail_checks(Free)
def blank(x, s1, s2, s3, s4, s5, s6, s7, s8, s9):
           x.itemconfigure(s1,state='hidden')
           x.itemconfigure(s2,state='hidden')
           x.itemconfigure(s3,state='hidden')
           x.itemconfigure(s4,state='hidden')
           x.itemconfigure(s5,state='hidden')
           x.itemconfigure(s6,state='hidden')
           x.itemconfigure(s7,state='hidden')
           x.itemconfigure(s8,state='hidden')
           x.itemconfigure(s9,state='hidden')

def dnum(x, num, f1d, f2d, f3d, f4d, f5d, f6d, s1, s2, s3, s4, s5, s6, s7, s8, s9):
   blank(x, s1, s2, s3, s4, s5, s6, s7, s8, s9)
   for i in locals()['f'+str(num)+'d']:
       x.itemconfigure(i, state='normal')
   return num

def roll(self, s1, s2, s3, s4, s5, s6, s7, s8, s9, dice1, dice2, f1d, f2d, f3d, f4d, f5d, f6d, roll_label, Pturn, T):
   global last_player
   if(last_player == Pturn):
    if(len(ps)>1):
        info['status'].configure(text='End Turn to roll.')
    else:
       num1 = dnum(dice1, random.randint(1,6), f1d, f2d, f3d, f4d, f5d, f6d, s1, s2, s3, s4, s5, s6, s7, s8, s9)
       num2 = dnum(dice2, random.randint(1,6), f1d, f2d, f3d, f4d, f5d, f6d, s1, s2, s3, s4, s5, s6, s7, s8, s9)
       total = num1+num2
       roll_label.configure(text=str(total))
       if(num1==num2):
        Free = True
       else:
        Free = False
       self.update()
       time.sleep(0.5)
       move_player(Pturn,total, self,Free)
       last_player = 'p'+str(int(last_player[1])+1)
       if(last_player == 'p7'):
        last_player='p1'
   else:
       num1 = dnum(dice1, random.randint(1,6), f1d, f2d, f3d, f4d, f5d, f6d, s1, s2, s3, s4, s5, s6, s7, s8, s9)
       num2 = dnum(dice2, random.randint(1,6), f1d, f2d, f3d, f4d, f5d, f6d, s1, s2, s3, s4, s5, s6, s7, s8, s9)
       total = num1+num2
       roll_label.configure(text=str(total))
       if(num1==num2):
        Free = True
       else:
        Free = False
       self.update()
       time.sleep(0.5)
       move_player(Pturn,total, self,Free)
       last_player = 'p'+str(int(last_player[1])+1)
       if(last_player == 'p7'):
        last_player='p1'



def change_turn():
    global last_player
    if MonopolyConstants.cur_player in p_in_j:
        p_in_j[MonopolyConstants.cur_player] += 1
        jail_checks(False)
    MonopolyConstants.change_cur_player()
    if MonopolyConstants.cur_player in p_in_j:
        info['status'].configure(
            text='Roll doubles to be free.\n Pay £50 to be free.\n Wait 3 turns to be free.\n Turn {}/3.'.format(
                p_in_j[MonopolyConstants.cur_player]))
        show(info['pay_50_button'])
    else:
        temp = pis[info['pay_50_button']]
        hide(info['pay_50_button'])
        pis[info['pay_50_button']] = temp
    info['turn_label'].configure(text="Player {}'s turn".format(MonopolyConstants.cur_player[1]))
    if MonopolyConstants.cur_player == "p2":
        bot_turn()



def Buy(prop):
    global can_buy_right_now
    if(info[prop]['type'] == 'property' or info[prop]['type'] == 'railroad' or info[prop]['type'] == 'utility'):
        if(prop not in po_props[MonopolyConstants.cur_player]):
            if(isFree(prop) == True):
                if(can_buy_right_now):
                    if(p_bals[MonopolyConstants.cur_player] >= int(info[prop]['cost'])):
                        po_props[MonopolyConstants.cur_player].append(prop)
                        transaction(MonopolyConstants.cur_player,int(info[prop]['cost'])*-1)
                        p_worths[MonopolyConstants.cur_player] += int(info[prop]['mortgage'])
                        transaction(MonopolyConstants.cur_player,0)
                        info[MonopolyConstants.cur_player + '_prop_box'].insert(END, prop)
                        info[MonopolyConstants.cur_player + '_prop_box'].itemconfig(END, bg=info[prop]['colour'])
                        info['status'].configure(text='{} Bought for £{}'.format(prop, info[prop]['cost']))
                    else:
                        info['status'].configure(text='Not Enought Money!')
        else:
            info['status'].configure(text='Already Owned By You!')
    else:
        info['status'].configure(text="You can't buy this.")
def build():
    def check_group(col, prop):
        if(col != 'blue' and col != 'brown'):
            t=0
            for i in po_props[MonopolyConstants.cur_player]:
                if(info[i]['colour'] == col):
                    t+=1
            if(t==3):
                return True
            else:
                return False
        else:
            t=0
            for i in po_props[MonopolyConstants.cur_player]:
                if(info[i]['colour'] == col):
                    t+=1
            if(t==2):
                return True
            else:
                return False
    prop = cur_pos[MonopolyConstants.cur_player]
    col = info[prop]['colour']
    if(info[prop]['type'] == 'property'):
        if(p_bals[MonopolyConstants.cur_player]>=int(info[prop]['HCost'])):
            if(check_group(col, prop)):
                add_house(prop)
                transaction(MonopolyConstants.cur_player,int(info[prop]['HCost'])*-1)
            else:
                info['status'].configure(text='You need to own all the\n properties in the\n colour group to buy a house.')
        else:
            info['status'].configure(text='Not enought money.')
    else:
        info['status'].configure(text="You can't build here.")
last_player = 'p0'
can_buy_right_now = True


BOT_DIFFICULTY = "Normal"

def bot_turn():
    if MonopolyConstants.cur_player == "p2":
        if BOT_DIFFICULTY == "Easy":
            prop = cur_pos["p2"]
            if info[prop]['type'] in ['property', 'railroad', 'utility']:
                if isFree(prop) == True and p_bals["p2"] >= int(info[prop]['cost']):
                    Buy(prop)
        elif BOT_DIFFICULTY == "Normal":
            prop = cur_pos["p2"]
            if info[prop]['type'] in ['property', 'railroad', 'utility']:
                if isFree(prop) == True and p_bals["p2"] >= int(info[prop]['cost']):
                    if random.random() < 0.7:
                        Buy(prop)
        elif BOT_DIFFICULTY == "Hard":
            prop = cur_pos["p2"]
            if info[prop]['type'] in ['property', 'railroad', 'utility']:
                if isFree(prop) == True and p_bals["p2"] >= int(info[prop]['cost']):
                    color = info[prop]['colour']
                    count = sum(1 for p in po_props["p2"] if info[p]['colour'] == color)
                    if (color in ['brown', 'blue'] and count == 1) or \
                            (color not in ['brown', 'blue'] and count == 2) or \
                            info[prop]['type'] in ['railroad', 'utility']:
                        Buy(prop)
                    elif random.random() < 0.5:
                        Buy(prop)
        info['turn_label'].configure(text="Player {}'s turn".format(MonopolyConstants.cur_player[1]))

