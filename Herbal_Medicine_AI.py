print("===============================================")
print("")
print("*** WELCOME TO HERBAL SPECIALISTS***")
print("")
print("================================================")
name= input("Enter your name: ")
age=input("enter your age: ")
address=input("enter your address: ")
print("")
print("DISEASES THAT CAN BE CURED BY HERBAL TREATMENT")
print("")
print("1 caugh")
print("2 viral feaver")
print("3 maleria")
print("4 stomach ache")
print("5 diarrhea")
print("6 ulcer")
print("7 cancer")
print("8 blood pressure")
print("9 asthama")
print("10 rabis")
disease=input("enter your disease name from the above:")
p=disease.lower()
if(p=="caugh"):
 print("THE SYMPTOMS OF THE DISEASE ARE:")
 print("1 A runny or stuffy nose.A feeling of liquid running down the back of your throat (postnasal dripFrequent throat clearing and sore throat\n2 Hoarseness\n")
 tab1=input("treatment requird? yes or no")
 if(tab1=="yes"):
     print("The treatment that you required is:")
     print("")
     print("1:TREATMENT WITH PEPPERMINT LEAVES")
     print("")
     print("3-4 drops of pepperment oil for every 150ml of hot water\ndrape a towel over your head,and take deep breaths direvtly above the water")
     print("")
     print("Name:"+name)
     print("Age:"+age)
     print("The address of the patient is:"+address)
     print("Disease occured is:"+disease)
     print("***THANK YOU VISIT AGAIN***")
     
 else:
     print("THANK YOU!!!!")
elif(p=="viral feaver"):
    print("")
    print("THE SYMPTOMS OF THE DISEASE ARE:")
    print("")
    print("1 fatigue\n2 dizziness\n3 weakness\n4 chills\n5 headache\n6 muscle body and joint pains\n7 inflammation of the pharynx\n")
    tab2=input("treatment requird? yes or no")
    if(tab2=="yes"):
        print("THE TREATMENT THAT YOU REQUIRED IS:")
        print("1) MORNIGA")
        print(" is a tropical plant that has a variety of nutritional and medicinal benefits. Almost all parts of the plant contain vitamins, minerals, antioxidants, and antibacterial agents. A 2014 study found that Moringa bark reduced fevers in rabbits.")
        print("")
        print("2) Coriander Seeds")
        print("Containing essential vitamins and phytonutrients, coriander leaves are very much effective in boosting your immune system. They also contain antibiotic compounds and volatile oils. Thereby, coriander seeds make up a great herb for treating viral infection. You can seek the benefits of coriander leaves by either preparing a coriander tea, or making a coriander-water mixture for yourself")
        print("")
        print("3) Tulsi Leaves")
        print("With anti-bacterial, germicidal, anti-biotic and fungicidal properties, tulsi leaves are yet another effective home remedy for treating the symptoms of viral fever. All you have to do is boil some tulsi leaves in clean water, and mix a half-spoon clove powder. Let the solution boil until the water shrinks to half. Drink this solution in regular periods to fight off the infecti")
        print("4)  Rice Starch")
        print("Known as kanji in Hindi, rice starch is a popular home remedy for treating viral infection. It is known to work as a diuretic agent that increases urination and enhances immunity, thereby helping you cure viral fever.")
        print("")
        print("Name:"+name)
        print("Age:"+age)
        print("The address of the patient is:"+address)
        print("Disease occured is:"+disease)
        print("***THANK YOU VISIT AGAIN***")
    else:
        print("THANK YOU!!!!")      
elif(p=="maleria"):
    print("THE SYMPTOMS OF THE DISEASE ARE:")
    print("1 Head ache\n2 feaver\n3fatigue\n4 muscel pain\n 5 back pain\n 6 chills\n ")
    tab3=input("treatment requird? yes or no")
    if(tab3=="yes"):
        print("THE TREATMENT THAT YOU REQUIRED IS:")
        print("1) CINNAMON\n 2) GRAPEFRUIT\n 3) GINGER\n 4) ORANGE JUICE\n 5) HOLY BASIL\n 6)NATURAL DIET")
        print("")
        print("Name:"+name)
        print("Age:"+age)
        print("The address of the patient is:"+address)
        print("Disease occured is:"+disease)
        print("***THANK YOU VISIT AGAIN***")
    else:
     print("THANK YOU!!!!")
