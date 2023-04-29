from colorama import Fore

room_descriptions = {

    'a1': "luxurious study. The room's many shelves are home to"
          " various odd trinkets which you've never seen before."
          " You suddenly feel like something to the north moved"
          " ever so slightly. You whip your gaze around to that side"
          " of the room but everything lies still...",

    'a2': "pitch-dark chamber. The ground beneath your feet is hard stone"
          " but you cannot see anything more than a few inches in front"
          " of your face",

    'a3': "library. Rows of books line shelves on the northern and"
          " southern walls, all covered in a thick layer of dust.",

    'a4': "dining room. A fire burns in the huge hearth on the"
          " opposite wall, casting warm orange light on to the"
          " centerpiece of the room:\na gigantic oaken dining table.\n\n"
          " On this dining table sits a single plate, upon which"
          " rests the most, soft, warm, appetizing loaf of bread\n"
          " Your stomach grumbles...",

    'b1': "long candlelit corridor. The candles' glow illuminates a"
          " door at the southern end of the corridor, and you can see"
          " an alcove on the western side with another door.",

    'b2': "huge circular room. The floor below your feet is hard stone"
          " and stained a dark crimson colour. You look up and see dark"
          " alcoves set in to the walls every few meters. You can just"
          " about make out what look like seats in the alcoves. You then"
          " see this place for what it is: an arena."
          " \n As you go to run back the way you came, a voice comes"
          " booming out from behind you.",

    'b3': "storage room. Wooden crates are piled high"
          "\nall around you. There is very little light,"
          "\nbut you can just make out a spiral staircase to the east",

    'b4': "grand hall. your eyes follow the intricate pattern on the"
          " red and gold carpet up to the staggeringly high walls,"
          " adorned from bottom to top with countless beautiful paintings"
          " and portraits.\n\n There are large ornate wooden doors"
          " to the north and to the south.",

    'c1': "grand entranceway. In front of you stands a huge wooden door,"
          " beatifully carved with intricate flowing designs from bottom"
          " to top. Your eyes follow the lines from one design to the next"
          " and then, as you take in the door as a whole, you realise that"
          " all the carvings come together to form the outline of... a face?",

    'c2': "large alcove. This seems to be the place where that cloaked man"
          " might sit and watch the fighting below.",

    'c3': "cold, stone room. It seems to be a cell of "
          "some sort\nbut the large iron-barred door "
          "to the north hangs open.",

    'c4': "narrow, stone-walled corridor. A single, small lantern"
          " hangs from the curved roof, casting a dim light onto the"
          " floor below, upon which you see a puddle has formed,"
          " presumably from a leak in the stone ceiling."
          " Through the hanging lantern's dim light, you also"
          " see a strange door on the south end of the corridor.",

    'd1': "You enter a large room, beautifully decorated, but your eyes are"
          " transfixed on the door at the opposite wall."
          " The door to freedom..."
          " You take a step forwards and the figure of the man in the red"
          " and gold cloak appeears between you and the door.",


    'd2': "small marble chamber. The floor and walls are white marble"
          " with veins of shining silver running through them like lightning."
          " Ahead of you, between two pillars stands an altar, upon which"
          " sits a large, beautiful white and silver chest.",

    'd3': "dark, damp cave. Up ahead you see the glow of firelight"
          " and the shadows of a strange figure dancing on the cave walls.",

    'd4': "square stone chamber. As soon as you take a step"
          " forwards, the door behind you slams shut and locks."
          " A tall, slender figure in a red and gold cloak appears"
          " before you."

}

room_descriptions_completed = {

      'a1': "luxurious study where you fought the haunted chest",

      'a2': "pitch-dark chamber. You use your lantern once again"
            " to light the way along the inding stone path",

      'a3': "library. Rows of books line shelves on the northern and"
            " southern walls, all covered in a thick layer of dust.",

      'a4': "dining room, the ogre's body lies slumped over the"
            " giant dining table.",

      'b1': "long candlelit corridor. The candles' glow illuminates a"
            " door at the southern end of the corridor, and you can see"
            " an alcove on the western side with another door.",

      'b2': "arena where you fought Gorehowl",

      'b3': "storage room where you found your dagger and map.",

      'b4': "grand hall where you found the silver key.",

      'c1': "grand entranceway, the huge door, since you gave it the"
            "correct password, lies open.",

      'c2': "large alcove where you found the mysterious eyeglass.",

      'c3': "cold stone prison cell where you first awoke.",

      'c4': "narrow, stone-walled corridor where you found your lantern.",

      'd2': "marble chamber where you found the silver sword.",

      'd3': "dark damp cave where you fought the goblin.",

      'd4': "square stone chamber that previously closed in upon you."
}

