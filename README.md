# PROTOTYPE
# STILL IN DEVELOPMENT
# WHAT IS IT ?
Do you have a black shirt and do not know what to wear with it ?
You could search hours on the internet or you could use Fashion API.
Fashion API suggests you clothes based on your Criteria. 
Read API documentation for more info.
# API DOCUMENTATION 
Base URL : /api
# Data to choose from :
shirt_colors = [Black , Maroon, Green, Deep Green, Brown, Blue, Yellow, Deep violet, Deep Blue]
pant_colors = [white, khaki, Light Blue, Light Green, grey]
shirts = [polo-tshirt,  henley-tshirt, collar-shirt, no-collar-shirt]
pants = [jeans ,chinos]
accessories = [brown-watch, brown-shoes, white-shoes]
place = [party, date, hangout ]
gender = [male, female, unisex]
# GET REQUEST OPTIONS :
type

gender

place

shirt_color

shirt_type

pant_color

pant_type

accessories
# Options allowed to be paired :
type  and gender  and place  and shirt_color :            

type  and gender  and place and shirt_type :

type  and gender  and place and pant_color :

type  and gender  and place and pant_type :

type  and gender  and place and shirt_color and shirt_type :

type  and gender  and place and pant_color and pant_type :

type   and place  and shirt_color and shirt_type :

type  and  place  and pant_color and pant_type :

type  and  gender  and shirt_color and shirt_type :

type  and  gender and pant_color and pant_type :

type   and place  and shirt_color  :

type   and place and shirt_type  :

type   and  place and pant_color  :

type  and  place  and pant_type :

type   and  gender  and shirt_color  :

type   and gender  and shirt_type :

type   and  gender  and pant_color  :

type  and  gender  and pant_type :

type  and gender and place :

type  and  place  :

type  and  gender :

gender  and  place :

shirt_color and shirt_type :

pant_color and pant_type :

type :

place :

gender :

shirt_color:

shirt_type :

pant_color:

pant_type :

accessories  :

# Sample GET REQUEST :
<URL>/api?shirt_color=Black&shirt_type=polo-tshirt

