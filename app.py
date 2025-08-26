from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Sample templates for generating recipes
RECIPE_NAMES = [
    "{vibe} {ingredient} Fiesta",
    "Cheeky {ingredient} {vibe} Bowl",
    "{ingredient} {vibe} Surprise",
    "{vibe} Night {ingredient} Treat",
]

MEASUREMENTS = [
    "1 cup {ingredient}, 2 tbsp olive oil, pinch of salt",
    "2 cups {ingredient}, 1 tsp honey, squeeze of lemon",
    "1/2 cup {ingredient}, 1 tbsp butter, dash of pepper",
]

CAPTIONS = [
    "Perfect for a {vibe} evening!",
    "Serve this at your next {vibe} gathering.",
    "A {vibe} twist that highlights {ingredient}.",
]


def generate_recipes(ingredient: str, vibe: str, count: int = 3):
    recipes = []
    for _ in range(count):
        name = random.choice(RECIPE_NAMES).format(ingredient=ingredient.title(), vibe=vibe.title())
        ingredients_list = random.choice(MEASUREMENTS).format(ingredient=ingredient)
        caption = random.choice(CAPTIONS).format(ingredient=ingredient, vibe=vibe)
        recipes.append({
            "name": name,
            "ingredients": ingredients_list,
            "caption": caption,
        })
    return recipes


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    ingredient = request.form.get("ingredient", "")
    vibe = request.form.get("vibe", "")
    if not ingredient or not vibe:
        return redirect(url_for("index"))
    recipes = generate_recipes(ingredient, vibe)
    return render_template("results.html", recipes=recipes)


if __name__ == "__main__":
    app.run(debug=True)
