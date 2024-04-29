# sound_synthesis.py
# Module for sound synthesis in the Melodic Muse AI Music Generation Script

import numpy as np
import pysoundfile as psf
from config import SS_SAMPLE_RATE, SS_DURATION

def generate_tone(frequency, duration, sample_rate):
    """
    Generate a pure tone based on a sine wave.

    Args:
    frequency (float): Frequency of the tone in Hz.
    duration (float): Duration of the tone in seconds.
    sample_rate (int): Sample rate in Hz.

    Returns:
    np.array: Array containing the generated tone.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    tone = 0.5 * np.sin(2 * np.pi * frequency * t)
    return tone

def save_waveform(waveform, file_name, sample_rate):
    """
    Save a waveform array as a WAV file.

    Args:
    waveform (np.array): Array containing the waveform to save.
    file_name (str): Name of the output WAV file.
    sample_rate (int): Sample rate of the waveform.
    """
    psf.write(file_name, waveform, sample_rate, format='WAV', subtype='PCM_16')

def main():
    """
    Main function to generate and save a sound file.
    """
    # Example frequency for a tone (A4)
    frequency = 440  # Hz
    # Generate a tone
    tone = generate_tone(frequency, SS_DURATION, SS_SAMPLE_RATE)
    # Save the generated tone to a WAV file
    save_waveform(tone, 'output_tone.wav', SS_SAMPLE_RATE)
    print("Generated tone saved as 'output_tone.wav'.")

if __name__ == "__main__":
    main()
