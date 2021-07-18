from tkinter import *
import random
import webbrowser



## Hustle Database
rockerboy_hustle = ['Rockerboy','Played a small local gig',200,300,600,'No gigs of jobs to be had this week',0,100,300,'Played a big gig for a rich Corporate or Local Personality',300,500,800,'Got some royalties in for your most recent Data Pool download',300,500,800,'Opening act for a Big-Name group',300,500,800,'Personal appearance netted you a large fee.',200,300,600]
solo_hustle = ['Solo','Bodyguard work, low-end client.',100,200,500,'Bodyguard work, high-end client.',200,300,600,'Difficult hit or extration.',200,300,600,'Hired out as muscle to a Fixer, Corp, or Gang.',100,200,500,'Atrracted undue attention, had to lay low.',0,100,300,'Basic enforcer or hitmanwork for a local Corp.',100,200,500]
netrunner_hustle = ['Netrunner','Cracked a small system and sold the data', 100,200,500,'Cracked a major Corporate System and sold the data',200,300,600,'You got sidetracked and didn\'t hack anything this week.',0,100,300,'Found a valuable data cache in an abandoned system and sold it.',200,300,600,'Brought down a major system with ransomware and got paid off to uninstall it.',200,300,600,'Sabotaged or otherwised disabled a major system for a faceless client.',200,300,600]
tech_hustle = ['Tech','No Jobs this week.',0,100,300,'Rebuilt some tech you scavenged in the Combat Zone.',100,200,500,'Helped a client break into some place or installed security systems for a client.',200,300,600,'Did some modigications or repairs to some cybertech.',100,200,500,'Did some modifications or repairs to some weapons',100,200,500,'Sabotaged or otherwise disabled something for a client.',100,200,500]
medtech_hustle = ['Medtech','Patched up someone after a firefight.',100,200,500,'Sold cyberware from a "Failed" medical case.',200,300,600,'Helped Trauma Team on some backup work when they were overloaded',100,200,500,'Did some minor "free clinic" work for locals. You can\'t eat goodwill though.',0,100,300,'Did a major medical procedure for a very well-heeled client',200,300,600,'Designed and delivered medicenes or street drugs to a client',100,200,500]
media_hustle = ['Media','Wrote an expose that covered a major topic, made a big sale.',300,500,800,'Wrote a popular "puff piece" that got you some notice and some cash.',200,300,600,'Did some boring ad writing to pay the bills.',200,300,600,'Exposed a big story that got you a few enemies and some cash.',200,300,600,'No good stories or leads this week.',0,100,300,'Wrote an expose that blew the lid off a major topic.',300,500,800]
lawman_hustle = ['Lawman','Made a few minor busts, busines as usual.',100,200,500,'Got a reward from a grateful citizen. Or was it a bribe?',200,300,600,'Bust went bad, and it came out of your salary.',0,100,300,'Nothing much happened this week. Collected a paycheck and that was it.',100,200,500,'Pulled off a major drug or smuggling bust and gained a bonus from thee boss.',200,300,600,'Took down a big gang and got some of a "civil seizure" bonus.',200,300,600]
exec_hustle = ['Exec','Landed a moderate success on a project, earned a reward bonus',300,500,800,'Nothing much happened, and Corporate was unimpressed. Lost a bonus',0,100,300,'Collected a paycheck and that was it.',200,300,600,'Got some dirt on a rival and used it to score a bonus.',300,500,800,'Pulled of a major project success and gained a bonus from the Head Office.',300,500,800,'Took out a legitimate target that was threatning a job and took their funding.',200,300,600]
fixer_hustle = ['Fixer','Got a media some information for a good bribe',200,300,600,'Got a Rocker a good Gig for your 12% fee.',200,300,600,'Helped a client locate a desireable item they needed and got a cut.',200,300,600,'Deal went south; you\'re keeping your head down till it blows over.',0,100,300,'Got a Solo or a Netrunner a profitiable "job" and took your agency fee.',200,300,600,'Brought in a rare, illegal, or very hard item to get for a client.',300,500,800]
nomad_hustle = ['Nomad','Made a legit shipment.',100,200,500,'Protected a shipment',100,200,500,'Smuggled some small contraband.',100,200,500,'Smuggled a huge shipment.',200,300,600,'Delivered a client safely to a destination.',100 ,200,500,'Couldn\'t find work this week, legit or otherwise.',0,100,300]
roles = ['null',rockerboy_hustle,solo_hustle,netrunner_hustle,tech_hustle,medtech_hustle,media_hustle,lawman_hustle,exec_hustle,fixer_hustle,nomad_hustle]



## Critical HIt Tables. 

    #Body
