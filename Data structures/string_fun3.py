from data import story

print(f"total chars in the story {len(story)}")

words = story.split()
print(f"total words in the story {len(words)}")
print(f"total unique words in the story {len (set(words))}")

sentences = story.split('.')
print(f"total sentences in the story {len(sentences)}")
print(sentences)

lines = story.split('\n')
print(f"total lines in the story {len(lines)}")
print(lines)

poem_list = [
    'twinkle twinkle little star \n',
    'How i wonder what you are! \n',
    'up above the world so high \n',
    'like a diamond in the sky \n',
]
poem = "\n".join(poem_list)
print(poem)