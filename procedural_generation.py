# procedural_generation.py
# Module for procedural music generation in the Melodic Muse AI Music Generation Script

import numpy as np
from mido import MidiFile, MidiTrack, Message
from config import MIDI_DEFAULT_TEMPO, MIDI_DEFAULT_VELOCITY, MIDI_DEFAULT_INSTRUMENT, PG_PATTERN_LENGTH

def generate_midi_pattern(pattern_length, mood):
    """
    Generate a MIDI pattern based on procedural rules.

    Args:
    pattern_length (int): Length of the pattern to generate.
    mood (str): Mood setting which influences the pattern generation.

    Returns:
    MidiTrack: A MIDI track containing the generated musical pattern.
    """
    track = MidiTrack()
    track.append(Message('program_change', program=MIDI_DEFAULT_INSTRUMENT, time=0))

    # Simple mood-based note selection
    base_note = 60  # Middle C (C4)
    if mood == 'upbeat':
        scale = [0, 2, 4, 5, 7, 9, 11, 12]  # Major scale
    elif mood == 'melancholic':
        scale = [0, 2, 3, 5, 7, 8, 10, 12]  # Minor scale
    elif mood == 'mysterious':
        scale = [0, 2, 4, 6, 8, 10, 12]  # Whole tone scale
    elif mood == 'energetic':
        scale = [0, 3, 4, 7, 9, 10, 12]  # Mixolydian scale
    else:
        scale = [0, 2, 4, 5, 7, 9, 11, 12]  # Default to Major scale if mood is undefined

    # Generate notes based on the selected scale
    for i in range(pattern_length):
        note = base_note + np.random.choice(scale)
        velocity = MIDI_DEFAULT_VELOCITY
        time = int(480 / pattern_length)  # Assuming 4/4 time, 480 ticks per beat
        track.append(Message('note_on', note=note, velocity=velocity, time=time))
        track.append(Message('note_off', note=note, velocity=velocity, time=time))

    return track

def save_midi_file(track, file_name):
    """
    Save the MIDI track to a file.

    Args:
    track (MidiTrack): The MIDI track to save.
    file_name (str): Name of the output MIDI file.
    """
    mid = MidiFile()
    mid.tracks.append(track)
    mid.save(file_name)

def main(mood='upbeat', output_file='output_song.midi'):
    """
    Main function to generate and save a procedural MIDI file.

    Args:
    mood (str): Mood setting for the music generation.
    output_file (str): Name of the output MIDI file.
    """
    track = generate_midi_pattern(PG_PATTERN_LENGTH, mood)
    save_midi_file(track, output_file)
    print(f"Procedural MIDI file generated and saved as '{output_file}'.")

if __name__ == "__main__":
    main()

