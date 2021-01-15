#random poem generator
import random
from tkinter import *

#Create vowel and words that act like they are starting with vowel lists
#so that the appropriate article can be assigned
VOWELS = "eoaui"
H_WORDS = ["honor","hour","honest","heir"]

#Create appropriate word lists
VERB_INTRANSITIVE_SINGULAR = ["runs","sleeps","dreams","laughs","cries","howls","chuckles","sits","falls","bakes","cooks","writes","eats","breaks","dies","coughs","goes","sits","sneezes", "smiles", "bakes", "dreams", "walks", "hates", "understands", "thinks", "falls", "winces", "loves", "ponders"]
VERB_TRANSITIVE_SINGULAR = ["sees","likes","eats","smells","writes","bakes","cooks","tells","breaks","opens","borrows","cleans","kicks","swallows","steals","kills","closes"]
VERB_DIRECT_SINGULAR = ["gives","sends","brings","buys"]
VERB_SINGULAR = VERB_INTRANSITIVE_SINGULAR + VERB_TRANSITIVE_SINGULAR + VERB_DIRECT_SINGULAR

PRONOUNS_SINGULAR = ["he","she","it"]
HIM_HER = ["him", "her", "them"]

DEFINITE = ["a","the", "one", "that"]
PREPOSITON = ["in", "like", "on","at","around","along", "next to", "during"]
CONJUGATION = ["and","but","however","while","furthermore","but I believe","when", "as", "yet", "still"]
CANNONICAL = ["very","nearly","somewhat","hardly","completely","rather", "sometimes"]

#Open text files and create the relevant word lists for these
noun_singulars = open("nouns_singular.txt")
adjectives = open("ADJECTIVEs.txt")
adverbs = open("ADVERBs.txt")

NOUN_SINGULAR = []
ADJECTIVE = []
ADVERB = []
for elements in noun_singulars:
    NOUN_SINGULAR.append(elements.strip())
for elements in adjectives:
    ADJECTIVE.append(elements.strip())
for elements in adverbs:
    ADVERB.append(elements.strip())
    


def noun_phrase():
    #Create the noun phrase by selecting random cannonicals, adjectives and nouns
    #Assign the article appropriately, according to the word's first letter
    #Return the appropriate noun phrase in a list format
    cannonical = 0
    adj = random.choice([0,1])
    if adj == 1:
        cannonical = random.choice([0,0,0,0,1])
    
    my_article = random.choice(DEFINITE)
    my_adj = random.choice(ADJECTIVE)
    my_noun_singular = random.choice(NOUN_SINGULAR)
    my_cannonical = random.choice(CANNONICAL)
    
    if adj == 0 and cannonical == 0:
        if my_article == "a" or my_noun_singular in H_WORDS:
            if my_noun_singular[0] in VOWELS:
                my_article = "an"
        return [my_article, my_noun_singular]
    
    if adj == 1 and cannonical == 0:
        if my_article == "a" or my_adj in H_WORDS:
            if my_adj[0] in VOWELS:
                my_article = "an"
        return [my_article, my_adj, my_noun_singular]
        
    if adj == 1 and cannonical == 1:
        if my_article == "a":
            if my_cannonical[0] in VOWELS:
                my_article == "an"
        return [my_article, my_cannonical, my_adj, my_noun_singular]
                
            
    
def verb_phrase():
    #Create the verb phrase by selecting random verb phrase formats, 
    #Return the appropriate noun phrase in a list format
    which = random.choice([0,1,2,3,4,5])
    if which == 0:
        return [random.choice(VERB_INTRANSITIVE_SINGULAR)]
    if which == 1:
        return [random.choice(VERB_TRANSITIVE_SINGULAR), noun_phrase()]
    if which == 2:
        return [random.choice(VERB_DIRECT_SINGULAR), noun_phrase(), "to", noun_phrase()]
    if which == 3:
        return [random.choice(VERB_INTRANSITIVE_SINGULAR),random.choice(ADVERB)]
    if which == 4:
        return [verb_phrase(), preposition_phrase()]
    return [random.choice(VERB_DIRECT_SINGULAR), noun_phrase(), "to", random.choice(HIM_HER)]
    
def preposition_phrase():
    #Return the preposition phrase in a list format by selecting a random preposition and calling the noun phrase
    return [random.choice(PREPOSITON), noun_phrase()]
    


def haiku():
    #Create the haiku in a list format
    #Then transform it to a string by iterating a for loop over the list elements
    #Return the haiku string 
    output = [noun_phrase(), [random.choice(VERB_INTRANSITIVE_SINGULAR),random.choice(ADVERB)], preposition_phrase()]


    my_haiku = "\n"

    for outer_elements in output:
        for inner_elements in outer_elements:
            if type(inner_elements) == str:
                my_haiku += inner_elements + " " 
            else:
                for word in inner_elements:
                    my_haiku += word + " "
        my_haiku += "\n"
    
    return my_haiku


def show_haiku_pop_up():
    #Create the popup window that will display the haiku
    root = Tk()
    root.title("Random Haiku Generator")
    width = 300    
    height = 200    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width - width)/2
    y_coordinate = (screen_height - height)/2
    root.geometry('%dx%d+%d+%d' % (width, height, x_coordinate, y_coordinate))
    window = Label(root, text=haiku(), width=120, height=10)
    window.pack()
    
    #create the button that lets the user ask for another poem
    again_button = Button(root, text="Generate me another one!", command = lambda:[root.destroy(), show_haiku_pop_up()], width=25)
    again_button.pack()
    mainloop()
    


show_haiku_pop_up()






