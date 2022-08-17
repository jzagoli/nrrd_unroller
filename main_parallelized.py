from nrrd_to_png import nrrd_to_png as unroll_nrrd
from pathlib import Path
import os
import multiprocessing
from multiprocessing import Pool

dataset_src = Path("C:/Users/user/Desktop/dataset/mri")
dataset_dst = Path("C:/Users/user/Desktop/dataset_preprocessed/mri")


def gen_single(nrrd):
    nrrddir = nrrd.parent
    out = Path(str(nrrddir).replace(str(dataset_src), str(dataset_dst)))
    if not out.exists():
        os.makedirs(out)
    unroll_nrrd(nrrd, out)


if __name__ == '__main__':
    assert dataset_src.exists()
    nrrdfiles = []
    for dirpath, subdirs, files in os.walk(dataset_src):
        for f in files:
            if f.endswith(".nrrd") and (f.startswith("MRI") or f.startswith("Prostate") or f.startswith("Target")):
                nrrdfiles.append(Path(dirpath) / f)
    print("Processing...")
    with Pool(multiprocessing.cpu_count()) as pool:
        pool.map(gen_single, nrrdfiles)
    print("Done.")
