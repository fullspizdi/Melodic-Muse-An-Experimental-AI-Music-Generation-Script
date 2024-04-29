```python
# melodic_muse.py
# Main script for the Melodic Muse AI Music Generation Project

import argparse
from mido import MidiFile
from config import AVAILABLE_TECHNIQUES, MOOD_SETTINGS, DEFAULT_OUTPUT_FILE
from rule_based_system import generate_music_rule_based
from procedural_generation import generate_midi_pattern
from genetic_algorithm import run_genetic_algorithm
from sound_synthesis import generate_tone, save_waveform

def parse_arguments():
    """
    Parse command line arguments.
    """
    parser = argparse.ArgumentParser(description="Melodic Muse: AI Music Generation Script")
    parser.add_argument('--technique', type=str, choices=AVAILABLE_TECHNIQUES, required=True,
                        help='Technique for music generation (rule_based, procedural, genetic_algorithm, sound_synthesis)')
    parser.add_argument('--mood', type=str, choices=MOOD_SETTINGS, required=False,
                        help='Mood to influence the music generation (optional)')
    parser.add_argument('--output', type=str, default=DEFAULT_OUTPUT_FILE,
                        help='Output file name for the generated music')
    return parser.parse_args()

def main():
    """
    Main function to handle music generation based on specified technique and mood.
    """
    args = parse_arguments()

    if args.technique == 'rule_based':
        rules = load_rules()
        notes = apply_rules(rules, args.mood)
        midi = generate_music_rule_based(notes)
    elif args.technique == 'procedural':
        midi = generate_midi_pattern(PG_PATTERN_LENGTH, args.mood)
    elif args.technique == 'genetic_algorithm':
        midi = run_genetic_algorithm(GA_POPULATION_SIZE, GA_GENERATIONS, args.mood)
    elif args.technique == 'sound_synthesis':
        tone = generate_tone(440, SS_DURATION, SS_SAMPLE_RATE)  # Example frequency set to A4
        save_waveform(tone, args.output, SS_SAMPLE_RATE)
        print(f"Generated sound saved as '{args.output}'.")
        return

    if args.technique != 'sound_synthesis':
        midi.save(args.output)
        print(f"Generated MIDI file saved as '{args.output}'.")

if __name__ == "__main__":
    main()
```
