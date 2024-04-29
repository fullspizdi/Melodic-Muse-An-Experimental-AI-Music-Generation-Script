# rule_based_system.py
# Module for rule-based music generation in the Melodic Muse AI Music Generation Script

import json
from mido import MidiFile, MidiTrack, Message
from config import RBS_RULES_FILE, MIDI_DEFAULT_TEMPO, MIDI_DEFAULT_VELOCITY, MIDI_DEFAULT_INSTRUMENT

def load_rules():
    """
    Load musical rules from a JSON file.

    Returns:
    dict: Dictionary containing musical rules.
    """
    with open(RBS_RULES_FILE, 'r') as file:
        rules = json.load(file)
    return rules

def apply_rules(rules, mood):
    """
    Apply musical rules based on the specified mood.

    Args:
    rules (dict): Dictionary containing musical rules.
    mood (str): The mood setting for music generation.

    Returns:
    list of tuple: List containing note (int) and duration (float) tuples.
    """
    if mood in rules:
        return rules[mood]
    else:
        return rules['default']

def generate_midi_from_rules(note_sequence, file_name):
    """
    Generate a MIDI file from a sequence of notes and durations.

    Args:
    note_sequence (list of tuple): List containing note (int) and duration (float) tuples.
    file_name (str): The output file name.
    """
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    track.append(Message('program_change', program=MIDI_DEFAULT_INSTRUMENT, time=0))
    sum_time = 0  # To keep track of cumulative time for note events

    for note, duration in note_sequence:
        delta_time = int(480 * duration)  # Assuming 480 ticks per beat
        track.append(Message('note_on', note=note, velocity=MIDI_DEFAULT_VELOCITY, time=sum_time))
        track.append(Message('note_off', note=note, velocity=MIDI_DEFAULT_VELOCITY, time=delta_time))
        sum_time += delta_time

    mid.save(file_name)

def main(mood='upbeat', output_file='output_song.midi'):
    """
    Main function to generate music based on rules and save as a MIDI file.

    Args:
    mood (str): The mood setting for music generation.
    output_file (str): The output MIDI file name.
    """
    rules = load_rules()
    note_sequence = apply_rules(rules, mood)
    generate_midi_from_rules(note_sequence, output_file)
    print(f"Generated MIDI file saved as '{output_file}' with mood '{mood}'.")

if __name__ == "__main__":
    main()