body_injury = ['Dismembered Arm','Dismembered Hand','Collapsed Lung','Broken Ribs','Broken Arm','Foreign Object','Broken Leg','Torn Muscle','Spinal Injury','Crushed Fingers','Dismembered Leg']
body_effect = ["The Dismembered Arm is gone. You drop any items in that dismembered arm\'s hand immediately. Base Death Save Penalty is increased by 1.",'The Dismembered Hand is gone. You drop any items in the dismembered hand immediately. Base Death Save Penalty is increased by 1.','-2 to MOVE ( Min 1) Base Death Save Penalty is increased by 1.','At the end of every Turn where you move further than 4m/yds on foot you resuffer this Critical Injury\'s Bonus Damage directly to your Hit Points.','The Broken Arm cannot be used. You drop any items in that arms\'s hand immeadiately.','At the end of every Turn where you move further than 4m/yds on foot you resuffeer this Critical Injury\'s Bonus Damage directly to your Hit Points.','-4 to MOVE ( Min 1)','-2 to Melee Attacks','Next Turn, you cannot take an action, but you can still take a Move Action. Base Death Save Penalty is increased by1.','-4 to all Actions involving that hand','The Dismembered Leg is gone. -6 to MOVE (Min 1) You cannot dodge attacks. Base Death Save Penalty is increased by 1.']
body_quick = ['N/A','N/A','Paramedic DV 15','Paramedic DV13','Paramedic DV13','First Aid or Paramedic DV13','Paramedic DC13','First Aid or Paramedic DC13','Paramedic DV15','Paramedic DV13',' N/A']
body_treat = ['Surgery DV17','Surgery DV17','Surgery DV15','Paramedic DV15 or Surgery DV13','Paramedic DV15 or Surgery DV13','Quick Fix removes Injury Effect permanently','Paramedic DV15 or Surgery DV13','Quick Fix removes Injury Effect permanently','Surgery DV15','Surgery DV15','Surgery DV17']

    #Head
head_injury = ['Lost Eye','Brain Injury','Damaged Eye','Concussion','Broken Jaw','Foreign Object','Whiplash','Cracked Skull','Damaged Ear','Crushed Windpipe','Lost Ear']
head_effect = ['The Lost Eye is gone. -4 to Ranged attacks a& Perception Checks involving Vision. Base Death Save Pentaly is increased by 1.','-2 to all Actions. Base Death Save Pentaly is increased by 1.','-2 to Ranged attacks & Perception Checks involving vision.','-2 to all Actions','-4 to all Actions involving speech','At the end to every turn where you move further than 4m/yds on foot, you resuffer this Critical Injury\'s Bonus Damage directly to your Hit Points.','Base Death Save Pentaly is increased by 1.','Aimed Shots to your head multiply the damage that gets through your SP by 3 instead of 2. Base Death Save Pentaly is increased by 1.','Whenever you move further th an 4m/yds on foot in a Turn, you cannot take a Move Action on your next Turn. Additionally you take a -2 to Perception Checks involving Hearing.','You Cannot speak.Base Death Save Penalty is increased by 1.','The lost Ear is Gone. Whenever you move further than 4m/yds on foot in a turn you cannot take a Move action on your next turn. Additionally you take a -4 ot Perception Checks involving hearing. Base Death Save Pentaly is increased by 1.']
head_quick = ['N/A','N/A','Paramedic DV15','First Aid or Paramedic DV13','Paramedic DV13','First Aid or Paramedic DV13','Paramedic DV13','Paramedic DV15','Paramedic DV13','N/A','N/A']
head_treat = ['Surgery DV15','Surgery DV17','Surgery DV13','Quick Fix removes Injury Effect permenantly','Paramedic or Surgery DV13','Quick Fix removes Injury Effect permenantly','Paramedic or Surgery DV13','Surgery DV13','Paramedic or Surgery DV15','Surgery DV15','Surgery DV17']



# Main Window
root = Tk()
root.title('CyberDeck .1 Beta')
root.resizable(True,True)
root.columnconfigure(0,weight=1,pad=3)
##    root.columnconfigure(3,weight=1,pad=3)
##    root.columnconfigure(5,weight=1,pad=3)
##    root.columnconfigure(7,weight=1,pad=3)
##    root.columnconfigure(9,weight=1,pad=3)
root.rowconfigure(0,weight=1,pad=3)
root.rowconfigure(1,weight=1,pad=3)
root.rowconfigure(2,weight=1,pad=3)
root.rowconfigure(3,weight=1,pad=3)
root.rowconfigure(4,weight=1,pad=3)
root.rowconfigure(5,weight=1,pad=3)
##root.rowconfigure(0,weight=1,pad=3)

##    root.rowconfigure(2,weight=1,pad=3)
##




#root.geometry('250x300')