room_descriptions_goblin_attack = {
      'd3': "You re-enter the cave, and hear none of the grunting"
            " and crunching that you heard earlier. You cautiously"
            " step forward but stop in your tracks as a drop of"
            " water hits your forehead. You look upwards and see"
            " the goblin, clinging to the roof, its mouth cracked"
            " into a wide toothy grin and its tongue lolling out,"
            " dripping saliva onto you as you stand frozen below."
            " You lock eyes with it for a split second before it lets"
            " out a horrific screech and descends upon you!"
}

room_details = {

    'a1': "You step nervously towards the north side of the room"
          " and see, on the ground, a large sturdy wooden chest."
          " You know that it can't have been the chest that moved"
          " but at the same time, something about it looks... off",

    'a2': "You take your first step forward into the blackness."
          " Your right foot meets the solid ground below. You"
          " step again but this time your left foot never touches"
          " the ground. You tumble down through the empty dark"
          " before meeting the ground, and your end, at the bottom",

    'a3': "As you walk forward, eyes scanning along the countless"
          " old tomes lining the walls, you see one book whose"
          " cover does not seem to have any dust on it at all."
          " You reach over and open it, but cannot read any of"
          " its contents as it seems to be written in a strange script"
          " that you have never seen before..."
          "\n You leave the book back where you found it for now.",

    'a4': "Your eyes are transfixed on the loaf of bread.\n\n",

    'b1': "As you make your way down the corridor, you notice that"
          " there is a small brass ring hanging from the wall."
          " You give it a slight pull and a little drawer pulls"
          " out from the wall! Inside this drawer sits a sealed"
          " vial of thick blue liquid. It looks unnatural but you"
          " are tempted to try it.",

    'b2': "The arena lies empty, but it looks like you might be able"
          " to climb up to the large alcove to the south.",

    'b3': f"You search around in the dark and find a {Fore.CYAN}RUSTY DAGGER"
          f"\n{Fore.WHITE}It looks like decades of rust"
          " have blunted its blade,"
          "\nbut it's better than your fists."
          "\nThere is probably more hidden among the crates, but "
          "\nit's too dark to see anything",

    'b4': "You inspect the paintings. They are all beautifully done."
          " You notice that the characters in the portraits are never"
          " looking straight out, as you would expect, but instead"
          " looking up or down at other portraits...\n\n"
          " You follow the gaze of one portrait to the next, and again"
          " and again and again \nuntil finally coming to a portrait"
          " of a young girl.\n"
          " The girl is holding out her hands as if presenting something"
          " but her hands are empty. \n\n"
          " As you peer into the painting, you realise that there is a"
          " voice coming from it!\n"
          " You press your ear close to it and try to make out what"
          " it is saying...\n\n\n",

    'c1': "As you stare at the carvings, they begin to move! The giant wooden"
          " features of the face on the door creasing and opening."
          " The wood cracks and groans as the face's eyes fully open."
          " It stares directly at you with its huge, green, wooden eyes"
          " and speaks one word...\n\n 'PASSWORD' \n\n"
          " You stare blankly back for a moment before realising that"
          " it is expecting an answer from you. "
          " You try to think of what this password could be but nothing"
          " comes to your mind. Perhaps there is a clue hidden somewhere"
          " in another room..."
          " \n\n You step away from the door and the face's eyes slowly"
          " close shut again. Its features sinking back into the surface of"
          " the huge door.",

    'c2': "You see a small stone table beside the seat. Upon the table"
          " there sits an elegantly ornate little box. You lift its"
          " lid and see a line of strange script that you cannot"
          " make sense of carved into the inside of the lid."
          " Sitting snugly in a recess in the box's red and gold"
          " interior is what looks like a miniature metallic telescope"
          " you take it and hold it up to your eye and peer through it."
          " You squint as you look through its lens but you can't seem"
          " to see any effect compared to your vision."
          "\n That is until you use it to look back at the ornate box."
          " The script on the inside of the box slides and moves, the"
          " lines of the letters turning and rotating to form a sentence!"
          "\n\n'See beyond what is shown'\n\n"
          " You place the eyeglass in your pocket.",

    'c3': "It's too dark to see anything."
          " Perhaps if you had a light source...",

    'c4': "You take a few steps forward up to the edge of the"
          " puddle. You look up at the lantern above, and notice that"
          " the liquid is coming from directly above the lantern. Not"
          " only that, but the liquid seems to have corroded the lantern's"
          " chain, which looks like it could come off if given a tug..."
          " \nYou think you might be able to reach the lantern, but"
          " if you slip, you might end up falling straight into the"
          " puddle of strange, corrosive liquid.",

    'd2': "You apprach the chest and try to open it, but it is locked."
          " A heavy silver latch with a keyhole locks the chest shut.",

    'd3': "You creep forward and see a small green figure with its"
          " back to you, hunched by the fire. It's inhuman grunts and groans"
          " reach your ears, as well as the awful sound of teeth crunching"
          " through bone.",

    'd4': "The riddle room",

}

