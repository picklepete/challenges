from urllib2 import urlopen

def main():
	"""
	The Greplin Programming Challenge

	Level 1

	----------------------------------------

	Embedded in this block of text is the password for level 2.
	The password is the longest substring that is the same in reverse.

	As an example, if the input was "I like racecars that go fast"
	the password would be "racecar".
	"""
	# Track the longest palindrome.
	longest = ''

	# Read the gettysburg text.
	text = urlopen('http://challenge.greplin.com/static/gettysburg.txt').read()

	# Enumerate over each letter in the corpus.
	for position, letter in enumerate(text):

		# Track the current position, we will use this
		# value to loop backwards with.
		back = position

		# While the back variable isn't 0.
		while back != 0:

			# Extract the substring.
			substring = text[back:position + 1]

			# If the substring is the same as itself in reverse
			# and it's longer than the current longest palindrome,
			# make it the new longest one.
			if substring == substring[::-1] and len(substring) > len(longest):

				longest = substring

			# Decrement our back position.
			back -= 1

	# And print the password to level 2.
	print 'The password to level 2 is "%s".' % longest


if __name__ == '__main__':
	main()
