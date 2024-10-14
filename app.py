from flask import Flask,jsonify,request

app = Flask(__name__)

games = [
    {"id": 1, "title": "Call Of Duty: Warzone", "developer": "Activision",
      "genre": "Battle Royae", "release year": 2020},
    {"id": 2, "title": "Uncharted 4", "developer": "Naughty Dog",
      "genre": "Adventure", "year": 2016}
]

@app.route('/')
def home():
    return "Welcome to my first api", 200

@app.route('/games', methods=['GET'])
def get_game():
    return jsonify(games),200

@app.route('/find_game/<int:game_id>',methods = ['GET'])
def find_game(game_id):
    game = next((game for game in games if game['id'] == game_id),None)
    if game:
        return jsonify(game),200
    return jsonify({"error":"game dose not exist"}),404

@app.route('/add_game',methods = ['POST'])
def add_game():
    new_game = request.json
    new_game['id'] = len(games)+1
    games.append(new_game)
    return jsonify(new_game),201

@app.route('/game_update/<int:game_id>', methods=['PUT'])
def game_update(game_id):
    game = next((game for game in games if game['id'] == game_id),None)
    if game:
        u_game = request.json
        game.update(u_game)
        return jsonify(game),200
    return jsonify({"error":"game not found"}),404

app.route('delete_game/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    game = next((game for game in games if game['id'] == game_id),None)
    if game:
        games.remove(game)
        return jsonify({"message":"game deleted"})
    return jsonify({"error":"game not found"})

if __name__ == '__main__':
    app.run(debug=True)