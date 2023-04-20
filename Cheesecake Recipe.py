#Cheesecake recipe

import fractions

print('Welcome to the cheesecake recipe!')

SERVINGS_PER_CAKE = 12

slices = int(input("\nHow many servings of cheesecake do you want to make? (One serving is one slice): "))

print("\nFirst, we will start with the crust!")

grahamCrust = fractions.Fraction((slices/SERVINGS_PER_CAKE)*1.5).limit_denominator(10000)
sugarCrust = fractions.Fraction((slices/SERVINGS_PER_CAKE)*2).limit_denominator(10000)
brownSugarCrust = fractions.Fraction((slices/SERVINGS_PER_CAKE)).limit_denominator(10000)
butterCrust = fractions.Fraction((slices/SERVINGS_PER_CAKE)*7).limit_denominator(10000)

print("\nYou will need: \n\
-", grahamCrust, "cup(s) graham cracker crumbs\n\
-", sugarCrust, "tablespoon(s) of sugar\n\
-", brownSugarCrust, "tablespoon(s) of brown sugar\n\
-", butterCrust, "tablespoons of butter (melted)\n\
")

print("""

Here are the steps for the crust: 
1. Prepare Graham Cracker crust first by combining graham cracker crumbs, sugar, and brown sugar, and stirring well. Add melted butter and use a fork to combine ingredients well.
2. Pour crumbs into a 9” Springform pan(s) and press firmly into the bottom and up the sides of your pan. Set aside.

""")

input("Press enter key to continue. ")

print("Now for the real deal: the filling!\n")

creamCheeseCake = fractions.Fraction((slices/SERVINGS_PER_CAKE)*32).limit_denominator(10000)
sugarCake = fractions.Fraction((slices/SERVINGS_PER_CAKE)).limit_denominator(10000)
sourCreamCake = fractions.Fraction((slices/SERVINGS_PER_CAKE) * (2/3)).limit_denominator(10000)
vanillaCake = fractions.Fraction((slices/SERVINGS_PER_CAKE)*(1.5)).limit_denominator(10000)
saltCake = fractions.Fraction((slices/SERVINGS_PER_CAKE)*(1/8)).limit_denominator(10000)
eggsCake = fractions.Fraction((slices/SERVINGS_PER_CAKE)*4).limit_denominator(10000)

print("\nYou will need: \n\
-", creamCheeseCake, "oz of cream cheese (softened to room temperature)\n\
-", sugarCake, " cup(s) of sugar\n\
-", sourCreamCake, "cup(s) of sour cream\n\
-", vanillaCake, "teaspoon(s) of vanilla extract\n\
-", saltCake, "teaspoon(s) of salt\n\
-", eggsCake, "large egg(s) (room temperature, lightly beaten)\n\
")

print("""

1. Preheat oven to 325F (160C)

2. In the bowl of a stand mixer or in a large bowl (using a hand mixer) add cream cheese and stir until smooth and creamy (don't over-beat or you'll incorporate too much air).

3. Add sugar and stir again until creamy.

4. Add sour cream, vanilla extract, and salt, and stir until well-combined. If using a stand mixer, make sure you pause periodically to scrape the sides and bottom of the bowl with a spatula so that all ingredients are evenly incorporated.

5. With mixer on low speed, gradually add lightly beaten eggs, one at a time, stirring just until each egg is just incorporated. Once all eggs have been added, use a spatula to scrape the sides and bottom of the bowl again and make sure all ingredients are well combined.

6. Pour cheesecake batter into prepared springform pan. To insure against leaks, place pan on a cookie sheet that's been lined with foil.

7. Transfer to the center rack of your oven and bake on 325F (160C) for about 75 minutes. Edges will likely have slightly puffed and may have just begun to turn a light golden brown and the center should spring back to the touch but will still be Jello-jiggly. Don't over-bake or the texture will suffer, which means we all suffer.

8. Remove from oven and allow to cool on top of the oven³ for 10 minutes. Once 10 minutes has passed, use a knife to gently loosen the crust from the inside of the springform pan (this will help prevent cracks as your cheesecake cools and shrinks). Do not remove the ring of the springform pan.

9. Allow cheesecake to cool another 1-2 hours or until near room temperature before transferring to refrigerator and allowing to cool overnight or at least 6 hours. I remove the ring of the springform pan just before serving then return it to the pan to store. 

10. Cut up into slices and enjoy!

""")

input("Press enter key to exit. ")