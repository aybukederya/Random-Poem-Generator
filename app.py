from flask import *
from haiku_generator import *
import random


app = Flask(__name__)
app.secret_key = "poem" 

@app.route('/', methods=['POST', 'GET'])

   
def generate():
    poem = haiku()
    poem = poem.split("/n")

    first_line = poem[0]
    second_line = poem[1]
    third_line = poem[2]

    r = (random.randint(128,255) + 255) /2
    g = (random.randint(128,255)+255) /2
    b = (random.randint(128,255)+255) /2 

    '''
    color_value = (r,g,b,0.6)
    color_value=str(color_value)
    color_value="rgba"+color_value

    title_value = (r,g,b,1)
    title_value=str(title_value)
    title_value="rgba"+title_value

    
    r_lighter = (r + 255)/2
    g_lighter= (g + 255)/2
    b_lighter= (b + 255)/2
    
    
    lighter_color_value = (r_lighter,g_lighter,b_lighter,0.4)

    

    lighter_color_value=str(lighter_color_value)
    lighter_color_value="rgba"+lighter_color_value
    '''

    #complementary = (255-r, 255-g, 255-b, 0.1)
    #lighter_color_value=str(complementary)
    #lighter_color_value="rgba"+lighter_color_value
    
    hue = random.randint(0,360)
    saturation = random.randint(25,95)
    lightness = random.randint(85,95)

    color = "hsl("+ str(hue) + ', ' +  str(saturation) + '%, ' + str(lightness) + '%)'
    back_color = "hsl("+ str((hue+180)%360) + ', ' +  str(saturation) + '%, ' + str(lightness) + '%)'
    title = "hsl("+ str(hue) + ', ' +  str(saturation) + '%, ' + str(lightness) + '%)'
    return render_template("index.html", title_value=title, lighter_color_value = back_color, first_line=first_line, second_line=second_line, third_line=third_line, color_value=color)
    
    
    
    
    
