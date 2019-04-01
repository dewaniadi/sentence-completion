from prediction import *

quotes = [
    "It is not a lack of love, but a lack of friendship that makes unhappy marriages.",
    "That which does not kill us makes us stronger.",
    "I'm not upset that you lied to me, I'm upset that from now on I can't believe you.",
    "And those who were seen dancing were thought to be insane by those who could not hear the music.",
    "It is hard enough to remember my opinions, without also remembering my reasons for them!",
    "They all pose as though their real opinions had bee"
]

for q in quotes:
    seq = q[:40].lower()
    ret = predict_completions(seq, 5)

    print("\nSequence: " + seq)
    for val in ret:
        print(val)