def launch_nightmarket():


    ## Night Market Tables


    goods_sold = ['null','Food and Drugs','Personal Electronics','Weapons and Armor','Cyberware','Clothing and Fasionware','Survival Gear']


    food_and_drugs = ['null','Cannded Goods 10eb (Cheap','Packacked Goods 10eb (Cheap)','Frozen Goods 10eb (Cheap)','Bags of Grain 20eb (Everyday)','Kibble Pack 10eb (Cheap)','Bags of Prepak 20 eb (Everyday)','Street Drugs of 20 eb or less','Poor Quality Alcohol 10eb (Cheap)','Alcohol 20eb (Everyday)','Exellent Quality Alcohol 100eb (Premium)','MRE 10eb (Cheap)','Live Chicken 50eb (Costly)','Live Fish 50eb (Costly)','Fresh Fruits 50eb Costly','Fresh Vegetables 50eb (Costly)','Root Vegetables 20eb (Everyday)','Live Pigs 100eb (Premium)','Exotic Fruits 100eb (Premium)','Exotic Vegetables 100eb (Premium)','Street Drugs of exactly 50eb']
    personal_electronics = ['null','Agent 100eb (Premium)','Programs or Hardware of 100eb or less','Audio Recorder 100eb (Premium)','Bug Detector 500eb (Expensive)','Chemical Analyzer 1,000eb (Very Expensive)','Computer 50eb (Costly','Cyberdeck 500eb (Expensive)','Disposable Cellphone 50eb (Costly)','Electric Guitar or Other Instrument 500eb (Expensive)','Programs or other Hardwarde of exactly 500eb','MedScanner 1,000eb (V. Expensive)','Homing Tracer 500eb','Radio Communicator 100eb','Techscanner 1,000eb (V Expensive)','Smart Glasses 500eb (Expensive)','Radar Detector 500eb (Expensive)','Scrambler/Descrambler 500eb (Expensive)','Radio Scanner/Music Player 50eb (Costly)','Braindance Viewer 1,000eb (V. Expensive)','Virtuality Goggles 100eb (Premium)']
    weapons_and_armor = ['null','Medium Pistol 50eb (Costly)','Heavy or V. Heavy Pistol 100eb (Premium)','SMG 100eb (Premium','Heavy SMG 100eb (Premium)','Shotgun 500eb (Expenseive)','Assault Rifle 500eb (Expensive)','Sniper Rifle 500eb (Expensive)','Bows or Crossbow 100eb (Premium)','Grenade Launcher or Rocker Launcher 500eb (Expensive)','Ammunition of 500eb or less','A Signgle Exotic Weapon of GMs Choice','Light Melee Weapon 50eb (Costly)','Medium Melee Weapon 50eb (Costly)','Heavy Melee Weapon 100eb (Prmeium)',' V. Heavy Melee Weapon 100eb (Premium)',' Armor of 100eb or Less','Armor of exactly 500eb','Armor of Exactly 1,000eb','Weapon Attachments of 100eb or less','Weapon Attachments of 500eb or higher']
    cyberware = ['null','Cybereye 100eb (Premium)','Cyberaudio Suite  500eb (Expensive)','Neural Link 500eb (Expensive)','Cyberarm 500eb (Expensive)','Cyberleg 100eb (Premium)','External Cyberware of exactly 1,00eb','External Cyberware of 500eb or less','Internal Cyberware of exactly 1,000eb','Internal Cyberware of 500eb or less','Cybereye Option of exactly 1,000eb','Cybereye Option of 500eb or less','Cyberaudio Option of exactly 1,000eb','Cyberaudio Option of 500eb or less','Neuralware Option of exactly 1,000eb','Neuralware option of 500eb or less','Cyberlimb Option of eactly 1,000eb','Cyberlimb Option of 500eb or less','Fashionware of GMs Choice','Borgware of GMs Choice','Any Cyberware of Gms Choice']
    clothing = ['null','Bag Lady Chic','Gang Colors','Generic Chic','Bohemian','Leisurewear','Nomad Leathers','Asia Pop','Urban Flash','Business Wear','High Fashion','Biomonitor 100eb (Premium','Chemskin 100eb (Premium)','EMP Threading 10eb (Cheap)','Light Tattoo 100eb (Premium)','Shift Tacts 100eb (Premium)','Skinwatch 100eb (Premium)','Techhair 100eb (Premium)','Generic Chic','Leisurewear','Gang Colors']
    survival_gear = ['null','Anti-Smog Breathing Mask 20eb (Everyday)','Auto Level Dampening Ear Protectors 1,000eb (V. Expensive)','Binoculars 50eb (Costly)','Carryall 20eb (Everyday)','Flashlight 20eb (Everyday)','Duct Tape 20eb (Everyday)','Inflatable Bed & Sleep-Bag 20eb (Everyday)','Lock Picking Set 20eb (Everyday)','Handcuffs 50eb (Costly)','Medtech Bag 100eb (Premium)','Tent and Camping Equipment 50eb (Costly)','Rope 60m/yds 20eb (Everyday)','Techtool 100eb(Premium)','Personal CarePak 20eb (Everyday)','Radiation Suit 1,000eb (V. Expensive)','Road Flare 10eb (Cheap)','Grapple Gun 100eb (Premium)','Tech Bag 500eb (Expensive)','Shovel or Axe 50eb (Costly)','Airhypo 50eb (Costly)']



    shelf1=[]
    shelf2=[]
    roll1 = random.randint(1,6)
    roll2 = roll1
    while roll1 == roll2:
        
        roll2 = random.randint(1,6)


    type1 = random.randint(1,10)
    type2 = random.randint(1,10)


    if roll1 == 1:
        shelf1 = food_and_drugs
        store1 = goods_sold[1]
    elif roll1 ==2:
        shelf1 = personal_electronics
        store1 = goods_sold[2]
    elif roll1 ==3:
        shelf1 = weapons_and_armor
        store1 = goods_sold[3]
    elif roll1 ==4:
        shelf1 = cyberware
        store1 = goods_sold[4]
    elif roll1 ==5:
        shelf1 = clothing
        store1 = goods_sold[5]
    elif roll1 ==6:
        shelf1 = survival_gear
        store1 = goods_sold[6]

    if roll2 == 1:
        shelf2 = food_and_drugs
        store2 = goods_sold[1]
    elif roll2 ==2:
        shelf2 = personal_electronics
        store2 = goods_sold[2]
    elif roll2 ==3:
        shelf2 = weapons_and_armor
        store2 = goods_sold[3]
    elif roll2 ==4:
        shelf2 = cyberware
        store2 = goods_sold[4]
    elif roll2 ==5:
        shelf2 = clothing
        store2 = goods_sold[5]
    elif roll2 ==6:
        shelf2 = survival_gear
        store2 = goods_sold[6]

    product1 = []
    product2 =[]
   ## print(shelf1)
  ##  print(shelf2)

    x=1
    while x<= type1:
      ##  print(len(shelf1))
        product1.append(shelf1.pop(random.randint(1,len(shelf1)-1)))
        x=x+1

    x=1
    while x<=type2:
    ##    print(len(shelf2))
        product2.append(shelf2.pop(random.randint(1,len(shelf2)-1)))
        x=x+1

        # pad product offerings
    while len(product1)<10:
        product1.append(' ')

    while len(product2)<10:
        product2.append(' ')
        


    market=Toplevel()
    market.title('Night Market')

    market.resizable(True,True)
    market.columnconfigure(1,weight=1,pad=3)
    market.columnconfigure(3,weight=1,pad=3)
    market.rowconfigure(2,weight=1,pad=3)
    market.rowconfigure(3,weight=1,pad=3)
    market.rowconfigure(4,weight=1,pad=3)
    market.rowconfigure(5,weight=1,pad=3)
    market.rowconfigure(6,weight=1,pad=3)
    market.rowconfigure(7,weight=1,pad=3)
    market.rowconfigure(8,weight=1,pad=3)
    market.rowconfigure(9,weight=1,pad=3)
    market.rowconfigure(10,weight=1,pad=3)
    market.rowconfigure(11,weight=1,pad=3)
    market.rowconfigure(13,weight=1,pad=3)
    

    toplbl = Label(market, bg='red',fg='white', font='bold',text='Night Market').grid(row=0,column=0,columnspan=6,sticky=NSEW)


    bd=Label(market,bg='red').grid(row=1,column=0,rowspan=14,sticky=NSEW)
    goods=Label(market,bg='red',fg='white',font='bold',text=store1).grid(row=1,column=1,sticky=NSEW)
    bd=Label(market,bg='red').grid(row=1,column=2,rowspan=14,sticky=NSEW)
    goods=Label(market,bg='red',fg='white',font='bold',text=store2).grid(row=1,column=3,sticky=NSEW)
    bd=Label(market,bg='red').grid(row=1,column=5,rowspan=14,sticky=NSEW)

    r=2
    i=0
    while i<10:
        if r%2==0:
            bck='white'

        elif r%2==1:
            bck='pink'
                
        product=Label(market,bg=bck,text=product1[i]).grid(row=r,column=1,sticky=NSEW)
        product=Label(market,bg=bck,text=product2[i]).grid(row=r,column=3,sticky=NSEW)
        
        r+=1
        i+=1

    bd=Label(market,bg='red').grid(row=12,column=0,columnspan=6,sticky=NSEW)
    ref=Label(market,justify='left',bg='white',text=' Melee Weapons \t \t \t Page 340 \n Ranged Weapons \t  \t Page 341 \n Weapon Qualities & Examples \t Page 342 \n Weapon Attachments  \t \t Page 342 \n Ammunition  \t  \t \t Page 344 \n Exotic Weapons \t  \t  \t Page 347 \n Armor  \t  \t \t  \t Page 350 \n General Gear \t  \t \t Page 351').grid(row=13,column=1,sticky=NSEW)
    ref=Label(market,justify='left',bg='white',text=' Fashion \t   \t  \t Page 356 \n Street Drugs \t \t Page 357 \n Cyberware  \t \t Page 358 \n Cyberdeck Hardware \t Page 368 \n Programs  \t \t Page 368 \n Home Defenses  \t \t Page 372 \n Services & Entertainment \t Page 376 \n Lifestyle & Housing \t Page 377').grid(row=13,column=3,sticky=NSEW)
    bd=Label(market,bg='red').grid(row=14,column=0,columnspan=6,sticky=NSEW)
    market.mainloop()
                
        

