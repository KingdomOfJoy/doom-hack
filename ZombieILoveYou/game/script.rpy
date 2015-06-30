# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
$import os
# Declare characters used by this game.
define april = Character('April', color="#c8ffc8")
define jess = Character('Jess', color="#c8ffc8")
define clyde = Character('Clyde', color="#c8ffc8")
define riley = Character('Riley', color="#c8ffc8")
define matt = Character('Matt', color="#c8ffc8")

image opening picture im1 = "1.jpg"
image opening picture im3 = "3.jpg"
image opening picture im4 = "4.jpg"
image opening picture im5 = "5.jpg"
image opening picture im6 = "6.jpg"
image opening picture im7 = "7.jpg"
image opening picture im9 = "9.jpg"
image opening picture im10 = "10.jpg"
image opening picture im11 = "11.jpg"
image opening picture im12 = "12.jpg"
image opening picture im13 = "13.jpg"
image opening picture im14 = "14.jpg"
image opening picture im15 = "15.jpg"
image opening picture im16 = "16.jpg"
image opening picture im18 = "18.jpg"
image opening picture im19 = "19.jpg"
image opening picture im20 = "20.jpg"
image opening picture im21 = "21.jpg"
image opening picture im22 = "22.jpg"

image bg episode1 = "episode1.png"
image bg episode2 = "episode2.png"
image bg dead = "dead.png"

image april neutral = "april_neutral.png"
image jess neutral = "jess_neutral.png"
image clyde neutral = "clyde_neutral.png"
image matt neutral = "matt_neutral.png"

image bg garage = "garage.jpg"
image bg office = "office.jpg"
image bg oilpump = "oilpump.jpg"
image bg supermarket = "supermarket.jpg"

image opening picture title_1 = "zombie_logo_0.jpg"
image opening picture title_2 = "zombie_logo_1.jpg"


label splashscreen:
    play sound "siren.wav" noloop fadeout 1.0 fadein 1.0
    scene opening picture im16
    $renpy.pause(3)
    $renpy.music.stop(channel='sound', fadeout=1)
    $renpy.music.set_volume(0.1, delay=0, channel='music')
    $renpy.music.set_volume(2.0, delay=3, channel='voice')
    scene opening picture im1
    play music "wind.wav" noloop fadein 1.0
    play voice "intro_speech.wav" noloop
    scene opening picture im1
    $renpy.pause(2)
    scene opening picture im3
    $renpy.pause(2)
    scene opening picture im4
    $renpy.pause(2)
    scene opening picture im5
    $renpy.pause(2)
    scene opening picture im6
    $renpy.pause(2)
    scene opening picture im7
    $renpy.pause(2)
    scene opening picture im9
    $renpy.pause(2)
    scene opening picture im10
    $renpy.pause(2)
    scene opening picture im11
    $renpy.pause(2)
    scene opening picture im12
    $renpy.pause(2)
    scene opening picture im13
    $renpy.pause(2)
    scene opening picture im14
    $renpy.pause(2)
    scene opening picture im15
    $renpy.pause(2)
    scene opening picture im18
    $renpy.pause(2)
    scene opening picture im20
    $renpy.pause(2)
    scene opening picture im21
    $renpy.pause(2)
    scene opening picture im22
    $renpy.pause(2)
    
    show opening picture title_1
    $renpy.pause(1)
    scene opening picture title_2
    $renpy.pause(1)
    $renpy.music.stop(channel='music', fadeout=1)
    return
    
# The game starts here.
label start:
   
label l1:
    scene bg episode1
    play music "wind.wav" loop fadein 1.0 fadeout 1.0
    riley "Arrgh! How long it been since I saw a live zombie being for the last time? A week ago? A month ago? I can’t recall a thing!"
    riley "This radiation complete screwed my brains! BTW some brains now would be nice!"
    riley "Wait! It seems there is something ahead!"
    
label l2:    
    scene bg oilpump
    riley "{i}I’ve rushed with all my might. The structures ahead
    turned out to be an old oil well with a couple cabins around. The pump seemed to be still working. I’ve wondered whether there is anyone around.{/i}"
    
label l3:
    #$renpy.music.set_volume(1.0, delay=0, channel='music')
    $renpy.music.set_volume(0.3, delay=0, channel='music')
    play music "april.mp3" loop fadein 1.0 fadeout 1.0
    show april neutral at left: 
        zoom 1.3
    april "Hey! Where do you think you’re going? This is restricted territory! And who the hell are you in the first place?"


