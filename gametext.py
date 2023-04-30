from colorama import Fore

room_descriptions = {

    'a1': "luxurious study.\nThe room's many shelves are home to"
          "\nvarious odd trinkets which you've never seen before."
          "\nYou suddenly feel like something to the north moved"
          "\never so slightly. You whip your gaze around to that side"
          "\nof the room but everything lies still...",

    'a2': "pitch-dark chamber.\nThe ground beneath your feet is hard stone"
          "\nbut you cannot see anything more than a few inches in front"
          "\nof your face",

    'a3': "library.\nRows of books line shelves on the northern and"
          "\nsouthern walls, all covered in a thick layer of dust.",

    'a4': "dining room.\nA fire burns in the huge hearth on the"
          "\nopposite wall, casting warm orange light on to the"
          "\ncenterpiece of the room:\na gigantic oaken dining table."
          "\nOn this dining table sits a single plate, upon which"
          "\nrests the most soft, warm, appetizing loaf of bread"
          "\nYour stomach grumbles...",

    'b1': "long candlelit corridor.\nThe candles' glow illuminates a"
          "\ndoor at the southern end of the corridor, and you can see"
          "\na short hallway on the eastern side with another door.",

    'b2': "huge circular room.\nThe floor below your feet is hard stone"
          "\nand stained a dark crimson colour. You look up and see dark"
          "\nalcoves set in to the walls every few meters. You can just"
          "\nabout make out what look like seats in the alcoves. You then"
          "\nsee this place for what it is: an arena."
          "\nAs you go to run back the way you came, a voice comes"
          "\nbooming out from behind you.",

    'b3': "storage room.\nWooden crates are piled high"
          "\nall around you. There is very little light,"
          "\nbut you can just make out a spiral staircase to the east",

    'b4': "grand hall.\nYour eyes follow the intricate pattern on the"
          "\nred and gold carpet up to the staggeringly high walls,"
          "\nadorned from bottom to top with countless beautiful paintings"
          "\nand portraits.\n\nThere are large ornate wooden doors"
          "\nto the north and to the south.",

    'c1': "grand entranceway.\nIn front of you stands a huge wooden door,"
          "\nbeatifully carved with intricate flowing designs from bottom"
          "\nto top. Your eyes follow the lines from one design to the next"
          "\nand then, as you take in the door as a whole, you realise that"
          "\nall the carvings come together to form the outline of... a face?",

    'c2': "large alcove.\nThis seems to be the place where that purple cloaked"
          "\nman might sit and watch the fighting below.",

    'c3': "cold, stone room.\nIt seems to be a cell of "
          "some sort\nbut the large iron-barred door "
          "\nto the north hangs open.",

    'c4': "narrow, stone-walled corridor.\nA single, small lantern"
          "\nhangs from the curved roof, casting a dim light onto the"
          "\nfloor below, upon which you see a puddle has formed,"
          "\npresumably from a leak in the stone ceiling."
          "\nThrough the hanging lantern's dim light, you also"
          "\nsee a strange door on the south end of the corridor.",

    'd1': "You enter a large room,\nbeautifully decorated, but your eyes are"
          "\ntransfixed on the door at the opposite wall."
          "\nThe door to freedom..."
          "\nYou take a step forward and the figure of the man in the purple"
          "\ncloak appeears between you and the door.",


    'd2': "small marble chamber.\nThe floor and walls are white marble"
          "\nwith veins of shining silver running through them like lightning."
          "\nAhead of you, between two pillars stands an altar, upon which"
          "\nsits a large, beautiful white and silver chest.",

    'd3': "dark, damp cave.\nUp ahead you see the glow of firelight"
          "\nand the shadows of a strange figure dancing on the cave walls.",

    'd4': "square stone chamber.\nAs soon as you take a step"
          "\nforward, the door behind you slams shut and locks."
          "\nA tall, slender figure in a purple cloak appears"
          "\nbefore you."

}