def launch_crits():

    root=Toplevel()
    root.title('Crit')
    roll = random.randint(1,6)+random.randint(1,6)
    
   
    root.title('Critical Injuries Table')

    root.resizable(True,True)
    root.columnconfigure(1,weight=1,pad=3)
    root.columnconfigure(3,weight=1,pad=3)
    root.columnconfigure(5,weight=1,pad=3)
    root.columnconfigure(7,weight=1,pad=3)
    root.columnconfigure(9,weight=1,pad=3)
    root.rowconfigure(1,weight=1,pad=3)
    root.rowconfigure(2,weight=1,pad=3)


    body1=StringVar(root)
    body2=StringVar(root)
    body3=StringVar(root)
    body4=StringVar(root)
    body1.set(body_injury[roll-2])
    body2.set(body_effect[roll-2])
    body3.set(body_quick[roll-2])
    body4.set(body_treat[roll-2])
    head1=StringVar(root)
    head2=StringVar(root)
    head3=StringVar(root)
    head4=StringVar(root)
    head1.set(head_injury[roll-2])
    head2.set(head_effect[roll-2])
    head3.set(head_quick[roll-2])
    head4.set(head_treat[roll-2])




    def reroll():

        roll = random.randint(1,6)+random.randint(1,6)
        body1.set(body_injury[roll-2])
        body2.set(body_effect[roll-2])
        body3.set(body_quick[roll-2])
        body4.set(body_treat[roll-2])

        head1.set(head_injury[roll-2])
        head2.set(head_effect[roll-2])
        head3.set(head_quick[roll-2])
        head4.set(head_treat[roll-2])
        root.geometry("")
        
        



    vert_line4=Label(root,bg='red').grid(row=0,column=0,sticky=NSEW)
    title_label=Label(root,wraplength=200,font='bold', fg='white',bg='red',text='Area').grid(row=0,column=1,sticky=NSEW)
    vert_line1=Label(root,bg='red').grid(row=0,column=2,sticky=NSEW,)
    injury_label=Label(root,wraplength=200,font='bold', fg='white',bg='red',text='Injury').grid(row=0,column=3,sticky=NSEW)
    vert_lin2e=Label(root,bg='red').grid(row=0,column=4,sticky=NSEW)
    effect_label=Label(root,wraplength=200, font='bold',fg='white',bg='red',text='Injury Effect').grid(row=0,column=5,sticky=NSEW)
    vert_line3=Label(root,bg='red').grid(row=0,column=6,sticky=NSEW)
    quick_label=Label(root,wraplength=200, font='bold',fg='white',bg='red',text='Quick Fix').grid(row=0,column=7, sticky=NSEW)
    vert_line4=Label(root,bg='red').grid(row=0,column=8,sticky=NSEW)
    treat_label=Label(root,wraplength=200, fg='white',font='bold',bg='red',text='Treatment').grid(row=0,column=9,sticky=NSEW)
    vert_line4=Label(root,bg='red').grid(row=0,column=10,sticky=NSEW)




    ##  This creates the Body Section

    vert_line=Label(root,bg='red').grid(row=1,column=0,sticky=NSEW)
    body_label = Label(root,wraplength =200,bg='white',text='Body').grid(row=1,column=1,sticky=NSEW)
    vert_line=Label(root,bg='red').grid(row=1,column=2,sticky=NSEW)
    body_injury_l =Label(root,wraplength =200,bg='white',textvariable=body1).grid(row=1,column=3,sticky=NSEW)
    vert_line=Label(root,bg='red').grid(row=1,column=4,sticky=NSEW)
    body_effect_l =Label(root,wraplength =200,bg='white',textvariable=body2).grid(row=1,column=5,sticky=NSEW)
    vert_line=Label(root,bg='red').grid(row=1,column=6,sticky=NSEW)
    body_quick_l =Label(root,wraplength =200,bg='white',textvariable=body3).grid(row=1,column=7,sticky=NSEW)
    vert_line=Label(root,bg='red').grid(row=1,column=8,sticky=NSEW)
    body_treat_l =Label(root,bg='white',wraplength =200,textvariable=body4).grid(row=1,column=9,sticky=NSEW)
    vert_line=Label(root,bg='red').grid(row=1,column=10,sticky=NSEW)

    # This creates the Head Section

    vert_line=Label(root,bg='red').grid(row=2,column=0,sticky=NSEW)
    head_label = Label(root,bg='pink',wraplength =200,text='Head').grid(row=2,column=1,sticky=NSEW)
    vert_line=Label(root,bg='red').grid(row=2,column=2,sticky=NSEW)
    head_injury_l =Label(root,bg='pink',wraplength =200,textvariable=head1).grid(row=2,column=3,sticky=NSEW)
    vert_line=Label(root,bg='red').grid(row=2,column=4,sticky=NSEW)
    head_effect_l =Label(root,bg='pink',wraplength =200,textvariable=head2).grid(row=2,column=5,sticky=NSEW)
    vert_line=Label(root,bg='red').grid(row=2,column=6,sticky=NSEW)
    head_quick_l =Label(root,bg='pink',wraplength =200,textvariable=head3).grid(row=2,column=7,sticky=NSEW)
    vert_line=Label(root,bg='red').grid(row=2,column=8,sticky=NSEW)
    head_treat_l =Label(root,bg='pink',wraplength =200,textvariable=head4).grid(row=2,column=9,sticky=NSEW)
    vert_line=Label(root,bg='red').grid(row=2,column=10,sticky=NSEW)


    horizon_break =Label(root,bg='red').grid(row=3,column=0,columnspan=11,sticky=NSEW)


    critical_note = Label(root,bg='white',wraplength=200,text='All Critical Injuries cause Injury Effect and deal 5 Bonus Damage directly to targets Hit Points').grid(row=4,column=3)
    reroll_btn = Button(root,text='ReRoll Table',command=reroll).grid(row=4,column=5,sticky=NSEW)
    ref_note =Label(root,bg='white',wraplength=250,text='Critical Injuries Ref. Page 187 Core book. \n Quick Fix & Treatments Ref. Page 223 Core Book').grid(row=4, column=7,columnspan=4,sticky=NSEW)


    root.mainloop()        


