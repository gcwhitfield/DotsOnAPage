# Before executing this file, run :
# export PATH="$PATH:/Applications/LilyPond.app/Contents/Resources/bin/"
# George Whitfield
# gwhitfie@andrew.cmu.edu
# 
# Brief: Generate random notes on a page. This is useful for practicing reading
# music.

import abjad
import random

MAX_NOTE = 32 
MIN_NOTE = -8 

# returns a list of random notes
def randomNotes(duration, numNotes):
    result = []
    for i in range(numNotes):
        pitch = random.randint(MIN_NOTE, MAX_NOTE)
        result.append(abjad.Note(pitch, duration))
    return result



def main():
    # copied from abjad documentation
    duration = abjad.Duration(1, 4) #quarater note
    notes = randomNotes(duration, 100)
    staff = abjad.Staff(notes)
    abjad.show(staff)
    return

main()