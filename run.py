# Before executing this file, run :
# export PATH="$PATH:/Applications/LilyPond.app/Contents/Resources/bin/"
# George Whitfield
# gwhitfie@andrew.cmu.edu
# 
# Brief: Generate random notes on a page. This is useful for practicing reading
# music.

import abjad
import random

MAX_NOTE = 30 
MIN_NOTE = -10
NUM_FILES_TO_GENERATE = 1

# returns a list of random notes
def randomNotes(duration, numNotes):
    result = []
    for i in range(numNotes):
        pitch = random.randint(MIN_NOTE, MAX_NOTE)
        result.append(abjad.Note(pitch, duration))
    return result



def main():
    # copied from abjad documentation
    duration = abjad.Duration(1, 1) # whole note
    for i in range(NUM_FILES_TO_GENERATE):
        notes = randomNotes(duration, 145)
        staff = abjad.Staff(notes)
        lily_file = abjad.LilyPondFile.new(staff)
        lily_file.header_block.title = abjad.Markup(f'Dots {i}')
        abjad.show(lily_file)
    return

main()