def launch_net():
##
    

    def main_net():
            
        if difficulty == 1:

            floor_diff = basic_floor

        elif difficulty == 2:

            floor_diff = standard_floor

        elif difficulty == 3:

            floor_diff = uncommon_floor

        elif difficulty == 4:

            floor_diff = advanced_floor




        floor_list=[]
        avail_floors =total_floors-2

        i=branches

        if branches !=0:

            while i>0:

                this_branch = avail_floors - random.randint(1,avail_floors)

                if this_branch != 0:
                    floor_list.append(this_branch)

                avail_floors = avail_floors-this_branch
                i=i-1

            if avail_floors != 0:

                floor_list.append(avail_floors)

        else:

            floor_list.append(avail_floors)

        floor_list.sort()
        floor_list.reverse()

        floor_list[0]=floor_list[0]+2

        all_floors=['***Main Branch***']

        b=0

        for x in floor_list:

            i=1
            if b != 0:

                all_floors.append('***Side Branch***')
            while i<=x:

                all_floors.append(floor_diff[roll()-2])
                i+=1
            b+=1
            

            
        r=1
        c=0


        net=Toplevel()
        net.title('Net Architecture')
        net.minsize(300,300)
        net.resizable(True,True)
        
        net.columnconfigure(1,weight=1,pad=3)
        
        net.columnconfigure(3,weight=1,pad=3)
        



        title = Label(net,bg='red',fg='white',font='bold', text='Net Architecture').grid(row=0,column=0,columnspan=5,sticky=NSEW)

        i=0
        flr=1
        ##print(all_floors)
        while i<len(all_floors):

            if all_floors[i]=='***Main Branch***':
                mlbl=Label(net,bg='red',fg='white',font='bold',text=all_floors[i]).grid(row=r,column=0,columnspan=5,sticky=NSEW)
                i+=1
                r+=1
            elif all_floors[i]=='***Side Branch***':
                
                slbl=Label(net,bg='red',fg='white',font='bold',text=all_floors[i]).grid(row=r,column=0,columnspan=5,sticky=NSEW)
                flr=1
                i+=1
                r+=1
                
            else:

                if flr%2==0:
                    bck='pink'
                else:
                    bck='white'
                net.rowconfigure(r,weight=1,pad=3)

                bd=Label(net,bg='red').grid(row=r,column=0,sticky=NSEW)
                floor=Label(net,bg=bck,text=('Floor: '+str(flr))).grid(row=r,column=1,sticky=NSEW)
                bd=Label(net,bg='red').grid(row=r,column=2,sticky=NSEW)
                event=Label(net,bg=bck,text=all_floors[i]).grid(row=r,column=3,sticky=NSEW)
                bd=Label(net,bg='red').grid(row=r,column=4,sticky=NSEW)
                i+=1
                r+=1
                flr=flr+1
           ## print(i)

        # Correct first two lobby floors
        event=Label(net,bg='white',text=lobby_floor[random.randint(1,6)]).grid(row=2,column=3,sticky=NSEW)
        event=Label(net,bg='pink',text=lobby_floor[random.randint(1,6)]).grid(row=3,column=3,sticky=NSEW)

        # Bottom Border

        bd=Label(net,bg='red').grid(row=r,column=0,columnspan=5,sticky=NSEW)
        ref=Label(net,bg='white',text='Programs Pg. 202 \n Black Ice Pg 206 \n Demons Pg 212').grid(row=r+1,column=0, columnspan=5,sticky=NSEW)


        
        
        
        
          




        net.mainloop()


    ##  Arch Data
    lobby_floor = ['null','File DV6','Password DV6','Password DV8','Skunk','Wisp','Killer']
    basic_floor =['null','Hellhound','Sabertooth','Raven x2','Hellhound','Wisp','Raven','Password DV6', 'File DV6','Control Node DV 6','Password DV6','Skunk','Asp','Scorpion','Killer, Skunk','Wisp x3','Liche']
    standard_floor =['null','Hellhound x2','Hellhound, Killer','Skunk x2','Sabertooth','Scorpion','Hellhound','Password DV8','File DV 8','Control Node DV8','Password DV8','Asp','Killer','Liche','Asp','Raven x3','Liche,Raven']
    uncommon_floor =['null','Kraken','Hellhound, Scorpion','Hellound, Killer','Raven x2','Sabertooth','Hellhound','Password DV10','File DV10','Control Node DV10','Password DV10','Killer','Liche','Dragon','Asp, Raven','Dragon, Wisp','Giant']
    advanced_floor =['null','Hellhound x3','Asp x2','Hellhound, Liche','Wisp x3','Hellhound, Sabertooh','Kraken','Password DV12','File DV12','Control Node DV12','Password DV12','Giant','Dragon','Killer, Scorpion','Kraken','Raven, Wisp, Hellhound','Dragon x2']


    def roll():
        dice=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
        return dice


    net1=Toplevel()
    net1.title('Net Architecture')




    levels=IntVar(net1)
    branch=IntVar(net1)

    def man_gen():

        global difficulty
        global total_floors
        global branches
        
        difficulty=v.get()

        if difficulty == 1:

            floor_diff = basic_floor

        elif difficulty == 2:

            floor_diff = standard_floor

        elif difficulty == 3:

            floor_diff = uncommon_floor

        elif difficulty == 4:

            floor_diff = advanced_floor

        total_floors=levels.get()
        branches=branch.get()

        main_net()


    def ran_gen():


        global difficulty
        global total_floors
        global branches
        
        total_floors=roll()
        branches = 0
        branch_chance = random.randint(1,10)

        while branch_chance > 6:
            branches=branches+1
            branch_chance = random.randint(1,10)
          
       
        set_list =[1,2,3,4]
        difficulty = random.choices(set_list,weights=(10,50,30,10))
        difficulty=difficulty[0]   


       ## print(difficulty)
       ## print(total_floors)
       ## print(branches)
       
        main_net()
            

        
            

    v=IntVar()
    v.set(1)
    titlelbl=Label(net1,text='Choose Generation Method').grid(row=0,column=0,sticky=NSEW,columnspan=3)
    ranbtn=Button(net1,text='Random Generation',command=ran_gen).grid(row=1,column=3,sticky=NSEW,columnspan=1,rowspan=7)

    levlbl=Label(net1,text='Levels').grid(row=1,column=1,sticky=NSEW)
    levent=Entry(net1,textvariable=levels).grid(row=1,column=2,sticky=NSEW)
    branlbl=Label(net1,text='Branches').grid(row=2,column=1,sticky=NSEW)
    branent=Entry(net1,textvariable=branch).grid(row=2,column=2)

    radiodiff1=Radiobutton(net1, text='Basic Difficulty',variable=v, value=0).grid(row=3,column=1)
    radiodiff2=Radiobutton(net1, text='Standard Difficulty',variable=v, value=1).grid(row=4,column=1)
    radiodiff2=Radiobutton(net1, text='Uncommon Difficulty',variable=v, value=2).grid(row=5,column=1)
    radiodiff2=Radiobutton(net1, text='Advanded Difficulty',variable=v, value=3).grid(row=6,column=1)

    manbtn=Button(net1,text='Manual Generation',command=man_gen).grid(row=7,column=1,sticky=NSEW,columnspan=2)

    
    net1.mainloop()






        



