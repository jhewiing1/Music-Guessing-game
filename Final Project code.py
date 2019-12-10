#introduction to the game
print('Hello! What is your name?')
myName = input("")
print('Well, ' + myName  +  '  this is Guess that song')
print("The game is about to start!")

 #There are 10 mutiple choice questions about the genre of hip-hop/rap
 # You get points for getting the correct answer and the goal is to have the most points as possible
 #Good luck!! 

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts=["Guess the song with these lyrics- 'bad things, its a lot of bad things'?\n(a) Stir Fry-Migos\n(b) God's Plam-Drake\n(c) Uproar-Lil Wayne\n",
"Guess the song with these lyrics-'sun is down, freezing cold\n That's how we already know winter's here'?\n(a) Nonstop-Drake\n(b) All the stars-Kendrick\n(c) Sicko Mode-Travis Scott\n", 
"Guess the song with these lyrics-'It's to the point that I love and I hate you\n And i cannot change you so i must replace you'?\n(a) Psycho-Post Malone\n(b)Lucid Dreams-Juice Wrld\n(c) Suge-Dababy\n", 
"Guess the song with these lyrics-'Cause I wnant ya, and I need ya\n And I'm down for you always'?\n(a) I like it- Cardi B\n(b) In my feelings- Drake\n(c) Wake up in the sky- Kodak Black\n",
"Guess the song with these lyrics- 'That's a real in your reflection\n Without a follow, without a mention'?\n(a)  Nice for what- Drake\n(b) No brainer- Dj Khaled\n(c)- Sunflower- Post Malone\n",
"Guess the song with these lyrics- 'Every other night, another dollar getting made\n Every other night started with a good day'?\n(a) Drip too hard- Gunna and Lil Baby\n(b) Yes Indeed- Lil Baby\n(c) Never recover- Gunna and Lil Baby\n",  
"Guess the song with these lyrics-'Eliot got me rocky\n Blow a socket,chicken terikayki'?\n(a) Nonstop-Drake\n(b) Mo Bamba- Sheck Wes\n(c) Walk it Talk it Migos\n",
"Guess the song with these lyrcis-'We at the door like we the delivery\n He not a plug, he the middle man'?\n(a) Going bad- Meek Mill\n(b) fall-Eminem\n(c) Look Alive- BlocBoy JB\n",
"Guess the song with these lyrics-'Aw, chains on the neck for the whole team\n And I feel like Gucci with the ice cream'?\n(a) ZEZE-Kodak Black\n(b) Taste- Tyga\n(c) Clout-Offset\n",
"Guess the song with these lyrics- I be drippin to death, I need a casket\n And we get more stripes than the ref'?\n(a) ZEZE- Kodak Black\n(b) Stargazing- Travis Scott\n(c) Don't come out the house- Metro Boomin\n"]
                    
              
                   

question=[Question(question_prompts[0],"b"),
          Question(question_prompts[1],"c"),
          Question(question_prompts[2],"b"), 
          Question(question_prompts[3],"b"),
          Question(question_prompts[4],"a"),
          Question(question_prompts[5],"a"),
          Question(question_prompts[6],"c"),
          Question(question_prompts[7],"c"),
          Question(question_prompts[8],"b"),
          Question(question_prompts[9],"a")]


     

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))
     print("Thanks for playing the game!")
     print("Try again if you think you can do better!")

run_quiz(question)