elif(p=="stomach ache"):
    print("THE SYMPTOMS OF THE DISEASE ARE:")
    print("A sevior pain in the stomach caused due to unhealthy diet")
    tab4=input("treatment requird? yes or no")
    if(tab4=="yes"):
        print("THE TREATMENT THAT YOU REQUIRED IS:")
        print("1)  Bitters and soda")
        print("A bar is probably the last place youíd think to look for relief from nausea, but many people swear by five or six drops of cocktail bitters mixed into a cold glass of tonic, club soda, or ginger ale")
        print("")
        print("2)Ginger ")
        print("A natural anti-inflammatory, ginger is available in many forms, all of which can help. Ginger chews and supplements are easy to take, while other people prefer their ginger in beverage form. Try an all-natural ginger ale or chop up some fresh ginger root and make a tea")
        print("")
        print("3) Chamomile tea")
        print("A nice cup of chamomile tea can help ease the pain of an upset stomach by acting as an anti-inflammatory. These anti-inflammatory properties help your stomach muscles relax, which can reduce the pain of cramping and spasms.")
        print("")
        print("4) BRAT diet")
        print(" BART contains low-fiber, high-binding foods. None of these foods contain salt or spices, which can further aggravate symptoms. This bland diet is a go-to for when youíre feeling sick but still have to eat something. Try overcooking the toast ó the charred bread is thought to reduce nausea")
        print("")
        print("Name:"+name)
        print("Age:"+age)
        print("The address of the patient is:"+address)
        print("Disease occured is:"+disease)
        print("***THANK YOU VISIT AGAIN***")
    else:
     print("THANK YOU!!!!")
        
elif(p=="diarrhea"):
    print("THE SYMPTOMS OF THE DISEASE ARE:")
    print("1 Loose, watery stools\n2 Abdominal cramps\n3 Abdominal pain\n4 Fever\n5 Blood in the stool\n6 Bloating\n7 Nausea.")
    print("")
    tab5=input("treatment requird? yes or no")
    if(tab5=="yes"):
        print("1) Bananas")
        print("Bananas are one of the best foods to eat while suffering from loose motions. The potassium in bananas will help in getting the digestion back to normal. Bananas contain resistant starch that helps to absorb water and salt in the colon and thus, makes your stool firmer. The fiber content in them also helps to restore normal bowel activity.")
        print("")
        print("2)Yogurt")
        print("One of the best foods for loose motion is yogurt which has a soothing and cooling effect on your stomach. It is a probiotic that helps to replenish your good gut bacteria that aid in digestion and healthier bowel movements.")
        print("")
        print("3)  White Rice")
        print("A light khichdi with moong dal can be a good option to add to your loose motion diet. It gives you the required strength and energy and is digested easily. White rice unlike fiber-rich whole grains is easier to digest and makes your stool more solid.")
        print("")
        print("4) Apples")
        print("If you're looking for a ideal food for lose motions, then skinned apples can be eaten. Apples are a good source of pectin, which has binding properties. Stewed apples are also a good option.  ")
        print("")
        print("Name:"+name)
        print("Age:"+age)
        print("The address of the patient is:"+address)
        print("Disease occured is:"+disease)
        print("***THANK YOU VISIT AGAIN***")
    else:
     print("THANK YOU!!!!")
        
        
elif(p=="ulcer"):
    print("THE SYMPTOMS OF THE DISEASE ARE:")
    print("1 dull pain in the stomach\n2 weight loss\n3 not wanting to eat because of pain\n4 nausea or vomiting\n5 bloating\n6 feeling easily full\n7 burping or acid")
    print("")
    tab6=input("treatment requird? yes or no")
    if(tab6=="yes"):
        print("1) Cabbage Juice")
        print("Cabbage is a popular natural ulcer remedy. Doctors reportedly used it decades before antibiotics were available to help heal stomach ulcers.Itís rich in vitamin C, an antioxidant shown to help prevent and treat H. pylori infections. These infections are the most common cause of stomach ulcers (3, 4, 5).")
        print("")
        print("2) Licorice")
        print("Licorice is a spice native to Asia and the Mediterranean region.It comes from the dried root of the Glycyrrhiza glabra plant and is a popular traditional herbal medicine used to treat many conditions.")
        print("")
        print("3) Honey")
        print("Honey is an antioxidant-rich food linked to a variety of health benefits. These include improved eye health and a reduced risk of heart disease, stroke and even certain types of cancer (15).Honey also appears to prevent the formation and promote the healing of many wounds, including ulcers (16).")
        print("")
        print("Name:"+name)
        print("Age:"+age)
        print("The address of the patient is:"+address)
        print("Disease occured is:"+disease)
        print("***THANK YOU VISIT AGAIN***")
    else:
     print("THANK YOU!!!!")
