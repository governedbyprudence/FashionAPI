import random
deep_colors = ["Black","Maroon","Green","Deep Green","Brown","Blue","Yellow","Deep violet","Deep Blue"]
light_colors = ["white","khaki","Light Blue","Light Green","grey"]
shirts = ["polo-tshirt","henley-tshirt","collar-shirt","no-collar-shirt"]
pants = ["jeans","chinos"]
accessories = ["brown-watch","brown-shoes","white-shoes"]
combo=[]
for i in deep_colors:
    for j in shirts:
        for k in light_colors:
            for l in pants:
                if i not in k:
                    combo.append(f"{i} {j} {k} {l} {accessories[random.randint(0,len(accessories)-1)]}")


