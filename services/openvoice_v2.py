import os
import torch
from openvoice import se_extractor
from openvoice.api import ToneColorConverter
from melo.api import TTS

device = "mps" if torch.backends.mps.is_available() else "cpu"

# Load models
tone_color_converter_v2 = ToneColorConverter('checkpoints/v2/converter/config.json', device=device)
tone_color_converter_v2.load_ckpt('checkpoints/v2/converter/checkpoint.pth')

def generate_audio_v2(text, reference_audio_path, accent, speed):
    outputs_dir = 'static/outputs'
    language = 'EN'
    os.makedirs(outputs_dir, exist_ok=True)

    target_se, _ = se_extractor.get_se(reference_audio_path, tone_color_converter_v2, vad=True)

    model = TTS(language=language, device=device)
    speaker_ids = model.hps.data.spk2id
    speaker_key = accent.lower().replace("_", "-")
    speaker_id = speaker_ids[accent]
    

    src_path = os.path.join(outputs_dir, 'tmp_v2.wav')
    model.tts_to_file(text, speaker_id, src_path, speed=speed)

    output_path = os.path.join(outputs_dir, f'output_v2.wav')
    source_se = torch.load(f'checkpoints/v2/base_speakers/ses/{speaker_key}.pth', map_location=device)

    tone_color_converter_v2.convert(src_path, source_se, target_se, output_path, message="@MyShell")

    return output_path