room_descriptions_completed = {

      'a1': "luxurious study where you fought the haunted chest",

      'a2': "pitch-dark chamber. You use your lantern once again"
            "\nto light the way along the inding stone path",

      'a3': "library, wherein you learned the password: 'Ajagar'.",

      'a4': "dining room, the ogre's body lies slumped over the"
            "\ngiant dining table.",

      'b1': "long candlelit corridor.\nThe candles' glow illuminates a"
            "\ndoor at the southern end of the corridor, and you can see"
            "\nan alcove on the western side with another door.",

      'b2': "massive arena where you fought Gorehowl",

      'b3': "storage room where you found your dagger and map.",

      'b4': "grand hall where you found the silver key.",

      'c1': "grand entranceway,\nthe huge door, since you gave it the"
            "\ncorrect password, lies open.",

      'c2': "large alcove where you found the mysterious eyeglass.",

      'c3': "cold stone prison cell where you first awoke.",

      'c4': "narrow, stone-walled corridor where you found your lantern.",

      'd2': "marble chamber where you found the silver sword.",

      'd3': "dark damp cave where you fought the goblin.",

      'd4': "square stone chamber that previously closed in upon you."
}

room_descriptions_goblin_attack = {
      'd3': "You re-enter the cave, and hear none of the grunting"
            "\nand crunching that you heard earlier. You cautiously"
            "\nstep forward but stop in your tracks as a drop of"
            "\nwater hits your forehead. You look upwards and see"
            "\nthe goblin, clinging to the roof, its mouth cracked"
            "\ninto a wide toothy grin and its tongue lolling out,"
            "\ndripping saliva onto you as you stand frozen below."
            "\nYou lock eyes with it for a split second before it lets"
            "\nout a horrific screech and descends upon you!"
}

room_details = {

    'a1': "You step nervously towards the north side of the room"
          "\nand see, on the ground, a large sturdy wooden chest."
          "\nYou know that it can't have been the chest that moved"
          "\nbut at the same time, something about it looks... off",

    'a2': "You take your first step forward into the blackness."
          "\nYour right foot meets the solid ground below. You"
          "\nstep again but this time your left foot never touches"
          "\nthe ground. You tumble down through the empty dark"
          "\nbefore meeting the ground, and your end, at the bottom",

    'a3': "As you walk forward, eyes scanning along the countless"
          "\nold tomes lining the walls, you see one book whose"
          "\ncover does not seem to have any dust on it at all."
          "\nYou reach over and open it, but cannot read any of"
          "\nits contents as it seems to be written in a strange script"
          "\nthat you have never seen before..."
          "\nYou leave the book back where you found it for now.",

    'a4': "Your eyes are transfixed on the loaf of bread.\n\n",

    'b1': "As you make your way down the corridor, you notice that"
          "\nthere is a small brass ring hanging from the wall."
          "\nYou give it a slight pull and a little drawer pulls"
          "\nout from the wall! Inside this drawer sits a sealed"
          "\nvial of thick blue liquid. It looks unnatural but you"
          "\nare tempted to try it.",

    'b2': "The arena lies empty, but it looks like you might be able"
          "\nto climb up to the large alcove to the south.",

    'b3': f"You search around in the dark and find a {Fore.CYAN}RUSTY DAGGER"
          f"\n{Fore.WHITE}It looks like decades of rust"
          " have blunted its blade,"
          "\nbut it's better than your fists."
          "\nThere is probably more hidden among the crates, but "
          "\nit's too dark to see anything",

    'b4': "You inspect the paintings. They are all beautifully done."
          "\nYou notice that the characters in the portraits are never"
          "\nlooking straight out, as you would expect, but instead"
          "\nlooking up or down at other portraits..."
          "\n\nYou follow the gaze of one portrait to the next, and again"
          "\nand again and again until finally coming to a portrait"
          "\nof a young girl."
          "\nThe girl is holding out her hands as if presenting something"
          "\nbut her hands are empty.",

    'c1': "As you stare at the carvings, they begin to move! The giant wooden"
          "\nfeatures of the face on the door creasing and opening."
          "\nThe wood cracks and groans as the face's eyes fully open."
          "\nIt stares directly at you with its huge, green, wooden eyes"
          "\nand speaks one word...\n\n 'PASSWORD'"
          "\n\nYou stare blankly back for a moment before realising that"
          "\nit is expecting an answer from you. "
          "\nYou try to think of what this password could be but nothing"
          "\ncomes to your mind. Perhaps there is a clue hidden somewhere"
          "\nin another room..."
          "\n\nYou step away from the door and the face's eyes slowly"
          "\nclose shut again. Its features sinking back into the surface of"
          "\nthe huge door.",

    'c2': "You see a small stone table beside the seat. Upon the table"
          "\nthere sits an elegantly ornate little box. You lift its"
          "\nlid and see a line of strange script that you cannot"
          "\nmake sense of carved into the inside of the lid."
          "\nSitting snugly in a recess in the box's red and gold"
          "\ninterior is what looks like a miniature metallic telescope"
          "\nyou take it and hold it up to your eye and peer through it."
          "\nYou squint as you look through its lens but you can't seem"
          "\nto see any effect compared to your vision."
          "\nThat is until you use it to look back at the ornate box."
          "\nThe script on the inside of the box slides and moves, the"
          "\nlines of the letters turning and rotating to form a sentence!",

    'c3': "It's too dark to see anything."
          "\nPerhaps if you had a light source...",

    'c4': "You take a few steps forward up to the edge of the"
          "\npuddle. You look up at the lantern above, and notice that"
          "\nthe liquid is coming from directly above the lantern. Not"
          "\nonly that, but the liquid seems to have corroded the lantern's"
          "\nchain, which looks like it could come off if given a tug..."
          "\nYou think you might be able to reach the lantern, but"
          "\nif you slip, you might end up falling straight into the"
          "\npuddle of strange, corrosive liquid.",

    'd2': "You approach the chest and try to open it, but it is locked."
          "\nA heavy silver latch with a keyhole locks the chest shut.",

    'd3': "You creep forward and see a small green figure with its"
          "\nback to you, hunched by the fire. It's inhuman grunts and groans"
          "\nreach your ears, as well as the awful sound of teeth crunching"
          "\nthrough bone.",

    'd4': "The riddle room",

}

