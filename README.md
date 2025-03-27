# TextToSpeech

TextToSpeech is a simple text-to-speech application using the Coqui XTTS V2 model.

## Setup

### 1. Install Dependencies

Ensure you have Python 3 installed. Then run the following command to install dependencies:

```sh
python3 -m pip install -r requirements.txt
```

### 2. Download the Model Files

Create a directory for the models:

```sh
mkdir -p models/coqui_tts
```

Navigate to the model's directory:

```sh
cd models/coqui_tts
```

Download the Coqui XTTS V2 model files:

```sh
wget https://coqui.gateway.scarf.sh/hf-coqui/XTTS-v2/main/model.pth
wget https://coqui.gateway.scarf.sh/hf-coqui/XTTS-v2/main/config.json
wget https://coqui.gateway.scarf.sh/hf-coqui/XTTS-v2/main/vocab.json
wget https://coqui.gateway.scarf.sh/hf-coqui/XTTS-v2/main/hash.md5
wget https://coqui.gateway.scarf.sh/hf-coqui/XTTS-v2/main/speakers_xtts.pth
```

Return to the project root directory:

```sh
cd ../../
```

## Recording a Sample File

### 1. Check Input Devices

List available recording devices to identify your microphone:

```sh
arecord -l
```

### 2. Record a 10-Second Sample

Use the following command to record a 10-second sample using your microphone. Replace `<card_number>` and `<interface_number>` with your actual device values:

```sh
arecord -D plughw:<card_number>,<interface_number> -f cd -t wav -d 10 input.wav
```

- `-f cd` ensures CD-quality (16-bit, 44.1 kHz, stereo)
- `-t wav` specifies the output format
- `-d 10` records for 10 seconds

## Run the Script

After setup, run the main script to perform text-to-speech synthesis:

```sh
python3 main.py
```

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

Feel free to contribute or report issues!