##
def launch_hustle():

    New_window=Toplevel()
    New_window.title('Hustles')

    New_window.resizable(True,True)
    New_window.columnconfigure(1,weight=1,pad=3)
    New_window.columnconfigure(3,weight=1,pad=3)
    New_window.columnconfigure(5,weight=1,pad=3)
    New_window.columnconfigure(7,weight=1,pad=3)
    New_window.columnconfigure(9,weight=1,pad=3)
    New_window.rowconfigure(0,weight=1,pad=3)
    
    
    
    
    lblVert=Label(New_window,bg='red').grid(row=0,column=0,rowspan=11,sticky=NSEW)
    lbl1=Label(New_window,bg='red',font='bold',fg='white',text='Role').grid(row=0,column=1,sticky=NSEW)
    lblVert=Label(New_window,bg='red').grid(row=0,column=2,rowspan=11,sticky=NSEW)
    lbl2=Label(New_window,bg='red',font='bold',fg='white',text='What did you do to \n make bank that week').grid(row=0,column=3,sticky=NSEW)
    lblVert=Label(New_window,bg='red').grid(row=0,column=4,rowspan=11,sticky=NSEW)
    lbl2=Label(New_window,bg='red',font='bold',fg='white',text='Role Ability Rank 1-4').grid(row=0,column=5,sticky=NSEW)
    lblVert=Label(New_window,bg='red').grid(row=0,column=6,rowspan=11,sticky=NSEW)
    lbl2=Label(New_window,bg='red',font='bold',fg='white',text='Role Ability Rank 5-7').grid(row=0,column=7,sticky=NSEW)
    lblVert=Label(New_window,bg='red').grid(row=0,column=8,rowspan=11,sticky=NSEW)
    lbl2=Label(New_window,bg='red',font='bold',fg='white',text='Role Ability Rank 8-10').grid(row=0,column=9,sticky=NSEW)
    lblVert=Label(New_window,bg='red').grid(row=0,column=10,rowspan=11,sticky=NSEW)

    i=1

    r=1
    c=1
    while i<11:

        ran=random.randint(0,5)

        if i%2==0:
            back='pink'
        if i%2==1:
            back='white'
        New_window.rowconfigure(r,weight=1,pad=3)
        
        lbl=Label(New_window,bg=back,text=roles[i][0]).grid(row=r,column=1,sticky=NSEW)
        banklbl=Label(New_window,bg=back,text=roles[i][ran*4+1]).grid(row=r,column=3,sticky=NSEW)        
        role1=Label(New_window,bg=back,text=roles[i][ran*4+2]).grid(row=r,column=5,sticky=NSEW)        
        role2=Label(New_window,bg=back,text=roles[i][ran*4+3]).grid(row=r,column=7,sticky=NSEW)        
        role3=Label(New_window,bg=back,text=roles[i][ran*4+4]).grid(row=r,column=9,sticky=NSEW)
        
        r+=1
        i+=1
    
    btmbdr=Label(New_window,bg='red').grid(row=r+1,column=0,sticky=NSEW,columnspan=11)

    New_window.mainloop()


