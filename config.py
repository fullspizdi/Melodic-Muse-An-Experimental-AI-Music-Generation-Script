# config.py
# Configuration settings for the Melodic Muse AI Music Generation Script

# Define the available techniques for music generation
AVAILABLE_TECHNIQUES = ['rule_based', 'procedural', 'genetic_algorithm', 'sound_synthesis']

# Define mood settings for music generation
MOOD_SETTINGS = ['upbeat', 'melancholic', 'mysterious', 'energetic']

# Default output file settings
DEFAULT_OUTPUT_FILE = 'output_song.midi'

# Path to store example outputs
EXAMPLES_DIRECTORY = 'examples/'

# MIDI settings
MIDI_DEFAULT_TEMPO = 120  # Default tempo in BPM
MIDI_DEFAULT_VELOCITY = 64  # Default velocity for MIDI notes
MIDI_DEFAULT_INSTRUMENT = 0  # Default MIDI instrument (0 = Acoustic Grand Piano)

# Genetic Algorithm specific settings
GA_POPULATION_SIZE = 50
GA_MUTATION_RATE = 0.01
GA_GENERATIONS = 100

# Sound Synthesis specific settings
SS_SAMPLE_RATE = 44100  # Sample rate in Hz
SS_DURATION = 5  # Duration of generated sound in seconds

# Rule-based system specific settings
RBS_RULES_FILE = 'rules.json'  # Path to the file containing rules for generation

# Procedural generation specific settings
PG_PATTERN_LENGTH = 16  # Length of the pattern to generate

# Logging settings
LOG_LEVEL = 'INFO'
