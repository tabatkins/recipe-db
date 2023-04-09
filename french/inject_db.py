import json
import mysql.connector

# Load the JSON file
with open("db-recipes-fr.json", "r") as file:
    data = json.load(file)

# Connect to the MySQL database
cnx = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="dbname",
)
cursor = cnx.cursor()

# Create the table for the recipes
table_create_query = (
    "CREATE TABLE IF NOT EXISTS recipes ("
    "id INT PRIMARY KEY AUTO_INCREMENT,"
    "recipe_id VARCHAR(255),"
    "name TEXT,"
    "source TEXT,"
    "preptime INT,"
    "waittime INT,"
    "cooktime INT,"
    "servings INT,"
    "comments TEXT,"
    "calories INT,"
    "fat INT,"
    "satfat INT,"
    "carbs INT,"
    "fiber INT,"
    "sugar INT,"
    "protein INT,"
    "instructions TEXT,"
    "ingredients TEXT,"
    "tags TEXT"
    ")"
)
cursor.execute(table_create_query)

# Loop through each recipe in the JSON file
for recipe_id, recipe_data in data.items():
    print("Processing recipe ID:", recipe_id)

    # Insert the recipe into the MySQL database
    insert_query = (
        "INSERT INTO recipes ("
        "recipe_id,"
        "name,"
        "source,"
        "preptime,"
        "waittime,"
        "cooktime,"
        "servings,"
        "comments,"
        "calories,"
        "fat,"
        "satfat,"
        "carbs,"
        "fiber,"
        "sugar,"
        "protein,"
        "instructions,"
        "ingredients,"
        "tags"
        ") VALUES ("
        "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s"
        ")"
    )

    cursor.execute(
        insert_query,
        (
            recipe_id,
            recipe_data["name"],
            recipe_data["source"],
            recipe_data["preptime"],
            recipe_data["waittime"],
            recipe_data["cooktime"],
            recipe_data["servings"],
            recipe_data["comments"],
            recipe_data["calories"],
            recipe_data["fat"],
            recipe_data["satfat"],
            recipe_data["carbs"],
            recipe_data["fiber"],
            recipe_data["sugar"],
            recipe_data["protein"],
            recipe_data["instructions"],
            json.dumps(recipe_data["ingredients"]),
            json.dumps(recipe_data["tags"]),)
)

cnx.commit()
cursor.close()
cnx.close()

print("Data has been imported successfully.")