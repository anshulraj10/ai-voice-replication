import os
import torch
from openvoice import se_extractor
from openvoice.api import BaseSpeakerTTS, ToneColorConverter

device = "mps" if torch.backends.mps.is_available() else "cpu"

# Load models
base_speaker_tts = BaseSpeakerTTS('checkpoints/v1/base_speakers/EN/config.json', device=device)
base_speaker_tts.load_ckpt('checkpoints/v1/base_speakers/EN/checkpoint.pth')

tone_color_converter = ToneColorConverter('checkpoints/v1/converter/config.json', device=device)
tone_color_converter.load_ckpt('checkpoints/v1/converter/checkpoint.pth')

def generate_audio_v1(text, reference_audio_path, style, speed):
    outputs_dir = 'static/outputs'
    os.makedirs(outputs_dir, exist_ok=True)

    target_se, _ = se_extractor.get_se(reference_audio_path, tone_color_converter, target_dir='static/uploads', vad=True)
    
    src_path = os.path.join(outputs_dir, 'tmp_v1.wav')
    base_speaker_tts.tts(text, src_path, speaker=style, language='English', speed=speed)
    
    output_path = os.path.join(outputs_dir, f'output_v1.wav')
    source_se = torch.load('checkpoints/v1/base_speakers/EN/en_default_se.pth').to(device)
    tone_color_converter.convert(src_path, source_se, target_se, output_path, message="@MyShell")

    return output_path