room_details_looked = {
    'b3': "You search around in the dark but don't find anything"
          "There is probably more hidden among the crates, but "
          "it's too dark to see anything",
}

room_details_lantern = {

    'a2': "You say a silent thanks for your lantern as you feel the"
          " oppresive dark pushed back from you, even if only slightly."
          " you step tentatively forwards and lower your lantern to"
          " see that the ground one step beyond your feet gives way"
          " to a black chasm. Stepping beyond where you stand seems"
          " like certain death, but you notice to your left, an"
          " extremely narrow stone path, winding its way left and right"
          " out across the chasm. You take the most careful steps you"
          " have ever taken and manage to follow the stone path to"
          " the other side of the room."
          " \n\n **The west side of this room is now reachable**\n\n",

    'b3': "With the aid of your lantern you search around the crates."
          " It seems to be mostly useless junk, but at the bottom of"
          " an old, rotting wooden crate you find a rolled-up scroll of"
          " parchment. You carefully unravel and examine it. It's a map"
          " of Fell Manor!",

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
          f"{Fore.WHITE}Not only that, but with the aid of your lantern"
          " you find, at the bottom of an old, rotting"
          " wooden crate, a rolled-up scroll of parchment."
          " You carefully unravel and examine it. It's a map"
          " of Fell Manor!"
          "\n\n You can now type 'map' when prompted to see a map of"
          " Fell Manor's rooms."
}

room_details_password = {

      'c1': "As you stare at the carvings, they begin to move! The giant"
            " wooden features of the face on the door creasing and opening."
            " The wood cracks and groans as the face's eyes fully open."
            " It stares directly at you with its huge, green, wooden eyes"
            " and speaks one word...\n\n 'PASSWORD' \n\n"
            " Knowing the password, you speak the word:"
            " \n\n'Ajagar'\n\n"
            " The wooden face grimaces, snapping and creaking as the door"
            " slowly swings open. Through it you can see Fell Manor's"
            " final room, and beyond it, the door to your escape..."
            "\n\n **The entrance to the south is now open**\n\n"


}

room_details_eyeglass = {

      'a3': "As you walk forward, eyes scanning along the countless"
            " old tomes lining the walls, you see one book whose"
            " cover does not seem to have any dust on it at all."
            " You reach over and open it, but cannot read any of"
            " its contents as it seems to be written in a strange script."
            " remembering the script on the inside of the eyeglass's box,"
            " you hastily pull out the eyeglass and peer through it at"
            " the script in the book."
            "\n Sure enough, the script begins to change as it did before,"
            " allowing you to decipher the book's contents"
            "\nYou skim along the pages of the book before stopping at a"
            " page containing only two words, \n'Password'\n and directly"
            " below it, \n'Ajagar'\n"
            " You make careful note of this word and slam the book shut.",

      'b4': "You inspect the paintings. They are all beautifully done."
            " You notice that the characters in the portraits are never"
            " looking straight out, as you would expect, but instead"
            " looking up or down at other portraits...\n\n"
            " You follow the gaze of one portrait to the next, and again"
            " and again and again \nuntil finally coming to a portrait"
            " of a young girl.\n"
            " The girl is holding out her hands as if presenting something"
            " but her hands are empty. \n\n"
            " You raise the eyeglass and peer through it, and you see in the"
            " girl's hands a shining silver key!"
            " You reach forward tentatively and your fingers sink through"
            " the fabric of the painting as if it were water."
            " As you grasp the key, the girl's hands clasp yours and"
            " you feel a surge of rejuvenating energy fill your body."
            
}

room_details_silver_key = {
      'd2': "You approach the chest and insert the silver key into"
            " the keyhole and turn. The latch clicks and the chest unlocks!"
            " You lift the heavy lid and peer inside to see an onrately"
            " decorated shining silver sword!"
            " You lift it from the chest and give it a couple of swings."
            " It feels beautifully balanced in your hand and looks like"
            " it could cause some serious damage!"
}

