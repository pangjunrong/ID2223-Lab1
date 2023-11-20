import os
import modal

LOCAL=True

if LOCAL == False:
   stub = modal.Stub("wine_daily")
   image = modal.Image.debian_slim().pip_install(["hopsworks"]) 

   @stub.function(image=image, schedule=modal.Period(days=1), secret=modal.Secret.from_name("id2223"))
   def f():
       g()


def generate_wine(quality, fixed_acidity_min, fixed_acidity_max, volatile_acidity_min, volatile_acidity_max,
        citric_acid_min, citric_acid_max, residual_sugar_min, residual_sugar_max,
        chlorides_min, chlorides_max, free_sulfur_dioxide_min, free_sulfur_dioxide_max,
        total_sulfur_dioxide_min, total_sulfur_dioxide_max, density_min, density_max,
        pH_min, pH_max, sulphates_min, sulphates_max, alcohol_min, alcohol_max):
    """
    Returns a single wine as a single row in a DataFrame
    """
    import pandas as pd
    import random

    df = pd.DataFrame({"type": [random.choice(["white","red"])],
                        "fixed_acidity": [random.uniform(fixed_acidity_min, fixed_acidity_max)],
                       "volatile_acidity": [random.uniform(volatile_acidity_min, volatile_acidity_max)],
                       "citric_acid": [random.uniform(citric_acid_min, citric_acid_max)],
                       "residual_sugar": [random.uniform(residual_sugar_min, residual_sugar_max)],
                        "chlorides": [random.uniform(chlorides_min, chlorides_max)],
                        "free_sulfur_dioxide": [random.uniform(free_sulfur_dioxide_min, free_sulfur_dioxide_max)],
                        "total_sulfur_dioxide": [random.uniform(total_sulfur_dioxide_min, total_sulfur_dioxide_max)],
                        "density": [random.uniform(density_min, density_max)],
                        "pH": [random.uniform(pH_min, pH_max)],
                        "sulphates": [random.uniform(sulphates_min, sulphates_max)],
                        "alcohol": [random.uniform(alcohol_min, alcohol_max)],

                      })
    df['quality'] = quality
    return df


def get_random_wine():
    """
    Returns a DataFrame containing one random wine
    """
    import pandas as pd
    import random

    three_df = generate_wine(3, 4.2, 10.5, 0.2, 1.2, 0, 0.7, 1, 17, 0.02, 0.15, 0, 60, 0, 380, 0.99, 1.00, 2.9, 3.6, 0.25, 0.75, 8, 12.8)
    four_df = generate_wine(4, 4.5, 10.5, 0.1, 1.18, 0, 0.75, 1, 14, 0.02, 0.12, 0, 55, 0, 280, 0.99, 1.00, 2.8, 3.7, 0.25, 0.80, 8.5, 13.2)
    five_df = generate_wine(5, 4.2, 10.5, 0.2, 1.2, 0, 0.7, 1, 17, 0.02, 0.15, 0, 60, 0, 380, 0.99, 1.00, 2.9, 3.6, 0.25, 0.75, 8, 12.8)
    six_df = generate_wine(6, 4.2, 10.5, 0.2, 1.2, 0, 0.7, 1, 17, 0.02, 0.15, 0, 60, 0, 380, 0.99, 1.00, 2.9, 3.6, 0.25, 0.75, 8, 12.8)
    seven_df = generate_wine(7, 4.2, 10.5, 0.2, 1.2, 0, 0.7, 1, 17, 0.02, 0.15, 0, 60, 0, 380, 0.99, 1.00, 2.9, 3.6, 0.25, 0.75, 8, 12.8)
    eight_df = generate_wine(8, 4.2, 10.5, 0.2, 1.2, 0, 0.7, 1, 17, 0.02, 0.15, 0, 60, 0, 380, 0.99, 1.00, 2.9, 3.6, 0.25, 0.75, 8, 12.8)
    nine_df = generate_wine(9, 4.2, 10.5, 0.2, 1.2, 0, 0.7, 1, 17, 0.02, 0.15, 0, 60, 0, 380, 0.99, 1.00, 2.9, 3.6, 0.25, 0.75, 8, 12.8)

    # randomly pick one of these 3 and write it to the featurestore
    pick_random = random.uniform(3,9)

    if pick_random >= 9:
        wine_df = nine_df
        print("Quality 9 added")
    elif pick_random >= 8:
        wine_df = eight_df
        print("Quality 8 added")
    elif pick_random >= 7:
        wine_df = seven_df
        print("Quality 7 added")
    elif pick_random >= 6:
        wine_df = six_df
        print("Quality 6 added")
    elif pick_random >= 5:
        wine_df = five_df
        print("Quality 5 added")
    elif pick_random >= 4:
        wine_df = four_df
        print("Quality 4 added")
    elif pick_random >= 3:
        wine_df = three_df
        print("Quality 3 added")

    return wine_df


def g():
    import hopsworks
    import pandas as pd

    project = hopsworks.login()
    fs = project.get_feature_store()

    wine_df = get_random_wine()

    wine_fg = fs.get_feature_group(name="wine",version=1)
    wine_fg.insert(wine_df)

if __name__ == "__main__":
    if LOCAL == True :
        g()
    else:
        stub.deploy("wine_daily")
        with stub.run():
            f()
