import yaml

def rotate_piece(piece, rotation):
    if rotation == 0:
        return piece
    if rotation == 1:
        rotated_piece = {}
        rotated_piece["T"] = piece["R"]
        rotated_piece["B"] = piece["L"]
        rotated_piece["L"] = piece["T"]
        rotated_piece["R"] = piece["B"]
        return rotated_piece
    if rotation == 2:
        rotated_piece = {}
        rotated_piece["T"] = piece["B"]
        rotated_piece["B"] = piece["T"]
        rotated_piece["L"] = piece["R"]
        rotated_piece["R"] = piece["L"]
        return rotated_piece
    if rotation == 3:
        rotated_piece = {}
        rotated_piece["T"] = piece["L"]
        rotated_piece["B"] = piece["R"]
        rotated_piece["L"] = piece["B"]
        rotated_piece["R"] = piece["T"]
        return rotated_piece

def expand_piece_list(list_in):
    list_out = {}
    for key, piece in list_in.items():
        for i in range(4):
            list_out[key + str(i)] = rotate_piece(piece, i)

    return list_out

def main():
    data_file = open("data.yaml", 'r')
    data = yaml.safe_load(data_file)
    data_file.close()

    all_pieces = {}
    corner_pieces = {}
    edge_pieces = {}

    all_pieces_expanded = {}
    corner_pieces_expanded = {}
    edge_pieces_expanded = {}

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

    all_pieces_expanded = expand_piece_list(all_pieces)
    corner_pieces_expanded = expand_piece_list(corner_pieces)
    edge_pieces_expanded = expand_piece_list(edge_pieces)

    possible_tops = {}
    possible_mids = {}
    possible_bottoms = {}

    outFile = open("lines.txt", 'w')
    for a_key, a_piece in corner_pieces_expanded.items():
        if a_piece["L"] == "X" and a_piece["T"] == "X":
            for b_key, b_piece in edge_pieces_expanded.items():
                if b_piece["T"] == "X" and b_piece["L"] == a_piece["R"]:
                    for c_key, c_piece in edge_pieces_expanded.items():
                        if c_piece["T"] == "X" and c_piece["L"] == b_piece["R"]:
                            for d_key, d_piece in edge_pieces_expanded.items():
                                if d_piece["T"] == "X" and d_piece["L"] == c_piece["R"]:
                                    for e_key, e_piece in edge_pieces_expanded.items():
                                        if e_piece["T"] == "X" and e_piece["L"] == d_piece["R"]:
                                            for f_key, f_piece in corner_pieces_expanded.items():
                                                if f_piece["R"] == "X" and f_piece["T"] == "X" and f_piece["L"] == e_piece["R"]:
                                                    top_key = a_key + b_key + c_key + d_key + e_key + f_key
                                                    possible_tops[top_key] = [a_piece, b_piece, c_piece, d_piece, e_piece, f_piece]

    print("########################### possible_tops ###########################")
    outFile.write(str(possible_tops.keys()))

    for a_key, a_piece in corner_pieces_expanded.items():
        if a_piece["L"] == "X" and a_piece["B"] == "X":
            for b_key, b_piece in edge_pieces_expanded.items():
                if b_piece["B"] == "X" and b_piece["L"] == a_piece["R"]:
                    for c_key, c_piece in edge_pieces_expanded.items():
                        if c_piece["B"] == "X" and c_piece["L"] == b_piece["R"]:
                            for d_key, d_piece in edge_pieces_expanded.items():
                                if d_piece["B"] == "X" and d_piece["L"] == c_piece["R"]:
                                    for e_key, e_piece in edge_pieces_expanded.items():
                                        if e_piece["B"] == "X" and e_piece["L"] == d_piece["R"]:
                                            for f_key, f_piece in corner_pieces_expanded.items():
                                                if f_piece["R"] == "X" and f_piece["B"] == "X" and f_piece["L"] == e_piece["R"]:
                                                    bottom_key = a_key + b_key + c_key + d_key + e_key + f_key
                                                    possible_bottoms[bottom_key] = [a_piece, b_piece, c_piece, d_piece, e_piece, f_piece]

    print("########################### possible_bottoms ###########################")
    outFile.write(str(possible_bottoms.keys()))

    for a_key, a_piece in edge_pieces_expanded.items():
        if a_piece["L"] == "X":
            for b_key, b_piece in all_pieces_expanded.items():
                if b_piece["L"] == a_piece["R"]:
                    for c_key, c_piece in all_pieces_expanded.items():
                        if c_piece["L"] == b_piece["R"]:
                            for d_key, d_piece in all_pieces_expanded.items():
                                if d_piece["L"] == c_piece["R"]:
                                    for e_key, e_piece in all_pieces_expanded.items():
                                        if e_piece["L"] == d_piece["R"]:
                                            for f_key, f_piece in edge_pieces_expanded.items():
                                                if f_piece["R"] == "X" and f_piece["L"] == e_piece["R"]:
                                                    mid_key = a_key + b_key + c_key + d_key + e_key + f_key
                                                    possible_mids[mid_key] = [a_piece, b_piece, c_piece, d_piece, e_piece, f_piece]

    print("########################### possible_mids ###########################")
    outFile.write(str(possible_mids.keys()))

    outFile.close()

main()