name = "Dan DuLeone"
age = 35 # is a lie
height = 74 # inches - also a lie
weight = 180 # lbs - also a lie
eyes = 'Blue' # still lying
teeth = 'White' # Truth, at least!
hair = "Brown" # IIRC

print "Let's talk about %s" % name
print "He's %d inchest tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d, I get %d." % (
    age, height, weight, age + height + weight)
