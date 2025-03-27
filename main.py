from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
import soundfile as sf

print("[+] Loading model . . .")

# Path to your files
model_path = "models/coqui_tts/model.pth"
config_path = "models/coqui_tts/config.json"
vocab_path = "models/coqui_tts/vocab.json"
speakers_path = "models/coqui_tts/speakers_xtts.pth"

config = XttsConfig()
config.load_json(file_name=config_path)

model = Xtts.init_from_config(config=config)
model.load_checkpoint(config=config, checkpoint_path=model_path, vocab_path=vocab_path)

print("[+] Model is loaded.")

while True:
    prompt = input("[>] What to say (Default: exit)? ")

    if prompt == "exit" or prompt == "":
        break

    save_location = input("[>] Where to save (Default: output.wav)? ")

    print("[+] Synthesizing . . .")

    output_wav = model.synthesize(
        config=config,
        text=prompt,
        speaker_wav= "input.wav", # This voice will be cloned
        language="en"
    )

    if save_location == "":
        sf.write("output.wav", output_wav["wav"], 24000)
    else:
        sf.write(save_location, output_wav["wav"], 24000)
    print("[+] Done!")
