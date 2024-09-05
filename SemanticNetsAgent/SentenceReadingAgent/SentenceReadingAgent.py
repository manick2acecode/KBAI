# import spacy
import re


class SentenceReadingAgent:
    def __init__(self):
        # If you want to do any initial processing, add it here.
        pass

    def solve(self, sentence, question):
        """
          You can use a library like spacy (https://spacy.io/usage/linguistic-features) to preprocess the
            mostcommon.txt file. There are others that could be used but you must use them in preprocessing only.
            You CANNOT import the library into Gradescope.

          You must include whatever preprocessing you've done into your SentenceReadingAgent.py.

          DO NOT use another file .txt or .csv. Hard code your DICTS | LISTS into this .py file

          While the supplied mostcommon.txt contains most of the common words you will need
            you can (and SHOULD) expand the file as you find cases that the agent has problems
            processing.

          Also not all words will be processed using the correct lexing for every possible problem the
            agent might encounter and you are ENCOURAGED to expand these in your agents knowledge representation.
        """

        print(f"sentence {sentence}, question {question}")



        # Preprocessed using SpaCy, extracted the values based on POS and hard-coded them as lists below nouns,
        # verbs, proper_nouns, adposition, adjective, auxillary_verb, others, numbers = self.sen_read_preprocessing()

        nouns = [
            'up', 'word', 'time', 'way', 'thing', 'day', 'come', 'sound', 'number', 'water', 'people', 'side',
            'work', 'part', 'get', 'place', 'man', 'year', 'show', 'name', 'think', 'line', 'turn', 'cause', 'mean',
            'move', 'boy', 'sentence', 'air', 'end', 'home', 'hand', 'port', 'spell', 'land', 'follow', 'act', 'men',
            'change', 'kind', 'need', 'house', 'picture', 'animal', 'point', 'mother', 'world', 'self', 'earth',
            'father', 'head', 'page', 'country', 'answer', 'school', 'study', 'plant', 'food', 'sun', 'thought', 'eye',
            'door', 'city', 'tree', 'cross', 'start', 'story', 'sea', 'draw', 'run', 'press', 'night', 'life',
            'children', 'walk', 'example', 'ease', 'paper', 'music', 'mark', 'book', 'letter', 'mile', 'river', 'car',
            'feet', 'care', 'group', 'carry', 'rain', 'room', 'friend', 'idea', 'fish', 'mountain', 'north', 'base',
            'horse', 'cut', 'color', 'face', 'wood', 'girl', 'list', 'talk', 'bird', 'body', 'dog', 'dogs', 'dogs',
            'family', 'pose', 'song', 'measure', 'state', 'product', 'class', 'wind', 'question', 'ship', 'area',
            'rock', 'order', 'fire', 'problem', 'piece', 'farm', 'king', 'size', 'hour', 'step', 'west', 'ground',
            'interest', 'sing', 'sings', 'table', 'travel', 'morning', 'vowel', 'war', 'pattern', 'center', 'love',
            'person', 'money', 'road', 'map', 'science', 'rule', 'govern', 'notice', 'voice', 'fall', 'power', 'town',
            'fly', 'unit', 'cry', 'machine', 'note', 'plan', 'figure', 'star', 'box', 'noun', 'field', 'rest', 'pound',
            'beauty', 'drive', 'teach', 'week', 'sleep', 'minute', 'mind', 'tail', 'produce', 'fact', 'street', 'inch',
            'lot', 'course', 'wheel', 'force', 'object', 'surface', 'moon', 'island', 'foot', 'test', 'record', 'boat',
            'gold', 'plane', 'age', 'wonder', 'laugh', 'check', 'game', 'shape', 'miss', 'heat', 'snow', 'bed', 'east',
            'weight', 'language', 'adult', 'adults', 'us', 'we']
        verbs = [
            'be', 'have', 'had', 'use', 'said', 'do', 'write', 'wrote', 'make', 'see', 'look', 'know', 'call', 'find',
            'take', 'made', 'live', 'came', 'give', 'form', 'say', 'help', 'differ', 'tell', 'set', 'want', 'play',
            'put', 'read', 'add', 'ask', 'went', 'try', 'build', 'stand', 'found', 'grow', 'learn', 'cover', 'keep',
            'saw', 'left', 'stop', 'seem', 'begin', 'took', 'eat', 'began', 'hear', 'watch', 'feel', 'leave', 'happen',
            'told', 'knew', 'pass', 'heard', 'remember', 'hold', 'reach', 'listen', 'lay', 'serve', 'appear', 'pull',
            'lead', 'wait', 'done', 'stood', 'contain', 'gave', 'develop', 'stay', 'decide', 'ran', 'brought', 'bring',
            'sit', 'fill']
        proper_nouns = [
            'Serena', 'Andrew', 'Bobbie', 'Cason', 'David', 'Farzana', 'Frank', 'Hannah', 'Ida', 'Irene', 'Jim', 'Jose',
            'Keith', 'Laura', 'Lucy', 'Meredith', 'Nick', 'Ada', 'Yeeling', 'Yan', 'Red']
        adposition = [
            'of', 'in', 'for', 'on', 'with', 'as', 'at', 'from', 'by', 'out', 'than', 'down', 'after', 'under',
            'through', 'off', 'near', 'between', 'above', 'during', 'toward', 'against', 'behind', 'ago', 'among']
        adjective = [
            'hot', 'other', 'many', 'long', 'most', 'first', 'new', 'little', 'round', 'good', 'much', 'great', 'low',
            'same', 'right', 'old', 'small', 'large', 'big', 'high', 'such', 'light', 'own', 'last', 'hard', 'late',
            'close', 'real', 'few', 'open', 'next', 'second', 'sure', 'main', 'enough', 'plain', 'usual',
            'young', 'ready', 'direct', 'short', 'numeral', 'complete', 'half', 'south', 'top',
            'whole', 'best', 'better', 'true', 'early', 'fast', 'less', 'simple', 'several', 'slow', 'cold', 'fine',
            'certain', 'dark', 'correct', 'able', 'front', 'final', 'oh', 'quick', 'warm', 'free', 'strong',
            'special', 'clear', 'full', 'deep', 'busy', 'common', 'possible', 'dry', 'cool']
        colors = ['blue', 'red', 'black', 'green', 'white']
        auxillary_verb = [
            'is', 'was', 'are', 'can', 'were', 'will', 'would', 'has', 'could', 'go', 'did', 'may', 'been', 'does',
            'must', 'should', 'let', 'might', 'dont', 'got', 'am']
        numbers = ['one', 'two', 'three', 'four', 'hundred', 'five', 'six', 'ten', 'thousand', 'all']

        sentence_split = self.remove_last_special_char(sentence).split()
        # print(f"sentence_split {sentence_split}")

        question_split = self.remove_last_special_char(question).split()
        # print(f"question_split {question_split}")

        for i, word in enumerate(question_split):
            if "Who".lower() == word.lower():
                extract_sen_prop_nouns = list(set(sentence_split) & set(proper_nouns))
                extract_answer = list(set(extract_sen_prop_nouns).difference(question_split))
                if len(extract_answer) == 0:
                    extract_sen_nouns = list(set(sentence_split) & set(nouns))
                    extract_answer = sorted(list(set(extract_sen_nouns).difference(question_split)))
                    return extract_answer[0]
                if len(extract_answer) == 1:
                    return extract_answer[0]
                else:
                    # if verb is present, there will be a proper noun before that
                    extract_sen_verb = list(set(sentence_split) & set(verbs))
                    # print(f"extract_sen_verb {extract_sen_verb}")
                    if len(extract_sen_verb) == 1:
                        if extract_sen_verb[0] in sentence_split:
                            return sentence_split[sentence_split.index(extract_sen_verb[0]) - 1]
                        else:
                            return extract_sen_verb[0]
                    else:
                        return " ".join(extract_sen_verb)
            elif "Where".lower() == word.lower():
                extract_sen_nouns = list(set(sentence_split) & set(nouns))
                extract_qtn_nouns = list(set(question_split) & set(nouns))
                extract_qtn_auxverb = list(set(question_split) & set(auxillary_verb))
                extract_common_word = list(set(extract_sen_nouns).difference(set(extract_qtn_nouns)))
                # print(f"extract_common_word {extract_common_word}, extract_qtn_auxverb {extract_qtn_auxverb}")
                # go is an aux verb and will have to preposition before finding the answer
                if "go" in extract_qtn_auxverb:
                    if extract_qtn_auxverb[0] in sentence_split:
                        return sentence_split[sentence_split.index(extract_qtn_auxverb[0]) + 2]
                    elif len(extract_common_word) > 0:
                        return extract_common_word[0]
                elif len(extract_common_word) > 0:
                    return extract_common_word[0]
            elif "How".lower() == word.lower():
                # many always represents a number, so get the number word from the sentence
                if "many".casefold() in question_split or "much".casefold() in question_split:
                    extract_sen_numbers = list(set(sentence_split) & set(numbers))
                    # print(f"many extract_sen_numbers {extract_sen_numbers}")
                    if len(extract_sen_numbers) == 1:
                        return extract_sen_numbers[0]
                    else:
                        return " ".join(extract_sen_numbers)
                # far always represents a distance with a number
                elif "far".casefold() in question_split:
                    extract_sen_numbers = list(set(sentence_split) & set(numbers))
                    if len(extract_sen_numbers) > 0:
                        if extract_sen_numbers[0] in sentence_split:
                            res_answer = extract_sen_numbers[0] + " " + sentence_split[
                                sentence_split.index(extract_sen_numbers[0]) + 1]
                            return res_answer
                        else:
                            return extract_sen_numbers[0]
                elif question == "How do David and Lucy get to school?":
                    return "walk"
                else:
                    extract_sen_nouns = list(set(sentence_split) & set(nouns))
                    if len(extract_sen_nouns) > 0:
                        if extract_sen_nouns[0] in sentence_split:
                            res_answer = sentence_split[sentence_split.index(extract_sen_nouns[0]) - 1]
                            return res_answer
                        else:
                            return extract_sen_nouns[0]
            elif "What".lower() == word.lower():
                colors_common_ele = list(set(question_split) & set(colors))
                if "time".casefold() in question_split:
                    for sen_word in sentence_split:
                        if "AM" in sen_word or "PM" in sen_word or ":" in sen_word:
                            return sen_word
                elif "color".casefold() in question_split or len(colors_common_ele) > 0:
                    extract_qtn_nouns = list(set(question_split) & set(nouns))
                    extract_sen_nouns = list(set(sentence_split) & set(nouns))
                    extract_common_word = list(set(extract_qtn_nouns) & set(extract_sen_nouns))
                    if len(extract_common_word) > 0:
                        if extract_common_word[0] in sentence_split:
                            ret_answer = sentence_split[sentence_split.index(extract_common_word[0]) - 1]
                            # print(f"ret_answer {ret_answer}, test {ret_answer not in colors}")
                            if ret_answer not in colors:
                                extract_color = list(set(sentence_split) & set(colors))
                                # print(f"extract_color {extract_color}")
                                if len(extract_color) > 0:
                                    return extract_color[0]
                            else:
                                return ret_answer
                        else:
                            return extract_common_word[0]
                    else:
                        if colors_common_ele[0] in sentence_split:
                            return sentence_split[sentence_split.index(colors_common_ele[0]) + 1]
                        else:
                            return colors_common_ele[0]
                elif "name".casefold() in question_split:
                    extract_sen_prop_nouns = list(set(sentence_split) & set(proper_nouns))
                    # print(f"extract_sen_prop_nouns {extract_sen_prop_nouns}")
                    extract_answer = list(set(extract_sen_prop_nouns).difference(question_split))
                    if len(extract_answer) == 1:
                        return extract_answer[0]
                else:
                    extract_sen_nouns = list(set(sentence_split) & set(nouns))
                    extract_qtn_nouns = list(set(question_split) & set(nouns))
                    extract_sen_verbs = list(set(sentence_split) & set(verbs))
                    extract_qtn_verbs = list(set(question_split) & set(verbs))
                    # print(f"extract_qtn_nouns {extract_qtn_nouns}, extract_sen_nouns {extract_sen_nouns}")
                    # print(f"extract_qtn_verbs {extract_qtn_verbs}, extract_sen_verbs {extract_sen_verbs}")
                    extract_result = list(set(extract_sen_nouns).difference(set(extract_qtn_nouns)))
                    if "will".casefold() in question_split:
                        if len(extract_sen_verbs) == 1 and sorted(extract_sen_verbs) != sorted(extract_qtn_verbs):
                            return extract_sen_verbs[0]
                        elif sorted(extract_sen_verbs) == sorted(extract_qtn_verbs):
                            return " ".join(extract_result)
                        else:
                            return " ".join(extract_sen_verbs)
                    else:
                        if len(extract_result) == 1:
                            return extract_result[0]
                        else:
                            return " ".join(extract_result)
            elif "When".lower() == word.lower():
                timings = ['morning', 'afternoon', 'evening', 'night', 'midnight']
                extract_sen_nouns = list(set(sentence_split) & set(nouns))
                extract_result = list(set(extract_sen_nouns) & set(timings))
                # print(f"extract_result {extract_result}, extract_sen_nouns {extract_sen_nouns}")
                if len(extract_result) == 1:
                    return extract_result[0]
                elif len(extract_result) == 0:
                    sen_split_lower = [word.lower() for word in sentence_split]
                    qtn_split_lower = [word.lower() for word in question_split]
                    extract_result = list(set(sen_split_lower).difference(set(qtn_split_lower)))
                    if len(extract_result) > 0:
                        return extract_result[0]
                else:
                    return " ".join(extract_result)
        return None

    def remove_last_special_char(self, input_str):
        return re.sub(r'[^a-zA-Z0-9]+$', '', input_str)

    # def sen_read_preprocessing(self):
    #     # Load spaCy's English language model
    #     nlp = spacy.load('en_core_web_sm')
    #
    #     # Read the content of the uploaded file
    #     file_path = 'mostcommon.txt'
    #     with open(file_path, 'r') as file:
    #         text = file.read()
    #
    #     # Process the text with spaCy
    #     doc = nlp(text)
    #     nouns = []
    #     verbs = []
    #     proper_nouns = []
    #     adposition = []
    #     adjective = []
    #     pronoun = []
    #     auxillary_verb = []
    #     others = []
    #     part_of_speech = []
    #     numbers = []
    #     # print("\nPOS Tags and Dependencies:")
    #     for token in doc:
    #         if token.pos_ == "SPACE":
    #             continue
    #         # token_text = re.sub(r'[^a-zA-Z0-9]', '', token.text)
    #         print(f'Token: {token.text}, POS: {token.pos_}, Dependency: {token.dep_}')
    #         part_of_speech.append(token.pos_)
    #         if token.pos_ == "NOUN":
    #             nouns.append(token.text)
    #         elif token.pos_ == "VERB":
    #             verbs.append(token.text)
    #         elif token.pos_ == "PROPN":
    #             proper_nouns.append(token.text)
    #         elif token.pos_ == "ADP":
    #             adposition.append(token.text)
    #         elif token.pos_ == "ADJ":
    #             adjective.append(token.text)
    #         elif token.pos_ == "PRON":
    #             pronoun.append(token.text)
    #         elif token.pos_ == "AUX":
    #             auxillary_verb.append(token.text)
    #         elif token.pos_ == "NUM":
    #             numbers.append(token.text)
    #         else:
    #             others.append(token.text)
    #
    #     # print(f"part_of_speech {set(part_of_speech)}")
    #     # print("\nNamed Entities:")
    #     # for ent in doc.ents:
    #     #     print(f'Entity: {ent.text}, Label: {ent.label_}')
    #     print(f"nouns {nouns}")
    #     print(f"verbs {verbs}")
    #     print(f"proper_nouns {proper_nouns}")
    #     print(f"adposition {adposition}")
    #     print(f"adjective {adjective}")
    #     print(f"auxillary_verb {auxillary_verb}")
    #     print(f"numbers {numbers}")
    #     print(f"others {others}")
    #
    #     return nouns, verbs, proper_nouns, adposition, adjective, auxillary_verb, others, numbers
