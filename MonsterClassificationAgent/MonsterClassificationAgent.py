import time


class MonsterClassificationAgent:
    def __init__(self):
        # If you want to do any initial processing, add it here.
        self.monster_aggr_features = {
            'size': ['tiny', 'small', 'medium', 'large', 'huge'],
            'color': ['black', 'white', 'brown', 'gray', 'red', 'yellow', 'blue', 'green', 'orange', 'purple'],
            'covering': ['fur', 'feathers', 'scales', 'skin'],
            'foot-type': ['paw', 'hoof', 'talon', 'foot', 'none'],
            'leg-count': [0, 1, 2, 3, 4, 5, 6, 7, 8],
            'arm-count': [0, 1, 2, 3, 4, 5, 6, 7, 8],
            'eye-count': [0, 1, 2, 3, 4, 5, 6, 7, 8],
            'horn-count': [0, 1, 2],
            'lays-eggs': [True, False],
            'has-wings': [True, False],
            'has-gills': [True, False],
            'has-tail': [True, False]
        }
        self.monster_features = {}
        self.count_dict = {}

    def max_count_method(self, monsters_feat, feature):
        # print(f"monsters_feat {type(monsters_feat)}")
        return max({monsters_feat[feature]}, key=lambda idx: idx)

    def calculate_ranking(self, monsters_feat):
        self.count_dict['size'] = max({monsters_feat['size']}, key=monsters_feat['size'].count)
        self.count_dict['color'] = max({monsters_feat['color']}, key=monsters_feat['color'].count)
        self.count_dict['covering'] = max({monsters_feat['covering']}, key=monsters_feat['covering'].count)
        self.count_dict['foot-type'] = max({monsters_feat['foot-type']}, key=monsters_feat['foot-type'].count)
        self.count_dict['leg-count'] = self.max_count_method(monsters_feat, 'leg-count')
        self.count_dict['arm-count'] = self.max_count_method(monsters_feat, 'arm-count')
        self.count_dict['eye-count'] = self.max_count_method(monsters_feat, 'eye-count')
        self.count_dict['horn-count'] = self.max_count_method(monsters_feat, 'horn-count')
        self.count_dict['lays-eggs'] = self.max_count_method(monsters_feat, 'lays-eggs')
        self.count_dict['has-wings'] = self.max_count_method(monsters_feat, 'has-wings')
        self.count_dict['has-gills'] = self.max_count_method(monsters_feat, 'has-gills')
        self.count_dict['has-tail'] = self.max_count_method(monsters_feat, 'has-tail')
        # print(f"self.count_dict {self.count_dict}")
        return self.count_dict

    def solve(self, samples, new_monster):
        # Add your code here!
        #
        # The first parameter to this method will be a labeled list of samples in the form of
        # a list of 2-tuples. The first item in each 2-tuple will be a dictionary representing
        # the parameters of a particular monster. The second item in each 2-tuple will be a
        # boolean indicating whether this is an example of this species or not.
        #
        # The second parameter will be a dictionary representing a newly observed monster.
        #
        # Your function should return True or False as a guess as to whether or not this new
        # monster is an instance of the same species as that represented by the list.

        # print(f"new_monster {type(new_monster)}")
        start = time.time()

        for i in range(len(samples)):
            # print(f"Index: {i}, Item: {samples[i]}")
            monster_attributes = list(samples[i][0].items())

            if samples[i][1]:
                self.monster_features['size'] = monster_attributes[0][1]
                self.monster_features['color'] = monster_attributes[1][1]
                self.monster_features['covering'] = monster_attributes[2][1]
                self.monster_features['foot-type'] = monster_attributes[3][1]
                self.monster_features['leg-count'] = monster_attributes[4][1]
                self.monster_features['arm-count'] = monster_attributes[5][1]
                self.monster_features['eye-count'] = monster_attributes[6][1]
                self.monster_features['horn-count'] = monster_attributes[7][1]
                self.monster_features['lays-eggs'] = monster_attributes[8][1]
                self.monster_features['has-wings'] = monster_attributes[9][1]
                self.monster_features['has-gills'] = monster_attributes[10][1]
                self.monster_features['has-tail'] = monster_attributes[11][1]

        ranked_dict = (self.calculate_ranking(self.monster_features))
        # Use a dictionary comprehension to create the desired dictionary
        new_monster_value = {k: v for k, v in ranked_dict.items() if k not in new_monster or ranked_dict[k] != new_monster[k]}
        feature_diff = len(new_monster_value)
        # print(f"feature_diff {feature_diff}")

        print(f"Processing time:" + str((time.time() - start) * 1000) + "ms")

        if 0 <= feature_diff <= 7:
            return True
        elif 8 <= feature_diff <= 11:
            return False
        else:
            return False