room_details_lesser_item = {
      'b3': "You search around and find a RUSTY DAGGER!\n"
            "It looks like decades of rust have blunted its blade, "
            " This dagger looks far less useful than your SILVER"
            " SWORD so you leave it behind."
            "\nAs well as the dagger, with the aid of your lantern"
            " you find, at the bottom of an old, rotting"
            " wooden crate, a rolled-up scroll of parchment."
            " You carefully unravel and examine it. It's a map"
            " of Fell Manor!"
            "\n\n You can now type 'map' when prompted to see a map of"
            " Fell Manor's rooms.",

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
      'b3': "You search around and find a RUSTY DAGGER!\n"
            "It looks like decades of rust have blunted its blade, "
            " This dagger looks far less useful than your SILVER"
            " SWORD so you leave it behind."
            "\nWith the aid of your lantern"
            " you also find, at the bottom of an old, rotting"
            " wooden crate, a rolled-up scroll of parchment."
            " You carefully unravel and examine it. It's a map"
            " of Fell Manor!"
            "\n\n You can now type 'map' when prompted to see a map of"
            " Fell Manor's rooms.",
}

item_text = {

    'lantern_success': "\nYou shuffle forward as close to the puddle as"
                       " you dare. You reach your arm up as high as you can"
                       " but you only just brush the underside of the lantern"
                       " with your fingertips."
                       " You steel yourself and try one more time, the liquid"
                       " on the ground sizzles the toe of your right boot and"
                       " you grimace and reach with all your might, until it"
                       " feels as if your arm will separate from your shoulder"
                       " and you grab it! With a quick sharp tug the lantern"
                       " breaks off from its chain and you step carefully back"
                       " from the still sizzling liquid, admiring your new"
                       " handheld light source",

    'lantern_failure': "\nYou step forward to the edge of the puddle and reach"
                       " as high as you can. You are just about to reach the"
                       " lantern when your foot slips and you stumble forward"
                       " into the puddle of corrosive liquid!"
                       " You leap backwards as fast as you can but the acid"
                       " burns your feet and hands!"
                       "\nYou take 1 point of damage",

    'health_potion': "\nThe lid unscrews easily"
                     " and a sickly sweet aroma floats out of the vial."
                     " You raise the vial to your lips and let the liquid"
                     " pour into your mouth. As soon as you've finished it"
                     " a strange feeling comes over you. You feel stronger,"
                     " healthier, refreshed - as if you've had a really good"
                     " night's sleep. You shake yourself out and continue on"
                     " feeling a tiny bit more able to take on the challenges"
                     " of this awful place."
}

enemy_text = {

      'ogre': "You suddenly hear a loud crash to your left. A hulking,"
              f" green {Fore.RED}ogre {Fore.WHITE}stands in the doorway."
              " You both stand frozen"
              " for a brief second before it bellows out in a deafening"
              " guttural roar:"
              "                    \n\n'MY BREEEEEEAD!!!!!'\n\n"
              " It bounds towards you and attacks!",

      'haunted_chest': "You reach down to open the chest, but before you"
                       " touch the latch, it springs open! Two encrusted"
                       " eyes snap open from lines in the wooden grain"
                       " and the chest leaps up at you, attempting to"
                       " clamp down on you with the hundreds of tiny teeth"
                       " that line the inside of its lid."
}

enemy_death = {

      'ogre': "You breath heavily and look around the room."
              " You don't know quite how you did that but you're"
              " thankful you're alive. Since the ogre won't be needing"
              " it anymore, you help yourself to the entire rest"
              " of the breadloaf: a well earned reward."
              f"{Fore.GREEN}\n\n"
              f"                **Your health increases by 10 points!**\n\n"
              f"{Fore.WHITE}",

      'haunted_chest': "The chest lies still, lid hanging open lifelessly."
                       " You wipe the sweat from your face and cautiously"
                       " peer into the body of the chest, where, amongst"
                       " broken bones, lies an ornate iron shield."
                       " You slowly reach your hand inside, grasp the shield"
                       " and quickly pull it out."
                       "This thing looks like it offers some serious"
                       " protection!",

      'gorehowl': "You fall to your knees beside the huge body of your"
                  " opponent, gasping for breath and staring at the"
                  " floor, dumbstruck over the feat you have just"
                  " accomplished. When you do look up, all the spectators"
                  " have vanished, and you are once again alone in this"
                  " massive arena. You pick yourself up and glance around"
                  " once more. The gate to the south, where this beast"
                  " emerged from has disappeared! but it looks like you"
                  " might just be able to climb up to the large alcove"
                  " on that side of the room.",

      'goblin': "You take a moment to curse your carelessness as the ugly,"
                " lifeless face of the goblin stares up at you. You glance"
                " around the room and see nothing but piles of bones"
                " and continue on your path.",

      'manor_lord': "You fall to the floor, battered and exhausted,"
                    " but you know you have finally triumphed over this"
                    " wretched place and its sadistic host."
                    " You look up at the final door and pull yourself slowly"
                    " to your feet. Dragging yourself over to the door, you"
                    " twist the handle, the door swings open and you"
                    " breathe in the night air, and escape from Fell Manor."

}