room_details_looked = {
    'b3': "You search around in the dark but don't find anything."
          "\nThere is probably more hidden among the crates,\nbut "
          "it's too dark to see anything",
}

room_details_lantern = {

    'a2': "You say a silent thanks for your lantern as you feel the"
          "\noppresive dark pushed back from you, even if only slightly."
          "\nyou step tentatively forward and lower your lantern to"
          "\nsee that the ground one step beyond your feet gives way"
          "\nto a black chasm. Stepping beyond where you stand seems"
          "\nlike certain death, but you notice to your left, an"
          "\nextremely narrow stone path, winding its way left and right"
          "\nout across the chasm. You take the most careful steps you"
          "\nhave ever taken and manage to follow the stone path to"
          "\nthe other side of the room."
          "\n\n             **The west side of this room is now reachable**",

    'b3': "With the aid of your lantern you search around the crates."
          "\nIt seems to be mostly useless junk, but at the bottom of"
          "\nan old, rotting wooden crate you find a rolled-up scroll of"
          "\nparchment. You carefully unravel and examine it. It's a map"
          "\nof Fell Manor!",

    'c3': "Your lantern lights up your immediate surroundings."
          "\nA family of mice scurries away from your footfall as"
          "\nyou scan the room. There is a grimy stone slab which serves"
          "\nas a bed and not much else. You do see, however, the"
          "\nbroken remains of a small wooden table. You pick up"
          "\na large slab of wood which looks like it could be used"
          "\nas a makeshift shield! You hug it to your side,"
          "\ngrateful for whatever protection it can offer"
}

room_details_combined = {
    'b3': f"You search around and find a {Fore.CYAN}Rusty Dagger\n"
          f"{Fore.WHITE}It looks like decades of rust have blunted its blade, "
          "but it's better than your fists."
          f"\n\n{Fore.CYAN}                      "
          "**You equip the RUSTY DAGGER**\n\n"
}

room_details_password = {

      'c1': "As you stare at the carvings, they begin to move! The giant"
            "\nwooden features of the face on the door creasing and opening."
            "\nThe wood cracks and groans as the face's eyes fully open."
            "\nIt stares directly at you with its huge, green, wooden eyes"
            "\nand speaks one word...\n\n 'PASSWORD' \n\n"
            "\nKnowing the password, you speak the word:"
            "\n\n'Ajagar'\n\n"
            "\nThe wooden face grimaces, snapping and creaking as the door"
            "\nslowly swings open. Through it you can see Fell Manor's"
            "\nfinal room, and beyond it, the door to your escape..."
            "\n\n **The entrance to the south is now open**\n\n"


}