menu:

    "Yikes! Jeez, you’ve scared me! My name is Riley, and I'm lost.":
        jump l5
    "Who the hell are YOU? And why do you scream on me?":
        jump l14


#label l4:
#    riley "Yikes! Jeez, you’ve scared me! My name is Riley, and I'm lost."
    
label l5:
    scene bg oilpump
    show april neutral at left: 
        zoom 1.3
    april "Sorry! Doen't mean to scare you, but you know after the calamity all kinds of creatures are lurking around."
    april "Ah, I'm April by the way."

menu:

    "What is this place anyway, April":
        jump l7
    "April, what a lame name for a zombie! So what's the matter with this god-forsaken place?":
        jump l12
    
#label l6:
#    riley "What is this place anyway, April?"
    
label l7:
    show april neutral at left: 
        zoom 1.3
    april "Oh! that's an oil-pumping station! The calamity shook it up re-e-eal good! 
           But the equipment survived somehow, nevertheless. So here four of us (Matt, Jess, Clyde and me) are working to keep the oil flowing."
    april "Anyway? Do you want something?"
    
menu:

    "To be honest, I'm really hungry, to the point that my brain cells are dying from starvation. Ha-ha! If only I had any.":
        jump l9
    "Don't know how to tell you, but want to get out from here as soon as possible.":
        jump l10
    
#label l8:
#    riley "To be honest, I'm really hungry, to the point that my brain cells are dying from starvation. Ha-ha! If only I had any."


label l9:
    show april neutral at left: 
        zoom 1.3
    april "Oh, that means you need to see Jess - our cook! But be careful, she is cookoo alright!"
    #Go to Jess #1 scene
    jump l18
    
label l10:
    #riley "Don't know how to tell you, but want to get out from here as soon as possible."
    april "Well, I wish you could stay longer, but anyway - the only person with a car here is our driver - Matt. You should go talk to him, maybe he knows how to help you."
    #Go to Matt #1 scene
    jump l41

#label l11:
#    riley "April, what a lame name for a zombie! So what's the matter with this god-forsaken place?"
    
label l12:
    april "Why you little! That's an oil-pumping staion, you dumb-ass!  I'm no talking to you anymore!
           Idiot! Riley, what a stupid name! Never met anyone smart with a name Riley! Go talk to Clyde, you two idiots worth each other! "
    #Go to Clyde #1 scene
    jump l64
    
#label l13:
#    riley "Who the hell are YOU? And why do you scream on me?"

label l14:
    april "Pfft! Doncha think you are acting too snarky for a stranger?"

menu:

    "Sorry, this radiation really screwed my brains, especially since I'm lost and scared. My name is Riley!":
        jump l15
    "Why do you care, stranger? Who's the boss here anywhere?":
        jump l17
    
label l15:
    #riley "Sorry, this radiation really screwed my brains, especially since I'm lost and scared. My name is Riley!"
    #Go back to label 5
    jump l5
    
#label l16:
#    riley "Why do you care, stranger?"
#    riley "Who's the boss here anywhere?"
    
label l17:
    # todo: make it look angry! :)
    show april neutral at left: 
        zoom 1.3
    april "WTF? Are you nuts, dude? Just came here from god-knows-where and already trying to boss around?"
    april "There, idiot! Go to Clyde! You two seems to worth each other..."
    #Go to Clyde #1 scene
    jump l64
    
label l18:
    scene bg supermarket
    $renpy.music.set_volume(0.5, delay=0, channel='music')
    play music "jess.mp3" loop fadein 1.0 fadeout 1.0
    riley "{i}My stomach was making noises, thinking it's a whale.{/i}"
    riley "{i}Funny thing that I thought of whales, since there are none left after the calamity due to extreme radiation levels in the ocean waters.{/i}"
    riley "{i}Anyway my stomach and what's left of my nose lead me to a dirty building they called a canteen here.{/i}"
    
    
label l19:
    scene bg supermarket
    show jess neutral at center: 
        zoom 1.7
    jess "My, my! Whom the fate, like, brought to us today? What's your, like, name?"
    
menu:
    "Hi My name is Riley! And you must be Jess. Am I right?":
        jump l21
    "Like the hell you care? Don't talk too much! Can't you see I'm starving?":
        jump l35
        
#label l20: 
#    riley "Hi My name is Riley!"
#    riley "And you must be Jess. Am I right?"
    