# Button activation


def callback():

    webbrowser.open(webbrowser.open("https://ko-fi.com/renkov"))



def about_button():
    about =Toplevel()
    about.title('About')
    aboutlbl = Label(about, text='This program was written in Python 3.8. It is not intended for commericial use.')
    kofiabout = Label(about, text='Programmed by R. Clark.')
    kofibtn = Button(about, text='Support us on Kofi', command=callback)

    aboutlbl.pack()
    kofiabout.pack()
    kofibtn.pack()


    about.mainloop()
                      
                      
    



#button menus

btn = Button(root,width=15, text='Hustles', command=launch_hustle).grid(column=0,row=0,sticky=NSEW)
btn2 = Button(root, width=15,text='Night Market', command=launch_nightmarket).grid(column=0,row=1,sticky=NSEW)
btn3 = Button(root,width=15, text='Critical Hits',command=launch_crits).grid(column=0,row=2,sticky=NSEW)
btn4= Button(root, width=15,text='Net Arch. ', command=launch_net ).grid(column=0,row=3,sticky=NSEW)
btn5 =Button(root, width=15,text='About',command=about_button).grid(column=0,row=4,sticky=NSEW)
btn6 =Button(root, width=15,text='Exit', command=root.destroy).grid(column=0,row=5,sticky=NSEW)
root.minsize(300,300)
              







root.mainloop()
