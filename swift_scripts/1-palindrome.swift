// Checks for palindrome using built-in reverse function
func is_palindrome(s: String) -> (Bool) {

	let reverse = String(s.characters.reverse())
	if reverse == s{
	return (true)
	}
	else {
	return (false)
	}
}