label l21:
    scene bg supermarket
    show jess neutral at center: 
        zoom 1.7
    jess "Oh my! A new face! You can't imagine, like, how much I, like, grew tired of all this zombie faces while I am, like, staying here!"
    jess "Ha-ha! You're like zombie too! We all, like, zombies here!"
    jess "Anyway what do you, like, want to eat, like? Like, dried opposum? Or, like, zombie-wolf leg?"
    
label l22:
    # todo: make it inner voice
    riley "{i}Both choices were terrible, but I guess beggars can't be choosers, right?{/i}"

menu:
    "Dried opposum, please.":
        jump l25
    "Wolf's leg would be nice.":
        jump l25
     
label l25:
    # todo: make it inner voice
    riley "{i}I was so hungry that even Jess' terrible food couldn't stop me. My stomach was filling up fast.{/i}"
    
label l26:
    scene bg supermarket
    show jess neutral at center: 
        zoom 1.7
    jess "You, like, seems to be, like, a nice person? Tell me what are you, like, planning to do in this, like, god-forsaken place?"

menu:
    "It seems that equipment on this station doesn't work properly, maybe I'll stay here for some time, so I can help April to fix it.":
        jump l28
    "You know, Jess, I want to get out from here, preferrably as soon as possible!":
        jump l30

#label l27:
#    riley "You, like, seems to be, like, a nice person? Tell me what are you, like, planning to do in this, like, god-forsaken place?"
    
label l28:
    scene bg supermarket
    show jess neutral at center: 
        zoom 1.7
    riley "It seems that equipment on this station doesn't work properly, maybe I'll stay here for some time, so I can help April to fix it."
    jess "Pfft! What do you, like, all see in that witch April.
          I am, like, much prettier that her (in zombie terms, like, anyway). Ok, go to your, like, missy, but don't, like, come back asking for, like, food again."
    # Go to April scene #2
    jump next_epi
    
#label l29:
#    riley "You know, Jess, I want to get out from here, preferrably as soon as possible!"
    
label l30:
    scene bg supermarket
    show jess neutral at center: 
        zoom 1.7
    jess "Oh, Riley, that's is just, like, my dream as well."
    jess "The only, like, thing that this chunk of a man Matt has, like, the only car around here."
    jess "Say, what do you, like, think of killing him and, like, taking his car?"

menu:

    "Wow, wow! Easy there! I don't want to kill anyone here, ok? I will just go and talk to Matt.":
        jump l31
    "That seems like a nice idea! I highly doubt matt would give us car just like that!":

        jump l33

label l31:
    #riley "Wow, wow! Easy there! I don't want to kill anyone here, ok? I will just go and talk to Matt."
    # Go to Matt scene #1
    jump l41
    
#label l32:
#    riley "That seems like a nice idea! I highly doubt matt would give us car just like that!"
    
label l33:
    jess "You go, my hero! Le't get this car and drive far-far away!"
    # Go to Matt scene #2 (bad ending ensue)
    jump next_epi

#label l34:
#    riley "Like the hell you care?"
#    riley "Don't talk too much! Can't you see I'm starving?"
    
label l35:
    scene bg supermarket
    show jess neutral at center: 
        zoom 1.7
    jess "Hey, freaking zombie? Who, like, teach you to talk like that?"
    jess "Does, like, too much wind in the head, like, blew away the whatever brains, like, you've had?"


menu:

    "Ok, it seem like I was a tad too harsh, but common I haven't ate for a week! Can you give me some food?":
        jump l37
    "Hey! Just give me the food! Pronto, witch!":
        jump l39

#label l36:
#    riley "Ok, it seem like I was a tad too harsh, but common I haven't ate for a week! Can you give me some food?"
    
label l37:
    scene bg supermarket
    show jess neutral at center: 
        zoom 1.7
        
    jess "Ok, like, you should've said it, like, right away"
    jess "Anyway, I, like, forbidden to give food just like that."
    jess "You should, like, talk to, like, Clyde first."
    # Go to Clyde scene #1
    jump l64

#label l38:
#    riley "Hey! Just give me the food! Pronto, witch!"
    
label l39:
    scene bg supermarket
    show jess neutral at center: 
        zoom 1.7
    jess "Ok, like, here is you food, like. Enjoy!"

label l40:
    hide jess neutral
    # todo: make it inner voice
    riley "{i}I've started eating without thinking even for a second.{/i}"
    stop music
    riley "{i}On a third chew something started to creep in to my mind...{/i}"
    scene black
    riley "{i}That witch Jess, she poisoned my food!{/i}"
    # bad ending
    jump bad_end
    