room_details_eyeglass = {

      'a3': "As you walk forward, eyes scanning along the countless"
            "\nold tomes lining the walls, you see one book whose"
            "\ncover does not seem to have any dust on it at all."
            "\nYou reach over and open it, but cannot read any of"
            "\nits contents as it seems to be written in a strange script."
            "\nremembering the script on the inside of the eyeglass's box,"
            "\nyou hastily pull out the eyeglass and peer through it at"
            "\nthe script in the book."
            "\n Sure enough, the script begins to change as it did before,"
            "\nallowing you to decipher the book's contents"
            "\nYou skim along the pages of the book before stopping at a"
            "\npage containing only two words, \n\n'Password'\n\n and directly"
            " below it, \n\n'Ajagar'\n\n"
            "\nYou make careful note of this word and slam the book shut.",

      'b4': "You inspect the paintings. They are all beautifully done."
            "\nYou notice that the characters in the portraits are never"
            "\nlooking straight out, as you would expect, but instead"
            "\nlooking up or down at other portraits..."
            "\nYou follow the gaze of one portrait to the next, and again"
            "\nand again and again until finally coming to a portrait"
            "\nof a young girl."
            "\nThe girl is holding out her hands as if presenting something"
            "\nbut her hands are empty."
            "\nYou raise the eyeglass and peer through it, and you see in the"
            "\ngirl's hands a shining silver key!"
            "\nYou reach forward tentatively and your fingers sink through"
            "\nthe fabric of the painting as if it were water."
            "\nAs you grasp the key, the girl's hands clasp yours and"
            "\nyou feel a surge of rejuvenating energy fill your body."

}

room_details_silver_key = {
      'd2': "You approach the chest and insert the silver key into"
            "\nthe keyhole and turn. The latch clicks and the chest unlocks!"
            "\nYou lift the heavy lid and peer inside to see an onrately"
            f"\ndecorated shining {Fore.CYAN}Silver Sword{Fore.WHITE}"
            "\nYou lift it from the chest and give it a couple of swings."
            "\nIt feels beautifully balanced in your hand and looks like"
            "\nit could cause some serious damage!"
}

room_details_lesser_item = {
      'b3': "You search around and find a RUSTY DAGGER!"
            "\nIt looks like decades of rust have blunted its blade, "
            "\nThis dagger looks far less useful than your SILVER"
            "\nSWORD so you leave it behind."
            "\nAs well as the dagger, with the aid of your lantern"
            "\nyou find, at the bottom of an old, rotting"
            "\nwooden crate, a rolled-up scroll of parchment."
            "\nYou carefully unravel and examine it. It's a map"
            "\nof Fell Manor!"
            "\n\n You can now type 'map' when prompted to see a map of"
            "\nFell Manor's rooms.",

      'c3': "Your lantern lights up your immediate surroundings."
            "\nA family of mice scurries away from your footfall as"
            "\nyou scan the room. There is a grimy stone slab which serves"
            "\nas a bed and not much else. You do see, however, the"
            "\nbroken remains of a small wooden table. You pick up"
            "\na large slab of wood which looks like it could be used"
            "\nas a makeshift shield, but much worse than your"
            "\nIRON SHIELD, so you leave it behind."
}

room_details_lesser_combined = {
      'b3': "You search around and find a RUSTY DAGGER!"
            "\nIt looks like decades of rust have blunted its blade, "
            "\nThis dagger looks far less useful than your SILVER"
            "\nSWORD so you leave it behind."
            "\nWith the aid of your lantern"
            "\nyou also find, at the bottom of an old, rotting"
            "\nwooden crate, a rolled-up scroll of parchment."
            "\nYou carefully unravel and examine it. It's a map"
            "\nof Fell Manor!"
            "\n\n You can now type 'map' when prompted to see a map of"
            "\nFell Manor's rooms.",
}