elif(p=="cancer"):
    print("THE SYMPTOMS OF THE DISEASE ARE:")
    print("1 Changes in bowel or bladder habits\n2 A sore that does not heal\n3 Unusual bleeding or discharge\n4 Thickening or lump in the breast or any other part of the body\n5 Indigestion or difficulty swallowing\n6 Obvious change in a wart or mole\n7 Nagging cough or hoarseness.")
    print("")
    tab7=input("treatment requird? yes or no")
    if(tab7=="yes"):
        print("1)Black cohosh")
        print("Herbalists often prescribe this to menopausal women who are experiencing hot flushes. While clinical trials show that black cohosh is relatively safe, it should not be used by people with liver damage. There is not enough scientific evidence to support the use of black cohosh in people with cancer.")
        print("")
        print("2) Ginkgo biloba and garlic")
        print("Studies have shown that these may have a blood-thinning effect, which can cause bleeding. This could be harmful in people with low platelet levels (e.g. from chemotherapy) or who are having surgery.")
        print("")
        print("3) Green tea")
        print("This has been to shown to stop the cancer bortezomib (VelcadeÆ) from working properly.")
        print("")
        print("Name:"+name)
        print("Age:"+age)
        print("The address of the patient is:"+address)
        print("Disease occured is:"+disease)
        print("***THANK YOU VISIT AGAIN***")
    else:
     print("THANK YOU!!!!")
        
elif(p=="blood preassure"):
    print("THE SYMPTOMS OF THE DISEASE ARE:")
    print("1 dull headaches\n2 dizzy spells\n3 nosebleeds\n")
    print("")
    tab8=input("treatment requird? yes or no")
    if(tab8=="yes"):
        print("1)  Eat more potassium-rich foods")
        print("It helps your body get rid of sodium and ease pressure on your blood vessels.Modern diets have increased most people's sodium intake while decreasing potassium intake (13).")
        print("")
        print("2) Cut back on caffeine")
        print("If you've ever downed a cup of coffee before you've had your blood pressure taken, you'll know that caffeine causes an instant boost.However, there's not a lot of evidence to suggest that drinking caffeine regularly can cause a lasting increase (14).")
        print("")
        print("3)Eat dark chocolate or cocoa")
        print("Here's a piece of advice you can really get behind.While eating massive amounts of chocolate probably won't help your heart, small amounts may.That's because dark chocolate and cocoa powder are rich in flavonoids, plant compounds that cause blood vessels to dilate (25).")
        print("")
        print("Name:"+name)
        print("Age:"+age)
        print("The address of the patient is:"+address)
        print("Disease occured is:"+disease)
        print("***THANK YOU VISIT AGAIN***")
    else:
     print("THANK YOU!!!!")
elif(p=="asthama"):
    print("THE SYMPTOMS OF THE DISEASE ARE:")
    print("1 chest pain or pressure that is atypical for the usual chest tightness associated with asthma\n2 coughing up blood\n3 high or long-lasting fever\n4 loss of appetite\n5 night sweats.")
    print("")
    tab9=input("treatment requird? yes or no")
    if(tab9=="yes"):
        print("Yoga Asana for asthma / Pranayama for asthma / Exercises for asthma")
        print("1) Bhujangasana (Cobra pose)")
        print("These poses expand the chest, increase blood circulation & improve oxygen in the body. They open chest and lungs. They improve the working of your respiratory system and keep a check on your hormone system")
        print("")
        print("2) Nadi Shodhan Pranayama & Kapalbhati")
        print("These alternative nostril breathing techniques help in relieving the accumulated stress of the body and the mind. These breathing techniques help in gaseous exchange in lungs to exhale out the retained CO2. These Pranayamas can efficiently improve your exhalation (CO2 retention is the main cause of obstructive disease like asthma)")
        print("")
        print("Name:"+name)
        print("Age:"+age)
        print("The address of the patient is:"+address)
        print("Disease occured is:"+disease)
        print("***THANK YOU VISIT AGAIN***")
    else:
     print("THANK YOU!!!!")

elif(p=="rabis"):
    print("THE SYMPTOMS OF THE DISEASE ARE:")
    print("1 pain or tingling at the bite site\n2 a general feeling of illness\n3 fever\n4 headache\n5 nausea and vomiting\n6 depression.")
    print("")
    tab10=input("treatment requird? yes or no")
    if(tab10=="yes"):
        print("1)DATHURA")
        print("APPLY THE JUICE OF DATHURA MIXING WITH RED CHILL")
        print("")
        print("2) TURKEY BERRY")
        print("TAKE A HAND FULL OF FRESH TURKEY BERRY LEAVES .GRIND THEM.ADD  1 TEASPOON OF SALT.APPLY ON THE EFFECTED PART TWICE A DAY FOR 3 DAYS")
        print("")
        print("3) INDIGO")
        print("CONSUME 1TSP LEAF JUICE WITH SAME QUANTITY OF MILK ONCE A DAY.USE IT FOR 1 WEEK")
        print("")
        print("Name:"+name)
        print("Age:"+age)
        print("The address of the patient is:"+address)
        print("Disease occured is:"+disease)
        print("***THANK YOU VISIT AGAIN***")
    else:
     print("THANK YOU!!!!")


print("=========================================================================================================================================================")
print("")
print("THANK YOU FOR VISITING US!!!!!!!!!!!")
print("")
print("==========================================================================================================================================================") 
time.sleep(15)     