label l41:
    scene bg garage
    $renpy.music.set_volume(0.3, delay=0, channel='music')
    play music "matt.mp3" loop fadein 1.0 fadeout 1.0
    riley "{i}Ahh, the smell of machine oil and old tires. I knew immediately that the garage is somewhere nearby{/i}"
    riley "{i}And so I came to the old pickup truck and it's enormous driver.{/i}"
    
label l42:
    scene bg garage
    show matt neutral at left: 
         zoom 1.7
    matt "Howdy, partner? What brought you to our places? You 'now what I mean?"
    

menu:

    "Hi, my name is Riley! I somehow found your oil-pumping station ":
        jump l44
    "Hey, redneck! Come here quick! I need you clothes, boots and your motorcycle, shoot! Your pickup!":
        jump l56
        
#label l43:
    # to do : option 1
#    rilley "Hi, my name is Riley!"
#    riley "I somehow found your oil -pumping station"
    
    
label l44:
    scene bg garage
    show matt neutral at left: 
         zoom 1.7
    matt "Oh, ya, partner! We're pumping oil here! You 'now what I mean?"

menu:

    "My friend, Matt, do you by any chance want to get out from here? To see the world? To feel how it's like outside this god-forsaken oil-pump? 
     You know what I mean, right, partner?":
        jump l46
    "Hey Matt! Let's get out from here?":
        jump l53
        
#label l45:
#    riley "My friend, Matt, do you by any chance want to get out from here?"
#    riley "My friend, Matt, do you by any chance want to get out from here?"
#    riley "My friend, Matt, do you by any chance want to get out from here?"

label l46:
    matt "Yeah, I know what you've saying"
    matt "Could you believe I lived all my life at this very pump!"
    matt "That's totally true, my pops brought us here when I was a tiny baby!"
    
label l47:
    riley "Wow!"
    
label l48:
    matt "We lived here for 20 years or so, and then the calamity stuck."
    matt "What I remeber that my mom and pops died in the first week after it."
    matt "But I somehow survived, yet I couldn't recognize myself. Oh god, what happened to us all!"
    matt "You 'now what I mean?"

label l49:
    riley "Yeah, totally! So how do we get out from here?"
    
label l50:
    matt "Right, partner! First we need to get some food from this witch Jess! Could you go and try to snatch something from her? You see she doesn't like me much."
    
label l51:
    riley "Sure thing, partner."
    # Go to Jess scene #2
    jump next_epi
    
#label l52:
#    riley "Hey Matt! Do you know by any chance how to get out from here?"
    
    
label l53:
    matt "I dunno, partner! After all I lived at this oil-pump station all my life!"
    matt "You 'now what I mean?"
    matt "Oh, right! You should ask Clyde! He sure is smart! Maybe he can help you somehow, you 'now what I mean?"

label l54:
    riley "Ah, ok then. See you soon!"
    # Go to Clyde scene #2
    jump next_epi

#label l55:
    # option 1
#    riley "Hey, redneck! Come here quick! I need you clothes, boots and your motorcycle, shoot! Your pickup!"
    
label l56:
    matt "Oops! That wasn't very nice, you 'know?"

menu:

    "Sorry, bro! Must be some April infuence here... Anyway I need to get out from this place ASAP":
        jump l58
    "I don't care who you are, what you are, just take me far from this place! Can you hear me, you stupid redneck-zombie! ":
        jump l61
        
#label l57:
    #option
#    riley "Sorry, bro! Must be some April infuence here..."
#    riley "Anyway I need to get out from this place ASAP"
    
label l58:
    matt "I don't really like you, partner, and your manners... You 'now what I mean?"
    matt "But let's strike a deal. You will go help my friend April to fix her equipment and I will drive to a nearest settlement. Deal?"

label l59:
    riley "Okay, okay!"
    # Go to April scene #2
    jump next_epi
    

#label l60:
    # option
#    riley "I don't care who you are, what you are, just take me far from this place!"
#    riley "Can you hear me, you stupid redneck-zombie!"
    
    
label l61:
    matt "Huh, partner, so you want to get far from here?"
    matt "Ok, let's go then. You 'now what I mean?"
    
label l62:
    riley "That is the line I was waiting for!"

label l63:
    stop music
    hide matt neutral
    # to do make it inner voice
    riley "{i}After several attempts, the truck is finally starting.{/i}"
    riley "{i}Me and Matt are getting into the truck and riding away.{/i}"
    scene black
    riley "{i}As we go far from the station suddenly something strikes my head!{/i}"
    riley "{i}When I awake there is no Matt or his truck nearby.{/i}"
    riley "{i}I don't know in which direction to go, and there is a zombie-wolf howling nearby.{/i}"
    # Bad ending
    jump bad_end
    
