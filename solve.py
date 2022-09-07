import yaml

data_file = open("data.yaml", 'r')
data = yaml.safe_load(data_file)
data_file.close()

all_pieces = {}
corner_pieces = {}
edge_pieces = {}

for key, piece in data["Pieces"].items():
    all_pieces[key] = piece
    if "X" in piece.values():
        edge_pieces[key] = piece
        if piece["T"] == "X" and piece["R"] == "X":
            corner_pieces[key] = piece
        elif piece["T"] == "X" and piece["L"] == "X":
            corner_pieces[key] = piece
        elif piece["B"] == "X" and piece["R"] == "X":
            corner_pieces[key] = piece
        elif piece["B"] == "X" and piece["L"] == "X":
            corner_pieces[key] = piece

print("Corners: " + str(len(corner_pieces)))
print("Edges: " + str(len(edge_pieces)))
print("Center: " + str(len(all_pieces)))