item_text = {

    'lantern_success': "\nYou shuffle forward as close to the puddle as"
                       "\nyou dare. You reach your arm up as high as you can"
                       "\nbut you only just brush the underside of the lantern"
                       "\nwith your fingertips."
                       "\nYou steel yourself and try one more time, the liquid"
                       "\non the ground sizzles the toe of your right boot and"
                       "\nyou grimace and reach with all your might, until it"
                       "\nfeels as if your arm will separate from your"
                       " shoulder"
                       "\nand you grab it! With a quick sharp tug the lantern"
                       "\nbreaks off from its chain and you step carefully"
                       " back"
                       "\nfrom the still sizzling liquid, admiring your new"
                       "\nhandheld light source",

    'lantern_failure': "\nYou step forward to the edge of the puddle and reach"
                       "\nas high as you can. You are just about to reach the"
                       "\nlantern when your foot slips and you stumble forward"
                       "\ninto the puddle of corrosive liquid!"
                       "\nYou leap backwards as fast as you can but the acid"
                       "\nburns your feet and hands!"
                       f"\nYou take {Fore.RED}1 {Fore.WHITE}point of damage",

    'health_potion': "\nThe lid unscrews easily"
                     "\nand a sickly sweet aroma floats out of the vial."
                     "\nYou raise the vial to your lips and let the liquid"
                     "\npour into your mouth. As soon as you've finished it"
                     "\na strange feeling comes over you. You feel stronger,"
                     "\nhealthier, refreshed - as if you've had a really good"
                     "\nnight's sleep. You shake yourself out and continue on"
                     "\nfeeling a tiny bit more able to take on the challenges"
                     "\nof this awful place."
}

enemy_text = {

      'ogre': "You suddenly hear a loud crash to your left. A hulking,"
              f"\ngreen {Fore.RED}ogre {Fore.WHITE}stands in the doorway."
              "\nYou both stand frozen"
              "\nfor a brief second before it bellows out in a deafening"
              "\nguttural roar:"
              "\n\n                     'MY BREEEEEEAD!!!!!'\n\n"
              "It bounds towards you and attacks!",

      'haunted_chest': "You reach down to open the chest, but before you"
                       "\ntouch the latch, it springs open! Two encrusted"
                       "\neyes snap open from lines in the wooden grain"
                       "\nand the chest leaps up at you, attempting to"
                       "\nclamp down on you with the hundreds of tiny teeth"
                       "\nthat line the inside of its lid."
}

enemy_death = {

      'ogre': "You breath heavily and look around the room."
              "\nYou don't know quite how you did that but you're"
              "\nthankful you're alive. Since the ogre won't be needing"
              "\nit anymore, you help yourself to the entire rest"
              "\nof the breadloaf: a well earned reward."
              f"{Fore.GREEN}\n\n"
              f"                **Your health increases by 10 points!**"
              f"{Fore.WHITE}",

      'haunted_chest': "The chest lies still, lid hanging open lifelessly."
                       "\nYou wipe the sweat from your face and cautiously"
                       "\npeer into the body of the chest, where, amongst"
                       "\nbroken bones, lies an ornate iron shield."
                       "\nYou slowly reach your hand inside, grasp the shield"
                       "\nand quickly pull it out."
                       "\nThis thing looks like it offers some serious"
                       "protection!",

      'gorehowl': "You fall to your knees beside the huge body of your"
                  "\nopponent, gasping for breath and staring at the"
                  "\nfloor, dumbstruck over the feat you have just"
                  "\naccomplished. When you do look up, all the spectators"
                  "\nhave vanished, and you are once again alone in this"
                  "\nmassive arena. You pick yourself up and glance around"
                  "\nonce more. The gate to the south, where this beast"
                  "\nemerged from has disappeared! but it looks like you"
                  "\nmight just be able to climb up to the large alcove"
                  "\non that side of the room.",

      'goblin': "You take a moment to curse your carelessness as the ugly,"
                "\nlifeless face of the goblin stares up at you. You glance"
                "\naround the room and see nothing but piles of bones"
                "\nand continue on your path.",

      'manor_lord': "You fall to the floor, battered and exhausted,"
                    "\nbut you know you have finally triumphed over this"
                    "\nwretched place and its sadistic host."
                    "\nYou look up at the final door and pull yourself slowly"
                    "\nto your feet. Dragging yourself over to the door, you"
                    "\ntwist the handle, the door swings open and you"
                    "\nbreathe in the night air, and escape from Fell Manor."

}
