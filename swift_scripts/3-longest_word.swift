// Splits sentence into tokens.  Assumes first token is longest word and
// substitutes in longer word if found

func longest_word(text: String) -> (String) {

	var text_split = text.characters.split{$0 == " "}.map(String.init)
	var longword = text_split[0]

	for current_word in text_split {
		if (current_word.characters.count) > (longword.characters.count) {
			longword = current_word
		}
	}
return longword
}