label l64:
    scene bg office
    $renpy.music.set_volume(0.3, delay=0, channel='music')
    play music "clyde.wav" loop fadein 1.0 fadeout 1.0
    #todo change to inner voice
    riley "{i}The trail lead me to an unremarkable building standing at the edge of oil-pumping station.{/i}"
    riley "{i}When I get in, I saw a huge table with piles of papers on it, and also boxes. Boxes, they were everywhere.{/i}"
    riley "{i}I wondered where the guy, who was standing in front of me got this all items from in this calamity?{/i}"
    
label l65:
    scene bg office
    show clyde neutral at left:
        zoom 2.4
    clyde "Khm, Khm? Did you wanted to speak with Clyde? Then talk! Clyde doesn't have much time!"

label l66:
    #todo change to inner voice
    riley "{i}What a weird dude? Does he really refer to himself in a third person?{/i}"

label l67:
    riley "Hi, you must be Clyde the station manager, rigth? I'm Riley."
    riley "I've got lost, but somehow found your station, while wondering around."
    
label l68:
    clyde "Look, stranger, Clyde is a busy person! Tell what you want or get out!"
    
menu:
    "It is an honor speaking with you, oh dear Clyde!":
        jump l68_2
    "Hey, weirdo, who talks about himself in a third person, I want to get out from here! Can you hear me? 
     I need you to order your station driver to take me to a nearest zombie settlement! ":
        jump l76
    
label l68_2:
    clyde "I like your tone, stranger! If only everyone at this station would have such respect to Clyde!"
    clyde "Espesially, that witch April! If only she wasn't an engineer here..."
    jump l69
label l69:
    #todo inner voice
    riley "{i}apparently Clyde is not very fond of April. {/i}"
label l70:
    clyde "Say stranger do you know a thing or two about the repairing of oil-pumps?"
    
menu:
    "Look before the calamity I was an engineer at an electric plant, so I think that dealing with an oil-pump wont be much of a difference.":
        jump l72
    "Clyde, with all due respect, I know nothing about oil-pumps. Say, mister Clyde, do you think your driver Matt could give me a tiny-bitsy ride from here?":
        jump l74
label l72:
    clyde "That's marvellous!"
    clyde "The go to and speak to April right away!"
    clyde "If you can fix the pump Clyde will reward you marvellously!"
    jump next_epi
    
label l74:
    clyde "Stranger, Clyde is impressed by your manners!"
    clyde "Say what? Why don't you speak with Matt himself, cause the last thing Clyde spoke with him the pickup truck had some issues."
    jump l41
    
label l76:
    clyde "Do you know who Clyde is? Clyde is the only who give orders here! Look stranger don't go along this lines any further! If you enrage Clyde, you will suffer dearly!"

menu:
    "Ok, ok, mister Clyde! Don't make haste decisions. Say can I help you somehow and get a ride as an exchange":
        jump l78
    "Look, I don't care who are you! A manager of a God himself! In this calamity this all doesn't matter a bit. All I want is a car to get out from this hole.":
        jump l82
        
label l78:
    clyde "That's much better tone, stranger"
    riley "I'm Riley!"
    clyde "Clyde doesn't have time to remember names!"
    jump l70
    
label l82:
    clyde "Why you, little! How do yo speak with Clyde!"
    clyde "Ok, all right! We'll give you a ride! We'll give you a ride you won't forget, Ha-ha-ha!"
    
label l83:
    #todo inner voice
    stop music
    riley "{i}I got a bad feeling from this promise of his, but it was too late to back down.{/i}"
    scene bg garage
    riley "{i}Three of us (a driver, me and, for some reason, Clyde) got in an old pickup truck.{/i}"
    
label l84:
    #todo inner voice
    scene black
    riley "{i}Wheels were taking us further and further from the station{/i}"
    riley "{i}After a while it was all but a tiny dot on a horizon.{/i}"
    
label l85:
    #todo inner voice
    riley "{i}I suddently felt something sharp in my chest and then stop feeling anything ever again.{/i}"
    riley "{i}That bastard Clyde put a giant knife through me, I knew I should've run from this place instead.{/i}"
    jump bad_end

label next_epi:
    stop music
    scene bg episode2
    $renpy.pause()
    return
    
label bad_end:
    stop music
    scene bg dead
    $renpy.pause()
    return
