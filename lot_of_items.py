#!/usr/bin/env python3

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, User, Category, Item

from flask import Flask, render_template, redirect, url_for, request, jsonify, flash
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, User, Category, Item

app = Flask(__name__)

engine = create_engine("sqlite:///catalog.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


print ("Creating Admin...")

admin = User(username="admin", email="admin@admin.com", password="123")
session.add(admin)
session.commit()

print ("Admin Created")


print ("Creating Categories ...")

arts = Category(name="Arts & Photography")
session.add(arts)
session.commit()

biographs = Category(name="Biographies & Memoirs")
session.add(biographs)
session.commit()

business = Category(name="Business & Investing")
session.add(business)
session.commit()

children = Category(name="Children's Books")
session.add(children)
session.commit()

cookbooks = Category(name="Cookbooks, Food & Wine")
session.add(cookbooks)
session.commit()

history = Category(name="History")
session.add(history)
session.commit()

fiction = Category(name="Literature & Fiction")
session.add(fiction)
session.commit()

mystery = Category(name="Mystery & Suspense")
session.add(mystery)
session.commit()

romance = Category(name="Romance")
session.add(romance)
session.commit()

scifi = Category(name="Sci-fi & Fantasy")
session.add(scifi)
session.commit()

teens = Category(name="Teens & Young Adult")
session.add(teens)
session.commit()


print ("Categories Created!")

print ("Creating Items ...")

# Arts books
the5Love = Item(name="The 5 Love Languages: The Secret to Love that Lasts",
        description="In the 1o New York Times bestseller The 5 Love Languages, you'll discover the secret that has transformed millions of relationships worldwide. Whether your relationship is flourishing or failing, Dr. Gary Chapman's proven approach to showing and receiving love will help you experience deeper and richer levels of intimacy with your partner-starting today.",
        category=arts,
        user=admin)

session.add(the5Love)
session.commit()

homebody = Item(name="Homebody: A Guide to Creating Spaces You Never Want to Leave",
        description="In Homebody: A Guide to Creating Spaces You Never Want to Leave, Joanna Gaines walks you through how to create a home that reflects the personalities and stories of the people who live there. Using examples from her own farmhouse as well as a range of other homes, this comprehensive guide will help you assess your priorities and instincts, as well as your likes and dislikes, with practical steps for navigating and embracing your authentic design style. Room by room, Homebody gives you an in-depth look at how these styles are implemented as well as how to blend the looks you're drawn to in order to create spaces that feel distinctly yours. A removable design template at the back of the book offers a step-by-step guide to planning and sketching out your own design plans. The insight shared in Homebody will instill in you the confidence to thoughtfully create spaces you never want to leave.",
        category=arts,
        user=admin)

session.add(homebody)
session.commit()


momLife= Item(name="Mom Life: A Snarky Adult Coloring Book",
        description="It's 6:30 PM. By some miracle, one of your kids is asleep while the other is watching cartoons in a food coma. Quick! Here's your chance! Grab some colored pencils and markers, this coloring book, and run to the bathroom (don't forget the wine)! First, lock the door and enjoy the solitude of private urination. Second, gulp down that wine and enjoy the most relaxing five minutes of your day as you surrender to the quietness and creativity of coloring. Celebrate the humor and frustration that are the highs and lows of motherhood featured in the pages of this book.",
        category=arts,
        user=admin)

session.add(momLife)
session.commit()


# Biographs books
howard = Item(name="Howard Stern Comes Again",
        description="Over his unrivaled four-decade career in radio, Howard Stern has interviewed thousands of personalities-discussing sex, relationships, money, fame, spirituality, and success with the boldest of bold-faced names. But which interviews are his favorites? It's one of the questions he gets asked most frequently. Howard Stern Comes Again delivers his answer.",
        category=biographs,
        user=admin)

session.add(howard)
session.commit()


becoming = Item(name="Becoming",
        description="In a life filled with meaning and accomplishment, Michelle Obama has emerged as one of the most iconic and compelling women of our era. As First Lady of the United States of America-the first African American to serve in that role-she helped create the most welcoming and inclusive White House in history, while also establishing herself as a powerful advocate for women and girls in the U.S. and around the world, dramatically changing the ways that families pursue healthier and more active lives, and standing with her husband as he led America through some of its most harrowing moments. Along the way, she showed us a few dance moves, crushed Carpool Karaoke, and raised two down-to-earth daughters under an unforgiving media glare. ",
        category=biographs,
        user=admin)

session.add(becoming)
session.commit()


waltDisney = Item(name="Walt Disney",
        description="Walt Disney was a true visionary whose desire for escape, iron determination and obsessive perfectionism transformed animation from a novelty to an art form, first with Mickey Mouse and then with his feature films-most notably Snow White, Fantasia, and Bambi. In his superb biography, Neal Gabler shows us how, over the course of two decades, Disney revolutionized the entertainment industry. In a way that was unprecedented and later widely imitated, he built a synergistic empire that combined film, television, theme parks, music, book publishing, and merchandise. Walt Disney is a revelation of both the work and the man-of both the remarkable accomplishment and the hidden life.",
        category=biographs,
        user=admin)

session.add(waltDisney)
session.commit()

muellerReport = Item(name="The Mueller Report",
        description="Read the findings of the Special Counsel's investigation into Russian interference in the 2016 election, complete with accompanying analysis by the Post reporters who've covered the story from the beginning.",
        category=biographs,
        user=admin)

session.add(muellerReport)
session.commit()

# Business books
daring = Item(name="Daring Greatly: How the Courage to Be Vulnerable Transforms the Way We Live, Love, Parent, and Lead",
        description="Every day we experience the uncertainty, risks, and emotional exposure that define what it means to be vulnerable or to dare greatly. Based on twelve years of pioneering research, Brene Brown PhD, LMSW, dispels the cultural myth that vulnerability is weakness and argues that it is, in truth, our most accurate measure of courage.",
        category=business,
        user=admin)

session.add(daring)
session.commit()

richDad = Item(name="Rich Dad Poor Dad: What the Rich Teach Their Kids About Money - That the Poor and Middle Class Do Not!",
        description="Robert Kiyosaki has challenged and changed the way tens of millions of people around the world think about money. With perspectives that often contradict conventional wisdom, Robert has earned a reputation for straight talk, irreverence, and courage. He is regarded worldwide as a passionate advocate for financial education.",
        category=business,
        user=admin)

session.add(richDad)
session.commit()


cribsheet = Item(name="Cribsheet: A Data-Driven Guide to Better, More Relaxed Parenting, from Birth to Preschool",
        description="With Expecting Better, award-winning economist Emily Oster spotted a need in the pregnancy market for advice that gave women the information they needed to make the best decision for their own pregnancies. By digging into the data, Oster found that much of the conventional pregnancy wisdom was wrong. In Cribsheet, she now tackles an even greater challenge: decision-making in the early years of parenting.",
        category=business,
        user=admin)

session.add(cribsheet)
session.commit()


earnIt = Item(name="Earn It!: Know Your Value and Grow Your Career, in Your 20s and Beyond",
        description="The whirlwind of job applications, interviews, follow-up, resume building, and networking is just the beginning. What happens after you've landed the job, settled in, and begun to make a difference-where do you go from here? What if you feel stuck in what you thought would be your dream profession? New York Times bestselling author Mika Brzezinski and producer Daniela Pierre-Bravo provide an essential manual for those crucial next steps. Earn It! is a practical career guidebook that not only helps you get your foot in the door; it also shows you how to negotiate a raise, advocate for more responsibility, and figure out whether you're in the career that's right for you.",
        category=business,
        user=admin)

session.add(earnIt)
session.commit()


# Children's books
ohPlaces = Item(name="Oh, the Places You'll Go!",
        description="From soaring to high heights and seeing great sights to being left in a Lurch on a prickle-ly perch, Dr. Seuss addresses life's ups and downs with his trademark humorous verse and illustrations, while encouraging readers to find the success that lies within. In a starred review, Booklist notes, 'Seuss's message is simple but never sappy: life may be a 'Great Balancing Act,' but through it all 'There's fun to be done.'' A perennial favorite and a perfect gift for anyone starting a new phase in their life!",
        category=children,
        user=admin)

session.add(ohPlaces)
session.commit()


caterpillar = Item(name="The Very Hungry Caterpillar",
        description="THE all-time classic picture book, from generation to generation, sold somewhere in the world every 30 seconds! Have you shared it with a child or grandchild in your life?",
        category=children,
        user=admin)

session.add(caterpillar)
session.commit()

drSeuss = Item(name="Dr. Seuss's Beginner Book Collection",
        description="A perfect gift for new parents, birthday celebrations, and happy occasions of all kinds, this collection of five beloved Beginner Books by Dr. Seuss-The Cat in the Hat, One Fish Two Fish Red Fish Blue Fish, Green Eggs and Ham, Hop on Pop, and Fox in Socks-will be cherished by young and old alike. Ideal for reading aloud or reading alone, they will begin a child on the adventure of a lifetime!",
        category=children,
        user=admin)

session.add(drSeuss)
session.commit()

# Cookbooks
airFryer = Item(name="The Skinnytaste Air Fryer Cookbook: The 75 Best Healthy Recipes for Your Air Fryer",
        description="1o New York Times bestselling author Gina Homolka is beloved for her incredible recipes that transform your favorite, comforting foods into healthy, low-cal dishes with tons of flavor. Now, she brings her expertise to the game-changing air fryer appliance. Using high-powered, super hot, circulating air like a convection oven, air fryers crisp up your favorite 'fried' foods with barely any oil needed. Cook times are shorter than traditional oven methods and the process requires little clean-up--meaning less time spent cooking and cleaning.",
        category=cookbooks,
        user=admin)

session.add(airFryer)
session.commit()

magnolia = Item(name="Magnolia Table: A Collection of Recipes for Gathering",
        description="Magnolia Table is infused with Joanna Gaines' warmth and passion for all things family, prepared and served straight from the heart of her home, with recipes inspired by dozens of Gaines family favorites and classic comfort selections from the couple's new Waco restaurant, Magnolia Table.",
        category=cookbooks,
        user=admin)

session.add(magnolia)
session.commit()

# History books
pioneers = Item(name="The Pioneers: The Heroic Story of the Settlers Who Brought the American Ideal West",
        description="As part of the Treaty of Paris, in which Great Britain recognized the new United States of America, Britain ceded the land that comprised the immense Northwest Territory, a wilderness empire northwest of the Ohio River containing the future states of Ohio, Indiana, Illinois, Michigan, and Wisconsin. A Massachusetts minister named Manasseh Cutler was instrumental in opening this vast territory to veterans of the Revolutionary War and their families for settlement. Included in the Northwest Ordinance were three remarkable conditions: freedom of religion, free universal education, and most importantly, the prohibition of slavery. In 1788 the first band of pioneers set out from New England for the Northwest Territory under the leadership of Revolutionary War veteran General Rufus Putnam. They settled in what is now Marietta on the banks of the Ohio River.",
        category=history,
        user=admin)

session.add(pioneers)
session.commit()


harryS = Item(name="The Accidental President: Harry S. Truman and the Four Months That Changed the World",
        description="eroes are often defined as ordinary characters who get pushed into extraordinary circumstances, and through courage and a dash of luck, cement their place in history. Chosen as FDR's fourth-term vice president for his well-praised work ethic, good judgment, and lack of enemies, Harry S. Truman was the prototypical ordinary man. That is, until he was shockingly thrust in over his head after FDR's sudden death. The first four months of Truman's administration saw the founding of the United Nations, the fall of Berlin, victory at Okinawa, firebombings in Tokyo, the first atomic explosion, the Nazi surrender, the liberation of concentration camps, the mass starvation in Europe, the Potsdam Conference, the controversial decision to bomb Hiroshima and Nagasaki, the surrender of imperial Japan, and finally, the end of World War II and the rise of the Cold War.",
        category=history,
        user=admin)

session.add(harryS)
session.commit()

# Literature & Fiction books
gotBook1 = Item(name="A Game of Thrones: A Song of Ice and Fire, Book 1",
        description="Winter is coming. Such is the stern motto of House Stark, the northernmost of the fiefdoms that owe allegiance to King Robert Baratheon in far-off King's Landing. There Eddard Stark of Winterfell rules in Robert's name. There his family dwells in peace and comfort: his proud wife, Catelyn; his sons Robb, Brandon, and Rickon; his daughters Sansa and Arya; and his bastard son, Jon Snow. Far to the north, behind the towering Wall, lie savage Wildings and worse - unnatural things relegated to myth during the centuries-long summer, but proving all too real and all too deadly in the turning of the season. Yet a more immediate threat lurks to the south, where Jon Arryn, the Hand of the King, has died under mysterious circumstances. Now Robert is riding north to Winterfell, bringing his queen, the lovely but cold Cersei, his son, the cruel, vainglorious Prince Joffrey, and the queen's brothers Jaime and Tyrion of the powerful and wealthy House Lannister - the first a swordsman without equal, the second a dwarf whose stunted stature belies a brilliant mind. ",
        category=fiction,
        user=admin)

session.add(gotBook1)
session.commit()


valencia = Item(name="Valencia and Valentine",
        description="Valencia, a timid debt collector with crippling OCD, is afraid of many things, but the two that scare her most are flying and turning thirty-five. To confront those fears, Valencia's therapist suggests that she fly somewhere-anywhere-before her upcoming birthday. And as Valencia begins a telephone romance with a man from New York, she suddenly has a destination in mind. There's only one problem-he might not actually exist.",
        category=fiction,
        user=admin)

session.add(valencia)
session.commit()


amyByler = Item(name="The Overdue Life of Amy Byler",
        description="Overworked and underappreciated, single mom Amy Byler needs a break. So when the guilt-ridden husband who abandoned her shows up and offers to take care of their kids for the summer, she accepts his offer and escapes rural Pennsylvania for New York City.",
        category=fiction,
        user=admin)

session.add(amyByler)
session.commit()


yellowSun = Item(name="Half of a Yellow Sun",
        description="With effortless grace, celebrated author Chimamanda Ngozi Adichie illuminates a seminal moment in modern African history: Biafra's impassioned struggle to establish an independent republic in southeastern Nigeria during the late 1960s. We experience this tumultuous decade alongside five unforgettable characters: Ugwu, a thirteen-year-old houseboy who works for Odenigbo, a university professor full of revolutionary zeal; Olanna, the professor's beautiful young mistress who has abandoned her life in Lagos for a dusty town and her lover's charm; and Richard, a shy young Englishman infatuated with Olanna's willful twin sister Kainene. Half of a Yellow Sun is a tremendously evocative novel of the promise, hope, and disappointment of the Biafran war.",
        category=fiction,
        user=admin)

session.add(yellowSun)
session.commit()


abduction = Item(name="The 18th Abduction (Women's Murder Club)",
        description="For a trio of colleagues, an innocent night out after class ends in a deadly torture session. They vanish without a clue -- until a body turns up. With the safety of San Francisco's entire school system at stake, Lindsay has never been under more pressure. As the chief of police and the press clamor for an arrest in the 'school night' case, Lindsay turns to her best friend, investigative journalist Cindy Thomas. Together, Lindsay and Cindy take a new approach to the case, and unexpected facts about the victims leave them stunned.",
        category=fiction,
        user=admin)

session.add(abduction)
session.commit()

# Mistery books
warning = Item(name="The Warning",
        description="A small southern town was evacuated after a freak power-plant accident. As the first anniversary of the mishap approaches, some residents are allowed to return past the national guard roadblocks.",
        category=mystery,
        user=admin)

session.add(warning)
session.commit()

crissCross = Item(name="Criss Cross",
        description='In a Virginia penitentiary, Alex Cross and his partner, John Sampson, witness the execution of a killer they helped convict. Hours later, they are called to the scene of a copycat crime. A note signed "M" rests on the corpse.  "You messed up big time, Dr. Cross."',
        category=mystery,
        user=admin)

session.add(crissCross)
session.commit()

deadlySin = Item(name="14th Deadly Sin (Women's Murder Club)",
        description="With a beautiful baby daughter and a devoted husband, Detective Lindsay Boxer can safely say that her life has never been better. Things seem to be going well for a change when all the members of the Women's Murder Club gather to celebrate San Francisco Medical Examiner Claire Washburn's birthday. But the party is cut short when Lindsay is called to a gruesome crime scene, where a woman has been murdered in broad daylight.",
        category=mystery,
        user=admin)

session.add(deadlySin)
session.commit()

oneGood = Item(name="One Good Deed",
        description="It's 1949. When war veteran Aloysius Archer is released from Carderock Prison, he is sent to Poca City on parole with a short list of do's and a much longer list of don'ts: do report regularly to his parole officer, don't go to bars, certainly don't drink alcohol, do get a job--and don't ever associate with loose women.",
        category=mystery,
        user=admin)

session.add(oneGood)
session.commit()

# Romance books
tempest = Item(name="Brave the Tempest (Cassie Palmer)",
        description="Cassie Palmer has been chief seer of the supernatural world for a little over four months. In that time, she's battled two gods, fallen in love with two men, and confronted the two sides of her own nature, both god and human. So it's not surprising that she currently finds herself facing two adversaries, although they have a single purpose: to wipe out the supernatural community's newest fighting force, leaving it vulnerable to enemies in this world and beyond.",
        category=romance,
        user=admin)

session.add(tempest)
session.commit()

nightBroken = Item(name="Night Broken (A Mercy Thompson Novel)",
        description="When her mate's ex-wife storms back into their lives, Mercy knows something isn't right. Christy has the furthest thing from good intentions-she wants Adam back, and she's willing to do whatever it takes to get him, including turning the pack against Mercy.",
        category=romance,
        user=admin)

session.add(nightBroken)
session.commit()

silenceFallen = Item(name="Silence Fallen (A Mercy Thompson Novel)",
        description="",
        category=romance,
        user=admin)

session.add(silenceFallen)
session.commit()

# Sci-fi & Fantasy books
clairdelune = Item(name="The Missing of Clairdelune: Book Two of The Mirror Visitor Quartet",
        description="When Ophelia is promoted to Vice-storyteller by Farouk, the ancestral Spirit of Pole, she finds herself unexpectedly thrust into the public spotlight. her gift-the ability to read the secret history of objects-is now known by all, and there can be no greater threat to the nefarious denizens of her icy adopted home than this. ",
        category=scifi,
        user=admin)

session.add(clairdelune)
session.commit()


fiveUnicorn = Item(name="Five Unicorn Flush (The Reason)",
        description="Reasonspace is in shambles after the disappearance of all magical creatures. Without faster-than-light travel, supply and communication routes have dried up, leaving humankind stranded and starving. Cowboy Jim and his complement of Reason soldiers search for the relocated Bala using the only surviving FTL drive. On their new utopian planet, the Bala are on the brink of civil war between those who want peace under old-fashioned unicorn rule and those who seek revenge on their human oppressors. Only Captain Jenny and her new brain parasite can stop the Reason plan to enslave the Bala again.",
        category=scifi,
        user=admin)

session.add(fiveUnicorn)
session.commit()


breach = Item(name="Breach (An Analog Novel)",
        description="When you've betrayed your revolutionary cadre, an off-grid fight club on a remote tropical island is a good place to hide-or die.",
        category=scifi,
        user=admin)

session.add(breach)
session.commit()

# Teens books
harryPotter = Item(name="Harry Potter and the Sorcerer's Stone",
        description="Harry Potter has never even heard of Hogwarts when the letters start dropping on the doormat at number four, Privet Drive. Addressed in green ink on yellowish parchment with a purple seal, they are swiftly confiscated by his grisly aunt and uncle. Then, on Harry's eleventh birthday, a great beetle-eyed giant of a man called Rubeus Hagrid bursts in with some astonishing news: Harry Potter is a wizard, and he has a place at Hogwarts School of Witchcraft and Wizardry. An incredible adventure is about to begin!",
        category=teens,
        user=admin)

session.add(harryPotter)
session.commit()

supernatural = Item(name="Supernatural Academy: Year One",
        description="The Supernatural Academy is where shifters, vampires, magic users, and fey are educated. Where they are taught about their abilities, and how to function in the human world. Maddison already has the human part down, but this supernatural thing is an entirely new dangerous game.",
        category=teens,
        user=admin)

session.add(supernatural)
session.commit()

shadowspell = Item(name="Shadowspell Academy: The Culling Trials",
        description="My younger brother has been chosen for the prestigious, secret magical school hidden within the folds of our mundane world. A place so dangerous, they don't guarantee you'll make it out alive.",
        category=teens,
        user=admin)

infinityWar = Item(name="Infinity War: Collected Edition",
        description="When evil dopplegangers of the Marvel heroes appear, it's all-out war! Why has Magus unleashed them on an unsuspecting world? And is the heroes only hope?Thanos?! Plus, will the Infinity Gauntlet swing the tide of the war?",
        category=teens,
        user=admin)

session.add(infinityWar)
session.commit()

print ("Items Created!")
