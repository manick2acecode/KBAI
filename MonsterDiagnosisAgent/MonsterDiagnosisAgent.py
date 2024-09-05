import itertools
import numpy as np


class MonsterDiagnosisAgent:
    def __init__(self):
        pass

    def solve(self, diseases, patient):
        """
        Determines the most likely disease based on patient symptoms.
        """
        # iterate diseases to form a list of feature names with its values
        dis_result = [(disease, *self.generate_code(value)) for disease, value in diseases.items()]
        # print(f"dis_result {type(dis_result)}")
        feature_list, code_list, value_list = zip(*dis_result)
        # print(f"feature_list {feature_list}")
        # print(f"code_list {code_list}")
        # print(f"value_list {value_list}")
        # use same generate_code method to extract feature name with its values
        patient_code, _ = self.generate_code(patient)
        # print(f"patient_code {patient_code}")
        # if number of features is more than 7 then it uses 7 as max_combination for forming subsets
        max_combinations = min(7, len(feature_list))
        # use itertools method to iterate over the max_combination and get the subsets
        subsets = [subset for r in range(2, max_combinations) for subset in
                   list(itertools.combinations(feature_list, r))]
        #print(f"subsets {subsets}")
        symptom_list = [self.calculate_symptom_code(subset, feature_list, value_list) for subset in subsets]
        # print(f"code {code} code_array {code_array}")
        result_index = symptom_list.index(patient_code)

        return list(subsets[result_index])

    def generate_code(self, features):
        """
        Converts features to a code and corresponding numerical array.
        """
        code = ""
        code_array = np.zeros(26)
        for i, (feature, value) in enumerate(features.items()):
            #print(f"feature {feature}, value {value}")
            code += f"{feature}{value}"
            code_array[i] = 1 if value == "+" else -1 if value == "-" else 0
            # If value is '0', code_array[i] remains 0 which is its default value
        # print(f"code {code} code_array {code_array}")
        return code, code_array

    def calculate_symptom_code(self, subset, feature_list, value_list):
        """
        Calculates the symptom code for a given subset of features.
        """
        total = np.zeros(26)
        for feature in subset:
            index = feature_list.index(feature)
            total = np.add(total, value_list[index])
        new_code = ['+' if x > 0 else '-' if x < 0 else '0' for x in total]
        # print(f"new_code {new_code}")
        code_dict = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", new_code))
        code_string, _ = self.generate_code(code_dict)
        # print(f"code_string {code_string}")
        return code_string
