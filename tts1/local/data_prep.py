#!/usr/bin/env python

import sys, argparse, os, glob

seed=4

def get_args():
    parser = argparse.ArgumentParser(description="", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--dataset_dir", help="Input data directory", required=True)
    print(' '.join(sys.argv))
    args = parser.parse_args()
    return args

            
    
def get_text(file):
    with open(file, 'r', encoding="utf-8") as f:
        return f.read().strip()

def prepare_data(dataset_dir):
    wav_files = glob.glob(os.path.join(dataset_dir, 'Audios/*.wav'))
    txt_files = glob.glob(os.path.join(dataset_dir, 'Transcripts/*.txt'))
    
    transcripts = {os.path.basename(x).replace('.txt', ''): get_text(x) for x in txt_files}
    
    wav_files.sort()

    path_root = 'data/train'
    
    with open(path_root + '/text', 'w', encoding="utf-8") as f1, \
    open(path_root + '/utt2spk', 'w', encoding="utf-8") as f2, \
    open(path_root + '/wav.scp', 'w', encoding="utf-8") as f3:
        for wav_path in wav_files: 
            filename = os.path.basename(wav_path).replace('.wav', '')
            transcription = transcripts[filename]
            f1.write(filename + ' ' + transcription + '\n')
            f2.write(filename + ' ' + filename + '\n')
            f3.write(filename + ' ' + wav_path + '\n') 
            
def main():
    args = get_args()
    
    dataset_dir = args.dataset_dir

    prepare_data(dataset_dir)


if __name__ == "__main__":
    main()