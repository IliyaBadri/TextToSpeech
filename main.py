from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
import soundfile as sf

# Path to your files
model_path = "models/coqui_tts/model.pth"
config_path = "models/coqui_tts/config.json"
vocab_path = "models/coqui_tts/vocab.json"
speakers_path = "models/coqui_tts/speakers_xtts.pth"

config = XttsConfig()
config.load_json(file_name=config_path)

model = Xtts.init_from_config(config=config)
model.load_checkpoint(config=config, checkpoint_path=model_path, vocab_path=vocab_path)

output_wav = model.synthesize(
    config=config,
    text="What is happening?",
    speaker_wav= "input.wav", # Provide a speaker wav for cloning, if needed
    language="en"
)

sf.write("output.wav", output_wav["wav"], 24000)
