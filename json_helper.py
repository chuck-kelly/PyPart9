#big help from roberto 
import json
import pickle
import os
#part a
def read_json(filepath: str):
    with open(filepath) as file:
        json_obj = json.load(file)
    return json_obj
#part b
def read_all_json_files(dir: str):
    json_obj_list = []
    for root, dirs, files in os.walk(dir):
        for f in files:
            if f.endswith('.json'):
                data = read_json(os.path.join(dir,f))
                json_obj_list.append(data)
    return json_obj_list
#part c
def write_pickle(filepath, data):
    with open(filepath, 'wb') as file:
        pickle.dump(data, file)

#part d
def load_pickle(filepath):
    with open(filepath, 'rb') as file:
        data = pickle.load(file)
    return data

if __name__ == '__main__':
    data = read_all_json_files('./data/dragon_ball_z')
    write_pickle("dragonball.pickle", data)
    dragon = load_pickle("dragonball.pickle")
    print(dragon)